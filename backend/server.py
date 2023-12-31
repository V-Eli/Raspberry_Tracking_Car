from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/")   
async def root():
    return {"message": "Hello World"}

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
        # car.direction(int(data))

# @app.websocket("/camera")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     cam = cv2.VideoCapture(1)
#     try:
#         while True:
#             ret, frame = cam.read()
#             if not ret:
#                 break
#             # resize the frame
#             frame = cv2.resize(frame, (640, 480))
#             # convert the image to base 64
#             base64_image = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
#             await websocket.send_bytes(base64_image)
#     except KeyboardInterrupt:
#         cam.release()
#         await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)