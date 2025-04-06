import os

import httpx


# 接続先のサーバー名（Podmanがコンテナ名を解決してくれる）
# 環境変数から取得するか、デフォルト値を使用
SVR_HOSTNAME = os.getenv("SVR_HOSTNAME", "unksvr")
SVR_PORT = 3000
URL = f"http://{SVR_HOSTNAME}:{SVR_PORT}"


def main():
    print(f"attempting to connect to: {URL}")
    response = httpx.get(URL)
    response.raise_for_status()
    print(f"status code: {response.status_code}")
    print(f"response text: {response.text}")


if __name__ == "__main__":
    main()
