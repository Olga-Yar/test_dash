import plotly.graph_objects as go

from color_project_list import COLOR_PROJECT_LIST

# GLOBAL DESIGN SETTINGS
CHARTS_TEMPLATE = go.layout.Template(
    layout=dict(
        font=dict(
            family='assets/font/CoFoSans-Regular.ttf',
            size=12
        ),
        legend=dict(
            orientation='h',
            title_text='',
            x=0,
            y=1.1
        )
    )
)

COLOR_STATUS_VALUES = [
    'lightgray',
    '#1F85DE',
    '#f90f04'
]

COLOR_PROJECT = COLOR_PROJECT_LIST
