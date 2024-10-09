from app.commands import CommandHandler
from app.commands.discord import DiscordCommand
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.hello import HelloCommand

class App:
    def __init__(self): 
        self.command_handler = CommandHandler()
        self.register_commands()

    def register_commands(self):
        """Register available commands with the command handler."""
        commands = {
            "greet": GreetCommand(),
            "goodbye": GoodbyeCommand(),
            "exit": ExitCommand(),
            "menu": MenuCommand(),
            "discord": DiscordCommand(),
            "hello": HelloCommand(),
        }

        for command_name, command_instance in commands.items():
            self.command_handler.register_command(command_name, command_instance)

    def start(self):
        """Start the command loop."""
        print("Type 'exit' to exit.")
        while True:  
            user_input = input(">>> ").strip()
            self.command_handler.execute_command(user_input)
