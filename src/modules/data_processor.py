#modules/data_processor.py

import pandas as pd
from glob import glob
from datetime import date

def load_and_combine_reservations(files):

    row_data = []

    for file in files:
        df = pd.read_csv(file,encoding = 'shift_jis')
        row_data.append(df)

    df = pd.concat(row_data,ignore_index=True)
    df = df.drop_duplicates()

    name_mapping = {
        'キムラヒロカズ':'木村博和',
        '古川':'古川洋子',
        '古川　修理の為':'古川洋子',
        '古川　点検のため':'古川洋子',
        '古谷篤史':'古市篤史',
        '古市　予約':'古市篤史',
        '古市　篤史':'古市篤史',
        '大橋':'大橋邦弘',
        '平賀　博之':'平賀博之',
        '日吉田':'日吉田拓哉',
        '日吉田 拓哉':'日吉田拓哉',
        '春田　真一':'春田真一',
        '木股':'木股寛',
        '木股　寛':'木股寛',
        '柏原':'柏原颯',
        '柏原 颯':'柏原颯',
        '神谷　信文':'神谷信文',
        '落合　則夫':'落合則夫',
        '西口':'西口映美',
        '西口　映美':'西口映美',
        '西村':'西村勝三',
        '西村　勝三':'西村勝三',
        '賚　純一':'賚純一',
        '越野　和久':'越野和久',
        '大川内　幸助':'大川内幸助'
    }
    df['名前_統一'] = df['名前'].map(name_mapping).fillna(df['名前'])
    df[['予約日','稼働時間']] = df['予約日時'].str.split(' ',n=1,expand=True)
    df[['利用開始時刻','利用終了時刻']] = df['稼働時間'].str.split('\r\n~',expand=True)
    df['利用開始時刻'] = df['利用開始時刻'].str.replace('：',':')
    df['利用終了時刻'] = df['利用終了時刻'].str.replace('：',':')
    df['予約日'] = pd.to_datetime(df['予約日'],errors='coerce')
    df['年度'] = df['予約日'].dt.year
    df['月度'] = df['予約日'].dt.month
    df['利用開始日時_str'] = df['予約日'].dt.strftime('%Y-%m-%d') +' '+df['利用開始時刻']
    df['利用終了日時_str'] = df['予約日'].dt.strftime('%Y-%m-%d') +' '+df['利用終了時刻']
    df['利用開始日時'] = pd.to_datetime(df['利用開始日時_str'],errors='coerce')
    df['利用終了日時'] = pd.to_datetime(df['利用終了日時_str'],errors='coerce')

    df = df.drop(columns=['予約日時','利用開始日時_str','利用終了日時_str','予約日','Unnamed: 11'], errors='ignore')

    df['稼働時間'] = (df['利用終了日時'] - df['利用開始日時'])
    df['稼働時間_hour'] = df['稼働時間'].dt.total_seconds()/3600

    three_month_ago = pd.Timestamp.now() - pd.DateOffset(months=3)
    df_recent = df[df['利用開始日時'] >= three_month_ago].copy()

    return df, df_recent
