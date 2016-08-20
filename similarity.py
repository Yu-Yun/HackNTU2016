import jieba
import os_weight
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


### document into tuple format
doc_file = open('data/allsents.txt','r').read()
doc_split = doc_file.split('\n')
doc_split = list(text) + doc_split
# TODO: check the variable name of the input text


def seg(sent):
    res = jieba.cut(sent)
    return ' '.join(res)

def similarity(corpus):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    res = cosine_similarity(tfidf_matrix[0], tfidf_matrix).tolist()
    return sorted(res[0])[-2]


# TODO: 把 svm 的 func 引進來分析 unknown sent, 把預測出來的 label 餵入 sub_cat() 裡面找 key
# 少一個 new_label 的 variable name

def adjusted_sim(new_label):
    sub_cat = os_weight.sub_cat()
    os_res = sub_cat[new_label]
    adjusted = similarity() * os_res
    return adjusted
    

doc_seg = [seg(i) for i in doc_split]

corpus = tuple(doc_seg)



if __name__ == "main":
    similarity(corpus)
    adjusted_sim(new_label)


