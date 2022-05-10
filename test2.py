'''
Spotify Top 200 Charts (2020-2021)에 있는 artist들을 
팔로워수가 많은 artist 순으로
'''
from audioop import reverse
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('E:\KOSTA-Python\PythonBigdata\musiclogo2.JPG')
imgArray = np.array(img)

df = pd.read_csv(
    'E:\KOSTA-Python\PythonBigdata\spotify_dataset.csv', encoding='utf-8')

df_artist_sample = df.loc[:, ['Artist', 'Artist Followers']]  # 새로운 데이터 프레임.
df_artist = df['Artist']
df_artist_followers = df['Artist Followers']

new_df = df_artist_sample.sort_values(
    by=['Artist Followers'], axis=0, ascending=False)  # 팔로워수 기준으로 artist 내림차순 정렬
only_df = new_df.drop_duplicates(['Artist'])  # 가수 이름 중복 제거
only_df = only_df.head(500)  # 상위 500명의 artist만 뽑기.
only_df = only_df.astype({'Artist Followers': 'int'})  # 특정 열 형 변환

wc = only_df.set_index("Artist").to_dict()["Artist Followers"]
# print(wc)

wordcloud = WordCloud(font_path="E:\KOSTA-Python\PythonBigdata\BMJUA_ttf.ttf", colormap="Dark2", width=400, height=400,
                      max_font_size=100, background_color='white', mask=imgArray).generate_from_frequencies(wc)

wordcloud.to_file("second.png")
plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
