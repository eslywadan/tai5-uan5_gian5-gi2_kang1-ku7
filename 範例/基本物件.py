from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

漢字 = '臺語工具'
音 = 'tai5-gi2 kang1-ku7'

章物件 = 拆文分析器.建立章物件(漢字)
print(章物件)
章物件 = 拆文分析器.建立章物件(音)
print(章物件)
章物件 = 拆文分析器.對齊章物件(漢字, 音)

print(章物件)
print(章物件.看型())
print(章物件.看音())
print(章物件.看分詞())


章物件 = 拆文分析器.建立章物件('臺語工ku7')
章物件 = 拆文分析器.對齊章物件('臺語工ku7', 'tai5-gi2 kang1-ku7')
print(章物件)
