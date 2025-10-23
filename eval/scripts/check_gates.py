import json, sys

report = json.load(open(sys.argv[1]))
failures = [m for m in report.get("metrics", []) if m.get("status") == "fail"]

if failures:
    print("❌ Gates failed:", failures)
    sys.exit(1)
else:
    print("✅ All gates passed")
