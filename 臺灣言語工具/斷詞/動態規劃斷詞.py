"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.字詞組集句章.基本元素.詞 import 詞
from 臺灣言語工具.字詞組集句章.基本元素.組 import 組
from 臺灣言語工具.字詞組集句章.基本元素.集 import 集
from 臺灣言語工具.字詞組集句章.基本元素.句 import 句
from 臺灣言語工具.字詞組集句章.基本元素.章 import 章
from 臺灣言語工具.字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.解析整理工具.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.斷詞.改字.阿拉伯數字 import 阿拉伯數字
from 臺灣言語工具.字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器

class 動態規劃斷詞:
	篩仔 = 字物件篩仔()
	分析器 = 拆文分析器()
	數字 = 阿拉伯數字()
	def 字陣列斷詞(self, 辭典, 字陣列):
		if hasattr(辭典, '空'):
			字陣列 = self.字陣列改數字(辭典, 字陣列)
		斷詞結果 = []
		# from multiprocessing import Pool
		for 所在 in range(len(字陣列)):
			斷詞結果.append(辭典.查詞(詞(字陣列[所在:所在 + 辭典.上濟字數])))
		# 分數 頂一个位置 有啥物詞通用
		分數表 = [(0, None, None)] * (len(字陣列) + 1)
		for 所在 in range(len(字陣列)):
			if 所在 != 0 and 分數表[所在][0] == 0:
				詞物件 = 詞([字陣列[所在 - 1]])
				詞物件.屬性 = {'無佇辭典':True}
				分數表[所在] = (分數表[所在 - 1][0] + 1, 所在 - 1, {詞物件})
			for 斷詞長度 in range(len(斷詞結果[所在])):
				if 斷詞結果[所在][斷詞長度] != set():
					新分數 = 分數表[所在][0] + 1.0 / (斷詞長度 + 1)
					if 分數表[所在 + 斷詞長度 + 1][0] == 0 or 新分數 < 分數表[所在 + 斷詞長度 + 1][0]:
						分數表[所在 + 斷詞長度 + 1] = (新分數, 所在, 斷詞結果[所在][斷詞長度])
		上尾 = len(字陣列)
		if 上尾 != 0 and 分數表[上尾][0] == 0:
			詞物件 = 詞([字陣列[上尾 - 1]])
			詞物件.屬性 = {'無佇辭典':True}
			分數表[上尾] = (分數表[上尾 - 1][0] + 1, 上尾 - 1, {詞物件})
# 		print(len(字陣列), len(斷詞結果), len(分數表))
# 		print((字陣列), (斷詞結果), (分數表), sep = '\n')
		挑出來 = []
		目前所在 = len(字陣列)
		while 目前所在 != None and 目前所在 != 0:
			挑出來.append(分數表[目前所在][2])
			目前所在 = 分數表[目前所在][1]
		# 因為愛保留屬性，所以愛用附加的
		句物件 = 句()
		集陣列 = 句物件.內底集
		for 詞組合 in 挑出來[::-1]:
			集物件 = 集()
			組陣列 = 集物件.內底組
			for 詞物件 in 詞組合:
				組物件 = 組()
				組物件.內底詞 = [詞物件]
				組陣列.append(組物件)
			集陣列.append(集物件)
		return 句物件
	def 章斷詞(self, 辭典, 章物件):
		if not isinstance(章物件, 章):
			raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
		標好章 = 章()
		用好句 = 標好章.內底句
		for 一句 in 章物件.內底句:
			用好句.append(self.斷詞(辭典, 一句))
		return 標好章

	# 字詞組集句=>句
	# 章=>章
	def 斷詞(self, 辭典, 物件):
		if isinstance(物件, 章):
			return self.章斷詞(辭典, 物件)
		字陣列 = self.篩仔.篩出字物件(物件)
		return self.字陣列斷詞(辭典, 字陣列)

	def 字陣列改數字(self, 辭典, 字陣列):
		改字了字陣列 = []
		for 字物件 in 字陣列:
			if self.數字.是數量無(字物件.型):
				數量 = self.數字.轉數量(辭典.空, 字物件.型)
				組物件 = self.分析器.建立組物件(數量)
				改字了字陣列 += self.篩仔.篩出字物件(組物件)
			elif self.數字.是號碼無(字物件.型):
				號碼 = self.數字.轉號碼(辭典.空, 字物件.型)
				組物件 = self.分析器.建立組物件(號碼)
				改字了字陣列 += self.篩仔.篩出字物件(組物件)
			else:
				改字了字陣列.append(字物件)
		return 改字了字陣列
