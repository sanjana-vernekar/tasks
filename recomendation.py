import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset
data = pd.DataFrame({
    'item_id': [1, 2, 3, 4],
    'title': ['Item A', 'Item B', 'Item C', 'Item D'],
    'description': ['A good item', 'A great item', 'An excellent item', 'A bad item']
})

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the description column
tfidf_matrix = tfidf_vectorizer.fit_transform(data['description'])

# Compute similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on item_id
def get_recommendations(item_id, cosine_sim=cosine_sim):
    idx = data.index[data['item_id'] == item_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3]  # Get top 2 recommendations
    item_indices = [i[0] for i in sim_scores]
    return data.iloc[item_indices]

# Example usage
recommendations = get_recommendations(1)
print(recommendations)