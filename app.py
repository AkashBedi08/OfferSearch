from flask import Flask, render_template, request
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load datasets from CSV files
brand_category_data = pd.read_csv("brand_category.csv", names=["BRAND", "BRAND_BELONGS_TO_CATEGORY", "RECEIPTS"])
categories_data = pd.read_csv("categories.csv", names=["CATEGORY_ID", "PRODUCT_CATEGORY", "IS_CHILD_CATEGORY_TO"])
offer_retailer_data = pd.read_csv("offer_retailer.csv", names=["OFFER", "RETAILER", "BRAND"])

# Load pre-trained English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    if pd.isna(text):  # Check if the value is NaN
        return ""
    
    # Tokenize and lemmatize the text
    doc = nlp(str(text).lower())  # Convert to lowercase and handle non-string values
    return " ".join([token.lemma_ for token in doc])

def build_tfidf_matrix(texts):
    # Use TF-IDF vectorizer to convert texts to a matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix, vectorizer

def search_offers(query, data, category_data, offer_retailer_data):
    # Preprocess the query
    processed_query = preprocess_text(query)

    # Prepare data for similarity comparison
    all_text_data = [preprocess_text(item) for item in offer_retailer_data["OFFER"]]

    # Build TF-IDF matrix
    tfidf_matrix, vectorizer = build_tfidf_matrix(all_text_data)

    # Transform the query into the TF-IDF space
    query_vector = vectorizer.transform([processed_query])

    # Calculate cosine similarity between the query and each item in the data
    similarities = cosine_similarity(query_vector, tfidf_matrix)

    if not similarities.any():
        return [{"type": "NO_OFFERS", "result": "No offers found", "score": 0.0}]

    # Get the indices of the most similar items
    max_similarity_indices = similarities.argsort()[0][::-1]

    # Create a list of relevant offers and their similarity scores
    results = []
    for index in max_similarity_indices:
        score = similarities[0, index]
        if score > 0.0:
            result_type = "OFFER"
            result = offer_retailer_data.iloc[index]["OFFER"]
            brand = offer_retailer_data.iloc[index]["BRAND"]
            retailer = offer_retailer_data.iloc[index]["RETAILER"]
            results.append({"type": result_type, "result": result, "brand": brand, "retailer": retailer, "score": score})

    return results

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    query = None
    if request.method == "POST":
        query = request.form["query"]
        results = search_offers(query, brand_category_data, categories_data, offer_retailer_data)
    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
