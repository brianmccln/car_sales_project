from dash import Dash,html
import dash_bootstrap_components as dbc
from components import dropdown, bar_chart,scatter

def create_layout(app,data):
    return dbc.Container(
        [
            dbc.Row(
                [   
                    html.H1("Care Sales Analysis"),
                    html.P("Find The Right Used Car For You. Search By Price, Make, Model, Mileage And More!"),
                    html.Img(src=Dash.get_asset_url(app,'car.png'),
                             style={'height':300,'width':600}),
                    dropdown.render(app,data)
                    ]
                ),
            dbc.Row(
                [
                    dbc.Col(bar_chart.render(app,data),lg=6),
                    dbc.Col(scatter.render(app,data),lg=6)
                ]
            )
        ]
    )