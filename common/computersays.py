#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

import os, copy

from cubed4th import FORTH

from dotenv import load_dotenv
load_dotenv(verbose=True)

class ComputerSays(dict):

    def __init__(self, **kwargs):
        ...

    @staticmethod ### OS_GETENV ###
    def word_OS_under_GETENV__R_s3(e, t, c, s1, s2):
        return (os.getenv(s2, s1),)

    def load(self, name, code):

        self.e = FORTH.Engine("""

```

: id 'id ! ;

        """)

        self.e.cs = ComputerSays()
        self.e.import_lib(None, self.e.cs)

        self.e.execute(code)

        self.__dict__[name] = copy.copy(self.e.root.memory)






