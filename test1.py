'''
Top 100 most Streamed Spotify
가장 많이 재생된 장르 순으로
'''
from tkinter.tix import IMAGE
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('E:\KOSTA-Python\PythonBigdata\cloud2.png')
imgArray = np.array(img)

df = pd.read_csv(
    'E:\KOSTA-Python\PythonBigdata\Top100mostStreamed.csv', encoding='utf-8')

df_genre_sample = df.loc[:, ['top genre']]  # 특정 열 선택
cnt_genre = Counter(df_genre_sample)

df_genre = df['top genre']
cnt = Counter(df_genre)
wc = dict(cnt)

wordcloud = WordCloud(font_path="E:\KOSTA-Python\PythonBigdata\BMJUA_ttf.ttf", width=400, height=400, max_font_size=100,
                      background_color='white', mask=imgArray).generate_from_frequencies(wc)

# wordcloud = wordcloud.generate(cnt)
wordcloud.to_file("first.png")
plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
