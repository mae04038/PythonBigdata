'''
Top 10 Highest Charting Songs
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

sort_chart = df.sort_values(by=['Highest Charting Position'], ascending=True)
plt.figure(figsize=(25, 8))
plt.title("Top 10 Highest Charted Songs")
sns.barplot(x='Number of Times Charted',
            y='Song Name', data=sort_chart.head(10))
plt.savefig("forth.png")


# new_df = df.head(200)

# plt.figure(figsize=(10, 8))
# plt.title("Popularity based on Loudness")
# sns.scatterplot(x='Popularity', y='Loudness', data=new_df)
# plt.savefig("third.png")
