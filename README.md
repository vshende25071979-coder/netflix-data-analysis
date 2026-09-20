# 🎬 Netflix Movies & TV Shows — Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4c72b0)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A complete exploratory data analysis (EDA) of Netflix's catalog of **8,800+ Movies and TV Shows**, uncovering trends in content growth, global production, genres, ratings, and runtime patterns using Python, Pandas, Matplotlib, and Seaborn.

---

## 📌 Project Overview

Netflix's public catalog metadata offers a rich look into how a global streaming platform builds and evolves its content library. This project cleans, explores, and visualizes the dataset to answer questions like:

- How has Netflix's content library grown over the years?
- Do Movies or TV Shows dominate the platform?
- Which countries and directors contribute the most content?
- What genres and content ratings are most common?
- How long are Netflix movies, and how many seasons do TV shows typically run?
- Is there seasonality in when new content gets added?

---

## 🗂️ Dataset

- **Source:** [Netflix Movies and TV Shows — Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Size:** 8,807 titles × 12 columns
- **Columns:** `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

---

## 🧹 Data Cleaning

| Step | Action |
|---|---|
| Missing `director` / `cast` / `country` | Filled with `"Not Specified"` |
| Missing `rating` | Filled with the mode (most frequent rating) |
| Missing `date_added` | Rows dropped (required for time-based analysis) |
| Duplicates | Removed |
| `date_added` | Parsed into datetime; `year_added` and `month_added` extracted |
| `country` | First listed country extracted as `primary_country` |
| `duration` | Numeric value extracted into `duration_int` (minutes for movies, seasons for TV shows) |

Full cleaning logic: [`src/analysis.py`](src/analysis.py)

---

## 📊 Key Insights

### 1. Movies dominate the catalog
![Content Type Distribution](images/01_content_type_distribution.png)

Roughly **70% of titles are Movies** and **30% are TV Shows** — Netflix's catalog has historically leaned toward film.

### 2. Explosive growth, then a pandemic-era dip
![Growth Over Years](images/02_growth_over_years.png)

Content additions grew sharply from 2015–2019, **peaking in 2019** with 1,400+ movies added in a single year, before slowing down in 2020–2021.

### 3. The US leads global content production
![Top Countries](images/03_top_countries.png)

The **United States**, **India**, and the **United Kingdom** are the top three content-producing countries on the platform.

### 4. International Movies & Dramas top the genre list
![Top Genres](images/04_top_genres.png)

### 5. TV-MA is the most common rating
![Rating Distribution](images/05_rating_distribution.png)

The catalog skews toward **mature audiences**, with TV-MA as the single most frequent content rating.

### 6. Average movie runtime is ~100 minutes
![Movie Duration](images/06_movie_duration_distribution.png)

### 7. Most TV shows run for just one season
![TV Seasons](images/07_tv_seasons_distribution.png)

### 8. Content additions peak around December–January
![Month/Year Heatmap](images/08_month_year_heatmap.png)

### 9. Top contributing directors
![Top Directors](images/09_top_directors.png)

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Pandas** — data cleaning & manipulation
- **NumPy** — numeric operations
- **Matplotlib / Seaborn** — data visualization
- **Jupyter Notebook** — analysis walkthrough

---

## 📁 Project Structure

```
netflix-data-analysis/
├── data/
│   ├── netflix_titles.csv            # Raw dataset
│   ├── netflix_titles_cleaned.csv    # Cleaned dataset (generated)
│   └── summary_stats.json            # Key summary stats (generated)
├── notebooks/
│   └── netflix_analysis.ipynb        # Full step-by-step EDA notebook
├── images/                           # All generated charts
├── src/
│   └── analysis.py                   # Cleaning + chart generation script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/netflix-data-analysis.git
cd netflix-data-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3a. Run the script (regenerates cleaned data + all charts)
python src/analysis.py

# 3b. OR explore interactively
jupyter notebook notebooks/netflix_analysis.ipynb
```

---

## 🔮 Future Work

- Build an interactive dashboard (Plotly Dash / Streamlit)
- Add a genre/content recommendation system
- Perform NLP analysis on the `description` column (sentiment, keyword extraction)
- Compare Netflix's catalog trends against competitors (Prime Video, Disney+)

---

## 👤 Author

**Your Name**
📧 your.email@example.com | 🔗 [LinkedIn](https://linkedin.com/in/your-profile) | 💻 [GitHub](https://github.com/your-username)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). The dataset itself is provided by Netflix/Kaggle for educational and research purposes.
