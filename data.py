import logging
import os

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi


class Data:
    def __init__(self) -> None:
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
                dataframes.append(pd.read_csv(f"{path}/{filename}"))
            dataset = pd.concat(dataframes)
            logging.debug(dataset)
            self.generate_heatmap(path=path, dataset=dataset)
            return dataset
        except Exception as e:
            logging.error(f"Error while getting dataset; Exception: {e}")
            return pd.DataFrame()
    
    def generate_heatmap(self, path: str, dataset: pd.DataFrame):
        try:
            # remove rows wit NaN values
            dataset.dropna()
            # filter datatypes
            dataset.select_dtypes(['float64','int64'])
            # remove duplicate entries
            dataset.drop_duplicates()
            plt.title("Pearson Correlation")
            heatmap = sns.heatmap(dataset.corr(), 
                annot=True,
                square=True,
                linewidth=.5
                )
            plt.savefig(f"{path}/heatmap.jpeg")
        except Exception as e:
            logging.error(f"Error while generating heatmap; Exception{e}")
        

