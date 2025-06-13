from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import random  # ランダムモジュールのインポート

app = FastAPI()

# トップページ
@app.get("/")
async def root():
    return {"message": "Hello World"}

# パラメータ付きルート
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# おみくじエンドポイント
@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉", "中吉", "小吉", "吉", "半吉",
        "末吉", "末小吉", "凶", "小凶", "大凶"
    ]
    return {"result": random.choice(omikuji_list)}

# HTMLページを返すエンドポイント
@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# POSTメソッドでプレゼントを受け取る
@app.post("/present")
async def give_present(present: str = Form(...)):
    return {
        "response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"
    }
