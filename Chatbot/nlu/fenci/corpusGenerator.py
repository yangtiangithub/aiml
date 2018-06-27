
class CorpusGenerator(object):
    def __init__(self):
        pass

    def singer_generator(self):
        singer_sentence = []
        singer_predicate_one = ["找", "帮我找", "给我找",
                              "请找", "请给我找", "请帮我找",
                              "想找", "要找", "我要找", "我想找",
                              "你帮我去找", "你给我去找",
                              "你帮我找", "你给我找",
                              "请你帮我找", "请你给我找",
                              "请你给我去找", "请你帮我去找",
                              "能不能给我找", "能不能帮我找", "能不能给我去找", "能不能帮我去找",
                              "我要你找", "我要你去找"]
        singer_predicate_two = ["找一下", "查找", "找找", "搜", "搜一下", "搜索", "搜索一下", "搜搜", "查", "查找一下", "找一首", "查找一首", "搜一首",
                              "搜索一首", "查一首",
                              "查一下", "查查", "播", "播首", "播一首", "播一个", "播个", "播歌", "播放", "播放首", "播放一首", "点", "点点", "点首",
                              "点一首", "点一个", "点歌", "来一首", "来个", "来一个", "来首", "放", "放放",
                              "放一首", "放首"]
        singer_predicate_else = ["听歌", "听", "听首", "听一个",
                               "要听歌", "要听", "要听首", "要听一个",
                               "想听歌", "想听", "想听首", "想听一个",
                               "我要听歌", "我要听", "我要听首", "我要听一个",
                               "我想听歌", "我想听", "我想听首", "我想听一个",
                               "听听", "要听听", "想听听", "我想听听", "我要听听",
                               "有没有"]
        # singer_object = ["周杰伦的歌", "周杰伦唱的歌", "周杰伦演唱的歌",
        #                "周杰伦的歌曲", "周杰伦唱的歌曲", "周杰伦演唱的歌曲",
        #                "周杰伦的音乐", "周杰伦唱的音乐", "周杰伦演唱的音乐",
        #                "周杰伦的乐曲", "周杰伦唱的乐曲", "周杰伦演唱的乐曲"]
        singer_object = [ "周杰伦唱的歌", "周杰伦演唱的歌",
                          "周杰伦唱的歌曲", "周杰伦演唱的歌曲",
                          "周杰伦唱的音乐", "周杰伦演唱的音乐",
                          "周杰伦唱的乐曲", "周杰伦演唱的乐曲"]

        for predicate_one in singer_predicate_one:
            for object in singer_object:
                singer_sentence.append(predicate_one + object)
                for predicate_two in singer_predicate_two:
                    singer_sentence.append(predicate_one.replace("找",predicate_two) + object)
        for predicate_else in singer_predicate_else:
             for object in singer_object:
                 singer_sentence.append(predicate_else + object)
        with open("./searchSinger.txt", "w") as searchSinger_file:
            for item in singer_sentence:
                searchSinger_file.write("\n"+item)
        print("singer_sentence",len(singer_sentence))

    def song_generator(self):
        song_sentence = []
        song_predicate_one = ["找", "帮我找", "给我找",
                              "请找", "请给我找", "请帮我找",
                              "想找", "要找", "我要找", "我想找",
                              "你帮我去找", "你给我去找",
                              "你帮我找", "你给我找",
                              "请你帮我找", "请你给我找",
                              "请你给我去找", "请你帮我去找",
                              "能不能给我找", "能不能帮我找", "能不能给我去找", "能不能帮我去找",
                              "我要你找", "我要你去找"]
        song_predicate_two = ["找一下", "查找", "找找", "搜", "搜一下", "搜索", "搜索一下", "搜搜", "查", "查找一下",
                              "查一下", "查查",  "播歌","点歌", "放歌"]
        song_predicate_three = "歌名晴天"
        for predicate_one in song_predicate_one:
            song_sentence.append(predicate_one + song_predicate_three)
            for predicate_two in song_predicate_two:
                song_sentence.append(predicate_one.replace("找", predicate_two) + song_predicate_three)
        with open("./searchSong.txt", "w") as output_file:
            for item in song_sentence:
                output_file.write("\n" + item)
        print("song_sentence:",len(song_sentence))

    def type_generator(self):
        type_sentence = []
        type_predicate_one = ["找", "帮我找", "给我找",
                                "请找", "请给我找", "请帮我找",
                                "想找", "要找", "我要找", "我想找",
                                "你帮我去找", "你给我去找",
                                "你帮我找", "你给我找",
                                "请你帮我找", "请你给我找",
                                "请你给我去找", "请你帮我去找",
                                "能不能给我找", "能不能帮我找", "能不能给我去找", "能不能帮我去找",
                                "我要你找", "我要你去找"]
        type_predicate_two = ["找一下", "查找", "找找", "搜", "搜一下", "搜索", "搜索一下", "搜搜", "查", "查找一下", "找一首", "查找一首", "搜一首",
                                "搜索一首", "查一首",
                                "查一下", "查查", "播", "播首", "播一首", "播一个", "播个", "播歌", "播放", "播放首", "播放一首", "点", "点点", "点首",
                                "点一首", "点一个", "点歌", "来一首", "来个", "来一个", "来首", "放", "放放",
                                "放一首", "放首"]
        type_predicate_else = ["听", "听首", "听一个",
                                 "要听", "要听首", "要听一个",
                                 "想听", "想听首", "想听一个",
                                 "我要听", "我要听首", "我要听一个",
                                 "我想听", "我想听首", "我想听一个",
                                 "听听", "要听听", "想听听", "我想听听", "我要听听",
                                 "有没有"]
        type_add1 = ["舒缓类型","舒缓一类", "舒缓类别", "舒缓风格",
                    "舒缓这一类", "舒缓这一类型", "舒缓这一类别","舒缓这一风格","舒缓这类风格"
                    "舒缓这种类型","舒缓这种类别", "舒缓这种风格"]
        type_add2 = ["歌", "歌曲", "音乐", "乐曲", "曲子"]
        type_add  = []
        # 舒缓类型的歌曲
        for item1 in type_add1:
            for item2 in type_add2:
                type_add.append(item1 + item2)
                type_add.append(item1 + "的" + item2)
        for item in type_add:
            type_sentence.append(item)
        # 找舒缓类型的歌曲
        for item1 in type_predicate_else:
            for item2 in type_add:
                type_sentence.append(item1 + item2)
        for predicate_one in type_predicate_one:
            for add in type_add:
                type_sentence.append(predicate_one + add)
                for predicate_two in type_predicate_two:
                    type_sentence.append(predicate_one.replace("找", predicate_two) + add)
        with open("searchType.txt","w") as output_file:
            for item in type_sentence:
                output_file.write("\n" + item)
        print("type_sentence:", len(type_sentence))

    def scene_generator(self):
        scene_sentence = []
        scene_predicate_one = ["找", "帮我找", "给我找",
                              "请找", "请给我找", "请帮我找",
                              "想找", "要找", "我要找", "我想找",
                              "你帮我去找", "你给我去找",
                              "你帮我找", "你给我找",
                              "请你帮我找", "请你给我找",
                              "请你给我去找", "请你帮我去找",
                              "能不能给我找", "能不能帮我找", "能不能给我去找", "能不能帮我去找",
                              "我要你找", "我要你去找"]
        scene_predicate_two = ["找一下", "查找", "找找", "搜", "搜一下", "搜索", "搜索一下", "搜搜", "查", "查找一下", "找一首", "查找一首", "搜一首",
                              "搜索一首", "查一首",
                              "查一下", "查查", "播", "播首", "播一首", "播一个", "播个", "播歌", "播放", "播放首", "播放一首", "点", "点点", "点首",
                              "点一首", "点一个", "点歌", "来一首", "来个", "来一个", "来首", "放", "放放",
                              "放一首", "放首"]
        scene_predicate_else = ["听", "听首", "听一个",
                               "要听", "要听首", "要听一个",
                               "想听", "想听首", "想听一个",
                               "我要听", "我要听首", "我要听一个",
                               "我想听", "我想听首", "我想听一个",
                               "听听", "要听听", "想听听", "我想听听", "我要听听",
                               "有没有"]
        scene_predicate = [""]
        scene_condition1 = ["适合睡觉", "合适睡觉", "可以睡觉",
                           "适合在睡觉", "合适在睡觉", "可以在睡觉",
                           "在睡觉", "睡觉"]
        scene_condition2 = ["", "时", "时候", "的时候"]
        scene_condition = []
        # 适合睡觉时候
        for item1 in scene_condition1:
            for item2 in scene_condition2:
                scene_condition.append(item1 + item2)
        tingge = ["听的歌", "听的歌曲", "听的音乐", "听的乐曲", "听的曲子"]
        scene_tingge = []
        # 适合睡觉时候听的歌
        for item1 in scene_condition:
            for item2 in tingge:
                scene_tingge.append(item1 + item2)
        # 找
        for predicate_else in scene_predicate_else:
            scene_predicate.append(predicate_else)
        for predicate_one in scene_predicate_one:
            scene_predicate.append(predicate_one)
            for predicate_two in scene_predicate_two:
                scene_predicate.append(predicate_one.replace("找", predicate_two))
        # 找适合睡觉时候听的歌
        for item1 in scene_predicate:
            for item2 in scene_tingge :
                scene_sentence.append(item1 + item2)
        with open("./searchScene.txt","w") as output_file:
            for item in scene_sentence:
                output_file.write("\n" + item)
        print("scene_sentence:", len(scene_sentence))

if __name__ == "__main__":
    corpusGenerator = CorpusGenerator()
    corpusGenerator.singer_generator()
    corpusGenerator.song_generator()
    corpusGenerator.type_generator()
    corpusGenerator.scene_generator()


