# My_Raspberry

## chatbot

### requirments

- voicetools (see https://github.com/namco1992/voicetoolsfor  for installation and usage)
- ALSA - arecord  (see https://linux.die.net/man/1/arecord for detailed parameter)
- mpg321 

### structure

```flow 
st=>start: 开始录音
e=>end: 结束录音
op1=>operation: arecord录音
op2=>operation: 百度语音识别
op3=>operation: 图灵机器人
op4=>operation: 百度语音合成
op5=>operation: mpg321播放
op6=>operation: arecord录音
op7=>operation: 百度语音识别
cond=>condition: 识别结果不为空

st->op1-op2->->cond
op3->op4->op5->op6->op7
cond(yes)->op3
cond(no)->yes
```

