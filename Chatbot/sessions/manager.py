# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:50.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
from Chatbot.sessions.user import User
from Chatbot.sessions.session import Session

import pymysql
import time

"""
SessionManager:
    - 处理数据库连接
    - 记录用户信息
    - 记录用户和Session之间的相关关系
    - 跟踪Session内容信息、是否过期等等
"""
class Manager(object):

    def __init__(self, configs):

        self.db_connection = pymysql.connect(configs.db_ip,
                                             configs.db_username,
                                             configs.db_password,
                                             configs.db_database,
                                             use_unicode=True,
                                             charset='utf8')
        self.cursor = self.db_connection.cursor()

        # User和Session的对应关系
        self.user_session = {}
        self.user_session_rev = {}
        # SessionID和Session的对应关系
        self.session_tracker = {}
        # User信息
        self.users = self._fetch_users_from_db()

    def new_user(self, user_ip="localhost"):
        u = User(user_ip)
        return self._insert_user_to_db(u)

    def get_user(self, user_ip, default=None):
        return self.users.get(str(user_ip), default)

    def new_session(self, user):
        session = Session(user.uid)
        self.user_session[user.uid].append(session)
        self.user_session_rev[session.id] = user.uid
        self.session_tracker[session.id] = session

        return session.id

    def _fetch_users_from_db(self):
        users = {}
        sql = "SELECT user_id, user_ip, user_name FROM users"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                user_id = row[0]
                user_ip = row[1]
                user_name = row[2]
                users[user_ip] = User(user_ip, user_id, user_name)
                self.user_session[user_id] = []
            print("[SessionManager]: Loaded %s users' information from database." % str(len(users)))
        except:
            print("[SessionManager]: Unable to load users' information from database.")

    def _insert_user_to_db(self, u):

        user_id = u.uid
        user_ip = u.uip
        user_name = u.uname

        sql = "INSERT INTO users(user_id, user_ip, user_name) VALUES(\'%s\',\'%s\',\'%s\')" % (user_id, user_ip, user_name)

        try:
            self.cursor.execute(sql)
            self.db_connection.commit()
            self.users[user_ip] = u
            return u
        except:
            print("[SessionManager]: Unable to insert user's information into database.")
            self.db_connection.rollback()
            return None

    def get_session_by_sid(self, session_id, default=None):
        return self.session_tracker.get(str(session_id), default)

    def get_session_by_uid(self, user_id, default=None):
        return self.user_session.get(str(user_id), default)

    def update_session_domain(self, session_id, domain):
        self.session_tracker[session_id].last_domain = domain

    def update_session_target(self, session_id, target):
        self.session_tracker[session_id].last_target = target

    def update_session_status(self, session_id, status):
        self.session_tracker[session_id].last_status = status

    def update_session(self, session_id, conversance, domain, target, status):
        session_id = str(session_id)
        if session_id in self.session_tracker.keys():
            self.session_tracker[session_id].conversation.append(conversance)
            self.session_details[session_id].last_conversate_time = int(time.time())

        self.update_session_domain(session_id, domain)
        self.update_session_target(session_id, target)
        self.update_session_status(session_id, status)

    def __del__(self):
        commit_list = list(self.session_tracker.keys())
        for session_id in commit_list:
            self.commit_session(self.session_tracker[session_id], commit_imediately=False)
        if len(commit_list) > 0:
            self._commit_db()
        else:
            print("[SessionManager]: Warning - No commits!")

    def _execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("[SessionManager]: Error while executing sql.")
            print(e)

    def _commit_db(self):
        try:
            self.db_connection.commit()
        except Exception as e:
            print("[SessionManager]: Error while committing db.")
            print(e)

    def commit_session(self, session, commit_imediately=True):
        session_id = session.id
        user_id = self.user_session_rev[session.id]

        sql = "INSERT INTO session_user(session_id, user_id) VALUES(\'%s\', \'%s\')" % (session_id, user_id)
        self._execute_sql(sql)

        for conversance in session.conversation:
            user_conversance = conversance[0]
            sql = "INSERT INTO session_detail(session_id, is_user, timestamp, sentence)" \
                    "VALUES(\'%s\',%s,\'%s\',\'%s\');" % (session_id, 1, user_conversance.timestamp, user_conversance.text)
            system_conversance = conversance[1]
            sql = sql + "INSERT INTO session_detail(session_id, is_user, timestamp, sentence)" \
                        "VALUES(\'%s\',%s,\'%s\',\'%s\');" % (session_id, 0, system_conversance.timestamp, system_conversance.text)

            self._execute_sql(sql)

        if commit_imediately:
            self._commit_db()


if __name__ == "__main__":
    from Chatbot.configs import Configs
    # from Chatbot.sessions.user import User
    configs = Configs()
    sm = Manager(configs)
    # nu = User(2, 'ieuy', 'Boss')
    sm.new_user()
