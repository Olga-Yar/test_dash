import dash_core_components as dcc

from data.price_list.data_price import project_list, location_list

# project_options = [{'label': project, 'value': project} for project in project_list if any(loc in selected_location for loc in project_location_mapping.get(project, []))]

project_selector = dcc.Dropdown(
    id='project-selector',
    options=[{'label': project, 'value': project} for project in project_list],
    # value=[df[df['локация SMLT'] == location_selector]['индекс_нейминг']],
    multi=True
)

location_selector = dcc.Dropdown(
    id='location-selector',
    options=[{'label': location, 'value': location} for location in location_list],
    value=['АЛХИМОВО / ОСТАФЬЕВО / ПОДОЛЬСКИЕ КВАРТАЛЫ / ЭКО БУНИНО'],
    multi=True
)
