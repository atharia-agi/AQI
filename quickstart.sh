#!/bin/bash
# Divine AI Suite - Quick Start (Unix/Linux/macOS)

set -e

echo "========================================"
echo "Divine AI Suite - Quick Start"
echo "========================================"

echo ""
echo "[1/4] Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "[2/4] Checking project integrity..."
python verification.py

echo ""
echo "[3/4] Running all demos..."
python run_all_demos.py

echo ""
echo "[4/4] Done!"
echo ""
echo "Next steps:"
echo "  - Explore each project folder (1.TES, 2.NBCD, ...)"
echo "  - Read README_MAIN.md for details"
echo "  - Edit demo.py to experiment"
