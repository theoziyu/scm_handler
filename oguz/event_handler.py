from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

from dataframe_checker import DataframeChecker
from dataframe_writer import DataframeWriter


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):

    _state: int = None
    _df_changed: bool = False
    _cam_edit: bool = False
    _cam_add: bool = False
    _cam_del: bool = False
    _cam_name: str = ""

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def add_camera_name(self, cam_name) -> None:
        print("\nAdding camera_name", cam_name)
        self._cam_name = cam_name
        self._cam_add = True
        self.notify()
        self.notify()

    def update_camera_name(self, cam_name) -> None:
        print("\nUpdating camera_name", cam_name)
        self._cam_name = cam_name
        self._cam_edit = True
        self.notify()
        self.notify()

    def remove_camera_name(self, cam_name) -> None:
        print("\nRemoving camera_name", cam_name)
        self._cam_name = cam_name
        self._cam_del = True
        self.notify()
        self.notify()

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class DataframeObserver(Observer):
    observer_obj = DataframeChecker("dataframe.csv")
    def update(self, subject: Subject) -> None:
        if subject._df_changed:
            print("DataframeObserver: Reacted to the event")
            self.observer_obj.update_orig_df()
            subject._df_changed = False


class DataframeEditor(Observer):
    editor_obj = DataframeWriter("dataframe.csv")
    def update(self, subject: Subject) -> None:
        if subject._cam_edit:
            print("DataframeEditor: Reacted to the edit event")
            self.editor_obj.update_camera_name(subject._cam_name)
            subject._df_changed = True
            subject._cam_edit = False
            subject._cam_name = ""
        if subject._cam_add:
            print("DataframeEditor: Reacted to the add event")
            self.editor_obj.add_camera_name(subject._cam_name)
            subject._df_changed = True
            subject._cam_add = False
            subject._cam_name = ""
        if subject._cam_del:
            print("DataframeEditor: Reacted to the del event")
            self.editor_obj.remove_camera_name(subject._cam_name)
            subject._df_changed = True
            subject._cam_del = False
            subject._cam_name = ""


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = DataframeObserver()
    subject.attach(observer_a)

    observer_b = DataframeEditor()
    subject.attach(observer_b)

    subject.remove_camera_name("ozlem")
    subject.add_camera_name("ozlem")
    subject.update_camera_name("bayat")
