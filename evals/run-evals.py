#!/usr/bin/env python3
"""
Rights by Design — evaluation harness.

Runs each case in cases/*.json through the skill (SKILL.md as the system prompt),
asks for a structured assessment matching schemas/assessment-schema.json, then scores
it deterministically (impact tier, sector overlay, dimension statuses, bottom line,
keyword coverage). Optionally runs an LLM judge against the expected/*.md rubric.

Usage:
    pip install anthropic jsonschema
    export ANTHROPIC_API_KEY=sk-...
    export RBD_EVAL_MODEL=<a model id you have access to>   # e.g. a current Claude model
    python run-evals.py                # deterministic checks
    RBD_JUDGE=1 python run-evals.py    # also run the rubric judge

Exit code is non-zero if any case fails, so this can gate CI.
"""
import os, sys, json, glob, re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent / "plugins" / "rights-by-design" / "skills" / "rights-by-design" / "SKILL.md"
SCHEMA = HERE / "schemas" / "assessment-schema.json"
MODEL = os.environ.get("RBD_EVAL_MODEL", "claude-sonnet-4-5")
JUDGE = os.environ.get("RBD_JUDGE") == "1"

def load(p): return pathlib.Path(p).read_text(encoding="utf-8")

def get_client():
    try:
        import anthropic
    except ImportError:
        sys.exit("Missing dependency: pip install anthropic jsonschema")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY in your environment.")
    return anthropic.Anthropic()

def extract_json(text):
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.S)
    raw = m.group(1) if m else text[text.find("{"): text.rfind("}") + 1]
    return json.loads(raw)

def run_case(client, skill_text, schema_text, case):
    sysprompt = (skill_text + "\n\n---\nOutput ONLY a JSON object conforming to this schema. "
                 "No prose outside the JSON.\n\nSCHEMA:\n" + schema_text)
    user = "Assess the following system.\n\n" + case["system_description"]
    resp = client.messages.create(model=MODEL, max_tokens=3000,
                                  system=sysprompt, messages=[{"role": "user", "content": user}])
    return extract_json("".join(b.text for b in resp.content if getattr(b, "type", "") == "text"))

def check(a, exp):
    res, blob = [], json.dumps(a).lower()
    res.append(("impact_tier", a.get("impact_tier") == exp["impact_tier"], a.get("impact_tier")))
    ov = " ".join(a.get("sector_overlays", [])).lower()
    for s in exp.get("sector_overlays_include", []):
        res.append((f"overlay:{s}", s.lower() in ov, ov))
    dims = {d.get("name", "").lower(): d.get("status") for d in a.get("dimensions", [])}
    for name in exp.get("dimensions_not_met", []):
        st = next((v for k, v in dims.items() if name.lower()[:12] in k), None)
        res.append((f"not-met:{name[:22]}", st not in ("met", "not_applicable", None), st))
    res.append(("bottom_line", a.get("bottom_line") == exp["bottom_line"], a.get("bottom_line")))
    kws = exp.get("must_mention", [])
    hit = [k for k in kws if k.lower() in blob]
    res.append((f"keywords {len(hit)}/{len(kws)}", len(hit) >= max(1, int(0.6 * len(kws))), hit))
    return res

def judge(client, assessment, rubric):
    p = ("Score this Rights by Design assessment against the rubric from 0-100 for how well it "
         "matches the required findings. Return JSON {\"score\": int, \"notes\": str}.\n\nRUBRIC:\n"
         + rubric + "\n\nASSESSMENT:\n" + json.dumps(assessment, indent=2))
    r = client.messages.create(model=MODEL, max_tokens=600, messages=[{"role": "user", "content": p}])
    try:
        return extract_json("".join(b.text for b in r.content if getattr(b, "type", "") == "text"))
    except Exception:
        return {"score": None, "notes": "judge parse error"}

def main():
    client = get_client()
    skill_text, schema_text = load(SKILL), load(SCHEMA)
    try:
        import jsonschema; schema = json.loads(schema_text)
    except ImportError:
        jsonschema = None; schema = None
    cases = sorted(glob.glob(str(HERE / "cases" / "*.json")))
    rows, all_pass = [], True
    for cf in cases:
        case = json.loads(load(cf)); cid = case["id"]
        try:
            a = run_case(client, skill_text, schema_text, case)
        except Exception as e:
            print(f"[{cid}] ERROR: {e}"); all_pass = False; continue
        if jsonschema:
            try: jsonschema.validate(a, schema); schema_ok = True
            except Exception as e: schema_ok = False; print(f"[{cid}] schema: {e}")
        else:
            schema_ok = None
        checks = check(a, case["expected"])
        passed = all(ok for _, ok, _ in checks) and (schema_ok is not False)
        all_pass = all_pass and passed
        jr = judge(client, a, load(HERE / "expected" / f"{cid}.md")) if JUDGE and (HERE / "expected" / f"{cid}.md").exists() else None
        print(f"\n[{cid}] {'PASS' if passed else 'FAIL'}  schema={schema_ok}" + (f"  judge={jr.get('score')}" if jr else ""))
        for name, ok, val in checks:
            print(f"    {'ok ' if ok else 'XX '} {name} -> {val}")
        (HERE / "reports" / f"{cid}.json").write_text(
            json.dumps({"id": cid, "passed": passed, "schema_ok": schema_ok,
                        "checks": [[n, ok, v] for n, ok, v in checks], "judge": jr,
                        "assessment": a}, indent=2), encoding="utf-8")
        rows.append((cid, passed, schema_ok, jr.get("score") if jr else None))
    lines = ["# Eval summary\n", "| case | result | schema | judge |", "|---|---|---|---|"]
    for cid, p, s, j in rows:
        lines.append(f"| {cid} | {'PASS' if p else 'FAIL'} | {s} | {j if j is not None else '-'} |")
    (HERE / "reports" / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n" + "\n".join(lines))
    sys.exit(0 if all_pass else 1)

if __name__ == "__main__":
    main()
