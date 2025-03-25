import pandas as pd
import numpy as np
import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
        return self.data

class DataPreprocessor:
    def __init__(self, data):
        self.data = data
    
    def preprocess(self):
        processed_data = []
        for chat_id, chat_info in self.data.items():
            article_url = chat_info.get("article_url", "Unknown")
            for message in chat_info.get("content", []):
                processed_data.append({
                    "chat_id": chat_id,
                    "article_url": article_url,
                    "message": message["message"],
                    "agent": message["agent"],
                    "sentiment": message["sentiment"],
                    "turn_rating": message.get("turn_rating", "Unknown")
                })
        return pd.DataFrame(processed_data)

# Load and preprocess the data
def get_processed_data(file_path):
    data_loader = DataLoader(file_path)
    raw_data = data_loader.load_data()
    
    preprocessor = DataPreprocessor(raw_data)
    df = preprocessor.preprocess()
    
    # Handle missing values
    df.fillna("Unknown", inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    
    return df
