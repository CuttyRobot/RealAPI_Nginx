from fastapi import FastAPI

app = FastAPI()
# uvicorn main:app --host localhost --port 8000

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
