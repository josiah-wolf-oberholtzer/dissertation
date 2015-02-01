all:
	scripts/collect-modules
	scripts/collect-scores
	xelatex dissertation.tex
	bibtex dissertation.tex
	xelatex dissertation.tex
	
abjad-book:
	abjad-book -a ./assets -l . -y ./assets/stylesheet.ily chapters/*.tex

clean:
	rm -Rif assets/lilypond-*.pdf