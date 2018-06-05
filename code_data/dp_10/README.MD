## Design Pattern 11: Cloud

### R - Deployment Steps

First, ensure that you have a free account at <https://www.shinyapps.io>.

Then, open RStudio project (`code_data.Rproj`) from `code_data` folder. 
Next, open `R_DP_10.Rmd` so that you can change API keys which you can found in your shinyapps.io dashboard (<https://www.shinyapps.io/admin/#/tokens>).

Shinyapps tutorial can be found at <http://docs.rstudio.com/shinyapps.io/getting-started.html>

### Python - Deployment Steps

First, ensure that you have a free account at <https://www.heroku.com>.

Then, you can follow this guideline <https://plot.ly/dash/deployment>.

In short:
- change directory to `python-plotly` in `dp_9`
- create a git repository `git init` there
- install `Heroku CLI` and execute for example `heroku create my-ds-dp-10-test` (or any other very unique name)
- push to Heroku by executing `git add . && git commit -m 'Initial app boilerplate' && git push heroku master` from the same folder 

Finally, open browser at <https://my-ds-dp-10-test.herokuapp.com>, <https://designpattern10.herokuapp.com/> respectively.

