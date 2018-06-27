# -*- coding:utf-8 -*-
"""
Created on 18-6-19 上午10:54

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class NegFilter(object):
    def __init__(self,words,postags,arcs):
        self.__arcs = arcs
        self.__negPos = [] #????????1??
        for i in range(len(words)):
            if words[i] in ["?","?"] and postags[i] in ["d","h"]:
                self.__negPos.append(i + 1)

    # ????????????
    def negfilter(self,wordidx):
        result = []
        for i in wordidx:
            if self.is_negtive(i,self.__negPos,self.__arcs):
                result.append(i)
        for i in self.__negPos:
            if self.__arcs[i - 1].relation in ["ADV","ATT"] and self.__arcs[self.__arcs[i - 1].head - 1].relation == "HED":
                for i in wordidx:
                    if i in result:
                        result.remove(i)
                    else:
                        result.append(i)
                break
        return result

    def is_negtive(self,idx,privative_idx,arcs):
        is_n = False
        for i in privative_idx:
            if arcs[i - 1].relation in ["ADV","ATT"] and arcs[i - 1].head == idx + 1:
                is_n = True
                break
        return is_n