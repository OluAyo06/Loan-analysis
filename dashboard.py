import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="Loan Default Analysis Dashboard", layout="wide")

st.title("📊 Loan Default Analysis Dashboard")

st.markdown("""
This dashboard presents an analysis of loan applicant data to understand the factors influencing loan defaults.
The dataset has been cleaned, with missing values handled and features explored.
""")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Feature Explanation", "Exploratory Data Analysis", "Model Insights"])

# Load Data for display
@st.cache_data
def load_data():
    return pd.read_csv('/app/data/loan_train_cleaned.csv')

df = load_data()

if page == "Feature Explanation":
    st.header("📋 Feature Explanations")
    st.markdown("""
    Below are the descriptions of the features present in the dataset:
    - **loan_id**: Unique identifier for each loan record.
    - **age**: The age of the person applying for the loan.
    - **education**: Level of education (represented as 1 or 2).
    - **proof_submitted**: Type of identity proof provided by the applicant (e.g., Aadhar, VoterID, PAN, etc.).
    - **loan_amount**: Total amount of the loan requested.
    - **asset_cost**: The value of the asset being financed.
    - **no_of_loans**: Total number of existing loans the applicant has.
    - **no_of_curr_loans**: Number of loans currently active.
    - **last_delinq_none**: Indicator if there has been no delinquency in the last period (1 = No delinquency, 0 = Delinquency).
    - **loan_default**: Target variable indicating if the loan was defaulted (1 = Default, 0 = No Default).
    """)
    st.subheader("Sample Data")
    st.write(df.head())

elif page == "Exploratory Data Analysis":
    st.header("🔍 Exploratory Data Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Target Distribution")
        st.image("static/images/target_dist.png")
        st.write("The distribution shows the count of defaults (1) vs non-defaults (0). There is usually a class imbalance with fewer defaults.")
        
        st.subheader("2. Age Distribution")
        st.image("static/images/age_dist.png")
        st.write("The age distribution helps understand the demographic of the borrowers.")

    with col2:
        st.subheader("3. Loan Amount Distribution")
        st.image("static/images/loan_amount_dist.png")
        st.write("Shows the range and frequency of loan amounts requested.")
        
        st.subheader("4. Default by ID Proof")
        st.image("static/images/default_by_proof.png")
        st.write("Comparison of default rates across different types of ID proofs submitted.")

    st.divider()
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("5. Default by Education")
        st.image("static/images/default_by_education.png")
        st.write("Analysis of whether education level (1 or 2) correlates with the likelihood of default.")
        
    with col4:
        st.subheader("6. Loan Amount Boxplot")
        st.image("static/images/loan_amount_boxplot.png")
        st.write("Distribution of loan amounts for both defaulted and non-defaulted cases.")

    st.header("🔥 Correlation Analysis")
    st.image("static/images/correlation_heatmap.png")
    st.write("The heatmap reveals relationships between numerical variables. For example, a high correlation between loan amount and asset cost is expected.")

elif page == "Model Insights":
    st.header("💡 Key Insights")
    st.markdown("""
    - **Demographics**: Borrowers are spread across various age groups, but certain ranges might show higher default risks.
    - **Collateral**: The relationship between asset cost and loan amount is a critical factor in loan approval.
    - **History**: The number of current loans and past delinquency status are strong indicators of future repayment behavior.
    - **Data Cleaning**: Handled missing values in the 'education' feature to ensure robust analysis.
    """)
