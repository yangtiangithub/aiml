# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午5:04.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import aiml
from Chatbot.utils.preprocessor import Preprocessor
from Chatbot.sessions.manager import Manager
from Chatbot.sessions.statement import Statement

from Chatbot.nlu.default_nlu import DefaultNLU
from Chatbot.nlu.aiml_nlu import AimlNLU
from Chatbot.dm.default_dm import DefaultDM
#from Chatbot.nlg.default_nlg import DefaultNLG
from Chatbot.nlg.aiml_nlg import AimlNLG

class Chatbot(object):

    def __init__(self, configs):

        self.name = configs.name
        self.preprocessor = Preprocessor(configs)

        self.sess_manager = Manager(configs)

        #self.nlu = DefaultNLU(configs)
        self.nlu = AimlNLU(configs)
        self.dm = DefaultDM(configs)
        #self.nlg = DefaultNLG(configs)
        self.nlg = AimlNLG(configs)


    def listen(self, sentence):

        # User和Session管理
        pass

        # PREPROCESS
        stmt = self.preprocessor.process(Statement(text=sentence, from_user=True))

        # NLU
        intent, ne = self.nlu.process(stmt)

        # DM
        status, target, policy = self.dm.process(stmt, None, intent, ne)

        # NLG
        response = self.nlg.process(status, target, policy)

        # 保存CONTEXT信息，持久化
        pass

        return response


if __name__ == "__main__":

    from Chatbot.configs import Configs

    configs = Configs()
    chatbot = Chatbot(configs)

    while True:
        speech = input(">> ")
        res = chatbot.listen(speech)
        print(res)