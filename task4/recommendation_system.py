import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genres into vectors
cv = CountVectorizer()
vectors = cv.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(vectors)

def recommend(movie):
    movie = movie.lower()

    titles = movies["title"].str.lower()

    if movie not in titles.values:
        print("Movie not found!")
        return

    index = titles[titles == movie].index[0]

    distances = list(enumerate(similarity[index]))

    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0

    for i in distances[1:]:
        print(movies.iloc[i[0]].title)
        count += 1

        if count == 5:
            break

print("Movie Recommendation System")

movie = input("Enter your favorite movie: ")

recommend(movie)
