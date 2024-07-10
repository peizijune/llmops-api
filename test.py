#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 10/7/2024 16:44
@Author : peizijune@gmail.com
@File   : test.py
"""
from injector import inject, Injector


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Name of Class A: {self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
