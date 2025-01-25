from fastapi import FastAPI

app = FastAPI()


@app.get("/calc/plus")
async def calc(first_num: int, second_num: int):
    return first_num + second_num
