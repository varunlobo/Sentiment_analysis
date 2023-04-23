# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:55:35 2023

@author: varulobo
"""

import streamlit as st

from textblob import TextBlob

st.header("Analyzing text sentiments using NLTK library in Python")


expander = st.expander("What is NLTK ?")
expander.write("NLTK stands for Natural Language Took Kit.It is a standard python library that provides a set of diverse algorithms for Natural Language Processing (NLP).\
               It is one of the most used libraries for NLP and Computational Linguistics.\
            NLTK is a leading platform for building Python programs to work with human language data")
 
 
text = st.text_input("Insert text here:")



blob = TextBlob(text)

sentiment = blob.sentiment.polarity

if st.button("Show Sentiment"):
    
    if sentiment >= 0.0:
     
        st.success(sentiment)
        
    else:
        st.error(sentiment)
        
        
st.caption("Sentiment is displayed in the form of polarity which lies between [-1,1], -1 defines a negative sentiment and 1 defines a positive sentiment.\
           0 is neutral sentiment.")
           
           
           