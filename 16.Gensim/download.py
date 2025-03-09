import gensim.downloader as api

model = api.load("word2vec-google-news-300", return_path=True)
print("Model downloaded to:", model)
