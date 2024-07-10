#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 10/7/2024 6:03 pm
@Author : peizijune@gmail.com
@File   : app_handler.py
"""


# $ pip install flask
class AppHandler:
    """应用控制器"""

    def ping(self):
        return {"ping": "pong"}
