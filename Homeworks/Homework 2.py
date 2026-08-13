import pandas as pd
from sklearn.cluster import KMeans

data = {
    "ScreenTime": [2, 8, 3, 9, 1, 7, 5, 10, 4, 6],
    "SocialLevel": [3, 9, 2, 8, 1, 7, 5, 10, 4, 6],
    "Spending": [50, 400, 60, 450, 30, 300, 150, 500, 100, 200]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3, random_state=42)

df["Group"] = kmeans.fit_predict(df)

print(df)