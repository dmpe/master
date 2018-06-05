# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.plotly as py
import plotly.graph_objs as go

#https://plot.ly/python/pie-charts/
#https://plot.ly/dash/interactive-graphing
#https://github.com/plotly/dash-docs/blob/master/tutorial/examples/graph_callbacks_simple.py
    
app = dash.Dash()
server = app.server
app.scripts.config.serve_locally = True

# Data source: https://gist.github.com/dmpe/8759f471468570d50a6ce04d27e948fc
df = pd.read_csv('https://gist.githubusercontent.com/dmpe/8759f471468570d50a6ce04d27e948fc/raw/08a24f3e41ed79d1d4a555eeaeca684e3c1bf668/swiss_religion2.csv', sep=",", usecols=[1,2,3,4,5])

labels = ['Catholic','Protestant']
colors = ['#FEBFB3', '#96D38C']

app.layout = html.Div(className="container-fluid row", children=[
    html.H1(children='Design Pattern 9: Interactive Application in Python (Plot.ly - Dash)'),
    html.Div([
        dcc.Markdown("""**Select one of 47 French-speaking provinces of Switzerland**"""),
        
        dcc.Dropdown(
            id='my-dropdown',
            options=[{'label': i, 'value': i} for i in df["Place"]],
            placeholder="Select one of 47 French-speaking provinces of Switzerland",
            value='Courtelary'
        ),
        html.Div(id='my-div'),
    ], className="col-md-3"),

    html.Div([
        dcc.Graph(id='example-graph-dropdown')
    ], className="col-md-9"),
        
])

@app.callback(
    Output('my-div', 'children'),
    [Input('my-dropdown', 'value')])
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

@app.callback(
    Output('example-graph-dropdown', 'figure'),
    [Input('my-dropdown', 'value')])
def render_graphic(selected_city):
    filtered_city = df[df.Place == selected_city]
    values2 = filtered_city[["Catholic", "Protestant"]].values.flatten().tolist()
    return {
        'data': [go.Pie(
            labels=labels, 
            values=values2,
            hoverinfo='label+percent',
            textfont=dict(size=20),
            marker=dict(colors=colors, 
                        line=dict(color='#000000', width=2)))],
        'layout': go.Layout(title='Distribution of Religion in Percent at about 1888 in ' + 
                           selected_city + ', Switzerland. <br>Source: Mosteller & Tukey (1977)', 
                           height=450)
    }

# adds Bootstrap styles 3.3.7
app.css.append_css({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'})

if __name__ == '__main__':
    app.run_server(debug=True,  host='0.0.0.0')
