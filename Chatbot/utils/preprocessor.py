# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午5:07.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
from Chatbot.utils.ltp.ltp_util import LtpUtil

class Preprocessor(object):

    def __init__(self, configs):
        self.ltp_util = LtpUtil(configs)

    def process(self, stmt):
        """
        对句子进行初始化处理，包括分词、依存句法分析、情感分析等等。
        """

        # 分词和词性标注
        seg, pos = self.cut(stmt.text)
        arcs = self.dependency_parse(seg, pos)

        stmt.set_words(list(seg))
        stmt.set_pos(list(pos))
        stmt.set_arcs(arcs)

        stmt.set_emotion(self.emotion_analysis(stmt.text))

        return stmt

    def cut(self, text, HMM=True):
        seg = self.ltp_util.Segmentor(text)
        pos = self.ltp_util.Postagger(seg)

        return seg, pos

    def dependency_parse(self, seg, pos):
        # 调用pyltp进行依存句法分析
        arcs = self.ltp_util.Parser(seg, pos)
        parse_result = []
        for item in list(arcs):
            parse_result.append((item.head, item.relation))
        return parse_result

    def emotion_analysis(self, text):
        # 返回情感分析结果
        return None

if __name__ == "__main__":
    from Chatbot.sessions.statement import Statement

    from Chatbot.configs import Configs

    cfg = Configs()

    cfg.ltp_seg_model_path = "./ltp/models/cws.models"
    cfg.ltp_seg_lexicon_path = "./ltp/user_lexicon.txt"
    cfg.ltp_pos_model_path = "./ltp/models/pos.models"
    cfg.ltp_rec_model_path = "./ltp/models/ner.models"
    cfg.ltp_par_model_path = "./ltp/models/parser.models"

    p = Preprocessor(configs=cfg)

    stmt = p.process(Statement(u"这是一个测试句子。"))