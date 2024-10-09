import os
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv

class App:
    def __init__(self): 
        load_dotenv()
        self.settings = {}  
      
        for key, value in os.environ.items():
            self.settings[key] = value
  
        self.settings.setdefault('ENVIRONMENT', 'TESTING')        
        self.command_handler = CommandHandler()

    def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
        return self.settings[envvar]
    
    def load_plugins(self):
     
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue 
    def start(self):
       
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())