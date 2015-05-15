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

abjad/book/composition:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/a-model-of-composition.tex
	say "rerendered chapter 4"

abjad/book/practicalities:
	abjad-book \
		-a ./assets \
		-g ./abjadbook.cfg \
		-l . \
		-y ./stylesheet.ily \
		source/chapters/practicalities.tex
	say "rerendered chapter 5"

compile:
	xelatex \
		-shell-escape \
		dissertation.tex
	bibtex dissertation.aux
	xelatex \
		-shell-escape \
		dissertation.tex
	xelatex \
       -shell-escape \
	   dissertation.tex
	#xelatex dissertation.tex
	#makeindex dissertation.tex
	#xelatex dissertation.tex
	say "recompiled document"

compile/fast:
	xelatex \
		-shell-escape \
		dissertation.tex

compile/talk:
	xelatex \
		-shell-escape \
		talk.tex

clean/temp:
	rm -Rif assets/tmp*
	rm -Rif tmp/tmp*
	rm -Rif dissertation.aux
	rm -Rif dissertation.bbl
	rm -Rif dissertation.bcf
	rm -Rif dissertation.blg
	rm -Rif dissertation.idx
	rm -Rif dissertation.ilg
	rm -Rif dissertation.ind
	rm -Rif dissertation.ist
	rm -Rif dissertation.out
	rm -Rif dissertation.run.xml
	rm -Rif dissertation.toc
	find . -name "*.aux" -exec rm -rf {} \;
	find . -name "*.bbl" -exec rm -rf {} \;
	find . -name "*.blg" -exec rm -rf {} \;
	find . -name "*.lof" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;
	find . -name "*.out" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.toc" -exec rm -rf {} \;
	say "cleaned temp files"

clean/assets:
	rm -Rif assets/lilypond*
	rm -Rif assets/graphviz*

open:
	open dissertation.pdf

copy-style:
	cp dissertation.py /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pygments/styles/dissertation.py