from __future__ import annotations
from typing import List

from subject_observer import Subject
from subject_observer import Observer

class ConcreteSubject(Subject):

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

