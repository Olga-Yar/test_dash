import plotly.express as px

from data.price_list.data_price import grouped_df_location_month_total
from global_design import COLOR_PROJECT


def fig_share_project_location(filtered_df):
    """Нормированный график с долей по проекту в локации в динамике"""
    fig = px.bar(
        filtered_df,
        x='дата',
        y='доля',
        color='нейминг',
        color_discrete_map=COLOR_PROJECT,
        category_orders={'дата': grouped_df_location_month_total['дата'].unique()},
        barmode='stack',
        text='доля'
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
