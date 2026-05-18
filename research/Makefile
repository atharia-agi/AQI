.PHONY: help install test lint paper compile-docs clean

help:
	@echo "Tawhid‑AI Research Repository"
	@echo ""
	@echo "Targets:"
	@echo "  install       install Python dependencies"
	@echo "  test          run unit tests"
	@echo "  lint          lint and format check"
	@echo "  paper         compile LaTeX paper"
	@echo "  compile-docs  build HTML documentation"
	@echo "  clean         remove build artefacts"

install:
	pip install -r requirements.txt
	pip install -e src/tawhid_unifier
	pip install -e src/mizan_fairness

test:
	pytest src/tawhid_unifier/tests/

lint:
	black src/ examples/ --check
	isort src/ examples/ --check-only
	flake8 src/ examples/

paper:
	@echo "Compiling paper.tex"
	@pdflatex -interaction=nonstopmode paper.tex
	@bibtex paper
	@pdflatex -interaction=nonstopmode paper.tex
	@pdflatex -interaction=nonstopmode paper.tex
	@echo "Output: paper.pdf"

compile-docs:
	sphinx-build -b html docs/ build/html

clean:
	rm -rf __pycache__ src/*/__pycache__ src/*/tests/__pycache__
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf build/ dist/ *.egg-info
	rm -f paper.aux paper.log paper.out paper.toc paper.synctex.gz
	rm -rf K:/Workspace/research-quran-ai-tech/.tox 2>/dev/null || true
