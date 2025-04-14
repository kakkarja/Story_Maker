# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import Tk, ttk
from story_maker import BeginningStory, MultipleChoices, MultipleStories, SaveButton

class MainFrame(Tk):
    """The Story Maker"""
    
    def __init__(self):
        super().__init__()
        self.beginning = BeginningStory(self)
        self.multiple_choices_first = MultipleChoices(self, "First Multiple Choices")
        self.multiple_stories_second = MultipleStories(self, "Second stories")
        self.multiple_choices_second = MultipleChoices(self, "Second Multiple Choices")
        self.multiple_stories_third = MultipleStories(self, "Third Stories")
        self.scriptures = MultipleStories(self, "Scriptures", True)
        self.button = SaveButton(self, "Save", self.stories_formats)

    def stories_formats(self):
        print("Test")
        # store = {}
        # self.beginning.begin.get("1.0", "end")
        # self.multiple_choices_first.entry_a.get()
        # self.multiple_stories_second.text_a.get("1.0", "end")


def main():
    story = MainFrame()
    story.mainloop()


if __name__ == "__main__":
    main()