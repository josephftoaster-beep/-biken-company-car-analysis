#modules/export_excel.py
import pandas as pd

def export_report_to_excel(pivot_table,file_name,sheet_name):
    car_list = [
        '和泉581み9657 (積算部管理)',
        '和泉581は5240 (積算部管理)',
        '和泉581む1869 (積算部管理)',
        '和泉581く9368 (安品ア室管理)',
        '和泉581の6302 (安品ア室管理)'
        ]
    pivot_table = pivot_table[car_list]
    with pd.ExcelWriter(file_name, engine='openpyxl', mode='w') as writer:
        pivot_table.to_excel(writer,sheet_name = sheet_name)