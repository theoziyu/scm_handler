from scm_handler import SCMHandler
from pubsub import pub

def main():
    
    #SCMHandler.register_camera_ip()
    #pub.subscribe(SCMHandler.listener_camera_ip, "num_of_IPs")
    obj=SCMHandler()
    print("New IP camera is adding...")
    obj.add_new_camera(camera_ip='192.168.1.105', camera_name='camera 6', model_a='1', model_b='0', model_c='1')
    print("An IP camera is removing...")
    obj.delete(camera_IP='192.168.1.100')
    print("Display df")           
    print(obj.view_df())
    
if __name__ == "__main__":
    main()