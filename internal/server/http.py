#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 12/7/2024 2:52 pm
@Author : peizijune@gmail.com
@File   : http.py
"""
from flask import Flask

from internal.router import Router


# HTTP服务引擎类，继承Flask类
class Http(Flask):
    # *args：非命名参数（直接传入1, 2, ...）
    # **kwargs：命名参数（传入a=1, b=2, ...）
    def __init__(self, *args, router: Router, **kwargs):
        # 调用父类的构造函数
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
