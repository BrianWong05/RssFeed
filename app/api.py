from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services import services as Services

tags_metadata = [
    {
        "name": "",
        "description": ""
    }
]

app = FastAPI(openapi_tags=tags_metadata)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/rss', status_code=200)
async def rss(url: str, limit: int=999, detail: bool=False):
    res = Services.rss(url=url, limit=limit, detail=detail)
    return res
