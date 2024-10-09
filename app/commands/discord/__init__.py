import sys
from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        print('I Will send something to discord')