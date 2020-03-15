import dash
from dash.dependencies import  Input,Output
import dash_core_components as dcc
import dash_html_components as html

app= dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash Initialization'),
    dcc.Graph(id='example',
              figure={
                  'data':[
                      {'x':[1,2,3,4,5,6],'y':[6,5,4,3,2,1], 'type':'line', 'name':'boats'},
                      {'x':[1,2,3,4,5,6],'y':[6,7,3,9,5,10], 'type':'bar', 'name':'car'},
                  ],
                  'layout':{
                      'title':'Basic Dash Example'
                  }
              }
              )

])

if __name__=='__main__':
    app.run_server(debug=True,port=8000)