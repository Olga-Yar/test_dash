import plotly.express as px
import plotly.graph_objects as go
from global_design import COLOR_PROJECT


def fig_table_last_price(grouped_df_last_price_sorted):
    """Создание таблицы с ценой на последний месяц"""
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>проект</b>', '<b>текущая цена</b>'],
            line_color='white',
            fill_color='#c6e6ff',
            align='center',
            font=dict(color='black', size=14)
        ),
        cells=dict(
            values=[grouped_df_last_price_sorted['нейминг'], grouped_df_last_price_sorted['price_finishing_short_K']],
            line_color='#f5f7f7',
            fill_color='white',
            align='center',
            font=dict(color='black', size=12)
        )
    )])

    return fig
