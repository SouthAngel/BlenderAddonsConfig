
bl_info = {
    "name": "My Blender",
    "author": "User is me",
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


def get_registrant():
    regist_ = importlib.import_module(__package__ + ".registrant")
    return regist_


def register():
    get_registrant().regist_all()


def unregister():
    get_registrant().unregist_all()

    
if __name__ == "__main__":
    register()
