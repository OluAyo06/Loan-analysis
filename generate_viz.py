import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a directory for plots if it doesn't exist
os.makedirs('static/images', exist_ok=True)

def generate_visualizations(df):
    sns.set_theme(style="whitegrid")
    
    # 1. Target Variable Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='loan_default', data=df, palette='viridis')
    plt.title('Distribution of Loan Default (Target)')
    plt.savefig('static/images/target_dist.png')
    plt.close()
    
    # 2. Age Distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(df['age'], bins=20, kde=True, color='purple')
    plt.title('Age Distribution of Borrowers')
    plt.savefig('static/images/age_dist.png')
    plt.close()
    
    # 3. Loan Amount Distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(df['loan_amount'], bins=30, kde=True, color='green')
    plt.title('Loan Amount Distribution')
    plt.savefig('static/images/loan_amount_dist.png')
    plt.close()
    
    # 4. Loan Default by Proof Submitted
    plt.figure(figsize=(10, 6))
    sns.countplot(x='proof_submitted', hue='loan_default', data=df, palette='Set2')
    plt.title('Loan Default by ID Proof Type')
    plt.savefig('static/images/default_by_proof.png')
    plt.close()
    
    # 5. Loan Default by Education
    plt.figure(figsize=(8, 6))
    sns.countplot(x='education', hue='loan_default', data=df, palette='pastel')
    plt.title('Loan Default by Education Level')
    plt.savefig('static/images/default_by_education.png')
    plt.close()
    
    # 6. Correlation Heatmap
    plt.figure(figsize=(12, 10))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['number'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='RdBu_r', fmt='.2f')
    plt.title('Feature Correlation Heatmap')
    plt.savefig('static/images/correlation_heatmap.png')
    plt.close()
    
    # 7. Boxplot: Loan Amount by Default
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='loan_default', y='loan_amount', data=df, palette='coolwarm')
    plt.title('Loan Amount by Default Status')
    plt.savefig('static/images/loan_amount_boxplot.png')
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv('/app/data/loan_train_cleaned.csv')
    generate_visualizations(df)
    print("Visualizations generated successfully in static/images/")
