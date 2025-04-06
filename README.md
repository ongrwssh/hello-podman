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

Podを作成する。

```sh
podman pod create -p 8080:3000 unkpod
```

サーバーをバックグラウンドで起動する。

```sh
podman run --name unksvr --pod unkpod --network unknet -p 8080:3000 -d unksvr:latest
podman run --name unksvr --pod unkpod -d unksvr:latest
```

サーバーコンテナにリクエストを投げるアプリを実行すると、

```sh
podman run --name unkapp --pod unkpod --network unknet unkapp:latest
podman run --name unkapp --pod unkpod unkapp:latest
```

次の通りにレスポンスが表示される。

```plain
attempting to connect to: http://unksvr:3000
status code: 200
response text: 💩 Hello from Podman!
```

k8s yamlを生成する。

```sh
podman generate kube unkpod >> unkplay.yaml
```

Podを起動する。

```sh
podman play kube unkplay.yaml
```

- Win/Mac環境ではローカルファイルからイメージを自動ビルドする機能が未サポートのため、`play kube`実行前にコンテナイメージを作成しておくこと

