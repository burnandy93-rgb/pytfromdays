from wordcloud import WordCloud
import matplotlib.pyplot as plt 
text = """
Dad Hero Guide Support Love
Strong Caring Mentor Friend
"""
wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()