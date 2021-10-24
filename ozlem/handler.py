from DataBaseSubject import DataBaseSubject
from ClassA import ClassA
from ClassB import ClassB
import pandas as pd
if __name__ == "__main__":
    # The client code.

    subject = DataBaseSubject()

    observer_a = ClassA(subject)
    subject.attach(observer_a)

    observer_b = ClassB()
    subject.attach(observer_b)
    print("subject is adding data ")
    df = pd.DataFrame(data={'camera_ip': ["5555.5555.5.5:9999"], 'camera_name': ['oğuz'], 'model_a':False,'model_b': True})
    
    subject.add_data_to_df(df)
    print("******")
    observer_a.some_process()
    print("****")

    subject.detach(observer_a)

