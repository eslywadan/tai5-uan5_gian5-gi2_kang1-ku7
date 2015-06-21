# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.官話.官話注音符號轉音值模組 import 官話注音符號轉音值模組
官話注音符號聲 = {
	'ㄅ', 'ㄆ', 'ㄇ', 'ㄈ', 'ㄉ', 'ㄊ', 'ㄋ', 'ㄌ',
	'ㄍ', 'ㄎ', 'ㄏ', 'ㄐ', 'ㄑ', 'ㄒ',
	'ㄓ', 'ㄔ', 'ㄕ', 'ㄖ', 'ㄗ', 'ㄘ', 'ㄙ', '',
}
官話注音符號空韻聲 = {
	'ㄓ', 'ㄔ', 'ㄕ', 'ㄖ', 'ㄗ', 'ㄘ', 'ㄙ',
}
官話注音符號韻 = {
	'', 'ㄧ', 'ㄨ', 'ㄩ',
	'ㄚ', 'ㄛ', 'ㄜ', 'ㄝ', 'ㄞ', 'ㄟ', 'ㄠ', 'ㄡ', 'ㄢ', 'ㄣ', 'ㄤ', 'ㄥ', 'ㄦ',
	'ㄧㄚ', 'ㄧㄛ', 'ㄧㄝ', 'ㄧㄞ', 'ㄧㄠ', 'ㄧㄡ', 'ㄧㄢ', 'ㄧㄣ', 'ㄧㄤ', 'ㄧㄥ',
	'ㄨㄚ', 'ㄨㄛ', 'ㄨㄞ', 'ㄨㄟ', 'ㄨㄢ', 'ㄨㄣ', 'ㄨㄤ', 'ㄨㄥ',
	'ㄩㄝ', 'ㄩㄢ', 'ㄩㄣ', 'ㄩㄥ',
		}
官話注音符號調 = {'', 'ˊ', 'ˇ', 'ˋ', '˙', }

#########################################
#  2013/11/1→12/13
#  意傳的客家話辨識用拼音→官話注音符號
#########################################
class 官話注音符號:

	#-------成員函式--------#
	def __init__(self, 音標):
		self.聲韻 = None
		if 音標[-1:] in self.調類對照表:
			self._分聲韻(音標[:-1])
			self.調 = 音標[-1:]
		elif 音標[:1] == '˙':
			self._分聲韻(音標[1:])
			self.調 = 音標[:1]
		else:  # :調是1聲
			self._分聲韻(音標)
			self.調 = ''
		if 	self.聲韻 != None:
			self.音標 = self.聲韻 + self.調
		else:
			self.音標 = None
	def _分聲韻(self, 聲韻):
		for 所在 in range(len(聲韻)):
			if 聲韻[:所在] in self.聲母對照表 and 聲韻[所在:] in self.韻母對照表:
				self.聲 = 聲韻[:所在]
				self.韻 = 聲韻[所在:]
				self.聲韻 = 聲韻
				break
		else:
			if 聲韻 in self.空韻聲:
				self.聲 = 聲韻
				self.韻 = ''
				self.聲韻 = 聲韻
	def 預設音標(self):
		return self.音標
	def 音值(self):
		return self.轉音值模組.轉(self.聲, self.韻, self.調)
	#-------成員變數--------#
	音標上長長度 = 5
	聲 = None
	韻 = None
	聲韻 = None
	調 = None
	音標 = None
	聲母對照表 = 官話注音符號聲
	韻母對照表 = 官話注音符號韻
	調類對照表 = 官話注音符號調
	空韻聲 = 官話注音符號空韻聲
	轉音值模組 = 官話注音符號轉音值模組()


