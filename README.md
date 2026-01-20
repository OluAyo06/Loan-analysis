# 📊 Loan Default Analysis Project

## Overview

This project focuses on analyzing loan applicant data to understand the factors that influence loan default. It covers the complete data workflow — from data cleaning and preprocessing to exploratory data analysis (EDA) and interactive visualization using a Streamlit dashboard.

The goal is to build a clean, reproducible analysis pipeline and present insights in a simple, user-friendly way.

---

## 📁 Project Structure

```
├── data/
│   ├── loan_train.csv
│   ├── loan_test.csv
│   ├── loan_train_cleaned.csv
│   └── loan_test_cleaned.csv
│
├── clean_data.py          # Script for data cleaning
├── generate_viz.py       # Script for EDA and visualization
├── dashboard.py          # Streamlit dashboard app
│
├── static/
│   └── images/           # Saved plots for the dashboard
│
└── README.md
```

---

## 🧹 Step 1: Data Cleaning (`clean_data.py`)

This script is responsible for preparing the raw loan datasets for analysis.

### What it does:

* Loads the training and test datasets from CSV files.
* Handles missing values in the `education` column by filling them with the mode (most frequent value).
* Removes duplicate records to avoid biased analysis.
* Prints a short cleaning report showing:

  * The value used to fill missing data.
  * Dataset shape before and after cleaning.
  * Remaining missing values.
* Saves cleaned versions of both training and test datasets.

### Output:

* `loan_train_cleaned.csv`
* `loan_test_cleaned.csv`

---

## ⚙️ Step 2: Exploratory Data Analysis & Visualization (`generate_viz.py`)

This script generates visual insights from the cleaned training dataset.

### What it does:

* Creates a `static/images` folder to store plots.
* Generates and saves the following visualizations:

  1. Distribution of loan defaults (target variable).
  2. Age distribution of borrowers.
  3. Loan amount distribution.
  4. Loan default by ID proof type.
  5. Loan default by education level.
  6. Feature correlation heatmap (numeric features only).
  7. Boxplot of loan amount by default status.

### Output:

* PNG images saved in `static/images/`

---

## 📊 Step 3: Interactive Dashboard (`dashboard.py`)

A Streamlit web application that presents the analysis results interactively.

### Dashboard Features:

* Sidebar navigation with three main sections:

#### 1️⃣ Feature Explanation

* Explains the meaning of each dataset column.
* Displays a preview of the cleaned dataset.

#### 2️⃣ Exploratory Data Analysis

* Displays all generated plots from the `static/images` folder.
* Includes short written interpretations for each visualization.

#### 3️⃣ Model Insights

* Highlights key observations such as:

  * Age and demographic trends.
  * Relationship between asset cost and loan amount.
  * Impact of past delinquency and existing loans.
  * Importance of data cleaning.

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install pandas matplotlib seaborn streamlit pillow
```

### 2. Run Data Cleaning

```bash
python clean_data.py
```

### 3. Generate Visualizations

```bash
python generate_viz.py
```

### 4. Launch the Dashboard

```bash
streamlit run dashboard.py
```

---

## 🚀 Future Improvements

* Add feature engineering (e.g., loan-to-asset ratio).
* Build and integrate a machine learning model.
* Add model performance metrics to the dashboard.
* Deploy the dashboard using Docker or Streamlit Cloud.

---
