import pandas as pd

dfs = pd.read_csv('data/sales/SMLT_SALES.csv')

# project_list = dfs['проект'].unique()

# location_list = dfs['локация SMLT'].unique()

# замена . на , в числах с плавающей точкой
dfs['м2'] = dfs['м2'].str.replace(',', '.')

# изменение типа данных в столбцах
dfs['дата'] = pd.to_datetime(dfs['дата'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d')
dfs['дата'] = pd.to_datetime(dfs['дата'])
dfs['м2'] = dfs['м2'].astype(float)
dfs['индекс'] = dfs['индекс'].fillna('0')
dfs['индекс'] = dfs['индекс'].astype(int)
dfs['кол-во месяцев для темпа'] = dfs['кол-во месяцев для темпа'].astype(int)


# ДОЛЯ проекта в локации в динамике. Группировка данных по локации, месяцу и проекту для расчета доли
grouped_dfs_location_month = dfs.groupby(['локация SMLT', 'дата', 'проект', 'индекс'])['м2'].sum().reset_index()

# расчет общего количества м2 по локации и месяцам
grouped_dfs_location_total = grouped_dfs_location_month.groupby(['локация SMLT', 'дата'])['м2'].sum().reset_index()

# объединение данных для расчета доли
grouped_dfs_location_month_total = pd.merge(grouped_dfs_location_month, grouped_dfs_location_total,
                                            on=['локация SMLT', 'дата'])

# расчет доли каждого проекта
grouped_dfs_location_month_total['доля'] = (
        (grouped_dfs_location_month_total['м2_x'] / grouped_dfs_location_month_total['м2_y'])
        * 100).astype(int)

# сортировка по индексу
grouped_dfs_location_month_total = grouped_dfs_location_month_total.sort_values(by='индекс', ascending=False)

# сортировка по индексу изначальную таблицу
sorted_dfs = dfs.sort_values(by='индекс', ascending=False)

# print(dfs.info())
# print(dfs.groupby('дата').head(5))
# print(grouped_dfs_location_month_total.head(5))
