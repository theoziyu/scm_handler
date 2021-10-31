from scm_handler import SCMHandler
from pubsub import pub
import time


def main():

    #pub.subscribe(listener_camera_ip, "num_of_IPs")
    SCMHandler.register(event = "num_of_IPs")

if __name__ == "__main__":
    main()