import importlib

def get_plugin(rel_path:str):
    return importlib.import_module(rel_path)
