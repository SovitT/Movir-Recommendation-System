# 🎬 Movie Recommendation System

A content-based movie recommender system built using Python, pandas, and scikit-learn. It suggests similar movies based on a selected title using key features like genre, director, and cast — and comes with a clean and interactive Streamlit GUI.

---

## 🔍 Features

- Recommend top 5 movies similar to the selected title
- IMDB ratings shown alongside recommendations
- Case-insensitive search functionality
- User-friendly interface with **Streamlit**
- Uses **IMDB Top 1000 Movies dataset** from Kaggle

---

## 📂 Project Structure

movie-recommender/
├── app.py # Streamlit web app
├── imdb_top_1000.csv # Dataset from Kaggle
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the repository

```bash```
git clone https://github.com/SovitT/movie-recommender.git
cd movie-recommender

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Streamlit app
streamlit run app.py



## 🧠 How It Works
Combine Features: Each movie’s genre, director, cast, and more are combined into a single text feature.

Vectorize: Text features are transformed using CountVectorizer.

Calculate Similarity: Cosine similarity is calculated between movie vectors.

Recommend: Based on similarity, the top N similar movies are shown.

## 📊 Example Output
Searching for "The Dark Knight" will return:

Batman Begins 

The Prestige 

Inception 

…and more.

## 🗃 Dataset
Source: Kaggle - IMDB Top 1000 Movies Dataset

## 📦 Dependencies
Listed in requirements.txt:

pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit

## ✨ Future Enhancements
Add collaborative filtering (user-based)

Deploy on Streamlit Cloud

## 📜 License
This project is licensed under the MIT License.

## 👨‍💻 Author
Sovit Thakre
📍 Bangalore, India
🔗 LinkedIn : [https://www.linkedin.com/in/sovit-thakre-255675246/
](url)

