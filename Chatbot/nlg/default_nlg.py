# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午5:30.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

from Chatbot.sessions.statement import Statement

class DefaultNLG(object):

    def __init__(self, configs):
        self.configs = configs

    def process(self, status, target, policy):
        return Statement(text="默认回复。", from_user=False)