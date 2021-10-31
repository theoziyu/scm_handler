from event import Subject, ConcreteSubject, Observer

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverB: Reacted to the event. Added to dataframe")


def main():
    subject=ConcreteSubject()
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    #subject.some_business_logic()
    subject.add_new_camera(camera_ip='192.168.1.105', camera_name='camera 6', model_a='1', model_b='0', model_c='1')
    
if __name__ == "__main__":
    main()

