from time import sleep
from random import randint

import pandas as pd

class Registrant():
    def __init__(self, database_path):
        self.database_path = database_path
        self.database = pd.read_csv(self.database_path)
        self.cams = dict()
    
    def update_database(self):
        self.database = pd.read_csv(self.database_path)

    def find_cam(self, cam_name):
        try:
            wanted_cam = self.database[self.database['camera_name'] == cam_name]
            ip = wanted_cam["camera_nickname"]
            model_a = wanted_cam["model_a"]
            model_b = wanted_cam["model_b"]
            model_c = wanted_cam["model_c"]

            return cam_name, ip, model_a, model_b, model_c
        except:
            return 0

    def initialize(self):
        for index in range(len(self.database)):
            cam_name = self.database.loc[index, "camera_name"]
            print("Initializing camera {}...".format(cam_name))
            ip = self.database.loc[index, "camera_nickname"]
            model_a = self.database.loc[index, "model_a"]
            model_b = self.database.loc[index, "model_b"]
            model_c = self.database.loc[index, "model_c"]
            self.cams[cam_name] = (ip, model_a, model_b, model_c)

            sleep(randint(1,2))
            print("Finished initializing camera {}!\n".format(cam_name))

    def register(self, cam_name):
        cam_list = list(self.cams.keys())
        
        if cam_name in cam_list:
            print("{} is already registered!".format(cam_name))
        else:
            self.update_database()
            if not self.find_cam(cam_name):
                print("No such camera")
            else:
                _, ip, m_a, m_b, m_c = self.find_cam(cam_name)
                self.cams[cam_name] = (ip, m_a, m_b, m_c)

    def unregister(self, cam_name):
        cam_list = list(self.cams.keys())

        if cam_name not in cam_list:
            print("{} is not registered!".format(cam_name))
        else:
            del self.cams[cam_name]


    def show_registered(self):
        print("Registered cameras are listed below...")
        cam_list = list(self.cams.keys())
        for index in range(len(cam_list)):
            print("\t{}) {}".format(index+1, cam_list[index]))



def test():
    foo = Registrant("dataframe.csv")
    foo.initialize()
    foo.show_registered()
    foo.unregister("ozlem")
    foo.show_registered()
    foo.register("ozlem")
    foo.show_registered()

test()