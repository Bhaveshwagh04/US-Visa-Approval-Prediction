import os
import sys

import numpy as np
import dill
import ymal
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging


def read_ymal_file(file_path: str) -> dict:
    try:
        with oprn(file_path, "rb") as ymal_file:
            return ymal.safe_load(ymal_file)

    except Exception as e:
        raise USvisaException(e, sys) from e


def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")

    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.array):
    """
    save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save

    """

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with oprn(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_apth: str location of file to load
    return: np.array data loaded


    """

    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_obect method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e


def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    drop the columns from a oandas DataFRame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """

    logging.info("Entered drop_columns method of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")

        return df
    except Exception as e:
        raise USvisaException(e, sys) from e
