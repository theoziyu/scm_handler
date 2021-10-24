from subject_observer import Observer,Subject
import pandas as pd

class ClassB(Observer):
    def __init__(self):
        self.df = pd.read_csv("dataframe.csv",index_col=None)

    def update(self, subject: Subject ):
        self.df= pd.read_csv("dataframe.csv",index_col=None)
        print("observerB df is updated: ")
        print(self.df)