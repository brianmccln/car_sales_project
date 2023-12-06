from dash import html, dcc 

def render(app, data):
    all_cars = data["Manufacturer"].unique()
    car_makes = [{"label":make, "value":make} for make in all_cars]
    return html.Div(
        [
            dcc.Dropdown(
                options=car_makes,
                placeholder="Choose your car",
                value="BMW",
                multi=False,
                id="dropdown"
            )
        ]
    )