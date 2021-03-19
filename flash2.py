import re
import random
import streamlit as st
import numpy as np

#テキストの読み込み
source = '形容詞.txt'

f = open(source, encoding='utf-8')
d = f.read()
f.close()    

#正規表現
keys = re.findall(r'[^a-z\n]+', d)

#テキストの読み込み（答え）
source02 ='形容詞answer.txt'

f02= open(source02, encoding='utf-8')
d2 = f02.read()
f02.close()    

#正規表現
values = re.findall(r'[^a-z\n]+', d2)

word_dict = dict(zip(keys, values))
#print(word_dict)

st.title('古文単語確認～形容詞～')

"""
### 次の（　）の単語の意味を答えなさい。

"""

question_word = random.choice(keys)
correct_answer = word_dict[question_word]
c_answer=correct_answer

st.header(question_word)

values_copy = values.copy()
values_copy.remove(correct_answer)
wrong_answers = random.sample(values_copy, 3)

answer_options = [correct_answer] + wrong_answers
random.shuffle(answer_options)

st.subheader(answer_options)

expander = st.beta_expander('答えを表示する')
expander.header(c_answer)
    
button = st.button('次の問題を表示する')
