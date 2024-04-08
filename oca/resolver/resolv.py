from config import *
from resolver.dynport import *
from challenge import Challenge
import dumper as dmp

class PlResolve():
    def __init__(self, chall: Challenge):
        self.challenge = chall
        self.plugins = []
        self.modules = []
    
    def load_plugins(self):
        for tag in self.challenge.categories:
            self.plugins = []
            try: 
                self.plugins = CONFIG[tag]["plugins"]
            except: pass
            
            for plugin in self.plugins:
                plug = get_plugin(
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