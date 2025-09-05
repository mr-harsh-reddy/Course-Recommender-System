from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_recommendations(user_input, courses_df):
    # Combine course title and description into one text string.
    courses_df['combined'] = courses_df['course_title'].fillna('') + ' ' + courses_df['course_description'].fillna('')
    documents = courses_df['combined']

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Vectorize the user input and compute cosine similarity
    query_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    top_indices = similarities.argsort()[-5:][::-1]
    return courses_df.iloc[top_indices][['course_title', 'course_url']].to_dict(orient='records')

