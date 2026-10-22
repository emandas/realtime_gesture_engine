from fastapi  import WebSocket,WebSocketDisconnect,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from vision import base64_2image_decoder


app = FastAPI(middleware= [Middleware(
        CORSMiddleware, # type : ignore
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )])


@app.websocket('/ws/stream')
async def real_time_vision(*,websocket:WebSocket):
    await websocket.accept()
    try:
        i = 0
        while True:
            data = await websocket.receive_text()
            img = base64_2image_decoder(base64str=data)
            print(f"{i} Received data : {data[:30]}")
            print(f"{i} generated image : {img.shape}")

            i += 1
            await websocket.send_text(data[:30])

    except WebSocketDisconnect:
        print("User Diconnected")
