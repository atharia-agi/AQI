#!/usr/bin/env python3
"""
Verification script: ensures all Divine AI Suite projects are complete.
"""

import sys
from pathlib import Path

PROJECTS = ["1.TES", "2.NBCD", "3.DNO", "4.EPM", "5.PDI-GPT"]

def check_project(proj: Path):
    errors = []
    if not (proj / "demo.py").exists():
        errors.append("demo.py missing")
    if not (proj / "src").exists():
        errors.append("src/ missing")
    else:
        if not any((proj / "src").glob("*.py")):
            errors.append("no Python modules in src/")
        if not (proj / "src" / "__init__.py").exists():
            errors.append("src/__init__.py missing")
    if not (proj / "data").exists():
        errors.append("data/ missing")
    else:
        if not any((proj / "data").glob("*.json")):
            errors.append("no JSON data files")
    return errors

def main():
    print("\nDivine AI Suite — Verification")
    print("="*60)
    all_ok = True
    for proj_name in PROJECTS:
        proj_path = Path(proj_name)
        errors = check_project(proj_path)
        if errors:
            print(f"[FAIL] {proj_name}:")
            for e in errors:
                print(f"    - {e}")
            all_ok = False
        else:
            print(f"[ OK ] {proj_name}")

    print("="*60)
    if all_ok:
        print("✅ All projects are complete and ready to run.")
        print("   Run: python run_all_demos.py")
        return 0
    else:
        print("❌ Some projects are incomplete. Fix errors before running.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
