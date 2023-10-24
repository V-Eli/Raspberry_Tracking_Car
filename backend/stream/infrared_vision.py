import cv2
import pyrealsense2 as rs
import numpy as np


hilo_corriendo = True

points = rs.points()

# Create a pipeline
pipeline = rs.pipeline()
# Create a config and configure the pipeline to stream
config = rs.config()
config.enable_stream(rs.stream.infrared, 1, 640, 480, rs.format.y8, 30)
# Start streaming
profile = pipeline.start(config)

def run():
    global hilo_corriendo
    #cap = cv2.VideoCapture(0)
    while hilo_corriendo:
        # Get frameset of color and depth
        frames = pipeline.wait_for_frames()
        ir1_frame = frames.get_infrared_frame(1)  # Left IR Camera, it allows 1, 2 or no input
        image = np.asanyarray(ir1_frame.get_data())
        im_np = image.copy()
        flip = cv2.flip(im_np, 1)
        cv2.imshow('Face Detection', flip)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            hilo_corriendo = False

def stop():
    global hilo_corriendo
    hilo_corriendo = False

if __name__ == "__main__":
    try:
        run()
        cv2.destroyAllWindows()  # Close OpenCV windows when done
    except KeyboardInterrupt:
        stop()
        cv2.destroyAllWindows()