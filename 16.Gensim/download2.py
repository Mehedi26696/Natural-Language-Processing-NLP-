import gensim.downloader as api

model = api.load("glove-twitter-25", return_path=True)
print("Model downloaded to:", model)