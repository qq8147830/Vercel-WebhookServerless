from fastapi import FastAPI, Request
app = FastAPI()

@app.post("/api/callback")
async def qq_callback(request: Request):
    try:
        data = await request.json()
        return {"code": 0, "msg": "success"}
    except:
        return {"code": 0}

@app.get("/")
def home():
    return {"status": "ok"}
