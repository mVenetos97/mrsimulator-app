# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from app.custom_widgets import custom_slider

__author__ = ["Maxwell C. Venetos"]
__email__ = ["venetos.5@buckeyemail.osu.edu"]


def gaussian_linebroadening_widget(i):

    broadeningFunction = dcc.RadioItems(
        options=[
            {"label": "Lorentzian", "value": 0},
            {"label": "Gaussian", "value": 1},
        ],
        value=0,  # "Lorentz",
        labelStyle={"display": "inline-block", "width": "50%"},
        id=f"Apodizing_function-{i}",
    )

    broaden_range = {
        0: "0",
        200: "200",
        400: "400",
        600: "600",
        800: "800",
        1000: "1000",
    }
    line_broadening = custom_slider(
        label="Line Broadening",
        return_function=lambda x: f"\u03BB = {x/1000} kHz",
        min=0,
        max=1000,
        step=25,
        value=25,
        marks=broaden_range,
        id=f"broadening_points-{i}",
    )

    return html.Div(
        [broadeningFunction, line_broadening, html.Br()],
        className="collapsible-body-control form",
    )

    # return [line_broadening]
