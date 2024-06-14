#!/usr/bin/env python3
import fastapi
from fastapi.middleware.cors import CORSMiddleware

import pydantic

import uvicorn

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(pydantic.BaseModel):
    content: str


# Define a path operation for a POST request
@app.post("/")
async def handle_post_item(item: Item):
    print(item.content)
    return {"message": "Success!"}


if __name__ == "__main__":
    # For reload to work, use rather:
    # python3 -m uvicorn --reload --host 127.0.0.1 --port 8080 srv:app
    uvicorn.run(app, host="127.0.0.1", port=8080)
