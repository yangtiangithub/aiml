import pyltp

class Fenci(object):
    def __init__(self):
        pass

    def replace(self, input_path,output_path, replace_key, pattern):
        with open(input_path, "r") as input_file:
            with open(output_path, "w") as output_file:
                # print(input_file.read())
                for line in input_file.readlines():
                    # 去掉回车
                    line = line.strip()
                    # ltp分词
                    segmentor = pyltp.Segmentor()
                    segmentor.load_with_lexicon("../utils/ltp/models/cws.model", "lexicon")
                    words = list(segmentor.segment(line))
                    segmentor.release()
                    # 合并分词结果
                    line = " ".join(words)
                    # 替换关键词
                    line = line.replace(replace_key, "*")
                    # 生成aiml
                    line = pattern.replace("模板句子", line)
                    output_file.write(line)

    def replace_singer(self, input_path,output_path, singer,pattern):
        print("singer")
        self.replace(input_path, output_path, singer, pattern)


    def replace_song(self, input_path,output_path, song, pattern):
        print("song")
        self.replace(input_path, output_path, song , pattern)


    def replace_scene(self, input_path,output_path, scene, pattern):
        print("scene")
        self.replace(input_path, output_path, scene, pattern)


    def replace_type(self, input_path,output_path, type, pattern):
        print("type")
        self.replace(input_path, output_path, type, pattern)



if __name__ == "__main__":
    fenci = Fenci()
    fenci.replace_singer("./searchSinger.txt", "./searchSinger-output.txt", "周杰伦", '''
    <category>
        <pattern>模板句子</pattern>
        <template>
        <think>
        <set name = "singer_name"> <star/> </set>
        <set name = "signal">singer_name_get</set>
        </think>
        #SEARCHBYSINGER:<get name = "singer_name"/>
        </template>
    </category>''')

    fenci.replace_song("./searchSong.txt", "./searchSong-output.txt", "晴天",  '''
    <category>
        <pattern>模板句子</pattern>
        <template>
        <think>
        <set name = "song_name"> <star/> </set>
        <set name = "signal">song_name_get</set>
        </think>
        #SEARCHBYSONG:<get name = "song_name"/>
        </template>
    </category>''')

    fenci.replace_type("./searchType.txt", "./searchType-output.txt", "舒缓", '''
   <category>
       <pattern>模板句子</pattern>
       <template>
       <think>
       <set name = "song_type"> <star/> </set>
       <set name = "signal">song_type_get</set>
       </think>
       #SEARCHBYTYPE:<get name = "song_type" />
       </template>
   </category>''')

    fenci.replace_scene("./searchScene.txt", "./searchScene-output.txt", "睡觉", '''
    <category>
        <pattern>模板句子</pattern>
        <template>
        <think>
        <set name = "song_scene"> <star/> </set>
        <set name = "signal">song_scene_get</set>
        </think>
        #SEARCHBYSCENE:<get name = "song_scene" />
        </template>
    </category>''')


