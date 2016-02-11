# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔


class 轉物件音家私單元試驗(unittest.TestCase):

    @patch('臺灣言語工具.基本物件.句.句.轉音')
    def test_轉音(self, 轉音mock):
        物件 = 拆文分析器.分詞句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')
        轉物件音家私.轉音(臺灣閩南語羅馬字拼音, 物件)
        轉音mock.assert_called_once_with(音標工具=臺灣閩南語羅馬字拼音, 函式='預設音標')

    @patch('臺灣言語工具.基本物件.句.句.轉音')
    def test_轉音有參數(self, 轉音mock):
        物件 = 拆文分析器.分詞句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')
        轉物件音家私.轉音(臺灣閩南語羅馬字拼音, 物件)
        轉音mock.assert_called_once_with(音標工具=臺灣閩南語羅馬字拼音, 函式='預設音標')

    def 處理語句(self, 音標工具, 語句):
        減號了 = 文章粗胚.建立物件語句前處理減號(音標工具, 語句)
        章物件 = 拆文分析器.建立章物件(減號了)
        return 轉物件音家私.轉音(音標工具, 章物件)

    def test_閏號音(self):
        原音拼音 = 臺灣閩南語羅馬字拼音
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音語句 = 'tshiǔnn tshiūnn'
        標準結果 = 'tshiunn6 tshiunn7'
        原音章物件 = self.處理語句(原音拼音, 原音語句)
        後來章物件 = self.處理語句(結果拼音, 標準結果)
        self.assertEqual(原音章物件, 後來章物件)

    def test_對齊完整漢羅(self):
        原音拼音 = 通用拼音音標
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音型 = '恁老母di3佗位'
        原音音 = 'lin1 lau3 vu4 di3 der1 ui2'
        標準型 = '恁老母ti3佗位'
        標準音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        原音減號了 = 文章粗胚.建立物件語句前處理減號(原音拼音, 原音音)
        原音章物件 = 拆文分析器.對齊章物件(原音型, 原音減號了)
        後來原音章物件 = 轉物件音家私.轉音(原音拼音, 原音章物件)
        標準減號了 = 文章粗胚.建立物件語句前處理減號(結果拼音, 標準音)
        標準章物件 = 拆文分析器.對齊章物件(標準型, 標準減號了)
        後來標準章物件 = 轉物件音家私.轉音(結果拼音, 標準章物件)
        self.assertEqual(後來原音章物件, 後來標準章物件)

    def test_對齊完整漢羅標點符號(self):
        原音拼音 = 通用拼音音標
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音型 = '恁老母,di3佗位?'
        原音音 = 'lin1 lau3 vu4, di3 der1 ui2?'
        標準型 = '恁老母,ti3佗位?'
        標準音 = 'lin1 lau3 bu2, ti3 to1 ui7?'
        原音減號了 = 文章粗胚.建立物件語句前處理減號(原音拼音, 原音音)
        原音章物件 = 拆文分析器.對齊章物件(原音型, 原音減號了)
        後來原音章物件 = 轉物件音家私.轉音(原音拼音, 原音章物件)
        標準減號了 = 文章粗胚.建立物件語句前處理減號(結果拼音, 標準音)
        標準章物件 = 拆文分析器.對齊章物件(標準型, 標準減號了)
        後來標準章物件 = 轉物件音家私.轉音(結果拼音, 標準章物件)
        self.assertEqual(後來原音章物件, 後來標準章物件)

    def test_對齊無聲調漢羅(self):
        原音拼音 = 通用拼音音標
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音型 = '恁老母di佗位'
        原音音 = 'lin1 lau3 vu4 di3 der1 ui2'
        標準型 = '恁老母ti佗位'
        標準音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        原音減號了 = 文章粗胚.建立物件語句前處理減號(原音拼音, 原音音)
        原音章物件 = 拆文分析器.對齊章物件(原音型, 原音減號了)
        後來原音章物件 = 轉物件音家私.轉音(原音拼音, 原音章物件)
        標準減號了 = 文章粗胚.建立物件語句前處理減號(結果拼音, 標準音)
        標準章物件 = 拆文分析器.對齊章物件(標準型, 標準減號了)
        後來標準章物件 = 轉物件音家私.轉音(結果拼音, 標準章物件)
        self.assertEqual(後來原音章物件, 後來標準章物件)

    def test_對齊無聲調連字號漢羅(self):
        原音拼音 = 通用拼音音標
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音型 = '恁老母di der-ui'
        原音音 = 'lin1 lau3 vu4 di3 der1 ui2'
        標準型 = '恁老母ti to-ui'
        標準音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        原音減號了 = 文章粗胚.建立物件語句前處理減號(原音拼音, 原音音)
        原音章物件 = 拆文分析器.對齊章物件(原音型, 原音減號了)
        後來原音章物件 = 轉物件音家私.轉音(原音拼音, 原音章物件)
        標準減號了 = 文章粗胚.建立物件語句前處理減號(結果拼音, 標準音)
        標準章物件 = 拆文分析器.對齊章物件(標準型, 標準減號了)
        後來標準章物件 = 轉物件音家私.轉音(結果拼音, 標準章物件)
        self.assertEqual(後來原音章物件, 後來標準章物件)

    def test_較長通用音(self):
        原音拼音 = 通用拼音音標
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音語句 = 'di2-mng2-kau4-ga1-ge4-bia2-dan2-tai4-tai4-leh6-kai2-gang4'
        標準結果 = 'ti7-mng7-khau2-ka1-ke2-pia7-tan7-thai2-thai2-leh8-khai7-kang2'
        原音章物件 = self.處理語句(原音拼音, 原音語句)
        後來章物件 = self.處理語句(結果拼音, 標準結果)
        self.assertEqual(原音章物件, 後來章物件)

    def test_無字(self):
        原音拼音 = 臺灣閩南語羅馬字拼音
        結果拼音 = 臺灣閩南語羅馬字拼音
        原音語句 = ''
        標準結果 = ''
        原音章物件 = self.處理語句(原音拼音, 原音語句)
        後來章物件 = self.處理語句(結果拼音, 標準結果)
        self.assertEqual(原音章物件, 後來章物件)

    def test_無用預設轉換函式(self):
        原音型 = '佗位'
        原音音 = 'to1 ui7'
        原音章物件 = 拆文分析器.對齊章物件(原音型, 原音音)
        後來原音章物件 = 轉物件音家私.轉音(臺灣閩南語羅馬字拼音, 原音章物件, 函式='音值')
        篩仔 = 字物件篩仔()
        字陣列 = 篩仔.篩出字物件(後來原音章物件)
        self.assertEqual(len(字陣列), 2)
        self.assertEqual(字陣列[0].型, '佗')
        self.assertEqual(字陣列[0].音, ('t', 'ə', '1',))
        self.assertEqual(字陣列[1].型, '位')
        self.assertEqual(字陣列[1].音, ('ʔ', 'ui', '7',))
