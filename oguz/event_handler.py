from __future__ import annotations

from concrete_subject import ConcreteSubject
from dataframe_observer import DataframeObserver
from dataframe_editor import DataframeEditor

if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = DataframeObserver()
    subject.attach(observer_a)

    observer_b = DataframeEditor()
    subject.attach(observer_b)

    # subject.remove_camera_name("elif")
    subject.add_camera_name("777.777.7.7:6666")
    subject.update_camera_name("222.222.2.2:1111")
