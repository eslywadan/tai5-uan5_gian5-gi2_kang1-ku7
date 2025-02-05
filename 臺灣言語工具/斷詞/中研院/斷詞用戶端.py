# -*- coding: utf-8 -*-
import re


from 臺灣言語工具.斷詞.中研院.用戶端連線 import 用戶端連線
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集


class 斷詞用戶端(用戶端連線):
    分詞性 = re.compile(r'(.*)\((.*)\)')

    def __init__(self, 主機='140.109.19.104', 埠=1501, 編碼='UTF-8',
                 帳號='ihcaoe', 密碼='aip1614'):
        super(斷詞用戶端, self).__init__(主機, 埠, 編碼, 帳號, 密碼)

    def 斷詞(self, 物件, 等待=10, 一定愛成功=False):
        if isinstance(物件, 章):
            return self._斷章物件詞(物件, 等待, 一定愛成功)
        return self._斷句物件詞(物件, 等待, 一定愛成功)

    def _斷章物件詞(self, 章物件, 等待, 一定愛成功):
        結果章物件 = 章()
        for 句物件 in 章物件.內底句:
            結果章物件.內底句.append(self._斷句物件詞(句物件, 等待, 一定愛成功))
        return 結果章物件

    def _斷句物件詞(self, 句物件, 等待, 一定愛成功):
        語句 = 句物件.看型()
        結構化結果 = self.語句斷詞後結構化(語句, 等待, 一定愛成功)
        try:
            結構 = 結構化結果[0][0]
        except IndexError:
            結構 = []
        結果詞陣列 = []
        字陣列 = 句物件.篩出字物件()
        字物件指標 = 字陣列.__iter__()
        for 詞文本, 詞性 in 結構:
            字物件 = 字物件指標.__next__()
            while not 詞文本.startswith(字物件.看型()):
                結果詞物件 = 詞([字物件])
                結果詞物件.屬性 = {'詞性': ''}
                結果詞陣列.append(結果詞物件)
                字物件 = 字物件指標.__next__()
            結果字陣列 = [字物件]
            賟的文本 = 詞文本[len(字物件.看型()):]
            while len(賟的文本) > 0:
                字物件 = 字物件指標.__next__()
                賟的文本 = 賟的文本[len(字物件.看型()):]
                結果字陣列.append(字物件)
            結果詞物件 = 詞(結果字陣列)
            結果詞物件.屬性 = {'詞性': 詞性}
            結果詞陣列.append(結果詞物件)
        try:
            while True:
                字物件 = 字物件指標.__next__()
                結果詞物件 = 詞([字物件])
                結果詞物件.屬性 = {'詞性': ''}
                結果詞陣列.append(結果詞物件)
        except StopIteration:
            pass
        結果組物件 = 組()
        結果組物件.內底詞 = 結果詞陣列
        結果集物件 = 集()
        結果集物件.內底組 = [結果組物件]
        結果句物件 = 句()
        結果句物件.內底集 = [結果集物件]
        return 結果句物件

    def 語句斷詞後結構化(self, 語句, 等待=10, 一定愛成功=False):
        語句結果 = self.語句斷詞做語句(語句, 等待, 一定愛成功)
        結構化結果 = []
        for 一逝字 in 語句結果:
            一逝結構化 = []
            for 一句 in 一逝字:
                逝結果 = []
                for 詞文本 in 一句.strip().split('\u3000'):
                    if 詞文本 == '':
                        continue
                    try:
                        字, 性 = self.分詞性.split(詞文本)[1:3]
                    except ValueError:
                        字, 性 = 詞文本, None
                    逝結果.append((字, 性))
                一逝結構化.append(逝結果)
            結構化結果.append(一逝結構化)
        return 結構化結果

    def 語句斷詞做語句(self, 語句, 等待=10, 一定愛成功=False):
        return self._語句做了嘛是語句(語句, 等待, 一定愛成功)
