import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input
import pandas as pd
import plotly.graph_objects as go

app=dash.Dash(__name__)

date = pd.read_csv('SynesisIT.csv',sep=";")['Date']


app.layout=html.Div(id='root',children=[

    html.H1('Web based data visualization',style={'text-align':'center'}),
    # dropdown
    html.Div([
        html.Label("Select X Series Data"),
        dcc.Dropdown(id='x-data',
                     options=[{'label': i, 'value': i} for i in set(date)],
                     multi=True
                     )
    ], ),
    html.Div(id='output'),





])


@app.callback(Output(component_id='output',component_property='children'),
             [Input(component_id='x-data',component_property='value')])

def update_all(data_by_search):
    date = pd.read_csv('SynesisIT.csv', sep=";")['Date']
    time = pd.read_csv('SynesisIT.csv', sep=";")['Time']
    datetime = list(date + ' ' + time)

    total_current = list(pd.read_csv('SynesisIT.csv', sep=";")['sum_of_line_currents'])
    total_power = list(pd.read_csv('SynesisIT.csv', sep=";")['total_system_power'])

    power_factor = list(pd.read_csv('SynesisIT.csv', sep=";")['total_system_power_factor'])

    if data_by_search is not None:
        data = pd.read_csv('SynesisIT.csv', sep=";")
        for date in list(data_by_search):
            data = data[data['Date']==date]


        datetime=list(data['Date']+' '+data['Time'])
        total_current= list(data['sum_of_line_currents'])
        total_power = list(data['total_system_power'])
        power_factor = list(data['total_system_power_factor'])

        return [
            html.Div(id='All', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
                        {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
                        {'x': datetime, 'y': power_factor, 'type': 'lines', 'name': 'Power Factor'},
                    ],
                    'layout': {
                        'title': 'All'
                    }
                }), ]),

            html.Div(id='total_current', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
                    ],
                    'layout': {
                        'title': 'Total Current'
                    }
                }), ]),

            html.Div(id='total_power', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
                    ],
                    'layout': {
                        'title': 'Total Power'
                    }
                }), ]),

            html.Div(id='power_factor', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': power_factor, 'type': 'lines', 'name': 'Power Factor'},
                    ],
                    'layout': {
                        'title': 'Power Factor'
                    }
                }), ]),
        ]


    return [
            html.Div(id='All', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
                        {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
                        {'x': datetime, 'y': power_factor, 'type': 'lines', 'name': 'Power Factor'},
                    ],
                    'layout': {
                        'title': 'All'
                    }
                }), ]),

            html.Div(id='total_current', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
                    ],
                    'layout': {
                        'title': 'Total Current'
                    }
                }), ]),

            html.Div(id='total_power', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
                    ],
                    'layout': {
                        'title': 'Total Power'
                    }
                }), ]),

            html.Div(id='power_factor', children=[
                dcc.Graph(figure={
                    'data': [
                        {'x': datetime, 'y': power_factor, 'type': 'lines', 'name': 'Power Factor'},
                    ],
                    'layout': {
                        'title': 'Power Factor'
                    }
                }), ]),
        ]


if __name__ == '__main__':
    app.run_server(debug=True)