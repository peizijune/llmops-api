#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 15/7/2024 09:34
@Author : peizijune@gmail.com
@File   : app.py
"""
from injector import Injector

from internal.router import Router
from internal.server import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

# 当本文件作为main()执行时，才运行debug=True
# 而不是其他文件引用本文件去执行时，也运行debug=True
if __name__ == '__main__':
    app.run(debug=True)
