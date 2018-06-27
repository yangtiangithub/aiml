# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午5:25.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class DefaultDM(object):

    def __init__(self, configs):
        self.configs = configs


    def process(self, stmt, context, intent, ne):

        if intent == "Greeting":
            return None, "REACTGREET", None

        return None, "REACTGREET", None