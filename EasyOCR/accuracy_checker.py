import mysql.connector
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(texts, rows, column_names):
    # Step 1: Check if there are any matching rows in the database
    if not rows:
        # If no matching rows, return an empty list
        return []

    # Step 2: Convert both the extracted texts and database rows to lowercase
    extracted_words = [text.lower() for text in texts]

    # Step 3: Calculate the similarity between the extracted texts and the rows in the database
    similarities = []
    for row in rows:
        similarity = sum(a == b for a, b in zip(row, extracted_words)) / len(row)
        similarities.append(similarity)

    # Step 4: Create a list of tuples (similarity, wine_name) and sort it based on similarity (highest similarity first)
    similarities_with_wine_names = [(similarity, row[column_names.index('wine_name')]) for similarity, row in
                                    zip(similarities, rows)]
    similarities_with_wine_names.sort(key=lambda x: x[0], reverse=True)

    return similarities_with_wine_names


def perform_accuracy_check(texts):
    # Connect to the database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='spring',
        port='3306',
        database='test'
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    top_results = []
    column_names = ['alcohol_content', 'bottle_information', 'brand_name', 'grape_variety',
                    'vintage', 'wine_name', 'region_of_production']

    # Perform the accuracy check for each individual extracted word
    for text in texts:
        # Query the specified columns
        query = "SELECT {} FROM wine_label WHERE wine_name LIKE %s".format(', '.join(column_names))
        # Use %% to escape % and perform partial matching
        mycursor.execute(query, (f"%{text}%",))
        rows = mycursor.fetchall()

        # Calculate the similarity between the extracted text and the database records
        similarities_with_wine_names = calculate_similarity(text, rows, column_names)

        # Append the results for this word to the top_results list
        top_results.extend([(similarity, wine_name) for similarity, wine_name in similarities_with_wine_names])

    # Sort the results based on similarity (highest similarity first)
    top_results.sort(key=lambda x: x[0], reverse=True)

    return top_results
