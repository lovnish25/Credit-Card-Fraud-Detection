# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
df = pd.read_csv("credit_card_fraud_dataset.csv")  

# Plot Fraud vs Non-Fraud Distribution
sns.countplot(x='IsFraud', data=df)
plt.title("Fraud vs Non-Fraud Distribution")
plt.show()

# Print percentage
fraud_percent = df['IsFraud'].mean() * 100
print(f"Fraudulent Transactions: {fraud_percent:.2f}%")
