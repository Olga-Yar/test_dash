import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.express as px

from data.price_list.data_price import df, grouped_df_location_month_total, grouped_df_last_price, \
    grouped_df_last_price_sorted
from data.sales.data_sales import grouped_dfs_location_month_total
from figures.price_list.finishing_price import fig_line
from figures.price_list.finishing_price_last_month import fig_table_last_price
from figures.price_list.share_project_m2 import fig_share_project_location
from figures.sales.share_project_m2_sales import fig_share_project_location_sales
from figures.sales.sum_sales_project import fig_sum_sales_project
from selector import location_selector, project_selector

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    # header
    html.Div([
        dbc.Row([
            dbc.Col([
                html.H1('КОТЕЛ СПРОСА'),
            ],
                style={'margin-top': '10px',
                       'margin-left': '100px',
                       'color': 'white'},
                width={'size': 7},
            )
        ])
    ],
        className="header-pink"),
    html.Div(className="circle"),
    html.Div([
        dbc.Row([
            dbc.Col(
                html.H6('продукт | аналитика',
                        style={'color': 'white'},
                        className="app-tail")
            ),
            dbc.Col(
                html.Img(src=app.get_asset_url('logo/SML.png')),
                style={
                    'width': '100px',
                    'position': 'fixed',
                    'bottom': '20px',
                    'right': '100px',
                    'margin-bottom': '20px',
                }
            )])]),
    # html.Div(style={'backgroundColor': '#007bfc'}),
    # filters
    html.Div([
        dbc.Row([
            dbc.Col(
                dbc.DropdownMenu(
                    label='Выбор локации SMLT',
                    children=location_selector,
                    className='mb-3'
                ),
                width={'size': 6, 'offset': 0.1},
            ),
            dbc.Col(
                dbc.DropdownMenu(
                    label='Выбор проекта',
                    children=project_selector,
                    className='mb-3'
                ),
                width={'size': 6, 'offset': 0.1},)],
            className='app-body'),
    ]),
    # charts
    html.Div([
        dbc.Row([
            dbc.Col([
                html.Div(id='price-finishing-chart')
            ],
                width={'size': 8, 'offset': 0.1},
                style={
                    'text-align': 'center',
                }),
            dbc.Col([
                html.Div(id='table-last-price')
            ],
                width={'size': 4, 'offset': 0.1}
            )
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(id='share-project-location-sales')
            ],
                width={'size': 10, 'offset': 0.1},
                style={
                    'text-align': 'center',
                })
        ]),
        # dbc.Row([
        #     dbc.Col([
        #         html.Div(id='sum-sales-project')
        #     ],
        #         width={'size': 10, 'offset': 0.1},
        #         style={
        #             'text-align': 'center',
        #         })
        # ])
    ],
        className='app-body')
])


"""CALLBACKS"""


@app.callback(
    [
        Output(component_id='price-finishing-chart', component_property='children'),
        Output(component_id='share-project-location-sales', component_property='children'),
        Output(component_id='table-last-price', component_property='children'),
        # Output(component_id='sum-sales-project', component_property='children'),
        ],
    [
        Input(component_id='location-selector', component_property='value'),   # value == location
        Input(component_id='project-selector', component_property='value')   # value == project
     ]
)
def update_price_finishing_chart(location, project):
    if location is None:
        """ Возвращает пустой график, если не выбрана локация"""
        return html.Div()

    filtered_df = df[
        df['локация SMLT'].isin(location)
    ]

    if project is not None and len(project) > 0:
        filtered_df = df[filtered_df['нейминг'].isin(project)]

    grouped_dfs = grouped_dfs_location_month_total[
        grouped_dfs_location_month_total['локация SMLT'].isin(location)
    ]

    if project is not None and len(project) > 0:
        grouped_dfs = grouped_dfs[grouped_dfs['проект'].isin(project)]

    grouped_df_price = grouped_df_last_price_sorted[
        grouped_df_last_price_sorted['локация SMLT'].isin(location)
    ]

    if project is not None and len(project) > 0:
        grouped_df_price = grouped_df_last_price_sorted[grouped_df_price['нейминг'].isin(project)]

    fig_price_finishing = fig_line(filtered_df)

    html_fig_price_finishing = [
        html.Div('ЦЕНА ЧИСТОВАЯ, руб./м2'),
        dcc.Graph(figure=fig_price_finishing)
    ]

    fig_share_project_sales = fig_share_project_location_sales(grouped_dfs)
    html_fig_share_project_sales = [
        html.Div('ДОЛЯ СПРОСА, %'),
        dcc.Graph(figure=fig_share_project_sales)
    ]

    fig_table_price = fig_table_last_price(grouped_df_price)
    html_fig_table_last_price = [
        html.Div('ЧИСТОВАЯ ЦЕНА НА ПОСЛЕДНИЙ МЕСЯЦ'),
        dcc.Graph(figure=fig_table_price)
    ]

    # fig_sum_sales = fig_sum_sales_project(grouped_dfs)
    # html_fig_sum_sales_project = [
    #     html.Div('СПРОС, м2'),
    #     dcc.Graph(figure=fig_sum_sales)
    # ]

    return html_fig_price_finishing, html_fig_share_project_sales, html_fig_table_last_price


if __name__ == '__main__':
    app.run_server(debug=True)
