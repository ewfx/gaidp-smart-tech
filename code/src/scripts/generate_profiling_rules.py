# scripts/generate_profiling_rules.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def generate_profiling_rules(data):
    encoder = LabelEncoder()
    data['Customer_ID_encoded'] = encoder.fit_transform(data['Customer_ID'])
    # Example rule: Ensure 'Transaction_Amount' is numeric and within a valid range.
    valid_amount_range = (0, 100)
    return valid_amount_range

if __name__ == "__main__":
    data = pd.read_csv('C://Users//jahna//IdeaProjects//DataProfiling//src//data//example_data.csv')
    profiling_rules = generate_profiling_rules(data)
    print(profiling_rules)
