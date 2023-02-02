import os
import json

#jsonファイルをロードし、オブジェクトを返す
config = json.load(open('config.json'))

#パイプが存在する場合は、それを削除して新しいスタートを切る
if os.path.exists(config['filepath']):
    os.remove(config['filepath'])

# mkfifoは与えられたfilepathを元に、モードパーミッションで名前付きパスを作成します
# modeはlinuxのファイルアクセスオプションであることに注意してください
# 各8進数は3ビットを表しrwx (読み取り、書き込み、実行) のパーミッションがあります
# 3つの8進数が必要です。ユーザー、グループ、その他にそれぞれ1つずつです
# 8進数600(0o600, bit - 110,000,000)はユーザのみが読み書き可能であることを意味します

''' 
   + ------------------ User Permissions Read
   | + ---------------- User Permissions Write
   | | + -------------- User Permissions Execute
   | | | + ------------ Group Permissions Read
   | | | | + ---------- Group Permissions Write
   | | | | | + -------- Group Permissions Execute
   | | | | | | + ------ Other Permissions Read
   | | | | | | | + ---- Other Permissions Write
   | | | | | | | | + -- Other Permissions Execute
   | | | | | | | | |
   r w x r w x r w x
   
   User Permissions: The user that own the file.
   Group Permissions: The group the file belongs to.
   Other Permissions: The other users i.e. everyone else.
'''
os.mkfifo(config['filepath'], 0o600)

print("FIFO named '%s' is created successfully." %config['filepath'])
print("Type in what you would like to send to clients.")

flag = True

while flag:
    inputstr = input()

    if(inputstr == 'exit'):
        flag = False
    else:
        with open(config['filepath'], 'w') as f:
            f.write(inputstr)

#終了時に名前付きパスを削除する
os.remove(config['filepath'])
