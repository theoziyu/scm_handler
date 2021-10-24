import Module_a, Module_b 
import scm_handler
from multiprocessing import Process

def main():
    #p1 = Process(target=scm_handler.main(), args=())
    #p2 = Process(target=Module_a.main(), args=())
    #p3 = Process(target=Module_b.main(), args=())

    #p1.start()
    #p3.start()
    #p2.start() 
    
    Module_b.main()
    #scm_handler.main()    
    Module_a.main()    

if __name__ == "__main__":
    main()