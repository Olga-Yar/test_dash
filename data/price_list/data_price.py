from datetime import datetime

import pandas as pd


df = pd.read_csv('data/price_list/SMLT_PRICE.csv')

project_list = df['нейминг'].unique()

location_list = df['локация SMLT'].unique()
# print(df.info())

# замена . на , в числах с плавающей точкой
df['м2'] = df['м2'].str.replace(',', '.')
df['микс'] = df['микс'].str.replace(',', '.')
df['базовая'] = df['базовая'].str.replace(',', '.')
df['чистовая'] = df['чистовая'].str.replace(',', '.')

# изменение типа данных в столбцах
df['дата_факт'] = pd.to_datetime(df['дата_факт'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d')
df['дата_факт'] = pd.to_datetime(df['дата_факт'], format='%Y-%m-%d')
df['м2'] = df['м2'].astype(float)
df['микс'] = df['микс'].astype(float)
df['базовая'] = df['базовая'].astype(float)
df['чистовая'] = df['чистовая'].astype(float)
df['дата'] = pd.to_datetime(df['дата'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d')
df['дата'] = pd.to_datetime(df['дата'], format='%Y-%m-%d')

# расчетные столбцы
df['price_finishing'] = (df['чистовая'] / df['м2']).astype(int)
df['avg_m2'] = (df['м2'] / df['шт']).astype(float)

df['индекс'] = df['индекс'].fillna('0')
df['индекс'] = df['индекс'].astype(int)

# ЦЕНА ЧИСТОВАЯ. Группируем данные по дате, месяцу и году и вычисляем среднее значение цены
grouped_df = df.groupby(['дата', 'нейминг', 'локация SMLT'])['price_finishing'].mean().reset_index()


# ЦЕНА ЧИСТОВАЯ на послледний месяц.
today = datetime.today().replace(day=1)
filtered_last_date = df[df['дата'].dt.strftime('%Y-%m') == today.strftime('%Y-%m')]
grouped_df_last_price = filtered_last_date.groupby(['дата', 'нейминг', 'локация SMLT'])['price_finishing'].mean().reset_index()
grouped_df_last_price['price_finishing_short_K'] = grouped_df_last_price['price_finishing'] / 1000

grouped_df_last_price['price_finishing_short_K'] = grouped_df_last_price['price_finishing_short_K'].astype(int)
grouped_df_last_price_sorted = grouped_df_last_price.sort_values('price_finishing_short_K', ascending=False)

# ДАТА ПЕРВОГО ПОЯВЛЕНИЯ В ПРАЙСЕ, если это не начало года

# ДОЛЯ проекта в локации в динамике. Группировка данных по локации, месяцу и проекту для расчета доли
grouped_df_location_month = df.groupby(['локация SMLT', 'дата', 'нейминг', 'индекс'])['м2'].sum().reset_index()

# расчет общего количества м2 по локации и месяцам
grouped_df_location_total = grouped_df_location_month.groupby(['локация SMLT', 'дата'])['м2'].sum().reset_index()

# объединение данных для расчета доли
grouped_df_location_month_total = pd.merge(grouped_df_location_month, grouped_df_location_total,
                                           on=['локация SMLT', 'дата'])

# расчет доли каждого проекта
grouped_df_location_month_total['доля'] = (
        (grouped_df_location_month_total['м2_x'] / grouped_df_location_month_total['м2_y'])
        * 100).astype(int)

# сортировка по индексу
grouped_df_location_month_total = grouped_df_location_month_total.sort_values(by='индекс', ascending=False)



# print(df.info())
# print(grouped_df)
# print(grouped_df_location_date)
# print(grouped_df_location_month_total)
# print(df[df['индекс'] > 0]['индекс_проект'].unique())
# print(grouped_df_last_price.head(5))





