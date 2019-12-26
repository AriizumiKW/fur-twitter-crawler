# -*- coding: UTF-8 -*-
import os
import io
import json
import shutil
import re as regex

class FollowingListModel:

    def __init__(self):
        self.following_list = {}
        self.initList()
        pass

    def initList(self):
        path = "./setting"
        if not os.path.exists(path):
            os.mkdir(path)
        if os.path.exists(path+"/record.json"):
            file_context = io.open(path+"/record.json", "r", encoding='utf-8').read()
            self.following_list = json.loads(file_context)

    def readList(self):
        path = "./readlist"
        if not os.path.exists(path):
            os.mkdir(path)
        files = os.listdir(path)
        for file in files:
            if not os.path.isdir(file):
                filename = os.path.splitext(file)[0] + os.path.splitext(file)[1]
                file_obj = open(path + "/" + filename, "r", encoding='utf-8')
                file_context = file_obj.read()  ## stage1. open files
                file_obj.close()
                regex_rule = "<a href=\"(.*?)\" data-scribe-action=\"profile_click\"><strong class=\"fullname\">" \
                             '(.*?)/strong></a>'
                results_list = regex.compile(regex_rule).findall(file_context)  ## stage2. regular
                for result in results_list:
                    screen_name = result[0]
                    key = regex.sub("\?p=s", "", screen_name)
                    key = regex.sub("\/", "", key) ## stage3. preprocessing
                    if key not in self.following_list.keys():
                        value = regex.sub('<', "", result[1])
                        self.following_list[key] = value  ## write to temp-dic
        if not os.path.exists("./finish reading"):
            os.rename("./readlist","./finish reading")
        else:
            for file in files:
                filename = os.path.splitext(file)[0] + os.path.splitext(file)[1]
                shutil.copy2(path + "/" + filename, "./finish reading")
                os.remove(path + "/" + filename) # 'readlist' move2 'finish reading'


    def writeList(self):
        path = "./setting"
        if not os.path.exists(path):
            os.mkdir(path)
        with io.open(path+"/record.json", 'w', encoding="utf-8") as file_obj:
            jd = json.dumps(self.following_list, ensure_ascii=False)
            file_obj.write(jd)
            #print(u"\u4f60\ud83d\udc0e")

    def appendfollower(self, id, name):
        self.following_list[id] = name
        self.writeList()

    def deletefollower(self, id):
        if id in self.following_list.keys():
            self.following_list.pop(id)
            self.writeList()

    def clearAll(self):
        self.following_list = {}
        self.writeList()