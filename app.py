from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

app = Flask(__name__)

# --- Load dataset ---
file_path = "movies.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found!")

movies = pd.read_csv(file_path)
movies['genre'] = movies['genre'].fillna('')

# --- ML setup ---
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genre'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend(movie_title, top_n=5):
    if movie_title not in indices:
        return []
    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    movie_name = ""
    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        recommendations = recommend(movie_name)
    return render_template("index.html", movie_name=movie_name, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
