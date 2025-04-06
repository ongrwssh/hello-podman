# hello-podman 🦭


## Quick Start

リポジトリからプロジェクトファイルを取得する。

```sh
git clone https://github.com/ongrwssh/hello-podman.git
```

`play kube`でコンテナイメージを作成し、コンテナをビルドし、Podを作成して実行する。

```sh
podman play kube unk.yaml
```

2025/04/06現在、Win/Macではローカルファイルを元にイメージを自動ビルドする機能が未サポートのため、`play kube`実行前に次の通り、コンテナイメージを作成しておくこと。

```sh
# サーバー用イメージを作成
cd unksvr && podman build -t unksvr:latest . && cd -
# アプリ用イメージを作成
cd unkapp && podman build -t unkapp:latest . && cd -
```
