from dash import html, dcc, Output, Input
import plotly.express as px

def render(app,data):
    @app.callback(
            Output("scatter", "children"),
            Input("dropdown","value")
    )
    def update_scatter_chart(dropdown):
        filtered_data = data.query("Manufacturer in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div("No data selected", id="scatter")
        s = [i*20 for i in filtered_data["Price_in_thousands"]]
        fig = px.scatter(
            filtered_data,
            x = "Model",
            y = "Price_in_thousands",
            size=s,
            title = f"{dropdown} Price by Model Scatter"
        )
        return html.Div(dcc.Graph(figure=fig), id="scatter")
    return html.Div(id="scatter")