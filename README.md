# プロジェクト名：agile-project-ja
このアプリケーションは、a, b 二つの数字を使って自動計算をするためのツールです。

# セットアップと実行の手順

### 1. Pythonのインストール：
公式のウェブサイトhttps://www.python.org/downloads/ から最新バージョンの Python をダウンロードしてインストールしてください。

### 2. IDEのインストール：
例として、Visual Studio Code（VS Code）公式のウェブサイトからhttps://code.visualstudio.com/から
お使いのオペレーティングシステムに合ったバージョンをダウンロードしてインストールしてください。

### 3. Githubからクローンして実行
git clone https://github.com/sadanobu-mizusako/agile-project-ja.git <クローン先のディレクトリ>
python main.py

# 使い方と機能詳細
起動時にメニュー画面が表示されるので、計算したいメニューを下記1－6から選びの数字を入力してください。
a, bにそれぞれ数字を入力すると、計算結果が表示されます。それぞれの入力値の制限があります。

### 選択可能なメニュー　※()内は入力値の制限
Input calculation type.   
1: addition, a + b　　　 足し算（a , bともfloat）    
2: subtraction, a - b 　　引き算（a , bともfloat）    
3: multiplication, a * b　掛け算（aはfloat , bは非ゼロのfloat）  
4: division, a / b　　　   割り算（a , bともfloat）  
5: exponent, a ^ b　　　指数（aは非負のfloat、bはfloat）  
6: square root, √a　　　平方根（aは非負のfloat）  

