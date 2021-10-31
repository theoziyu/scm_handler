from event import Subject, ConcreteSubject, Observer

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverA: Reacted to the event. Added to dataframe.")
        

def main():
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

if __name__ == "__main__":
    main()
