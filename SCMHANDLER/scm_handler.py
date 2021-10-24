from pubsub import pub
import pandas as pd
import time
from eventhandler import EventHandler
from pandas.core.frame import DataFrame

class SCMHandler:     

    def __init__(self):

        self.data = pd.read_csv('/home/elif/Desktop/SCMHANDLER/database.csv',sep=';')
        #self.event_handler = EventHandler('cameraIPs', 'Model_info')
        #self.event_handler.link(self.add_new_camera, 'Camera Ips')
        #self.event_handler.link(self.model_info, 'Model_info')

    def initialize(event):

        if(event=="num_of_IPs" and self.dataframe.shape[0]!=0):
            return True
    
    def add_new_camera(self, camera_ip, camera_name, model_a, model_b, model_c):
                
        self.data.loc[len(self.data.index)] = [camera_ip, camera_name, model_a, model_b, model_c]  
        #self.data = self.data.append([camera_ip, camera_name, model_a, model_b, model_c])
        self.data.to_csv('/home/elif/Desktop/SCMHANDLER/database.csv', index=False, sep=';', header = True)
        pub.sendMessage("num_of_IPs", arg = {'topic': 'Güncellenen aktif kamera sayısı:', 'news': self.data.shape[0] })
        #print(self.data)
    

    def view_df(self):
        
        df = DataFrame()
        df = self.data
        
        return df
      

    def delete(self, camera_IP):
                
        index_to_remove =self.data[self.data['camera IP']== camera_IP].index.values.astype(int)[0]
        self.data.drop(index_to_remove,axis=0, inplace = True)
        self.data.to_csv('/home/elif/Desktop/SCMHANDLER/database.csv', index=False, sep=';', header = True)
        pub.sendMessage("num_of_IPs", arg = {'topic': 'Güncellenen aktif kamera sayısı:', 'news': self.data.shape[0] })
  

    def listener_camera_ip(arg):
        # Bu fonksiyon kamera sayısı değiştiğinde tetiklenir.
        # Burada dönen aktif kamera sayısını alıp
        # dinleyen class gereken islemleri yapabilir.
        print(arg['topic'], arg["news"])
        print("Bu func tetiklendi")
  
    def register(event):
        """Parameters:
            event: num_of_IPs
        """
        if(event == "num_of_IPs"):
            pub.subscribe(SCMHandler.listener_camera_ip, "num_of_IPs")
    
    def unregister(event):
        """Parameters:
            event: num_of_IPs
        """
        if(event == "num_of_IPs"):
            #pub.unsubscribe(listener, topicName)()
            pub.unsubscribe(SCMHandler.listener_camera_ip, "num_of_IPs")

   
def listener_model_nums(arg):

    print("New models here", arg['topic'])
    print(arg["news"])
    print()

def num_of_camIPs():
    df = pd.read_csv('/home/elif/Desktop/SCMHANDLER/database.csv')
    return df.shape[0]


def main():
    pass
    #num_of_cam = num_of_camIPs()
    #print("Aktif kamera sayısı:", num_of_cam)
    #time.sleep(15)
    ##print(num_of_camIPs())
    #if(num_of_cam!=num_of_camIPs()):
    #    pub.sendMessage("num_of_IPs", arg = {'topic': 'Güncellenen aktif kamera sayısı:', 'news': num_of_camIPs() })

    
    #obj = SCMHandler()

    # Register Listeners
    #pub.subscribe(listener_camera_ip, "camera 1")
    #pub.subscribe(listener_camera_ip, "camera 2")
    #pub.subscribe(listener_model_nums, "Model A")

    # Send messages to all listeners of topics

    #pub.sendMessage("camera 1", arg = {'topic': 'Aktif', 'news': 'Modeli seç' })
    #pub.sendMessage("camera 2", arg = {'topic': 'Pasif', 'news': 'Modeli durdur'})
    #pub.sendMessage("Model A", arg = {'topic': 'Çalışıyor', 'news': 'Alarm verdi'})
    


if __name__ == "__main__":
    main()