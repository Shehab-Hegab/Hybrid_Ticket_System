import pandas as pd

# 1. Load the raw Kaggle dataset
file_path = 'customer_support_tickets.csv'

try:
    df = pd.read_csv(file_path)
    print("✅ Raw data loaded successfully.")
    print(f"Original shape: {df.shape}")
except FileNotFoundError:
    print(f"❌ Error: '{file_path}' not found. Please download it from Kaggle and rename it.")
    exit()

# 2. Select and Rename Columns
# We map the Kaggle column names to our project's standard names
column_mapping = {
    'Ticket Description': 'ticket_text',
    'Ticket Type': 'department',
    'Ticket Priority': 'urgency'
}

# Verify columns exist before proceeding
if not set(column_mapping.keys()).issubset(df.columns):
    print(f"❌ Error: The file does not have the expected columns: {list(column_mapping.keys())}")
    print(f"Columns found: {df.columns.tolist()}")
    exit()

# Keep only necessary columns and rename them
df_clean = df[column_mapping.keys()].rename(columns=column_mapping)

# 3. Clean the Data
# Remove rows where the text is empty (if any)
df_clean.dropna(subset=['ticket_text'], inplace=True)

# Standardize Urgency levels
# The dataset has 'Critical', 'High', 'Normal', 'Low'. 
# Let's simplify this for our model: 'Critical'/'High' -> Urgent, others -> Normal
urgency_mapping = {
    'Critical': 'Urgent',
    'High': 'Urgent',
    'Normal': 'Normal',
    'Low': 'Normal'
}
df_clean['urgency'] = df_clean['urgency'].map(urgency_mapping)

# 4. Save the processed data
# We save it as 'tickets.csv' which is the standard name our next steps will look for
df_clean.to_csv('tickets.csv', index=False)

print("\n✅ Data Cleaning Complete!")
print(f"Final data saved to 'tickets.csv' with shape: {df_clean.shape}")
print("\nSample Data (First 5 rows):")
print(df_clean.head())

# Optional: Print distribution to see how balanced the data is
print("\nDepartment Distribution:")
print(df_clean['department'].value_counts())
print("\nUrgency Distribution:")
print(df_clean['urgency'].value_counts())
