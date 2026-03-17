# 接收QQ机器人的事件推送
from fastapi import FastAPI, Request

app = FastAPI()

#  QQ平台会发送POST请求到这个接口
@app.post("/api/callback")
async def qq_callback(request: Request):
    try:
        # 获取QQ推送的事件数据
        data = await request.json()
        print("收到QQ事件：", data)
        # 必须返回正常响应，QQ平台才会验证通过
        return {"code": 0, "msg": "success"}
    except Exception as e:
        return {"code": -1, "msg": str(e)}

# 处理GET请求（Vercel默认校验用）
@app.get("/")
async def root():
    return {"message": "QQ机器人回调服务运行正常"}