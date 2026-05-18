.PHONY: help install test demo-all clean docs

help:
	@echo "Divine AI Suite — Five Revolutionary Frameworks"
	@echo ""
	@echo "Targets:"
	@echo "  install       install Python dependencies"
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

test:
	@echo "Running tests..."
	@for d in 1.TES 2.NBCD 3.DNO 4.EPM 5.PDI-GPT; do \
		echo "Testing $$d..."; \
		if [ -f "$$d/tests/test_*.py" ]; then pytest $$d/tests/; else echo "  (no tests)"; fi \
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
	sphinx-build -b html docs build/html

clean:
	rm -rf __pycache__ */__pycache__ */src/__pycache__ */tests/__pycache__
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf */data/*.npy */data/*.npz
	rm -rf K:/Workspace/divine-ai-suite/*/data/*.cache
