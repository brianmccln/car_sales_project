from dash import html, dcc, Output, Input
import plotly.express as px

def render(app,data):
    @app.callback(
            Output("bar-chart", "children"),
            Input("dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = data.query("Manufacturer in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div("No data selected", id="bar-chart")
        fig = px.bar(
            filtered_data,
            x = "Model",
            y = "Sales_in_thousands",
            title = f"{dropdown} Sales by Model"
        )
        return html.Div(dcc.Graph(figure=fig), id="bar-chart")
    return html.Div(id="bar-chart")