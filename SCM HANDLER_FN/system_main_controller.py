from observer import Subject
from module_a import ClassA
from module_b import ClassB

def main():
    class_a_obj = ClassA("Class A")
    class_b_obj = ClassB()

    class_a_obj.attach(class_b_obj)

    class_a_obj.add_camera_name()
    class_a_obj.remove_camera_name()

if __name__ == "__main__":
    main()