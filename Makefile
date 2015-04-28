all:
	make clean
	make collect
	make abjad/book
	make compile
	make open

fast:
	make abjad/book/composition
	make compile
	make open

collect:
	scripts/collect-modules
	scripts/collect-scores
	say "collected assets"

examples:
	$(MAKE) -C assets examples

abjad/book:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/*.tex
	say "rerendered all chapters"

abjad/book/composition:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/a-model-of-composition.tex
	say "rerendered chapter 4"

abjad/book/notation:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/a-model-of-notation.tex
	say "rerendered chapter 2"

abjad/book/time-tools:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/time-tools.tex
	say "rerendered chapter 3"

compile:
	xelatex \
		-shell-escape \
		-shell-restricted \
		dissertation.tex
	bibtex dissertation.aux
	xelatex \
		-shell-escape \
		-shell-restricted \
		dissertation.tex
	xelatex \
       -shell-escape \
	   -shell-restricted \
	   dissertation.tex
	#xelatex dissertation.tex
	#makeindex dissertation.tex
	#xelatex dissertation.tex
	say "recompiled document"

compile/fast:
	xelatex \
		-shell-escape \
		dissertation.tex

clean:
	rm -Rif assets/graphviz-*.pdf
	rm -Rif assets/graphviz-*.dot
	rm -Rif assets/lilypond-*.pdf
	rm -Rif assets/lilypond-*.ly
	rm -Rif assets/tmp*
	rm -Rif tmp/tmp*
	find . -name "*.aux" -exec rm -rf {} \;
	find . -name "*.bbl" -exec rm -rf {} \;
	find . -name "*.blg" -exec rm -rf {} \;
	find . -name "*.lof" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;
	find . -name "*.out" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.toc" -exec rm -rf {} \;
	say "cleaned assets"

open:
	open dissertation.pdf