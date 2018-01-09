# coding: utf-8 
import os
import time
import sys
from voicetools import BaiduVoice
from voicetools import TuringRobot
reload(sys)
sys.setdefaultencoding('utf8')

class Chatbot:
	# token for baidu_speech api
	Baidu_API_KEY = 'ysV1Ku0rW2HyiVwzxP9APACj'
	SECRET_KEY = '708f103737dd9878a227ba3efbec26b8'
	token = BaiduVoice.get_baidu_token(Baidu_API_KEY, SECRET_KEY)
	bv = BaiduVoice(token['access_token'])

	# for tuling robot api
	Tuling_API_KEY = 'e0b08108fcb54bafa6d26c9f2524991c'
	robot = TuringRobot(Tuling_API_KEY)

	def record(self):
		print "start recording"
		os.system('arecord -D plughw:1,0 -c 1 -d 4 temp.wav -r 8000 -f S16_LE 2>/dev/null')

	def speech_recoginize(self):
		print "start recognizing"
		text = self.bv.asr('temp.wav')
		text = text[0].encode('utf-8')
		print text
		return text

	def speech_compose(self,text):
		print "start composing"
		data = self.bv.tts(text)
		f = open('result.mp3','w')
		f.write(data)
		f.close()

	def tuling(self,text):
		answer = self.robot.ask_turing(text)
		answer = answer.decode('utf-8')
		print answer
		return answer
		
if __name__ == "__main__":
	bot = Chatbot()
	text = "开始聊天吧"
	bot.speech_compose(text)
	os.system('mpg321 result.mp3')

	bot.record()
	text = bot.speech_recoginize()
	while text != 'Null' :
		text = bot.tuling(text)
		bot.speech_compose(text)
		os.system('mpg321 result.mp3')
		# time.sleep(1)
		bot.record()
		text = bot.speech_recoginize()

	text = "主人再见啦"
	bot.speech_compose(text)
	os.system('mpg321 result.mp3')