# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import ttk
from pathlib import Path
from typing import Any


class StorySelection(ttk.Frame):

    def __init__(self, root, path: Path, command: dict[str|Any] = {"selected": ""}):
        super().__init__()
        self.path = path

        self.pack(fill="both")
        self.combo_frame = ttk.Frame(self)
        self.combo_frame.pack(fill="both")

        self.combo_stories = ttk.Combobox(self.combo_frame, width = 30)
        self.combo_stories.pack(side="top", pady=3)
        self.combo_stories.bind("<<ComboboxSelected>>", command["selected"])
        self.combo_stories["value"] = [
            file.name[:-4] for file in self.path.iterdir() if ".zip" in file.name
        ]