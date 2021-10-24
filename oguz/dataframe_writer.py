from time import sleep
import pandas as pd

class DataframeWriter():
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.orig_df = pd.read_csv(self.csv_path)

    def update_csv(self):
        print("Updating the Database (csv) ...")
        self.orig_df.to_csv(self.csv_path, index=False)
        print("Updated the Database (csv)!")

    def add_camera_name(self, cam_name):
        print("Adding a new camera named", cam_name)
        ip = input("Enter the IP of camera (xxx.yyy.z.w:uuuu):")
        model_a = input("Run on Model A? (True or False):")
        model_b = input("Run on Model B? (True or False):")
        model_c = input("Run on Model C? (True or False):")
        temp_df = pd.DataFrame([[cam_name, ip, model_a, model_b, model_c]],
                        columns=["camera_name", "camera_ip",
                                 "model_a", "model_b", "model_c"])
        self.orig_df = self.orig_df.append(temp_df, ignore_index=True)
        self.update_csv()
        print("Finished adding the new camera", cam_name)
    
    def remove_camera_name(self, cam_name):
        print("Removing camera {} from the database...".format(cam_name))
        indexNames = self.orig_df[
            self.orig_df['camera_name'] == cam_name].index
        self.orig_df.drop(indexNames, inplace=True)
        self.update_csv()
        print("Removed camera {} from the database!".format(cam_name))

    def get_camera_name(self, cam_name):
        print("Getting the info for camera {}...".format(cam_name))
        wanted_cam = self.orig_df[self.orig_df['camera_name'] == cam_name]
        ip = wanted_cam["camera_ip"]
        model_a = wanted_cam["model_a"]
        model_b = wanted_cam["model_b"]
        model_c = wanted_cam["model_c"]

        return cam_name, ip, model_a, model_b, model_c

    def update_camera_name(self, cam_name):
        print("Updating the info for camera {}...".format(cam_name))
        print("Press ENTER to keep the existing value.")
        indexes = self.orig_df[
            self.orig_df['camera_name'] == cam_name].index
        name = input("Enter the new namefor the camera: ")
        ip = input("Enter the IP of the camera (xxx.yyy.z.w:uuuu): ")
        model_a = input("Run on Model A? (True or False): ")
        model_b = input("Run on Model B? (True or False): ")
        model_c = input("Run on Model C? (True or False): ")
        
        if name != "":
            self.orig_df.loc[indexes, "camera_name"] = name
        if ip != "":
            self.orig_df.loc[indexes, "camera_ip"] = ip
        if model_a != "":
            self.orig_df.loc[indexes, "model_a"] = model_a
        if model_b != "":
            self.orig_df.loc[indexes, "model_b"] = model_b
        if model_c != "":
            self.orig_df.loc[indexes, "model_c"] = model_c
        self.update_csv()
        print("Finished updating the database!")

def test():
    csv_path = "dataframe.csv"
    writer_obj = DataframeWriter(csv_path)
    print("Setting up environment, can take several seconds...")
    sleep(5)
    which_cam = input("What camera to update?\n")
    writer_obj.update_camera_name(which_cam)

test()