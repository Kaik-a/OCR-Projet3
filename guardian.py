"""class representing the guardian inside the maze. It is not possible to
MacGyver to go through the exit if he doesn't have the three items hidden inside
the maze"""

from config import GUARDIAN_PICTURE
from macgyver import MacGyver


class Guardian:
    def __init__(self, position: tuple):
        self.picture = GUARDIAN_PICTURE
        self.position = position

    @staticmethod
    def block_exit(macgyver: MacGyver):
        """If MacGyver go all items from maze he can sleep the guardian and go
        through exit, otherwise the guardian knock him out"""
        if macgyver.item_count == 3:
            print("What's happening to me!? Hugh... \n "
                  "The guardian felt asleep")
            return "victory"
        else:
            print("You'll never go out!!! \n "
                  "The guardian knocks out MacGyver's head")
            return "fail"
