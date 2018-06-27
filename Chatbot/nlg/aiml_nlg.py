# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午6:08.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import aiml

class AimlNLG(object):

    def __init__(self, configs):
        self.configs = configs

        self.aiml = aiml.Kernel()
        self.aiml.learn(self.configs.aiml_nlg_path)
        self.aiml.respond(self.configs.aiml_nlg_pattern)

    def process(self, status, target, policy):
        response = self.aiml.respond(target)

        return response