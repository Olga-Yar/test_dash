import plotly.express as px

from data.price_list.data_price import df
from global_design import COLOR_PROJECT


def fig_line(filtered_df):
    """Создание графика с ценой"""
    fig = px.line(
            filtered_df,
            x='дата',
            y='price_finishing',
            color='нейминг',
            color_discrete_map=COLOR_PROJECT,
            category_orders={'дата': df['дата'].unique()}
        )
    fig.update_layout(
        plot_bgcolor='#f5f7f7',
        legend=dict(orientation='h', yanchor='bottom', y=-0.3, x=.5, xanchor="center"),
        showlegend=True,
        xaxis=dict(title=dict(text='')),
        yaxis=dict(title=dict(text=''))
    )
    return fig
