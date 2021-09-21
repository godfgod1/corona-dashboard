import pandas as pd

conditions =['confirmed','deaths','recovered']

daily_df = pd.read_csv('data/daily_report.csv')

#! 전세계 일일 현황(전 세계 현황 차트)
#* 매일 전체 확진자, 사망자, 완치자 지역별로

totals_df = (
    daily_df[['Country_Region','Confirmed','Deaths','Recovered']].sum().reset_index(name='count')
)

totals_df = totals_df.rename(columns={"index":"condition"})


#! 국가별 확진자, 사망자, 완치자 수 현황(테이블과 지도)
countries_df = daily_df[['Country_Region','Confirmed','Deaths','Recovered']]
countries_df  = countries_df.groupby('Country_Region').sum().sort_values(by="Confirmed",ascending=False).reset_index()



dropdown_options = countries_df.sort_values("Country_Region").reset_index()
dropdown_options = dropdown_options["Country_Region"]

#! 전세계 확진자 총합, 완치자 총합, 사망자총합(차트,국가별 필터링)
def make_global_df():
    def make_df(condition):
        df = pd.read_csv(f'data/time_{condition}.csv')
        df = df.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum().reset_index(name=condition)
        df = df.rename(columns={'index':'date'})
        return df 
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)

        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df



#! 국가별별 일일 코로나 현황
def make_country_df(country):
    def make_df(condition):
        df = pd.read_csv(f'data/time_{condition}.csv')
        df = df.loc[df["Country/Region"] == country]
        df = df.drop(columns = ["Province/State","Country/Region","Lat","Long"]).sum().reset_index(name=condition)
        df = df.rename(columns={'index':'date'})
        return df
    final_df = None
    for condition in conditions:
        condition_df =  make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)

    return final_df

