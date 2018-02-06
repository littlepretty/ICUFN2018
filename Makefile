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

TRANS_NAME=main
CONF_NAME=main_conf

.PHONY: clean, view

trans:
	$(PDFLATEX) $(TRANS_NAME).tex
	$(BIBTEX)   $(TRANS_NAME).aux
	$(PDFLATEX) $(TRANS_NAME).tex
	$(PDFLATEX) $(TRANS_NAME).tex

conf:
	$(PDFLATEX) $(CONF_NAME).tex
	$(BIBTEX)   $(CONF_NAME).aux
	$(PDFLATEX) $(CONF_NAME).tex
	$(PDFLATEX) $(CONF_NAME).tex

view_trans: trans 
	$(VIEWER) $(TRANS_NAME).pdf
	rm *.log *.aux *.out *.blg *.bbl
	#rm *-eps-converted-to.pdf
	#pdffonts main.pdf

view_conf: conf
	$(VIEWER) $(CONF_NAME).pdf
	rm *.log *.aux *.out *.blg *.bbl
	#rm *-eps-converted-to.pdf
	#pdffonts main.pdf

clean:
	rm *.log *.aux *.dvi *.out *.blg *.bbl *.ps *.bak
