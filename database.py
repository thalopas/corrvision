import logging
from sqlalchemy import (
    Integer,
    Text,
    Column,
    MetaData,
    create_engine,
)
from data import Data

from sqlalchemy.orm import DeclarativeBase, class_mapper, relationship, sessionmaker

engine = create_engine("sqlite:///corrvision")

Session = sessionmaker(bind=engine)
session = Session()
my_metadata = MetaData()

# SQL Alchemy object to dictionary
def object_as_dict(obj) -> dict:
    mapper = class_mapper(obj.__class__)
    data = {}
    for column in mapper.columns:
        data[column.name] = getattr(obj, column.name)
    return data

class Base(DeclarativeBase):
    metadata = my_metadata

class Dataset(Base):
    __tablename__ = "datasets"

    datasetId = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=True)
    attributes = Column(Text(), nullable=True)

    @staticmethod
    def create_dataset(content: dict, attributes = None):
        try:
            dataset = Dataset.get_dataset_by_name(content['datasetName'])
            if not dataset:
                new_dataset = Dataset(name = content['datasetName'], attributes = attributes)
                session.add(new_dataset)
                session.commit()
                dataset = Dataset.get_dataset_by_name(content['datasetName'])
                data = Data()
                data.get_dataset(dataset)
            return dataset['datasetId']
        except Exception as e:
            logging.error(f"Error while creating dataset; Exception: {e}")
            return None

    @staticmethod
    def get_dataset_by_name(datasetName: str) -> dict:
        try:
            dataset_row = (
                session.query(Dataset)
                .filter(Dataset.name == datasetName)
                .first()
            )
            dataset = object_as_dict(dataset_row)
            session.close()
            return dataset
        except Exception as e:
            logging.error(f"Error while getting dataset by name; Excetion {e}")
            return dict()
        
    @staticmethod
    def get_dataset_by_id(datasetId: str) -> dict:
        try:
            dataset_row = (
                session.query(Dataset)
                .filter(Dataset.datasetId == datasetId)
                .first()
            )
            dataset = object_as_dict(dataset_row)
            session.close()
            return dataset
        except Exception as e:
            logging.error(f"Error while getting dataset by name; Excetion {e}")
            return dict()
        