import plotly.express as px

from data.sales.data_sales import grouped_dfs_location_month_total
from global_design import COLOR_PROJECT


def fig_sum_sales_project(data):
    """Объем продаж по проекту в локации в динамике"""
    fig = px.bar(
        data,
        x='дата',
        y='м2_x',
        color='проект',
        color_discrete_map=COLOR_PROJECT,
        category_orders={'дата': grouped_dfs_location_month_total['дата'].unique()},
        barmode='stack',
        text='м2_x'
    )
    fig.update_traces(textangle=360, textfont_size=14)
    fig.update_layout(
        plot_bgcolor='#f5f7f7',  # Установить цвет фона графика
        legend=dict(orientation='h', yanchor='bottom', y=-0.3, x=.5, xanchor="center"),
        showlegend=True,
        xaxis=dict(title=dict(text='')),
        yaxis=dict(title=dict(text=''))
    )
    return fig