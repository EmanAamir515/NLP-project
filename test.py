####################### Create a test file to verify your setup
import pandas as pd

test_data = {
    'text': [
        "Bohat khush hun aaj",
        "Bura lag raha hai",
        "Theek thaak hai",
        "Zabardast kaam kiya!",
        "Bohatt bekaar hai ye"
    ],
    'sentiment': ['positive', 'negative', 'neutral', 'positive', 'negative']
}

pd.DataFrame(test_data).to_csv('Data/corpus.csv', index=False)
print("Sample data created successfully!")