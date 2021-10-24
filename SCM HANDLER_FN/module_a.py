import pandas as pd
from csv import writer

from observer import Subject

class ClassA(Subject):
    def __init__(self, name =''):
        Subject.__init__(self)
        self.name = name
        self.message = ""


    def add_camera_name(self):
        # Open file in append mode
        with open("database.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(["192.168.1.102","camera 0",0,1,0])
            self.message = "add_camera_name method worked..."
            self.notify()


    def remove_camera_name(self):
        f = open('database.csv', "r+")
        lines = f.readlines()
        lines.pop()
        f = open('database.csv', "w+")
        f.writelines(lines)
        self.message = "remove_camera_name method worked..."
        self.notify()
