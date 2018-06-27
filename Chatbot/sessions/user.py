# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:28.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import uuid

class User(object):

    def __init__(self, uip, uid=None, uname="Unknown"):

        if uid is None:
            self.uid = str(uuid.uuid1())
            self.uname = "uuid_"+str(self.uid).split("-")[0]
        else:
            self.uid = uid
            self.uname = uname

        self.uip = uip

        # 用户个性化模型
        self.umodel = None