from app.commands import Command

class HelloCommand(Command):
    def execute(self):
        """Prints a greeting message."""
        print("Hello!")

