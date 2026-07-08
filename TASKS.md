# 練習步驟

目前只有 `app.py` 和 `requirements.txt`。請依序完成：

1. 寫一個 `Dockerfile`，把這個 Flask app 包成 image。
2. `docker build` 出 image，`docker run` 起來，瀏覽器打 `http://localhost:5000` 應該看到 `Hello Docker`。
3. 在 `tests/test_app.py` 寫一個 unit test 驗證 `/` 會回傳 200 和 `Hello Docker`。
4. 寫一個 `docker-compose.yml`，加入 PostgreSQL service。
5. 把 `docker-compose.yml` 改成開發模式（volume mount），改 `app.py` 不用重新 build 就生效。
6. （進階）加上 `/todos` 的 CRUD API，接 PostgreSQL。

## 練習：接手別人開的 PR

`feature/health-check` 是同事開的 PR，加了一個 `/health` 健康檢查 endpoint，程式碼看起來沒問題、也不會 crash，但實際跑起來有 bug。請接手把它修好：

1. `git checkout feature/health-check`，看一下這個 PR 加了什麼。
2. 把 app 跑起來（`python app.py` 或用你在前面步驟做好的 Dockerfile / docker-compose），打 `http://localhost:5000/health`，觀察回傳結果是否合理。
3. 找出問題在哪裡、為什麼會這樣，修正它。
4. 在 `tests/test_app.py` 補一個測試，斷言 `/health` 在正常情況下回傳 `status: healthy`，避免以後回歸。
5. 修完後 commit，並想像你要在這個 PR 底下留言，寫一段說明：你發現了什麼問題、怎麼修的。
