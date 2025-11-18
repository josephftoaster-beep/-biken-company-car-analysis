#main.py
import sys
import os
import pandas as pd
from datetime import date
from glob import glob

csv_file_path = r'C:\Users\robek\Github\biken-car-analyser\data'
csv_file_pattern = os.path.join(csv_file_path,'ご予約リスト_*.csv')
files = glob(csv_file_pattern)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.modules.data_processor import load_and_combine_reservations
from src.modules.report_generator import make_report
from src.modules.visualizer import visualize_report
from src.modules.export_excel import export_report_to_excel

# 1. 共通変数の定義
today = date.today().strftime('%Y%m%d')
file_name = f'月別_社有車別_総稼働時間_{today}.xlsx'
sheet_name = '月別_社有車別_稼働時間'

def main():
    print("--- 1. データ処理開始 ---")
    df1,df2 = load_and_combine_reservations(files)
    
    if df1.empty:
        print("処理するデータがありません。")
        return

    print("--- 2. レポートテーブル生成 ---")
    # 3つのレポートを同時に受け取る
    repo1, repo2, repo3 = make_report(df1,df2)
    
    print("--- 3. グラフ描画と保存 ---")
    # today 変数を visualize_report に渡す
    visualize_report(repo1, repo2, repo3)
    
    print("✅ 全処理完了: レポート画像を保存しました。")

    export_report_to_excel(repo1,file_name,sheet_name)

if __name__ == "__main__":
    # このファイルが直接実行された場合に main() 関数を呼び出す
    main()