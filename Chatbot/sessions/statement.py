# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:30.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class Statement(object):

    def __init__(self,
                 text,
                 from_user=True):

        self.text = text

        self.words = None
        self.pos = None
        self.arcs = None

        self.emotion = None

        self.from_user = from_user


    def set_words(self, words):
        self.words = words

    def get_words(self):
        return self.words

    def set_emotion(self, emotion):
        self.emotion = emotion

    def get_emotion(self):
        return self.emotion

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def set_arcs(self, arcs):
        self.arcs = arcs

    def get_arcs(self):
        return self.arcs