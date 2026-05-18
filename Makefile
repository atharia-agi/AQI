.PHONY: help install test demo-all clean docs verify

help:
	@echo "Divine AI Suite - Five Revolutionary Frameworks"
	@echo ""
	@echo "Targets:"
	@echo "  install       install Python dependencies"
	@echo "  verify        run file integrity verification"
	@echo "  test          run unit tests for all modules"
	@echo "  demo-all      run all 5 demos sequentially"
	@echo "  demo-tes      run Theological Embedding Space demo"
	@echo "  demo-nbcd     run Nass-Based Causal Discovery demo"
	@echo "  demo-dno      run Divine Names Ontology demo"
	@echo "  demo-epm      run Eschatological Predictive Modeling demo"
	@echo "  demo-pdi      run Prophetic Dream Interpreter demo"
	@echo "  docs          build documentation (Sphinx)"
	@echo "  clean         remove temporary files"

install:
	pip install -r requirements.txt

verify:
	python verification.py

test:
	@echo "Running tests..."
	@for d in 1.TES 2.NBCD 3.DNO 4.EPM 5.PDI-GPT; do \
		echo "Testing $$d..."; \
		if [ -d "$$d/tests" ]; then pytest "$$d/tests/"; else echo "  (no tests)"; fi \
	done

demo-all: demo-tes demo-nbcd demo-dno demo-epm demo-pdi

demo-tes:
	@echo "=== TES DEMO ==="
	@cd 1.TES && python demo.py

demo-nbcd:
	@echo "=== NBCD DEMO ==="
	@cd 2.NBCD && python demo.py

demo-dno:
	@echo "=== DNO DEMO ==="
	@cd 3.DNO && python demo.py

demo-epm:
	@echo "=== EPM DEMO ==="
	@cd 4.EPM && python demo.py

demo-pdi:
	@echo "=== PDI-GPT DEMO ==="
	@cd 5.PDI-GPT && python demo.py

docs:
	python -m sphinx -b html docs docs/_build/html

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.cache" -delete 2>/dev/null || true
	rm -rf docs/_build build dist *.egg-info .coverage htmlcov 2>/dev/null || true
