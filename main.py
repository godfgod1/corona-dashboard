import pandas as pd
daily_df = pd.read_csv('data/daily_report.csv')


totals_df = (
    daily_df[['Country_Region','Confirmed','Deaths','Recovered']].sum().reset_index(name='count')
)
totals_df = totals_df.rename(columns={"index":"condition"})

daily_df = daily_df[['Country_Region','Confirmed','Deaths','Recovered']]
daily_df  = daily_df.groupby('Country_Region').sum()
daily_df

