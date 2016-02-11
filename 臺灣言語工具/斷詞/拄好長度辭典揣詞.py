# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拄好長度辭典揣詞:
    分析器 = 拆文分析器()
    數字 = 阿拉伯數字()

    # 字詞組集句=>句
    # 章=>章
    @classmethod
    def 揣詞(cls, 辭典, 物件):
        return cls.揣詞分析(辭典, 物件)[0]

    @classmethod
    def 揣詞分析(cls, 辭典, 物件):
        if isinstance(物件, 章):
            return cls.章揣詞(辭典, 物件)
        字陣列 = 物件.篩出字物件()
        詞組合陣列, 分數, 詞數 = cls._字陣列揣詞(辭典, 字陣列)
        return cls._詞組合陣列轉句物件(詞組合陣列), 分數, 詞數

    @classmethod
    def _字陣列揣詞(cls, 辭典, 字陣列):
        if False and hasattr(辭典, '空'):
            字陣列 = cls.字陣列改數字(辭典, 字陣列)
        揣詞結果 = []
        # from multiprocessing import Pool
        for 所在 in range(len(字陣列)):
            揣詞結果.append(辭典.查詞(詞(字陣列[所在:所在 + 辭典.上濟字數()])))
        # 分數 頂一个位置 有啥物詞通用
        分數表 = [(0, None, None)] * (len(字陣列) + 1)
        for 所在 in range(len(字陣列)):
            if 所在 != 0 and 分數表[所在][0] == 0:
                詞物件 = 詞([字陣列[所在 - 1]])
                詞物件.屬性 = {'無佇辭典': True}
                分數表[所在] = (分數表[所在 - 1][0] + 1, 所在 - 1, {詞物件})
            for 揣詞長度 in range(len(揣詞結果[所在])):
                if 揣詞結果[所在][揣詞長度] != set():
                    新分數 = 分數表[所在][0] + 1.0 / (揣詞長度 + 1)
                    if 分數表[所在 + 揣詞長度 + 1][0] == 0 or 新分數 < 分數表[所在 + 揣詞長度 + 1][0]:
                        分數表[所在 + 揣詞長度 + 1] = (新分數, 所在, 揣詞結果[所在][揣詞長度])
        上尾 = len(字陣列)
        if 上尾 != 0 and 分數表[上尾][0] == 0:
            詞物件 = 詞([字陣列[上尾 - 1]])
            詞物件.屬性 = {'無佇辭典': True}
            分數表[上尾] = (分數表[上尾 - 1][0] + 1, 上尾 - 1, {詞物件})
# 		print(len(字陣列), len(揣詞結果), len(分數表))
# 		print((字陣列), (揣詞結果), (分數表), sep = '\n')
        挑出來 = []
        目前所在 = len(字陣列)
        while 目前所在 is not None and 目前所在 != 0:
            挑出來.append(分數表[目前所在][2])
            目前所在 = 分數表[目前所在][1]
        return 挑出來[::-1], -分數表[len(字陣列)][0], len(挑出來)

    @classmethod
    def 章揣詞(cls, 辭典, 章物件):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
        標好章 = 章()
        用好句 = 標好章.內底句
        總分 = 0
        總詞數 = 0
        for 一句 in 章物件.內底句:
            斷好句物件, 分數, 詞數 = cls.揣詞分析(辭典, 一句)
            用好句.append(斷好句物件)
            總分 += 分數
            總詞數 += 詞數
        return 標好章, 總分, 總詞數

    @classmethod
    def _詞組合陣列轉句物件(cls, 詞組合陣列):
        # 因為愛保留屬性，所以愛用附加的
        句物件 = 句()
        集陣列 = 句物件.內底集
        for 詞組合 in 詞組合陣列:
            集物件 = 集()
            組陣列 = 集物件.內底組
            for 詞物件 in 詞組合:
                組物件 = 組([詞物件])
                if hasattr(詞物件, '屬性'):
                    組物件.內底詞[0].屬性 = 詞物件.屬性
                組陣列.append(組物件)
            集陣列.append(集物件)
        return 句物件

    @classmethod
    def 字陣列改數字(cls, 辭典, 字陣列):
        改字了字陣列 = []
        for 字物件 in 字陣列:
            if cls.數字.是數量無(字物件.型):
                數量 = cls.數字.轉數量(辭典.空, 字物件.型)
                組物件 = 拆文分析器.建立組物件(數量)
                改字了字陣列 += cls.篩仔.篩出字物件(組物件)
            elif cls.數字.是號碼無(字物件.型):
                號碼 = cls.數字.轉號碼(辭典.空, 字物件.型)
                組物件 = 拆文分析器.建立組物件(號碼)
                改字了字陣列 += cls.篩仔.篩出字物件(組物件)
            else:
                改字了字陣列.append(字物件)
        return 改字了字陣列
