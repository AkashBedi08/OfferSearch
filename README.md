# OfferSearch
This project is for FETCH assesment which involves searching offers through their dataset.

# Fetch Offer Search Tool

This is a Flask web application that allows users to search for relevant offers based on text input. The tool utilizes a dataset of brands, categories, and offers to provide users with matching results.

# Fetch Offer Search Tool

This is a Flask web application that allows users to search for relevant offers based on text input. The tool utilizes a dataset of brands, categories, and offers to provide users with matching results.

## Getting Started

1. Ensure you have Python installed on your machine.

2. Install the required Python packages:

    ```bash
    pip install flask pandas spacy scikit-learn
    ```

3. Download the pre-trained spaCy model for English:

    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Place your CSV datasets (`brand_category.csv`, `categories.csv`, `offer_retailer.csv`) in the same directory as the `app.py` file.

5. Run the Flask application:

    ```bash
    python app.py
    ```

6. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to use the Offer Search Tool.

## HTML Styling

The HTML file (`index.html`) provides a visually appealing and user-friendly interface for the Offer Search Tool. It includes a header with the company name "FETCH," a search form, and a results table. The styling is done using CSS to enhance the overall appearance.

Make sure that the HTML file is inside a folder called templates

## Usage

1. Enter your search query in the provided input box.

2. Click the "Search" button.

3. View the results table, which includes information about the type of result (OFFER), the matched result, the associated brand, the retailer, and the similarity score.

## Important Notes

- Make sure your CSV datasets have the correct structure and naming (`brand_category.csv`, `categories.csv`, `offer_retailer.csv`).

- The application uses spaCy for text preprocessing and scikit-learn for TF-IDF vectorization and cosine similarity calculation.

- Adjustments to the HTML template or Python code can be made based on your specific requirements.

- The code and the datasets should be in the same folder, in that make sure that you craete a templates folder and keep the Index.html file in that folder.

- If any queries feel free to contact via email on bediakash861@gmail.com

Enjoy using the Fetch Offer Search Tool!
