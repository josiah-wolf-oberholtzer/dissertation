all:
	make clean
	make collect
	make abjad-book
	make compile

collect:
	scripts/collect-modules
	scripts/collect-scores

abjad-book:
	abjad-book -a ./assets -l . -y ./assets/stylesheet.ily chapters/*.tex

compile:
	xelatex dissertation.tex
	bibtex dissertation.tex
	xelatex dissertation.tex

clean:
	rm -Rif assets/lilypond-*.pdf
	find . -name "*.aux" -exec rm -rf {} \;
	find . -name "*.lof" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;
	find . -name "*.out" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.toc" -exec rm -rf {} \;