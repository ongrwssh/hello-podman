// server.mjs
import { createServer } from 'node:http';

const hostname = '0.0.0.0'; // コンテナ外からのアクセスを受け付けるために 0.0.0.0 を指定
const port = 3000;

const server = createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('💩 Hello from Podman!\n');
});

// starts a simple http server
server.listen(port, hostname, () => {
  console.log(`Listening on ${hostname}:${port}`);
});

// run with `node main.mjs`
