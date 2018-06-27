# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午5:35.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import aiml

class AimlNLU(object):

    def __init__(self, configs):
        self.configs = configs

        self.aiml = aiml.Kernel()
        self.aiml.learn(configs.aiml_nlu_path)
        self.aiml.respond(configs.aiml_nlu_pattern)

    def process(self, stmt):
        sentence = " ".join(stmt.get_words())
        res = self.aiml.respond(sentence)

        if self.configs.debug_mode: print("[AimlNLU]:\'%s\'" % res)

        if "Greeting" in res:               # 问候
            return "Greeting", None

        elif "SEARCHGENERAL" in res:        # 可能带有歧义的模板
            # 如：搜周杰伦的歌 -> search by singer
            # 如：搜轻松的歌 -> search by type
            entity = res.strip().split(":")[-1]
            entity_type = self.entity_recognizer(entity)
            if entity_type == "SINGER":
                return "SearchBySinger", {"singer": entity}
            elif entity_type == "TYPE":
                return "SearchByType", {"type": entity}

        elif "SEARCHBYSONG" in res:         # 按歌曲名搜索
            song = res.strip().split(":")[-1]
            return "SearchBySong", {"song": song}

        elif "SEARCHBYSINGER" in res:       # 按歌手搜索
            singer = res.strip().split(":")[-1]
            return "SearchBySinger", {"singer": singer}

        elif "SEARCHBYTYPE" in res:         # 按歌曲类型搜索
            type = res.strip().split(":")[-1]
            return "SearchByType", {"type": type}

        elif "SEARCHBYSCENE" in res:        # 按场景搜索
            scene = res.strip().split(":")[-1]
            return "SearchByScene", {"scene": scene}

        else:
            return None, None

    def entity_recognizer(self, text):

        # 通过字典匹配、知识图谱等等技术手段判断实体类型
        pass

        return "SINGER"

if __name__ == "__main__":

    from Chatbot.configs import Configs
    from Chatbot.sessions.statement import Statement
    cfg = Configs()

    cfg.aiml_nlu_path = "../aiml/nlu-startup.xml"

    nlu = AimlNLU(cfg)
    nlu.process(Statement(text="搜好听的歌"))
