# 練習步驟

目前只有 `app.py` 和 `requirements.txt`。請依序完成：

1. 寫一個 `Dockerfile`，把這個 Flask app 包成 image。
2. `docker build` 出 image，`docker run` 起來，瀏覽器打 `http://localhost:5000` 應該看到 `Hello Docker`。
3. 在 `tests/test_app.py` 寫一個 unit test 驗證 `/` 會回傳 200 和 `Hello Docker`。
4. 寫一個 `docker-compose.yml`，加入 PostgreSQL service。
5. 把 `docker-compose.yml` 改成開發模式（volume mount），改 `app.py` 不用重新 build 就生效。
6. （進階）加上 `/todos` 的 CRUD API，接 PostgreSQL。
