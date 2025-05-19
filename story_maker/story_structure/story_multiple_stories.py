# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import ttk, Text

__all__ = [""]


class MultipleStories(ttk.LabelFrame):
    """Multiple Stories Results"""

    def __init__(self, root, judul: str, skipped: bool = False):
        super().__init__()
        self.skipped = skipped

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

        if not self.skipped:
            self.lif_right_choice = ttk.LabelFrame(self.left_frame, text="C", labelanchor="w")
            self.lif_right_choice.pack(fill="both", expand=1)
            self.text_c = Text(self.lif_right_choice, height=1, wrap="word")
            self.text_c.pack(side="left", fill="both", expand=1)
            self.scrollbar = ttk.Scrollbar(self.lif_right_choice, orient="vertical", command=self.text_c.yview)
            self.text_c.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.pack(side="right", fill="y")

    def format_stories(self) -> (dict[str, str] | None):

        stories = [
        self.text_a.get("1.0", "end")[:-1].strip(),
        self.text_b.get("1.0", "end")[:-1].strip(),
        self.text_c.get("1.0", "end")[:-1].strip(),
        ] if not self.skipped else [
        self.text_a.get("1.0", "end")[:-1].strip(),
        self.text_b.get("1.0", "end")[:-1].strip(),
        ]
        if all(stories):
            if len(stories) == 3:
                return {
                    "A": stories[0],
                    "B": stories[1],
                    "C": stories[2],
                }
            else:
                return {
                    "A": stories[0],
                    "B": stories[1],
                }
    
    def delete_all(self):
        stories = [
            self.text_a, self.text_b, self.text_c,
        ] if not self.skipped else [
            self.text_a, self.text_b,
        ]
        
        for story in stories:
            story.delete("1.0", "end")
    
    def insert_text(self, format_: dict[str|str]):
        self.delete_all()
        stories = [
            self.text_a, self.text_b, self.text_c,
        ] if not self.skipped else [
            self.text_a, self.text_b,
        ]
        sentences = [
            format_["A"], format_["B"], format_["C"]
        ] if not self.skipped else [
            format_["A"], format_["B"]
        ]
        for story, sentence in zip(stories, sentences):
            story.insert("1.0", sentence)
        del stories, sentences