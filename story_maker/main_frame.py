# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import Tk
from .story_structure import BeginningStory, MultipleChoices, MultipleStories, SaveLoadButton


class MainFrame(Tk):
    """The Story Maker"""
    
    def __init__(self):
        super().__init__()
        self.stories = {"stories": {
            "begin": "",
            "first": "",
            "second": "",
        }}
        self.choices = {"choices":{
            "first": "",
            "second": "",
        }}
        self.scriptures = {"scriptures": ""}
        self.beginning = BeginningStory(self)
        self.multiple_choices_first = MultipleChoices(self, "First Multiple Choices")
        self.multiple_stories_first = MultipleStories(self, "First Stories")
        self.multiple_choices_second = MultipleChoices(self, "Second Multiple Choices")
        self.multiple_stories_second = MultipleStories(self, "Second Stories")
        self.scriptures = MultipleStories(self, "Scriptures", True)
        self.button = SaveLoadButton(self, 
            {
                "save": self.stories_formats, 
                "load": self.stories_formats
            }
        )
    def _begin_story(self):
        if bg := self.beginning.format_begin():
            self.stories["stories"]["begin"] = bg["begin"]

    def _multiple_s(self):
        pass

    def stories_formats(self):
        print("Test")
        # store = {}
        # self.beginning.begin.get("1.0", "end")
        # self.multiple_choices_first.entry_a.get()
        # self.multiple_stories_second.text_a.get("1.0", "end")


def main():
    MainFrame().mainloop()
