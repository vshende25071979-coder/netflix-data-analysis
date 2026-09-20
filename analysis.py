"""
Netflix Titles - Exploratory Data Analysis
Generates cleaned dataset + all visualizations used in the project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

sns.set_theme(style="whitegrid")
PALETTE = ["#E50914", "#221f1f", "#F5F5F1", "#B81D24", "#831010", "#564d4d"]
plt.rcParams["figure.dpi"] = 120
plt.rcParams["savefig.bbox"] = "tight"

DATA_PATH = "data/netflix_titles.csv"
IMG_DIR = "images"

# ------------------------------------------------------------------
# 1. LOAD
# ------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)
print(f"Raw shape: {df.shape}")

# ------------------------------------------------------------------
# 2. CLEAN
# ------------------------------------------------------------------
df["director"] = df["director"].fillna("Not Specified")
df["cast"] = df["cast"].fillna("Not Specified")
df["country"] = df["country"].fillna("Not Specified")
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])
df = df.dropna(subset=["date_added"])
df = df.drop_duplicates()

df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), format="%B %d, %Y")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()

# primary country (first listed)
df["primary_country"] = df["country"].apply(lambda x: x.split(",")[0].strip())

# duration split (movies = minutes, tv shows = seasons)
df["duration_int"] = df["duration"].str.extract(r"(\d+)").astype(float)

df.to_csv("data/netflix_titles_cleaned.csv", index=False)
print(f"Cleaned shape: {df.shape}")

# ------------------------------------------------------------------
# 3. CONTENT TYPE DISTRIBUTION
# ------------------------------------------------------------------
plt.figure(figsize=(6, 6))
type_counts = df["type"].value_counts()
colors = ["#E50914", "#221f1f"]
plt.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%",
        colors=colors, startangle=90, textprops={"color": "white", "fontsize": 12, "weight": "bold"},
        wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title("Movies vs TV Shows on Netflix", fontsize=14, weight="bold")
plt.savefig(f"{IMG_DIR}/01_content_type_distribution.png")
plt.close()

# ------------------------------------------------------------------
# 4. CONTENT ADDED OVER THE YEARS
# ------------------------------------------------------------------
plt.figure(figsize=(10, 5))
yearly = df.groupby(["year_added", "type"]).size().unstack(fill_value=0)
yearly = yearly[yearly.index <= 2021]
yearly.plot(kind="line", marker="o", ax=plt.gca(), color=["#221f1f", "#E50914"], linewidth=2.5)
plt.title("Content Added to Netflix by Year", fontsize=14, weight="bold")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.legend(title="Type")
plt.savefig(f"{IMG_DIR}/02_growth_over_years.png")
plt.close()

# ------------------------------------------------------------------
# 5. TOP 10 COUNTRIES
# ------------------------------------------------------------------
plt.figure(figsize=(9, 6))
top_countries = df[df["primary_country"] != "Not Specified"]["primary_country"].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index,
            palette="Reds_r", legend=False)
plt.title("Top 10 Countries by Number of Titles Produced", fontsize=14, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.savefig(f"{IMG_DIR}/03_top_countries.png")
plt.close()

# ------------------------------------------------------------------
# 6. TOP GENRES
# ------------------------------------------------------------------
all_genres = df["listed_in"].str.split(", ").explode()
top_genres = all_genres.value_counts().head(10)
plt.figure(figsize=(9, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, hue=top_genres.index,
            palette="rocket", legend=False)
plt.title("Top 10 Genres on Netflix", fontsize=14, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.savefig(f"{IMG_DIR}/04_top_genres.png")
plt.close()

# ------------------------------------------------------------------
# 7. RATING DISTRIBUTION
# ------------------------------------------------------------------
plt.figure(figsize=(10, 5))
rating_counts = df["rating"].value_counts().head(10)
sns.barplot(x=rating_counts.index, y=rating_counts.values, hue=rating_counts.index,
            palette="mako", legend=False)
plt.title("Distribution of Content Ratings", fontsize=14, weight="bold")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.savefig(f"{IMG_DIR}/05_rating_distribution.png")
plt.close()

# ------------------------------------------------------------------
# 8. MOVIE DURATION DISTRIBUTION
# ------------------------------------------------------------------
movies = df[df["type"] == "Movie"]
plt.figure(figsize=(9, 5))
sns.histplot(movies["duration_int"].dropna(), bins=30, color="#E50914", kde=True)
plt.title("Distribution of Movie Durations", fontsize=14, weight="bold")
plt.xlabel("Duration (minutes)")
plt.ylabel("Count")
plt.axvline(movies["duration_int"].mean(), color="black", linestyle="--",
            label=f"Mean = {movies['duration_int'].mean():.0f} min")
plt.legend()
plt.savefig(f"{IMG_DIR}/06_movie_duration_distribution.png")
plt.close()

# ------------------------------------------------------------------
# 9. TV SHOW SEASONS DISTRIBUTION
# ------------------------------------------------------------------
tv = df[df["type"] == "TV Show"]
plt.figure(figsize=(9, 5))
season_counts = tv["duration_int"].value_counts().sort_index().head(10)
sns.barplot(x=season_counts.index.astype(int), y=season_counts.values,
            hue=season_counts.index.astype(int), palette="Reds", legend=False)
plt.title("TV Shows: Number of Seasons", fontsize=14, weight="bold")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of Shows")
plt.savefig(f"{IMG_DIR}/07_tv_seasons_distribution.png")
plt.close()

# ------------------------------------------------------------------
# 10. HEATMAP: MONTH vs YEAR ADDED
# ------------------------------------------------------------------
month_order = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
heat = df.groupby(["month_added", "year_added"]).size().unstack(fill_value=0)
heat = heat.reindex(month_order)
heat = heat[[c for c in heat.columns if 2015 <= c <= 2021]]
plt.figure(figsize=(11, 6))
sns.heatmap(heat, cmap="Reds", linewidths=0.5, annot=False, cbar_kws={"label": "Titles Added"})
plt.title("Content Additions: Month vs Year", fontsize=14, weight="bold")
plt.xlabel("Year")
plt.ylabel("Month")
plt.savefig(f"{IMG_DIR}/08_month_year_heatmap.png")
plt.close()

# ------------------------------------------------------------------
# 11. TOP DIRECTORS
# ------------------------------------------------------------------
directors = df[df["director"] != "Not Specified"]["director"].str.split(", ").explode()
top_directors = directors.value_counts().head(10)
plt.figure(figsize=(9, 6))
sns.barplot(x=top_directors.values, y=top_directors.index, hue=top_directors.index,
            palette="flare", legend=False)
plt.title("Top 10 Directors by Number of Titles", fontsize=14, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.savefig(f"{IMG_DIR}/09_top_directors.png")
plt.close()

# ------------------------------------------------------------------
# SUMMARY STATS (for README)
# ------------------------------------------------------------------
summary = {
    "total_titles": int(len(df)),
    "movies": int((df["type"] == "Movie").sum()),
    "tv_shows": int((df["type"] == "TV Show").sum()),
    "countries_represented": int(df["primary_country"].nunique()),
    "oldest_release_year": int(df["release_year"].min()),
    "newest_release_year": int(df["release_year"].max()),
    "avg_movie_duration": round(float(movies["duration_int"].mean()), 1),
    "top_country": top_countries.index[0],
    "top_genre": top_genres.index[0],
    "peak_year_added": int(yearly.sum(axis=1).idxmax()),
}

print("\n--- SUMMARY ---")
for k, v in summary.items():
    print(f"{k}: {v}")

import json
with open("data/summary_stats.json", "w") as f:
    json.dump(summary, f, indent=2)

print("\nAll charts saved to images/. Cleaned data saved to data/netflix_titles_cleaned.csv")
