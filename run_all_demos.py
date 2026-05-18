#!/usr/bin/env python3
"""
Master demo runner: executes all five framework demos in sequence.

Usage:
    python run_all_demos.py
"""

import subprocess
import sys
import time
from pathlib import Path


def run_demo(project_dir: str, demo_script: str = "demo.py"):
    """Run a single demo in its directory."""
    cwd = Path(__file__).parent / project_dir
    if not cwd.is_dir():
        print(f"[FAIL] {project_dir} directory not found at {cwd}")
        return False
    demo_path = cwd / demo_script
    if not demo_path.is_file():
        print(f"[FAIL] {demo_script} not found in {project_dir}")
        return False
    print(f"\n{'=' * 80}")
    print(f"STARTING: {project_dir}")
    print(f"{'=' * 80}\n")
    result = subprocess.run([sys.executable, demo_script], cwd=str(cwd))
    if result.returncode != 0:
        print(f"[FAIL] {project_dir} failed with exit code {result.returncode}")
        return False
    else:
        print(f"[OK] {project_dir} completed successfully")
        return True


def main():
    print("\n" + "=" * 80)
    print("  DIVINE AI SUITE MASTER DEMO")
    print("  Running all 5 revolutionary frameworks")
    print("=" * 80)

    projects = [
        "1.TES",
        "2.NBCD",
        "3.DNO",
        "4.EPM",
        "5.PDI-GPT",
    ]

    results = {}
    start = time.time()

    for proj in projects:
        ok = run_demo(proj)
        results[proj] = ok
        time.sleep(1)

    elapsed = time.time() - start

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for proj, ok in results.items():
        status = "[OK] PASS" if ok else "[FAIL] FAIL"
        print(f"{status} {proj}")
    print(f"\nTotal time: {elapsed / 60:.1f} minutes")
    print("=" * 80 + "\n")

    if all(results.values()):
        print("[SUCCESS] All demos executed successfully!")
        print("   The Divine AI Suite is operational.")
    else:
        print("[WARNING] Some demos failed. Check the logs above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
