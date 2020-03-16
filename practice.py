#need to optimizion code of solving .py
import datetime
import dash
import dash_html_components as html
from dash.dependencies import Output,Input

app=dash.Dash(__name__)

def rahi():
    return html.H1('THis is time:'+str(datetime.datetime.now()))
app.layout= rahi


if __name__ == '__main__':
    app.run_server(debug=True)