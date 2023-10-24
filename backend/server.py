from fastapi import FastAPI
import uvicorn
# from utils.Rasberry import Car

# car = Car()

app = FastAPI()

@app.get("/")   
def root():
    return {"message": "Hello World"}

# Endpoint POST to start running the car
@app.post("/car_up")
def car_forward():
    # car.forward()
    return {"message": "Car is running"}

# Endpoint POST to start running the car on reverse
@app.post("/car_down")
def car_backward():
    # car.backward()
    return {"message": "Car is running on reverse"}

# Endpoint POST to stop the car
@app.post("/car_stop")
def car_stop():
    return {"message": "Car is stopped"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)


