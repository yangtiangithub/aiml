# -*- coding:utf-8 -*-
"""
Created on 18-6-14 下午4:07

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

import pyltp

class LtpUtil(object):
    def __init__(self, configs):

        self.configs = configs

        self.__segmentor = None
        self.__seg_model_path = configs.ltp_seg_model_path
        self.__seg_lexicon_path = configs.ltp_seg_lexicon_path
        self.__postagger = None
        self.__pos_model_path = configs.ltp_pos_model_path
        self.__recognizer = None
        self.__rec_model_path = configs.ltp_rec_model_path
        self.__parser = None
        self.__par_model_path = configs.ltp_par_model_path

        self._model_initialize()


    def _model_initialize(self):
        if self.__segmentor == None:
            self.__segmentor = pyltp.Segmentor()
            if self.__seg_lexicon_path == None:
                self.__segmentor.load(self.__seg_model_path)
            else:
                self.__segmentor.load_with_lexicon(self.__seg_model_path, self.__seg_lexicon_path)

        if self.__postagger == None:
            self.__postagger = pyltp.Postagger()
            if self.__seg_lexicon_path == None:
                self.__postagger.load(self.__pos_model_path)
            else:
                self.__postagger.load_with_lexicon(self.__pos_model_path, self.__seg_lexicon_path)

        if self.__recognizer == None:
            self.__recognizer = pyltp.NamedEntityRecognizer()
            self.__recognizer.load(self.__rec_model_path)

        if self.__parser == None:
            self.__parser = pyltp.Parser()
            self.__parser.load(self.__par_model_path)

    # split sentences
    def SentenceSplitter(self, sents):
        sentList = pyltp.SentenceSplitter.split(sents)
        return sentList

    # segment
    def Segmentor(self, sent):
        if self.__segmentor == None:
            print("[LtpUtil]: Uninitial segmentor!")

        words = self.__segmentor.segment(sent)
        return words

    # postagger
    def Postagger(self, words=None, sent=None):
        if self.__postagger == None:
            print("[LtpUtil]: Uninitial postagger!")

        postags = None
        if sent != None:
            words = self.Segmentor(sent)
            postags = self.__postagger.postag(words)
        else:
            postags = self.__postagger.postag(words)
        return postags

    # named entity recognizer
    def NamedEntityRecognizer(self, words=None, postags=None, sent=None):
        if self.__recognizer == None:
            print("[LtpUtil]: Uninitial recognizer!")

        if sent != None:
            words = self.Segmentor(sent)
            postags = self.Postagger(words)
        netags = self.__recognizer.recognize(words, postags)
        return netags

    # parser
    def Parser(self, words=None, postags=None, sent=None):
        if self.__parser == None:
            print("[LtpUtil]: Uninitial parser!")

        if sent != None:
            words = self.Segmentor(sent)
            postags = self.Postagger(words)
        arcs = self.__parser.parse(words, postags)
        return arcs

    def __del__(self):
        if self.__segmentor != None:
            self.__segmentor.release()

        if self.__postagger != None:
            self.__postagger.release()

        if self.__recognizer != None:
            self.__recognizer.release()

        if self.__parser != None:
            self.__parser.release()