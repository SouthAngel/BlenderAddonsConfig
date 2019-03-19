import importlib
import bpy


def register():
    print("Load test")


def unregister():
    print("Unregister test")

    
if __name__ == "__main__":
    register()
