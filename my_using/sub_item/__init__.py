
bl_info = {
    "name": "My Blender",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "Config user preferences",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "category": "User",
    }


import importlib
import bpy


def register():
    regist_ = importlib.import_module(__package__ + ".registrant")
    regist_.regist_all()


def unregister():
    print("Unregister %s" % bl_info["name"])

    
if __name__ == "__main__":
    register()
