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

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)

# websocket
@app.websocket("/direction")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # car.direction(data)
        print(data)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)