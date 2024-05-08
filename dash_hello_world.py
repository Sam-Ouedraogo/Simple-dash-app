from dash import Dash, html, dcc

#Initialize the app
app = Dash(__name__)

#App layout
app.layout = html.Div([
    html.Div(children='Hello World')
])

#run app
if __name__ == '__main__':
    app.run(debug=True)
