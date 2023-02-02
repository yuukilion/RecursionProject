# File Manipulator Program

## 使用方法
このプログラムはファイルを操作するプログラムです。以下の4つのコマンドを使用できます。
- reverse inputpath outputpath
- copy inputpath outputpath
- duplicate-contents inputpath n
- replace-string inputpath needle newstring

## 使用例

使用例を以下に記載しますのでご確認ください
### 各コマンド実行前に
```
> cat sample.txt

this is sample file
```

### reverse
```
> python3 file_manipulator.py reverse sample.txt sample-reversed.txt

> cat sample-reversed.txt

elif elpmas si siht
```

### copy
```
> python3 file_manipulator.py copy sample.txt sample-copied.txt

this is sample file
```

### duplicate-contents
```
> python3 file_manipulator.py duplicate-contents sample.txt 3 

> cat sample.txt

this is sample file this is sample file this is sample file
```

### replace-string
```
> python3 file_manipulator.py replace-string sample.txt sample test

> cat sample.txt

this is test file
```
