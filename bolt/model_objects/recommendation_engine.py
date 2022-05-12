from rake_nltk import Rake
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import joblib


class Recommender():
    
    def __init__(self):
        self.jobs_matrix = joblib.load('jobs_matrix.joblib')
        self.encoder = joblib.load('jobs_encoder.joblib') 
        self.jobs_df = joblib.load('jobs_filtered_data.joblib')
        self.key_extractor = Rake()
        
    def transform_input(self, description) -> str:
        """Helper function to transform """
        self.key_extractor.extract_keywords_from_text(description)
        key_words_dict_scores = self.key_extractor.get_word_degrees()
        key_words_list = list(key_words_dict_scores.keys())
        return ' '.join(key_words_list) 

    def recommend(self, user_description):
        """Function to recommend the best matching job based on the description"""
        #transform the user input (get the key-words)
        user_bag_of_words = self.transform_input(user_description)
        #encode the user input
        user_matrix = self.encoder.transform([user_bag_of_words])
        #calcule the similarities matrix
        cosine_sim = cosine_similarity(user_matrix, self.jobs_matrix)
        #append to dataFrame
        self.jobs_df['similarity'] = cosine_sim[0]
        #return the top 10 with greater similarity 
        return self.jobs_df.sort_values('similarity', ascending=False).head(10)