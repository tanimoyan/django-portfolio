# Name
 
1.Djangoを用いたportfolioサイト

 
# Features

Django girlチュートリアル(https://tutorial.djangogirls.org/ja/) を参考に作ったのでこちらを参考にしていただきたい。


# Points

画像とテキストをデータベースで管理している点

 
# 実行環境

EC2

サーバー:pythonanywhere

# 注意

Sqlite3をバージョンアップさせないとEC2でDjangoを使用することができないので、Sqlite3をバージョンアップさせること。

# Requirement
 
"manage.py "を動かすのに必要なライブラリ  

Django~=2.2.4

djangogirls/requirements.txtファイルの中にDjango~=2.2.4を書き込む

# Installation
 
Requirementで列挙したライブラリなどのインストール方法
 
```bash
(myvenv) ~$ pip install -r requirements.txt
```
 
# Usage
 
"manage.py"の基本的な使い方
 
```bash
cd djangogirls
source myvenv/bin/activate
(myvenv) ~/djangogirls$ python manage.py runserver 0.0.0.0:8080
```
 
# Author
 
* tanimoto