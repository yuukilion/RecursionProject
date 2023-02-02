import json
import os

config = json.load(open('config.json'))

f = open(config['filepath'],'r')

#名前付きパイプの続きを読む
flag = True
while flag:
    if not os.path.exists(config['filepath']):
        flag = False

    data = f.read()
    if len(data) != 0:
        print('Data received from pipe: "{}"'.format(data))

#パイプが存在しなくなった後に閉じる
f.close()
