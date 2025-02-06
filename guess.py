import gensim.downloader as api

def main():
    model= api.load('word2vec-google-news-300')