from subject_observer import Subject, Observer
from typing import List
import pandas as pd

class DataBaseSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """
    def __init__(self):

    
        self._state: int = None

        self._observers: List[Observer] = []
        self.df = pd.read_csv("dataframe.csv", index_col=None)

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self):
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)


    def add_data_to_df(self,row_value):
        print("the data is added to df")
      
        self.df = self.df.append(row_value)
        self.df.to_csv("dataframe.csv",index=None)
        self.notify()