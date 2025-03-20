# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import ttk, Text


class BeginningStory(ttk.LabelFrame):
    """Beginning of story"""

    def __init__(self, root):
        super().__init__()
    
        self.config(text="Beginning of a story")
        self.pack(fill="x")
        self.b = Text(self, height=4)
        self.b.pack(fill="x")


class MultipleChoices(ttk.LabelFrame):
    """Multiple Choices"""

    def __init__(self, root, judul: str):
        super().__init__()

        self.config(text=judul)
        self.pack(fill="x")
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(fill="x", expand=1)

        self.lif_left_choice = ttk.LabelFrame(self.left_frame, text="A", labelanchor="w")
        self.lif_left_choice.pack(side="left", fill="x", expand=1)
        self.lif_entry_a = ttk.Entry(self.lif_left_choice)
        self.lif_entry_a.pack(fill="x", expand=1)

        self.lif_mid_choice = ttk.LabelFrame(self.left_frame, text="B", labelanchor="w")
        self.lif_mid_choice.pack(side="left", fill="x", expand=1)
        self.lif_entry_b = ttk.Entry(self.lif_mid_choice)
        self.lif_entry_b.pack(fill="x", expand=1)

        self.lif_right_choice = ttk.LabelFrame(self.left_frame, text="C", labelanchor="w")
        self.lif_right_choice.pack(side="left", fill="x", expand=1)
        self.lif_entry_c = ttk.Entry(self.lif_right_choice)
        self.lif_entry_c.pack(fill="x", expand=1)


class MultipleStories(ttk.LabelFrame):
    """Multiple Stories Results"""

    def __init__(self, root, judul: str, skipped: bool = False):
        super().__init__()

        self.config(text=judul)
        self.pack(fill="x")
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(fill="x")

        self.lif_left_choice = ttk.LabelFrame(self.left_frame, text="A", labelanchor="w")
        self.lif_left_choice.pack(fill="x")
        self.lif_text_a = Text(self.lif_left_choice, height=4)
        self.lif_text_a.pack(fill="x")

        self.lif_mid_choice = ttk.LabelFrame(self.left_frame, text="B", labelanchor="w")
        self.lif_mid_choice.pack(fill="x")
        self.lif_text_b = Text(self.lif_mid_choice, height=4)
        self.lif_text_b.pack(fill="x")

        if not skipped:
            self.lif_right_choice = ttk.LabelFrame(self.left_frame, text="C", labelanchor="w")
            self.lif_right_choice.pack(fill="x")
            self.lif_text_c = Text(self.lif_right_choice, height=4)
            self.lif_text_c.pack(fill="x")