import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
df = pd.read_csv('imdb_top_1000.csv')
df.dropna(inplace=True)
df = df[['Series_Title', 'Genre', 'Director', 'Overview', 'IMDB_Rating']]

def combine_features(row):
    return f"{row['Genre']} {row['Director']} {row['Overview']}"

df['combined'] = df.apply(combine_features, axis=1)

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index mapping
df = df.reset_index(drop=True)
indices = pd.Series(df.index, index=df['Series_Title'].str.lower())

# Recommend function
def recommend_movies(title, num=5):
    idx = indices.get(title.lower())
    if idx is None:
        return ["Movie not found."]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['Series_Title'].iloc[movie_indices]

# Streamlit app
st.title("🎬 Movie Recommendation System")
movie_name = st.text_input("Enter a movie title (case-sensitive):")

if st.button("Recommend"):
    recommendations = recommend_movies(movie_name)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)

    # if isinstance(recommendations, list):
    #     for movie in recommendations:
    #         st.write(movie)
    # else:
    #     st.write(recommendations[0])  # handles "Movie not found"
