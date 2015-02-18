all:
	make clean
	make collect
	make abjad/book
	make compile

collect:
	scripts/collect-modules
	scripts/collect-scores

abjad/book:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/*.tex

abjad/clean:
	abjad-book \
		--clean \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/*.tex

compile:
	xelatex dissertation.tex
	xelatex dissertation.tex
	bibtex dissertation.aux
	xelatex dissertation.tex
	xelatex dissertation.tex

clean:
	rm -Rif assets/lilypond-*.pdf
	find . -name "*.aux" -exec rm -rf {} \;
	find . -name "*.bbl" -exec rm -rf {} \;
	find . -name "*.blg" -exec rm -rf {} \;
	find . -name "*.lof" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;
	find . -name "*.out" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.toc" -exec rm -rf {} \;