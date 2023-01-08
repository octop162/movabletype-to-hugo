# movabletype-to-hugo
MovableTypeをhugoの形式に修正する。

## 必要な項目

```
pip install -r requirements.txt
```

## 修正が必要な箇所

`main.py` の変数 `FILENAME` を修正する。

## 既知の問題

タイトルに記号が入っているとhugoのビルドに失敗する。

## やりたいこと

* main.pyを直接実行しているのでfireを導入してCLIを拡充する
* setup.pyを導入してインストール可能にする
