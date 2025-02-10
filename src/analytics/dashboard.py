import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/transformed_data.csv")

app = dash.Dash(__name__)
fig = px.bar(df, x="product", y="price", title="Product Prices")

app.layout = html.Div([dcc.Graph(figure=fig)])

if __name__ == "__main__":
    app.run_server(debug=True)
