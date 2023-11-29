from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
import cv2
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")   
async def root():
    return {"message": "Hello World"}

@app.websocket("/camera")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cam = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            # resize the frame
            frame = cv2.resize(frame, (640, 480))
            # convert the image to base 64
            base64_image = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
            await websocket.send_bytes(base64_image)
    except KeyboardInterrupt:
        cam.release()
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)