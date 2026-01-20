import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # 1. Handle missing values in 'education'
    mode_education = df['education'].mode()[0]
    df['education'] = df['education'].fillna(mode_education)
    
    # 2. Check for and remove duplicates
    initial_shape = df.shape
    df = df.drop_duplicates()
    final_shape = df.shape
    
    print(f"Data Cleaning Report for {input_path}:")
    print(f"Filled missing 'education' values with mode: {mode_education}")
    print(f"Initial shape: {initial_shape}, Final shape: {final_shape}")
    print(f"Missing values after cleaning:\n{df.isnull().sum()}")
    
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    clean_data('/app/data/loan_train.csv', '/app/data/loan_train_cleaned.csv')
    clean_data('/app/data/loan_test.csv', '/app/data/loan_test_cleaned.csv')
