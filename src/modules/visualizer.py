#modules/visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib
from datetime import date

def visualize_report(report01,report02,report03):

    today = date.today().strftime('%Y%m%d')

    plt.figure(figsize=(12,6))
    report01.plot(kind='line', ax=plt.gca(),marker='o')
    plt.title('月度別・社有車別 稼働時間の推移')
    plt.xlabel('(年度,月度)')
    plt.ylabel('総稼働時間(時間)')
    plt.legend()
    plt.grid(True,linestyle='--',alpha=0.6)
    plt.tight_layout()
    plt.savefig(f'company_car_usage_{today}.png')
    plt.show

    plt.figure(figsize=(12,10))
    sns.heatmap(
        report02,
        annot=True,
        fmt='.1f',
        cmap='Blues',
        linewidths=.5,
        cbar_kws={'label':'総稼働時間(Hour)'}
    )
    plt.title('利用者別・社有車別 稼働時間ヒートマップ', fontsize=16)
    plt.xlabel('車両ナンバー',fontsize=12)
    plt.ylabel('社員名', fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f'company_car_heatmap_{today}.png')
    plt.show

    total_usage_by_user = report03.sum(axis=1)
    sorted_index = total_usage_by_user.sort_values(ascending=True).index
    report03_sorted = report03.reindex(sorted_index)

    plt.figure(figsize=(20,10))
    report03_sorted.plot.barh()
    plt.title('月度別・利用者別 総稼働時間(Hours)')
    plt.xlabel('総稼働時間(時間)')
    plt.xticks(rotation=45)
    plt.ylabel('利用者')
    plt.legend(title='月度',bbox_to_anchor=(1.05,1),loc='upper left')
    plt.grid(axis='y',linestyle='--',alpha=0.6)
    plt.tight_layout()
    plt.savefig(f'company_car_user_{today}.png')
    plt.show()