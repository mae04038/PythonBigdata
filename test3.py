'''
Streams based on Artist Followers
'''
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

df = pd.read_csv(
    'E:\KOSTA-Python\PythonBigdata\spotify_dataset.csv', encoding='utf-8')
new_df = df.sort_values(
    by=['Artist Followers'], axis=0, ascending=False)  # 팔로워수 기준으로 artist 내림차순 정렬
only_df = new_df.drop_duplicates(['Artist'])  # 가수 이름 중복 제거
only_df = only_df.head(500)  # 상위 500명의 artist만 뽑기.
only_df = only_df.astype({'Artist Followers': 'int'})  # 특정 열 형 변환

sort_chart = only_df.sort_values(by=['Artist Followers'], ascending=True)

plt.figure(figsize=(25, 8))
plt.title("Streams based on Artist Followers")
sns.barplot(x='Artist Followers',
            y='Streams', data=sort_chart.head(30))

plt.savefig("third.png")
