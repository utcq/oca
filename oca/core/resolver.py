from utils.config import *
from core.challenge import Challenge
import utils.dumper as dmp
import os
import importlib

class PlResolve():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.plugins = []
        self.modules = []
    
    def load_plugins(self):
        for tag in self.challenge.categories:
            plugs = []
            try: 
                if (tag in CONFIG.keys()):
                    self.plugins += CONFIG[tag]["plugins"]
                    plugs += CONFIG[tag]["plugins"]
            except: pass
            
            for plugin in plugs:
                plug = self.get_plugin(
                    "payloads.{}.{}".format(
                        tag, plugin
                    )
                )
                self.modules.append(plug)
                dmp.print_plugin(plug.__name__)
        print("━"*24)
    
    def run_plugins(self):
        for plug,mod in zip(self.plugins, self.modules):
            dmp.print_plugin_run(mod.__name__)
            exec(
                "mod.{}(self.challenge)".format(
                    plug.capitalize()
                )
            )
            print("━"*24)

    def get_plugin(self, rel_path:str):
        return importlib.import_module(rel_path)
