from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'https://klipwallet.com',
    'https://stg.klipwallet.com'
    'https://dogesound.club/',
    'http://test.dogesound.club/',
    'https://v2.dogesound.club/',
    'https://egsa.io'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/json/{tokenId}.json')
async def f(tokenId):
    resData = {
        "tokenId": tokenId,
        "name": f'X PASS #{tokenId}',
        "description": "Welcome Aboard, URBAN BREAK's X PASS NFT Members!   \n\nURBAN BREAK’s first X PASS NFT membership service will present a whole new experience the members have never encountered before.",
        "image": "https://unpretty.club/image",
        "animation_url": "https://unpretty.club/video",
        "attributes": [
            {
                "trait_type": "Tier",
                "value": "2022"
            }
        ]
    }

    return JSONResponse(resData)


@app.get('/image')
async def f():
    return FileResponse('./assets/xpass.gif', response_class='xpass.gif')

@app.get('/video')
async def f():
    return FileResponse('./assets/xpass.mp4')





