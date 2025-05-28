# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

from tkinter import Tk, simpledialog, messagebox
from .story_structure import BeginningStory, MultipleChoices, MultipleStories, SaveDeleteButton, StorySelection
from .story_archive import StoryFilesArchive, StoryFilesLoads
from pathlib import Path
from contextlib import chdir


class MainFrame(Tk):
    """The Story Maker"""
    
    def __init__(self):
        super().__init__()
        self.stories = {"stories": {
            "begin": None,
            "first": "",
            "second": "",
        }}
        self.choices = {"choices":{
            "first": "",
            "second": "",
        }}
        self.title("Story Maker")
        self.scriptures = {"scriptures": ""}
        self.path = Path("~").expanduser().joinpath("StoryMaker")
        self.checking_dir()
        self.combo_stories = StorySelection(self, self.path, {"selected": self.load_formats})
        self.beginning = BeginningStory(self)
        self.multiple_choices_first = MultipleChoices(self, "First Multiple Choices")
        self.multiple_stories_first = MultipleStories(self, "First Stories")
        self.multiple_choices_second = MultipleChoices(self, "Second Multiple Choices")
        self.multiple_stories_second = MultipleStories(self, "Second Stories")
        self.scriptures_ = MultipleStories(self, "Scriptures")
        self.button = SaveDeleteButton(self, 
            {
                "save": self.save_formats,
                "delete": self.delete_zipfile
            }
        )
        self.bind_all("<Control-d>", self.stories_delete)
        self.name_to_save = None

    def _begin_story(self):
        if bg := self.beginning.format_begin():
            self.stories["stories"]["begin"] = bg["begin"]

    def _multiple_stories(self):
        self._begin_story()
        if isinstance(self.stories["stories"]["begin"], str):
            if ms := self.multiple_stories_first.format_stories():
                self.stories["stories"]["first"] = ms
            if ms := self.multiple_stories_second.format_stories():
                self.stories["stories"]["second"] = ms
            del ms
    
    def checking_multiple_stories(self):
        self._multiple_stories()
        check = [
            isinstance(self.stories["stories"]["begin"], str),
            isinstance(self.stories["stories"]["first"], dict),
            isinstance(self.stories["stories"]["second"], dict)
        ]
        return all(check)
    
    def _multiple_choices(self):
        if mc := self.multiple_choices_first.format_choices():
            self.choices["choices"]["first"] = mc
        if mc := self.multiple_choices_second.format_choices():
            self.choices["choices"]["second"] = mc
        del mc

    def checking_multiple_choices(self):
        self._multiple_choices()
        check = [
            isinstance(self.choices["choices"]["first"], dict),
            isinstance(self.choices["choices"]["second"], dict)
        ]
        return all(check)
    
    def _scriptures(self):
        if sc := self.scriptures_.format_stories():
            self.scriptures["scriptures"] = sc

    def checking_scriptures(self):
        self._scriptures()
        return isinstance(self.scriptures["scriptures"], dict)    
    
    def checking_dir(self):
        if not self.path.exists():
            with chdir(self.path.parent):
                Path("StoryMaker").mkdir()
    
    def _reload_combo(self):
        self.combo_stories.combo_stories["value"] = [
            file.name[:-4] for file in self.path.iterdir() if ".zip" in file.name
        ]

    def save_formats(self):
        checking = [
            self.checking_multiple_stories(),
            self.checking_multiple_choices(),
            self.checking_scriptures()
        ]
        if all(checking):
            
            confirm = (
                messagebox.askyesno(
                    "Story Maker", f"Save with same file name {self.name_to_save}", parent=self
                )
                if self.name_to_save else False
            )
            ask = (
                simpledialog.askstring("Story Maker", "Name of file:", parent=self) 
                if not confirm else
                self.name_to_save
            )
            if ask:
                data = [self.stories, self.choices, self.scriptures]
                archive = StoryFilesArchive(self.path, *data)    
                with chdir(self.path):
                    archive.archiving_zip(ask)
                del data, archive
                messagebox.showinfo(
                    "Story Maker", f"{self.path.joinpath(ask)}.zip file has been created!", parent=self
                )
                self._reload_combo()

    def load_formats(self, event=None):
        ask = self.combo_stories.selection_get()
        self.stories_delete()
        if ask and self.path.joinpath(f"{ask}.zip").exists():
            stores = []
            with chdir(self.path):
                stores.extend(StoryFilesLoads(self.path).data_extract(ask))
            self.beginning.insert_text({"begin": stores[0]["stories"]["begin"]})
            self.multiple_choices_first.insert_text(stores[1]["choices"]["first"])
            self.multiple_stories_first.insert_text(stores[0]["stories"]["first"])
            self.multiple_choices_second.insert_text(stores[1]["choices"]["second"])
            self.multiple_stories_second.insert_text(stores[0]["stories"]["second"])
            self.scriptures_.insert_text(stores[2]["scriptures"])
            self.name_to_save = ask
            del stores
        else:
            if ask:
                messagebox.showinfo("Story Maker", f"{ask}.zip is not exist!", parent=self)        

    def stories_delete(self, event=None):
        
        self.beginning.delete_text()
        self.multiple_choices_first.delete_all()
        self.multiple_stories_first.delete_all()
        self.multiple_choices_second.delete_all()
        self.multiple_stories_second.delete_all()
        self.scriptures_.delete_all()
    
    def delete_zipfile(self):
        if self.name_to_save:
            ask = messagebox.askokcancel(
                "Story Maker", f"Do you want to delete this {self.name_to_save}.zip file?", parent=self
            )
            if ask:
                check_path = StoryFilesArchive(self.path)
                file_path = check_path.path.joinpath(f"{self.name_to_save}.zip") 
                if file_path.exists():
                    check_path.delete_zipfile(self.name_to_save)
                    messagebox.showinfo("Story Maker", f"{file_path} has been deleted!")
                    self._reload_combo()
                    self.name_to_save = None
                del check_path, file_path

def story_maker():
    MainFrame().mainloop()
