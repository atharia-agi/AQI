@echo off
REM Compile script for Divine Ontology in Machine Intelligence paper
REM Requires: pdflatex, bibtex in PATH

echo Compiling paper.tex...
pdflatex -interaction=nonstopmode paper.tex
if errorlevel 1 (
    echo pdflatex failed. Check LaTeX installation.
    pause
    exit /b 1
)

echo Running bibtex...
bibtex paper
if errorlevel 1 (
    echo bibtex failed.
    pause
    exit /b 1
)

echo Second pdflatex pass...
pdflatex -interaction=nonstopmode paper.tex
if errorlevel 1 (
    echo pdflatex failed.
    pause
    exit /b 1
)

echo Third pdflatex pass (for references)...
pdflatex -interaction=nonstopmode paper.tex
if errorlevel 1 (
    echo pdflatex failed.
    pause
    exit /b 1
)

echo.
echo Compilation complete. Output: paper.pdf
pause