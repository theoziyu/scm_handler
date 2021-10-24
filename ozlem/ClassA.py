from subject_observer import Observer,Subject
import pandas as pd

class ClassA(Observer):
    def __init__(self,scm_subject: Subject):
        self.df = pd.read_csv("dataframe.csv",index_col=None)
        self.scm = scm_subject

    def update(self, subject: Subject):
        self.df = pd.read_csv("dataframe.csv",index_col=None)
        print("observerA is updated: ")
        print(self.df)
        
    def some_process(self,):
        print("observerA is editting the df.. adding özlem")
        df = pd.DataFrame(data={'camera_ip': ["4444.4444.4.4:8888"], 'camera_name': ['özlem'], 'model_a':False,'model_b': True})
        self.scm.add_data_to_df(df)