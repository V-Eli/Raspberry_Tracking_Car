# ARG BASE_IMAGE=nvcr.io/nvidia/dli/dli-nano-ai:v2.0.2-r32.7.1
# # ARG BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.7.1-pth1.10-py3
# # Jetson flasheada con:
# # L4T 32.7.3, Jetpack: 4.6.3, CUDA: 10.2.300, OpenCV: 4.5.3
# # Torch: 1.10.0, TorchVision: 0.11.0
# FROM ${BASE_IMAGE} as build


# RUN apt-key adv --fetch-keys https://apt.kitware.com/keys/kitware-archive-latest.asc \    
#     && apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main' \ 
#     && apt-get update && apt-get install -y --no-install-recommends \    
#     git  `# For developer container`    \ 
#     python3-pip  \
#     python3-dev \
#     gcc \   
#     && apt-get clean

# FROM ${BASE_IMAGE} as build

# Build evdev to reduce base image size
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     git  `# For developer container` \
#     make `# For Makefile usage` \
#     python3-pip \
#     && apt-get clean
# Install any needed packages specified in requirements.txt
# FROM hdgigante/python-opencv

# ARG BASE_IMAGE=arm64v8/python:3.10-slim-buster

# FROM ${BASE_IMAGE} as build

# Build evdev to reduce base image size
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     git  `# For developer container` \
#     make `# For Makefile usage` \
#     python3-pip \
#     && apt-get clean

# Install OpenCV
# RUN apt-get update && apt-get install -y \
#     libsm6 \
#     libxext6 \
#     libxrender-dev \
#  && apt-get clean \
#  && rm -rf /var/lib/apt/lists/*

# RUN pip3 install --upgrade pip

# COPY backend /code/backend/
# WORKDIR /code/backend/

# RUN pip3 install -r /code/backend/requirements.txt

# EXPOSE 8000

# CMD [ "python3", "server.py"]

# Use the base image
FROM balenalib/aarch64-python:3.8-buster

# Set the working directory
COPY backend /code/backend/
WORKDIR /code/backend/

RUN apt-get update && apt-get install -y \
    libopencv-dev

# Copy the requirements file to the working directory
COPY backend/requirements.txt /code/backend/requirements.txt

# Install any additional requirements
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Command to run your application
CMD ["python3", "./server.py"]