#!/bin/bash

clear
# https://tex.stackexchange.com/a/40101
# https://tex.stackexchange.com/a/218167
# https://manpages.debian.org/testing/texlive-binaries/xdvipdfmx.1.en.html

echo "Run with sudo (admin rights). You may need to also execute: "
echo "sudo chmod u+x create_pdf_thesis.sh"
echo " "
echo "to create PDF, read README file and then: sudo ./create_pdf_thesis.sh"

cd ..

cd tex_thesis

echo " "

echo "Changed folder. Now creates PDF"
echo " "

SECONDS=0

rm -f *.aux *.bbl *.bcf *.blg *.loa *.out *.lof *.toc *.lot *.run.xml *.xdv *.lol

echo "removed files such as .aux"
echo " "

xelatex -shell-escape -no-pdf thesis
biber thesis
xelatex -shell-escape -no-pdf thesis
xelatex -shell-escape -no-pdf thesis
xdvipdfmx -z 9 -V 7 thesis

latexmk -c
rm -f *.aux *.bbl *.bcf *.blg *.loa *.out *.lof *.toc *.lot *.run.xml *.xdv *.lol

echo "seconds:" $SECONDS
echo "    "
echo "Done"

exit
