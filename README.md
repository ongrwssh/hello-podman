# hello-podman 🦭


## セットアップ

リポジトリからプロジェクトファイルを取得する。

```sh
git clone https://github.com/ongrwssh/hello-podman.git
```

アプリのパッケージを同期する。

```sh
cd unkapp/
uv sync
```


## ビルド

サーバー:

```sh
cd unksvr && podman build -t unksvr:latest . && cd -
```

アプリ:

```sh
cd unkapp && podman build -t unkapp:latest . && cd -
```

## ネットワークの作成

```sh
podman network create unknet
```

## 起動

サーバーをバックグラウンドで起動する。

```sh
podman run --rm --name unksvr --network unknet -p 8080:3000 -d unksvr:latest
```

サーバーコンテナにリクエストを投げるアプリを実行すると、

```sh
podman run --rm --name unkapp --network unknet unkapp:latest
```

次の通りにレスポンスが表示される。

```plain
attempting to connect to: http://unksvr:3000
status code: 200
response text: 💩 Hello from Podman!
```
