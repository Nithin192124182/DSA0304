from sklearn.feature_extraction.text import TfidfVectorizer

# Define the documents
sentences = [
    "Climate change is a pressing global issue that requires immediate action.",
    "Renewable energy sources, such as solar and wind power, are essential for reducing carbon emissions.",
    "Greenhouse gases, like carbon dioxide and methane, contribute to global warming.",
    "The Paris Agreement is an international treaty aimed at addressing climate change.",
    "Sustainability and environmental conservation are crucial for the future of our planet."
]

# User query
query = "Climate change action"

# Add the query to the documents
sentences.append(query)

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Calculate TF-IDF scores for the documents
tfidf_matrix = vectorizer.fit_transform(sentences)

# Calculate TF-IDF scores for the query
query_tfidf = tfidf_matrix[-1]  # Last row corresponds to the query

# Calculate similarity scores between query and documents using dot product
similarity_scores = (tfidf_matrix[:-1] @ query_tfidf.T).toarray().flatten()

# Sort the documents by similarity score in descending order
sorted_indices = similarity_scores.argsort()[::-1]

# Display the retrieved documents in order of relevance
print("Retrieved documents (in order of relevance):")
for idx in sorted_indices:
    print(f"Document {idx + 1}: {sentences[idx]}")