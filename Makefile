all:
	scripts/collect-modules
	scripts/collect-scores
	xelatex dissertation.tex
	xelatex dissertation.tex