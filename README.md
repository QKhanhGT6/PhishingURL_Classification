# PhishingURL_Classification
This project is a web-based application designed to classify URLs as safe or unsafe using a logistic regression model built entirely from scratch without the use of any machine learning libraries (except splitting dataset and feature scaling). It serves as an educational demonstration of a binary classification problem while integrating a user-friendly web interface for interaction.

Info about visualization & model training can be found in **ML.ipynb** file.

Dataset used: https://www.kaggle.com/datasets/prishasawhney/phishing-url-website-dataset-cleaned/data

## Features
1) Custom Logistic Regression Model
    - Implemented gradient descent without the use of libraries like scikit-learn for learning purposes.
    - Includes preprocessing using StandardScaler to normalize feature values.

2) Interactive Web Interface
Built with Flask for the backend and HTML/CSS/Bootstrap for the frontend.
Users can:
    - Paste a URL for classification.
    - Enter feature values manually or auto-extract them from the provided URL.
    - View prediction results in a modal dialog.

3) Feature Auto-Extraction
    - The system can auto-extract numerical features based on the input URL utilizing BeautifulSoup library.

## Setup and Installation
1) Clone this repo
```bash
git clone https://github.com/yourusername/phishing-url-classification.git
cd phishing-url-classification
```
2) Set up a Python environment (recommended: venv or conda)
3) Install dependencies
```bash
pip install scikit-learn numpy flask beautifulsoup4
```
4) Run the Flask application
```bash
python app.py
```
5) Open your browser and navigate to http://127.0.0.1:5000

## Web interface preview
![Screenshot 2024-12-24 101615](https://github.com/user-attachments/assets/0f429d76-7757-4303-ba80-2f518dba74ff)
![Screenshot 2024-12-24 102300](https://github.com/user-attachments/assets/f3e20e2f-ad0b-4552-a86e-455d9ebb0d20)
![Screenshot 2024-12-24 102343](https://github.com/user-attachments/assets/d8e85804-c881-430d-b1e1-426e14bb4d43)





