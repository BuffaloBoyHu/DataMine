# -*- coding:utf-8 -*-

""" 从频繁项集挖掘关联规则 Apriori 的原理：如果某个项集是频繁项集，那么它所有的子集也是频繁的。"""
# 最小支持度
min_support = 0.3


def load_set():
    """数据源"""

    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def create_c1(dataset):
    """创建 c1 候选集 """
    result_set = set()

    for data in dataset:
        for item in data:
            result_set.add(frozenset([item]))

    return list(result_set)


def create_ck(Lk, k):
    """
    创建 k-候选集  注意LK 的实际长度是k-1
    :param Lk: 是（k-1)频繁集
    :param k:
    :return:
    """

    len_lk = len(Lk)
    result = []
    for i in range(len_lk):
        for j in range(i + 1, len_lk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                result.append(Lk[i] | Lk[j])

    return result


def create_ofthen_list(ck_list, data_list, min_support):
    """
    根据支持度 筛选候选集
    :param ck_list: 候选集
    :param data_list:
    :param min_support:
    :return:
    """

    tmp_dict = {}

    for c in ck_list:
        for data in data_list:
            if c.issubset(data):
                # 统计出现的次数
                if tmp_dict.has_key(c):
                    tmp_dict[c] += 1
                else:
                    tmp_dict[c] = 1

    total_num = float(len(data_list))

    result = []
    for key in tmp_dict:
        if tmp_dict[key] / total_num >= min_support:
            result.append(key)

    return result


def apriori(data_list, min_support):
    dataset = map(frozenset, data_list)
    c1 = create_c1(data_list)
    L1 = create_ofthen_list(c1, dataset, min_support)

    L = [L1]
    k = 2

    while (len(L[k - 2]) > 0):
        ck = create_ck(L[k - 2], k)
        LK = create_ofthen_list(ck, dataset, min_support)
        L.append(LK)
        k += 1

    return L


if __name__ == '__main__':
    data = load_set()
    L = apriori(data, min_support)
    print L

