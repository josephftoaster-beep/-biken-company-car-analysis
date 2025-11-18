#modules/report_generator.py
import pandas as pd

def make_report(dataframe1,dataframe2):
    report_pivot01 = pd.pivot_table(dataframe1,
                                index=['年度','月度'],
                                columns='予約内容',
                                values='稼働時間_hour',
                                aggfunc='sum',
                                fill_value=0)
    report_pivot02 = pd.pivot_table(dataframe2,
                                 index='名前_統一',
                                 columns='予約内容',
                                 values='稼働時間_hour',
                                 aggfunc='sum',
                                 fill_value=0)
    report_pivot03 = pd.pivot_table(dataframe2,
                                    index = '名前_統一',
                                    columns =['年度','月度'],
                                    values = '稼働時間_hour',
                                    aggfunc='sum',
                                    fill_value=0)

    return report_pivot01,report_pivot02,report_pivot03