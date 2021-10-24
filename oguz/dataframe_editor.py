from subject_observer import Subject
from subject_observer import Observer
from dataframe_writer import DataframeWriter

class DataframeEditor(Observer):
    editor_obj = DataframeWriter("dataframe.csv")
    def update(self, subject: Subject) -> None:
        if subject._cam_edit:
            print("DataframeEditor: Reacted to the edit event")
            self.editor_obj.update_camera_name(subject._cam_name)
            subject._df_changed = True
            subject._cam_edit = False
            subject._cam_name = ""
        if subject._cam_add:
            print("DataframeEditor: Reacted to the add event")
            self.editor_obj.add_camera_name(subject._cam_name)
            subject._df_changed = True
            subject._cam_add = False
            subject._cam_name = ""
        if subject._cam_del:
            print("DataframeEditor: Reacted to the del event")
            self.editor_obj.remove_camera_name(subject._cam_name)
            subject._df_changed = True
            subject._cam_del = False
            subject._cam_name = ""