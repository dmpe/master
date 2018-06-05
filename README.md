# Discovering Data Science Design Patterns with Examples from R and Python Software Ecosystem

This repository contains source code & other data for my graduate thesis.

All pictures are located in `tex_thesis/images` folder.

## 2. Ensure right software is installed on your PC

### 2.1 Code Examples
These are just necessary for **running code samples**.

For Python 3, execute:

```
sudo apt-get install python3-pip r-base r-base-dev 
sudo pip3 install jupyter pandas scipy jupyterhub fancyimpute tensorflow networkx==1.11 scikit-learn numpy mlens
sudo pip3 install -r code_data/dp_9/python-plotly/requirenments.txt
```

For R, install packages below to cover most important ones -- others will be installed too. 
It will take a long time but is worth it. 

```
ipak <- function(pkg){
new.pkg <- pkg[!(pkg %in% installed.packages()[, "Package"])]
if (length(new.pkg))
install.packages(new.pkg, dependencies = TRUE)
sapply(pkg, require, character.only = TRUE)
}
required.packages <- c("ggplot2", "tidyverse", "reshape2", "shiny", "caret", "knitr", "Rcpp", "rmarkdown", "pROC", "data.table", "mice", "mlbench", "caretEnsemble", "glmnet", "pls", "caTools")))
ipak(packages)
```

### 2.2 Thesis document

(tested on Ubuntu OS 17.10) 

To **reproduce thesis document**, install full `Tex` with biblatex/biber and `git-scm`

```
sudo apt-get install texlive-full git
```

Once done (it take a very long time), one needs to have specific fonts installed as well. 
First, those from Adobe for the source code, execute:

```
[ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
sudo git clone --depth 1 --branch release https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
sudo fc-cache -f -v
fc-cache -f -v
```

**Moreover**, one needs to have 4 fonts similar to EB(/Adobe) Garamond: Bold, BoldItalic, Regular and Italic (not the "cond" and "display" versions, just "classical").
You will **not** find them here due to licensing but make sure to put them into the `custom_fonts` folder and adjust `thesis.tex` file as needed.

## 3. Structure | Reproduce

#### code_data -- main folder with design pattern examples

In the `code_data` folder, execute `sudo ./create_pdf_thesis.sh` `bash` script.
Based on the content of the `tex_thesis` folder and **if fonts** are properly installed, this will ultimately create PDF (~ 300 seconds/5 minutes is minimum what it takes to compile). 

#### tex-thesis -- for creating PDF thesis:

Source templates come from adjusting <https://www.sharelatex.com/templates/thesis/lmu-thesis> and **mainly** from https://www.sharelatex.com/templates/thesis/university-of-michigan-thesis

## 4. How to run code examples

- For Plot.ly Dash: 
    - Run `python3 app.py` in `dp_9/python-plotly` folder (<https://designpattern10.herokuapp.com/> might be still working well)

- R(md) & Shiny: Use `RStudio IDE` to run `dp_9/R-Shiny/app.R` or `.Rmd` files. 
    - Or `Rscript -e "library(rmarkdown);rmarkdown::render('R_masterThesis.Rmd')"` from `bash`.

- Jupyter Notebooks: open any browser and
    - Run `jupyterhub --no-ssl` from `bash` and navigate to desired `ipynb` file.
    - Alternatively, just run `jupyter notebook`.

## 5. Sources

<https://stackoverflow.com/a/3452888>

<https://stackoverflow.com/a/15593865>

<https://gist.github.com/stevenworthington/3178163> 

<https://github.com/jupyterhub/jupyterhub/wiki/Installation-of-Jupyterhub-on-remote-server> 

<https://github.com/adobe-fonts/source-code-pro/issues/17#issuecomment-233178247>
