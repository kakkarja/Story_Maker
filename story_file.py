# -*- coding: utf-8 -*-
# Copyright © kakkarja (K A K)

import json
from pathlib import Path
from enum import Enum


Test = """
            3 Files:
            - stories
            - choices
            - scriptures

            These files are json formats:
            Stories - 
            {"stories": {
                    "begin": "......",
                    "second": {
                        "A": ".....",
                        "B": ".....",
                        "C": ".....",
                    },
                    "third": {
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

class Choices(Enum):
    A = 1
    B = 2
    C = 3


class SavingFiles:
    pass

