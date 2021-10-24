from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import pandas as pd


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self):
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
    def add_data_to_df(self,row_value):
        print("the data is added to df")
        df = pd.read_csv("dataframe.csv")
        df.append(row_value).to_csv("dataframe.csv",index=None)

        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def __init__(self,scm_subject):
        self.df = pd.read_csv("dataframe.csv",index_col=None)
        self.scm = scm_subject
    def update(self, subject: Subject):
        self.df= pd.read_csv("dataframe.csv",index_col=None)
        print("observerA is updated: ")
        print(self.df)
    def some_process(self,):
        print("observerA is editting the df.. adding 20 21 22 23")
        df = pd.DataFrame(data={'col1': [20, 21], 'col2': [22, 23]})
        self.scm.add_data_to_df(df)

     


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        self.df= pd.read_csv("dataframe.csv",index_col=None)
        print("observerB df is updated: ")
        print(self.df)


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA(subject)
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    print("subject is adding data ")
    df = pd.DataFrame(data={'col1': [5, 6], 'col2': [7, 8]})
    subject.add_data_to_df(df)
    print("******")
    observer_a.some_process()
    print("****")

    subject.detach(observer_a)

