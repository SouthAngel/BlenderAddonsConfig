# coding = utf-8
import os
import importlib


sub_folder_name = "sub_item"
mod_names = [os.path.splitext(x)[0] for x in 
        os.listdir(os.path.join(os.path.dirname(__file__), sub_folder_name)) 
        if not x.startswith("__") and x.endswith(".py")]
mods = []


def regist_all():
    print("regist all")
    global mods
    mods = [importlib.import_module(".".join((__package__, sub_folder_name, x))) 
            for x in iter(mod_names)
            ]
    for mod in iter(mods):
        if hasattr(mod, "register"):
            mod.register()


def unregist_all():
    print("unregist all")
    global mods
    for mod in iter(mods):
        if hasattr(mod, "unregister"):
            mod.unregister()
    
