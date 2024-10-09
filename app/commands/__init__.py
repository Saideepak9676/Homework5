from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class CommandHandler:
    def __init__(self):
        """Initialize the command handler with an empty command dictionary."""
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with the given name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute the command associated with the command name."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
