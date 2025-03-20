from tkinter import Tk
from story_maker import BeginningStory, MultipleChoices, MultipleStories

class MainFrame(Tk):
    """The Story Maker"""
    
    def __init__(self):
        super().__init__()
        self.l1 = BeginningStory(self)
        self.l2 = MultipleChoices(self, "First Multiple Choices")
        self.l3 = MultipleStories(self, "Second stories")
        self.l4 = MultipleChoices(self, "Second Multiple Choices")
        self.l5 = MultipleStories(self, "Third Stories")
        self.l6 = MultipleStories(self, "Scriptures", True)

def main():
    story = MainFrame()
    story.mainloop()


if __name__ == "__main__":
    main()