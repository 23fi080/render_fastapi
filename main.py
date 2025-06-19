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
    <meta charset="UTF-8">
    <title>今日のどうぶつ</title>
    <style>
        body {
            background-color: #e0f7fa;
            font-family: "Segoe UI", sans-serif;
            text-align: center;
            padding-top: 80px;
        }
        h1 {
            color: #00796b;
        }
        #animal-name {
            font-size: 2em;
            margin-top: 20px;
        }
        #animal-desc {
            margin-top: 10px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>🌟 今日のどうぶつ 🌟</h1>
    <div id="animal-name"></div>
    <div id="animal-desc"></div>

    <script>
        const animals = [
            { name: "ネコ 🐱", desc: "気まぐれでマイペース。でもたまに甘えてくる。" },
            { name: "イヌ 🐶", desc: "忠実で元気いっぱい。走るのが大好き！" },
            { name: "カピバラ 🦫", desc: "世界一おっとりした動物。温泉が好き。" },
            { name: "フクロウ 🦉", desc: "夜のハンター。見た目はふわふわ、目がするどい。" },
            { name: "ペンギン 🐧", desc: "氷の上でもスイスイ。泳ぐのが得意な鳥。" },
            { name: "パンダ 🐼", desc: "笹を食べながらゴロゴロ。見てるだけで癒やされる。" },
        ];

        const randomAnimal = animals[Math.floor(Math.random() * animals.length)];
        document.getElementById("animal-name").innerText = randomAnimal.name;
        document.getElementById("animal-desc").innerText = randomAnimal.desc;
    </script>
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
