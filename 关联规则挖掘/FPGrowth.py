# -*- coding:utf-8 -*-
# 实现详解 http://www.cnblogs.com/fengfenggirl/p/associate_fpgowth.html

""" 牛奶=1，面包=2，尿布=3，啤酒=4，鸡蛋=5，可乐=6"""
# 最小支持度
min_support = 3


def load_data():
    return [[1, 2], [2, 3, 4, 5], [1, 3, 4, 6, ], [2, 1, 3, 4], [2, 1, 3, 6]]


class Node:
    """
    节点
    """

    def __init__(self, name, count, parent):
        self.name = name
        self.count = count
        self.parent = parent

    def inc_count(self):
        self.count += 1


def create_ck(dataset):
    """创建第一级的频繁集 每一个项集只有一个元素"""

    result = {}

    for data in dataset:
        for item in data:
            key = frozenset([item])
            if result.has_key(key):
                result[key] += 1
            else:
                result[key] = 1

    result = sorted(result.items(), key=lambda d: d[1], reverse=True)

    return [key for key in result if key[0] >= min_support]




def create_tree(dataset, sorted_ck):
    # 根节点
    root_node = Node(name="null", count=0, parent=None)






