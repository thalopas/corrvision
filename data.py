import logging
import os

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi


class Data:
    def __init__(self, username: str, key: str) -> None:
        os.environ['KAGGLE_USERNAME'] = username
        os.environ['KAGGLE_KEY'] = key
        try:
            self.api = KaggleApi()
            self.api.authenticate()
        except Exception as e:
            logging.error(f"Failed to connect to Kaggle API; Exception: {e}")

    def get_dataset(self, dataset_entry: dict) -> pd.DataFrame:
        try:
            dataframes = []
            path = f"/tmp/{dataset_entry['name']}"
            self.api.dataset_download_files(dataset=dataset_entry['name'], path=path, unzip=True)
            for filename in os.listdir(path):
                dataframes.append(pd.read_csv(filename))
            dataset = pd.concat(dataframes)
            dataset = Data.analyze_dataset(dataset)
            return dataset
        except Exception as e:
            logging.error(f"Error while getting dataset; Exception: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def analyze_dataset(dataset: pd.DataFrame):
        # remove rows wit NaN values
        dataset.dropna()
        # remove duplicate entries
        dataset.drop_duplicates()
        # remove columns with excluesively unique values
        dataset_length = len(dataset.index)
        for column in dataset:
            if dataset[column].nunique() == dataset_length:
                dataset.drop(column, axis=1)
        return dataset
    
    def generate_heatmap(self, dataset_entry: dict):
        try:
            dataset = self.get_dataset(dataset_entry)
            plt.title("Pearson Correlation")
            heatmap = sns.heatmap(dataset.corr(), 
                    annot=True,
                    square=True,
                    linewidth=.5
                    )
            plt.savefig(f"{dataset_entry['path']}/heatmap.jpeg")
        except Exception as e:
            logging.error(f"Error while generating heatmap; Exception{e}")
        
