import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc

from selector import location_selector


layout = html.Div([
    html.Div([
            # filters
            dbc.Row([
                dbc.Col([
                    html.H6('Выбор локации SMLT'),
                    html.Div(location_selector),
                ],
                    width={'size': 3, 'offset': 0.1}),
            ]
            )
        ],
            className='app-body',
        )
    ])

