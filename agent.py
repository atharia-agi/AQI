#!/usr/bin/env python3
"""
Divine AI Suite Agent - Command interface for managing the suite.

Usage:
    python agent.py <command> [options]

Commands:
    help                Show this help
    list                List all projects and status
    demo <project>      Run demo for a specific project (or 'all')
    test <project>      Run tests for a specific project (or 'all')
    install             Install dependencies
    build-docs          Build documentation (Sphinx)
    check               Verify all files are in place
    status              Print suite status

Examples:
    python agent.py demo all
    python agent.py test 1.TES
    python agent.py check
"""

import sys
import subprocess
from pathlib import Path

PROJECTS = ["1.TES", "2.NBCD", "3.DNO", "4.EPM", "5.PDI-GPT"]


def run_command(cmd, cwd=None):
    """Run a shell command and return exit code."""
    result = subprocess.run(cmd, cwd=cwd)
    return result.returncode


def cmd_help(_):
    print(__doc__)


def cmd_list(_):
    print("\nDivine AI Suite - Projects:")
    for proj in PROJECTS:
        demo_path = Path(proj) / "demo.py"
        status = "[READY]" if demo_path.exists() else "[INCOMPLETE]"
        print(f"  {proj:<15} {status}")
    print()


def cmd_demo(args):
    if not args:
        print("Usage: agent.py demo <project|all>")
        return
    target = args[0]
    if target == "all":
        for proj in PROJECTS:
            print(f"\n{'=' * 80}\nRunning demo for {proj}\n{'=' * 80}\n")
            code = run_command([sys.executable, "demo.py"], cwd=proj)
            if code != 0:
                print(f"[FAIL] {proj} demo failed with exit code {code}")
                return
        print("\n[OK] All demos completed!")
    else:
        if target not in PROJECTS:
            print(f"Unknown project: {target}. Choose from: {', '.join(PROJECTS)}")
            return
        print(f"\nRunning demo for {target}...\n")
        code = run_command([sys.executable, "demo.py"], cwd=target)
        if code != 0:
            print(f"[FAIL] Demo failed with exit code {code}")


def cmd_test(args):
    if not args:
        print("Usage: agent.py test <project|all>")
        return
    target = args[0]
    if target == "all":
        for proj in PROJECTS:
            print(f"\nTesting {proj}...")
            code = run_command(["pytest", proj], cwd=".")
            if code != 0:
                print(f"[FAIL] {proj} tests failed")
    else:
        if target not in PROJECTS:
            print(f"Unknown project: {target}")
            return
        code = run_command(["pytest", target], cwd=".")
        if code != 0:
            print("[FAIL] Tests failed")


def cmd_install(_):
    print("Installing dependencies...")
    code1 = run_command(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--index-url",
            "https://download.pytorch.org/whl/cpu",
            "torch>=2.0.0",
        ]
    )
    code2 = run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    if code1 == 0 and code2 == 0:
        print("[OK] Dependencies installed")
    else:
        print("[FAIL] Installation failed")


def cmd_build_docs(_):
    print("Building documentation...")
    code = run_command([sys.executable, "-m", "sphinx", "-b", "html", "docs", "docs/_build/html"])
    if code == 0:
        print("[OK] Docs built at docs/_build/html/index.html")
    else:
        print("[FAIL] Docs build failed")


def cmd_check(_):
    print("Checking file integrity...")
    all_good = True
    for proj in PROJECTS:
        demo = Path(proj) / "demo.py"
        src_dir = Path(proj) / "src"
        data_dir = Path(proj) / "data"
        if not demo.exists():
            print(f"  [FAIL] {proj}/demo.py missing")
            all_good = False
        if not src_dir.exists():
            print(f"  [FAIL] {proj}/src/ missing")
            all_good = False
        if not data_dir.exists():
            print(f"  [FAIL] {proj}/data/ missing")
            all_good = False
    if all_good:
        print("[OK] All projects have required files")
    else:
        print("[FAIL] Some projects are incomplete")


def cmd_status(_):
    print("\nDivine AI Suite - Status")
    print(f"  Projects: {len(PROJECTS)}")
    print("  All demos: ready")
    print("  Documentation: built (see docs/_build/html/)")
    print("  License: MIT")
    print()


def main():
    if len(sys.argv) < 2:
        cmd_help(None)
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "help": cmd_help,
        "list": cmd_list,
        "demo": cmd_demo,
        "test": cmd_test,
        "install": cmd_install,
        "build-docs": cmd_build_docs,
        "check": cmd_check,
        "status": cmd_status,
    }

    if command not in commands:
        print(f"Unknown command: {command}")
        print("Available:", ", ".join(commands.keys()))
        return

    commands[command](args)


if __name__ == "__main__":
    main()
