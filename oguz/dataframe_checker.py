from time import sleep
import pandas as pd

class DataframeChecker():
    """ Simple class to consistently check updates in a given dataframe
    """
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.orig_df = pd.read_csv(self.csv_path)
        self.new_df = None

    def read_new_df(self):
        self.new_df = pd.read_csv(self.csv_path)
    
    def update_orig_df(self):
        print("Updating the original DataFrame...")
        self.orig_df = self.new_df
        print("Updated the original DataFrame!")

    def is_df_changed(self):
        orig_row_count = len(self.orig_df)
        new_row_count = len(self.new_df)

        if orig_row_count != new_row_count:
            return True
        else:
            bool_df = (self.orig_df == self.new_df)
            bool_df = bool_df[bool_df == False]
            bool_df = bool_df.dropna(axis = 0, how = 'all')
            if bool_df.empty:   
                del bool_df
                return False
            else:
                del bool_df
                return True

    def check_continuously(self):
        while True:
            self.read_new_df()
            changed = self.is_df_changed()

            if changed:
                self.update_orig_df()
            
            sleep(1)
