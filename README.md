# 🎬 Movie Recommendation System (Streamlit App)

This is a content-based movie recommendation system built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. It recommends movies based on content features such as genre, director, and description.

---

## 🚀 Features

- Recommend similar movies based on your favorite one
- View IMDB ratings of recommended movies
- Case-insensitive search
- Streamlit-powered user interface

---

## 📁 Dataset

The dataset used is:
- **[IMDB Top 1000 Movies](https://www.kaggle.com/datasets)**
- Columns used: `Series_Title`, `Genre`, `Director`, `Overview`, `IMDB_Rating`

---

## 🖥️ Demo

To run the app locally:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
