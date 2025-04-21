# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

import json
import os
from pathlib import Path
from enum import StrEnum
from zipfile import is_zipfile, ZipFile


Test = """
            3 Files:
            - stories
            - choices
            - scriptures

            These files are json formats:
            Stories - 
            {"stories": {
                    "begin": "......",
                    "first": {
                        "A": ".....",
                        "B": ".....",
                        "C": ".....",
                    },
                    "second": {
                        "A": ".....",
                        "B": ".....",
                        "C": ".....",
                    }
                }
            }

            Choices -
            {"choices":
                { 
                    "first": {
                        "A": ".....",
                        "B": ".....",
                        "C": ".....",
                    },
                    "second": {
                        "A": ".....",
                        "B": ".....",
                        "C": ".....",
                    }
                }
            }

            Scriptures -
            {"scriptures":
                {
                    "A": ".....",
                    "B": ".....",
                }
            }
"""

class Choices(StrEnum):
    A = "A"
    B = "B"
    C = "C"


class StoryFilesData:

    def __init__(self, stories: dict[str, str], choices: dict[str, str], scriptures: dict[str, str]):
        self.stories = stories
        self.choices = choices
        self.scriptures = scriptures

    

class StoryFilesArchive(StoryFilesData):
    """Archiving files of Stories, with Json format"""

    def __init__(self, path: str, **kwargs):
        super().__init__(**kwargs)
        self.path = Path(path)
        

    def creating_files(self) -> list[str]:
        """Creating json files for each story"""

        files = {"stories": self.stories, "choices": self.choices, "scriptures": self.scriptures}
        list_files = []
        for k, v in files.items():
            pth = self.path.joinpath(f"{k}.json")
            if not pth.exists():
                with open(pth, "w") as story:
                    json.dump(v, story)
            list_files.append(pth)
            del pth
        return list_files
    
    def deleting_files(self):
        """deleting json files"""

        files = ["stories", "choices", "scriptures"]
        for file in files:
            pth = self.path.joinpath(f"{file}.json")
            if pth.exists():
                os.remove(pth)
            del pth
        del files
    
    def archiving_zip(self, name: str):
        """Archiving story to a zip file for loading or deleting all json files"""

        if not is_zipfile(self.path.joinpath(f"{name}.zip")):
            with ZipFile(self.path.joinpath(f"{name}.zip"), "x") as zipped:
                for file in self.creating_files():
                    zipped.write(file.name)
            self.deleting_files()

    def unarchived_zip(self, name: str):
        """Extracting file from a zip file"""
        
        if is_zipfile(self.path.joinpath(f"{name}.zip")):
            with ZipFile(self.path.joinpath(f"{name}.zip")) as zipped:
                for file in self.creating_files():
                    zipped.extract(file.name)


class StoryFilesLoads:
    pass


class StoryFilesSets:
    pass


if __name__ == "__main__":

    path = Path(__file__).parent
    data = StoryFilesData({"Stories": "..."}, {"choices": "..."}, {"scriptures": "..."})
    story = StoryFilesArchive(
        path, stories=data.stories, choices=data.choices, scriptures=data.scriptures
    )
    # story.archiving_zip("test")
    # story.unarchived_zip("test")
    story.deleting_files()