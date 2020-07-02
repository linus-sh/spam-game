# Do you like SPAM?

## 概要

Python と pygame を利用して作成した簡単なクリックゲームです。Monty Python に敬意を払った内容にしました。</br>
画面内に表示される SPAM 缶をひたすらクリックするゲームです。</br>
Liberty Bell が流れている間、ひたすら SPAM 缶 を SPAM しましょう。</br>

## 免責事項

このリポジトリは学習目的で作成したものです。</br>
このリポジトリに含まれる一切を使用したことによに発生した不具合、損害等について製作者は一切の責任を負いません。</br>

## 遊び方

### 必要条件

このゲームは Python と Python 向けのゲームライブラリ pygame を使用しています。</br>
お使いの環境にインストールしてから起動してください。</br>
インストール方法については各公式サイトを参照してください。

- Python</br>
  https://www.python.org/

- pygame</br>
  https://www.pygame.org/news

※注意</br>
MacOS 環境では pygame 1.9.6 がうまく動作しないことがあります。</br>
その場合は最新の pygame をインストールしてください。

### 起動方法

このリポジトリをダウンロード後、ターミナルでこのリポジトリのフォルダに移動し、</br>`python spam-game.py`を実行してください

### 遊び方

起動すると”Do you like SPAM?”の文字とともに、SPAM 缶が表示されます。SPAM 缶をクリックするとゲーム開始です。</br>
ゲームを開始すると Libety Bell の曲とともに SPAM 缶が画面内にランダムに表示されます。</br>
制限時間内に画面内の SPAM 缶をひたすらクリックしてください。制限時間は 30 秒です。</br>
時間内にクリックした SPAM 缶の数がそのままスコアとなります。</br>
ゲーム終了後、SPAM 缶をクリックすると再度プレイできます。</br>

## 開発環境 / 使用技術

### 開発環境

- MacBookPro 2014 mid 15inch
- macOSX vsesion 10.14.6
- VSCode for mac 1.46.1

### 使用技術

- Python 3.8.3 64bit
- pygame 2.0.0.dev10
