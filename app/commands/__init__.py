from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with a given name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Try to execute a command by its name, handling non-existent commands gracefully."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

class ExampleCommand(Command):
    def execute(self):
        print("Executing example command.")
