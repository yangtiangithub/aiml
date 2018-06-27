# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:35.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class FixedSizeQueue(object):

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.queue = []

    def append(self, item):
        if len(self.queue) == self.maxsize:
            self.queue.pop(0)

        self.queue.append(item)

    def __len__(self):
        return len(self.queue)

    def __getitem__(self, index):
        return self.queue[index]

    def __contains__(self, item):
        return item in self.queue

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def flush(self):
        self.queue = []


class ResponseQueue(FixedSizeQueue):

    def get_last_response_statement(self):
        previous_interaction = self.peek()
        if previous_interaction:
            return previous_interaction[1]
        return None

    def get_last_input_statement(self):
        previous_interaction = self.peek()
        if previous_interaction:
            return previous_interaction[0]
        return None