# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午5:15.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class DefaultNLU(object):

    def __init__(self, configs):
        self.configs = configs


    def process(self, statement):
        # 输入是一个Statement数据，已经做好分词、依存句法分析、情感分析等
        # 参见Chatbot.sessions.statement

        # 理解部分（意图识别、实体抽取

        return "Chitchat", None     # 返回意图、实体DICT