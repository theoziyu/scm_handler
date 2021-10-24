from subject_observer import Observer
from subject_observer import Subject
from dataframe_checker import DataframeChecker

class DataframeObserver(Observer):
    observer_obj = DataframeChecker("dataframe.csv")
    def update(self, subject: Subject) -> None:
        if subject._df_changed:
            print("DataframeObserver: Reacted to the event")
            self.observer_obj.update_orig_df()
            subject._df_changed = False