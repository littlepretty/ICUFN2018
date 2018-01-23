PDFLATEX=pdflatex
LATEX=latex
BIBTEX=bibtex
DVI2PDF=dvipdf
PS2PDF=ps2pdf
UNAME:=$(shell uname -s)
ifeq ($(UNAME),Linux)
	VIEWER=xdg-open
endif
ifeq ($(UNAME), Darwin)
	VIEWER=open -a Preview
endif

NAME=main

.PHONY: clean, view

final:
	$(PDFLATEX) $(NAME).tex
	$(BIBTEX) $(NAME).aux
	$(PDFLATEX) $(NAME).tex
	$(PDFLATEX) $(NAME).tex

view: final
	$(VIEWER) $(NAME).pdf
	rm *.log *.aux *.out *.blg *.bbl
	#rm *-eps-converted-to.pdf
	#pdffonts main.pdf

clean:
	rm *.log *.aux *.dvi *.out *.blg *.bbl *.ps *.bak
