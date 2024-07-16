#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 12/7/2024 2:33 pm
@Author : peizijune@gmail.com
@File   : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


# 路由类
@inject
@dataclass
class Router:
    app_handler: AppHandler

    # 注册路由
    def register_router(self, app: Flask):
        # 1. 创建一个蓝图（使用蓝图管理一组路由）
        bp = Blueprint('llmops', __name__, url_prefix='')

        # 2. 将url与对应的控制器方法（不需要加()，加()代表返回的执行结果）做绑定
        # default是GET
        bp.add_url_rule('/ping', view_func=self.app_handler.ping)

        # 3. 在应用上去注册蓝图
        app.register_blueprint(bp)
