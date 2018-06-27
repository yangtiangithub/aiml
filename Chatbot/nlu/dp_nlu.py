# -*- coding:utf-8 -*-
"""
Created on 18-6-19 上午10:04

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import xml.etree.ElementTree as ET
from py2neo import Graph
from Chatbot.nlu.utils.neg_filter import NegFilter

class DpNLU(object):

    def __init__(self, configs):

        self.configs = configs

        self.root = None
        self.graph = None
        self.all_label = None

        self.__load_template()
        self.__conn_knowledge_graph()


    def __load_template(self):
        tree = ET.ElementTree(file=self.configs.dp_template_path)
        self.root = tree.getroot()

    def __conn_knowledge_graph(self):
        self.graph = Graph(self.configs.neo_db_ip,
                           user=self.configs.neo_username,
                           password=self.configs.neo_password)
        self.all_label = ["Actor", "Album", "Honour","Song"]

    def process(self, stmt):

        for i in range(len(stmt.get_words())):
            print(stmt.get_words()[i] + " " + stmt.get_pos()[i] + " " \
                  + str(stmt.get_arcs()[i][0]) + ":" + stmt.get_arcs()[i][1])

        result_idx = set()
        for template in self.root:
            tw_pos = self.getpos_tmp(stmt.get_words(),
                                     stmt.get_pos(),
                                     template.find("tempword"))
            wordidx = self.entityidx(tw_pos,
                                     stmt.get_pos(),
                                     stmt.get_arcs(),
                                     template.iterfind("entity"))
            result_idx = result_idx|wordidx
            nf = NegFilter(stmt.get_words(),
                           stmt.get_pos(),
                           stmt.get_arcs())
            negidx = nf.negfilter(wordidx)
            sim_result = []
            for i in wordidx:
                if i in negidx:
                    sim_result.append("-" + stmt.get_words()[i])
                else:
                    sim_result.append(stmt.get_words()[i])
            print(" ".join(sim_result))
        print("---------------------------")

        node_list = list()
        for i in result_idx:
            for l in self.all_label:
                nodes = self.graph.find(label=l,
                                        property_key="name",
                                        property_value=stmt.get_words()[i])
                node_list.extend(nodes)

        for node in node_list:
            print("|".join(node.labels())+":"+node["name"])

    def getpos_tmp(self, words, postags, tempword):
        tw_pos = []
        for i in range(len(words)):
            if words[i] in tempword.find("word").text.split(",") and postags[i] in tempword.find("wordclass").text.split(","):
                tw_pos.append(i+1)
        return tw_pos

    def entityidx(self, des, postags, arcs, entities):
        wordidx = set()
        for entity in entities:
            newdes = []
            for idx in range(len(postags)):
                hit = False
                if arcs[idx][1] in entity.find("relation").text.split(",") and postags[idx] in entity.find(
                        "wordclass").text.split(","):
                    i = arcs[idx][0]
                    if entity.attrib.get("direct") == "false":
                        while i not in des and i != 0:
                            i = arcs[i - 1][0]
                    if i in des:
                        hit = True
                if hit:
                    newdes.append(idx + 1)
                    if entity.attrib.get("isresult") == "true":
                        wordidx.add(idx)
            if entity.attrib.get("internode") == "true":
                des = newdes
        return wordidx


if __name__ == "__main__":
    from Chatbot.configs import Configs

    cfg = Configs()
    cfg.dp_template_path = "./templates/template.xml"

    cfg.ltp_seg_model_path = "../utils/ltp/models/cws.models"
    cfg.ltp_seg_lexicon_path = "../utils/ltp/user_lexicon.txt"
    cfg.ltp_pos_model_path = "../utils/ltp/models/pos.models"
    cfg.ltp_rec_model_path = "../utils/ltp/models/ner.models"
    cfg.ltp_par_model_path = "../utils/ltp/models/parser.models"

    dp_nlu = DpNLU(cfg)

    from Chatbot.sessions.statement import Statement
    from Chatbot.utils.preprocessor import Preprocessor
    input_str = "我想听周杰伦的稻香"
    pp = Preprocessor(cfg)
    stmt = pp.process(Statement(text=input_str))

    dp_nlu.process(stmt)
