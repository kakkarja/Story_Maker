# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import ttk, Text
from typing import Any


class BeginningStory(ttk.LabelFrame):
    """Beginning of story"""

    def __init__(self, root):
        super().__init__()
    
        self.config(text="Beginning of a story")
        self.pack(fill="both", expand=1)
        self.frame_top = ttk.Frame(self)
        self.frame_top.pack(fill="both", expand=1)
        self.begin = Text(self.frame_top, height=1, wrap="word")
        self.begin.pack(side="left", fill="both", expand=1)
        self.scrollbar = ttk.Scrollbar(self.frame_top, orient="vertical", command=self.begin.yview)
        self.begin.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")


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
        self.entry_a = ttk.Entry(self.lif_left_choice)
        self.entry_a.pack(fill="x", expand=1)

        self.lif_mid_choice = ttk.LabelFrame(self.left_frame, text="B", labelanchor="w")
        self.lif_mid_choice.pack(side="left", fill="x", expand=1)
        self.entry_b = ttk.Entry(self.lif_mid_choice)
        self.entry_b.pack(fill="x", expand=1)

        self.lif_right_choice = ttk.LabelFrame(self.left_frame, text="C", labelanchor="w")
        self.lif_right_choice.pack(side="left", fill="x", expand=1)
        self.entry_c = ttk.Entry(self.lif_right_choice)
        self.entry_c.pack(fill="x", expand=1)


class MultipleStories(ttk.LabelFrame):
    """Multiple Stories Results"""

    def __init__(self, root, judul: str, skipped: bool = False):
        super().__init__()

        self.config(text=judul)
        self.pack(fill="both", expand=1)
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(fill="both", expand=1)

        self.lif_left_choice = ttk.LabelFrame(self.left_frame, text="A", labelanchor="w")
        self.lif_left_choice.pack(fill="both", expand=1)
        self.text_a = Text(self.lif_left_choice, height=1, wrap="word")
        self.text_a.pack(side="left", fill="both", expand=1)
        self.scrollbar = ttk.Scrollbar(self.lif_left_choice, orient="vertical", command=self.text_a.yview)
        self.text_a.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")


        self.lif_mid_choice = ttk.LabelFrame(self.left_frame, text="B", labelanchor="w")
        self.lif_mid_choice.pack(fill="both", expand=1)
        self.text_b = Text(self.lif_mid_choice, height=1, wrap="word")
        self.text_b.pack(side="left", fill="both", expand=1)
        self.scrollbar = ttk.Scrollbar(self.lif_mid_choice, orient="vertical", command=self.text_b.yview)
        self.text_b.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        if not skipped:
            self.lif_right_choice = ttk.LabelFrame(self.left_frame, text="C", labelanchor="w")
            self.lif_right_choice.pack(fill="both", expand=1)
            self.text_c = Text(self.lif_right_choice, height=1, wrap="word")
            self.text_c.pack(side="left", fill="both", expand=1)
            self.scrollbar = ttk.Scrollbar(self.lif_right_choice, orient="vertical", command=self.text_c.yview)
            self.text_c.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.pack(side="right", fill="y")


class SaveButton(ttk.Frame):
    """Saving Button"""

    def __init__(self, root, judul: str, command: Any):
        super().__init__()

        self.pack(fill="both")
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill="both")
        self.save = ttk.Button(self.button_frame,text=judul, command=command)
        self.save.pack(fill="both", expand=1)