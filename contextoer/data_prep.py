import os
from config import DATA_DIR

import gensim.downloader as api
import nltk
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer

import numpy as np

# Download the all nltk corpus, this will only happen once
# nltk.download('all')

# if os.path.exists(os.path.join(DATA_DIR, "vocabs.txt")):
#     with open(os.path.join(DATA_DIR, "vocabs.txt"), "r") as f:
#         vocabs = f.read().split("\n")

# # save vocabs from gensim if it does not exist
# else: 
#     # download the model from gensim 
#     model = api.load("word2vec-google-news-300")

#     # Extract the words from the model
#     vocabs= list(model.key_to_index.keys())

#     with open(os.path.join(DATA_DIR, "vocabs.txt"), "w") as f:
#         f.write("\n".join(vocabs))
 
# save filtered words if it does not exist
if not os.path.exists(os.path.join(DATA_DIR, "vocabs.txt")):
    
    model = api.load("word2vec-google-news-300")

    # Extract the words from the model
    raw_vocabs = list(model.key_to_index.keys())

    lemmatizer = WordNetLemmatizer()

    english_words = set(words.words()) 

    vocabs = [] # list of words that are in the model and is valid in the English language
    for w in raw_vocabs:
        word= w.lower()
        lemma = lemmatizer.lemmatize(word, pos='n')

        if lemma == word and word in english_words and word not in vocabs:
            vocabs.append(word)
    
    with open(os.path.join(DATA_DIR, "vocabs.txt"), "w") as f:
        f.write("\n".join(vocabs))


if not os.path.exists(os.path.join(DATA_DIR, "vocab_embeddings.npy")):
    vocab_embeddings= np.stack([model[word] for word in vocabs if word in model])
    np.save(os.path.join(DATA_DIR, 'vocab_embeddings.npy'), vocab_embeddings)

