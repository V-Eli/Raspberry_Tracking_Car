from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
import cv2
# from utils.Rasberry import Car

# car = Car()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")   
# async def root():
#     return {"message": "Hello World"}

# Endpoint POST to start running the car
@app.post("/car_forward")
async def car_forward():
    # car.forward()
    return {"message": "Car is running"}

# Endpoint POST to start running the car on reverse
@app.post("/backward")
async def car_backward():
    # car.backward()
    return {"message": "Car is running on reverse"}

# Endpoint POST to stop the car
@app.post("/car_stop")
async def car_stop():
    return {"message": "Car is stopped"}

# websocket
@app.websocket("/direction")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # car.direction(data)
        print(data)

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
            frame = cv2.resize(frame, (100, 100))
            base64_image = cv2.imencode('.jpg', frame)[1].tobytes()
            await websocket.send_bytes(base64_image)
            print(base64_image)
            print("End of image")
            time.sleep(5)
    except KeyboardInterrupt:
        cam.release()
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)