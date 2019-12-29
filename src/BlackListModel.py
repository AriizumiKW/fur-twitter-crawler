# -*- coding: UTF-8 -*-
import os
import io
import json

class BlackListModel:

    def __init__(self):
        self.black_list = {}
        self.readList()
        pass

    def readList(self):
        path = "./setting"
        if not os.path.exists(path):
            os.mkdir(path)
        if os.path.exists(path+"/blacklist.json"):
            file_context = io.open(path+"/blacklist.json", "r").read()
            try:
                self.black_list = json.loads(file_context)
            except Exception:
                print("Empty File")
                pass
        else:
            self.writeBlackList()

    def banUser(self, screen_name):
        if screen_name not in self.black_list.keys():
            self.black_list[screen_name] = "banned"
            self.writeBlackList()

    def unbanUser(self, screen_name):
        if screen_name in self.black_list.keys():
            self.black_list.pop(screen_name)
            self.writeBlackList()
            return True # if succeed
        else:
            return False

    def clearBlackList(self):
        self.black_list.clear()
        self.writeBlackList()

    def writeBlackList(self):
        path = "./setting"
        if not os.path.exists(path):
            os.mkdir(path)
        with io.open(path+"/blacklist.json", 'w', encoding="utf-8") as file_obj:
            jd = json.dumps(self.black_list, ensure_ascii=False)
            if not len(self.black_list) == 0:
                file_obj.write(jd)