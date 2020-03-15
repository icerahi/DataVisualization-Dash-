import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input
import pandas as pd
import plotly.graph_objects as go

app=dash.Dash()

date = pd.read_csv('SynesisIT.csv',sep=";")['Date']
time = pd.read_csv('SynesisIT.csv',sep=";")['Time']
datetime=list(date+' '+time)
total_current = list(pd.read_csv('SynesisIT.csv',sep=";")['sum_of_line_currents'])
total_power = list(pd.read_csv('SynesisIT.csv',sep=";")['total_system_power'])

power_factor = list(pd.read_csv('SynesisIT.csv',sep=";")['total_system_power_factor'])

app.layout=html.Div([
    html.H1('Web Based Data Visualization',style={'text-align':'center'}),
    #dropdown
    html.Div([
                  html.Label("Select X Series Data"),
                dcc.Dropdown(id='x-data',
                             options=[{'label': i, 'value': i} for i in set(date)],
                             multi=True
                )
            ],),


    html.Div(id='total_current', children=[
        dcc.Graph(figure={
            'data': [
                {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
            ],
            'layout': {
                'title': 'Total Current'
            }
        }),
    ]),

    # html.Div(id='all_in_one',children=[
    #     dcc.Graph(id='all', figure={
    #         'data': [
    #             {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
    #             {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
    #             {'x': datetime, 'y': power_factor, 'type': 'lines', 'name': 'Power Factor'},
    #         ],
    #         'layout': {
    #             'title': 'All'
    #         }
    #     }),
    #
    # ]),


])

@app.callback(
    Output(component_id='total_current',component_property='children'),
 [Input(component_id='x-data',component_property='value')])

def update_graph(date_of_data):
    data = pd.read_csv('SynesisIT.csv', sep=";")
    if date_of_data is not None:
        for date in list(date_of_data):
            data = data[data['Date']==date]


        datetime =list(data['Date']+' '+data['Time'])

        total_current = list(data['sum_of_line_currents'])
        total_power = list(data['total_system_power'])
        power_factor = list(data['total_system_power_factor'])

        return [

        dcc.Graph(figure={
            'data': [
                {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
            ],
            'layout': {
                'title': 'Total Current'
            }
        }),
    ]

# app.layout=html.Div(children=[
#     html.Div(id='total_current', children=[
#         dcc.Graph(figure={
#             'data': [
#                 {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
#             ],
#             'layout': {
#                 'title': 'Total Current'
#             }
#         }),
#     ]),
#
#     html.Div(id='total_power', children=[
#         dcc.Graph(figure={
#             'data': [
#                 {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
#             ],
#             'layout': {
#                 'title': 'Total Power'
#             }
#         }),
#     ]),
#
#     html.Div(id='total_factor', children=[
#         dcc.Graph(figure={
#             'data': [
#                 {'x': datetime, 'y': power_factor, 'type': 'lines', 'name': 'Power Factor'},
#             ],
#             'layout': {
#                 'title': 'Power Factor'
#             }
#         }),
#
#     ]),
# ])


        # return dcc.Graph(
        #     figure=go.Figure(
        #         data=go.Scatter(x=datetime,y=total_current,mode='lines+markers'),
        #      )
        # )





"""
dcc.Graph(id='total_current',
                      figure={
                          'data': [
                              {'x': datetime, 'y': total_current, 'type': 'lines+markers', 'name': 'Total Current'},
                          ],
                          'layout': {'title': 'Total Current'}
                      }),

            dcc.Graph(id='total_power',
                      figure={
                          'data': [
                              {'x': datetime, 'y': total_power, 'type': 'lines+markers', 'name': 'Total Power'},
                          ],
                          'layout': {'title': 'Total Power'}
                      }),

            dcc.Graph(id='total_factor',
                      figure={
                          'data': [
                              {'x': datetime, 'y': power_factor, 'type': 'lines+markets', 'name': 'Power Factor'},
                          ],
                          'layout': {'title': 'Power Factor'}
                      })
"""


if __name__ == '__main__':
    app.run_server(debug=True,port=4200)