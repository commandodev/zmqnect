import cv
import numpy as np
import zmq
from time import sleep
from zmqnect import ADDR, context


def get_depth_array(data):
    arr = np.fromstring(data, dtype=np.uint16)
    arr.resize((480, 640))
    return arr

def get_rgb_array(data):
    arr = np.fromstring(data, dtype=np.uint8)
    arr.resize((480, 640, 3))
    return arr


def run_rgb():
    rgb_socket = context.socket(zmq.SUB)
    rgb_socket.connect(ADDR)
    rgb_socket.setsockopt(zmq.SUBSCRIBE, 'rgb')
    sleep(0.2)
    cv.NamedWindow('RGB')
    while True:
        # Get a numpy array (knocking off the 'rgb ' at the front
        data = get_rgb_array(rgb_socket.recv()[4:])
        image = cv.fromarray(data[:, :, ::-1].copy())
        cv.ShowImage('RGB', image)
        cv.WaitKey(5)

def run_depth():
    depth_socket = context.socket(zmq.SUB)
    depth_socket.connect(ADDR)
    depth_socket.setsockopt(zmq.SUBSCRIBE, 'depth')
    sleep(0.2)
    cv.NamedWindow('Depth')
    while True:
        # Get a numpy array (knocking off the 'depth ' at the front
        data = get_depth_array(depth_socket.recv()[6:])
        data -= np.min(data.ravel())
        data *= 65536 / np.max(data.ravel())
        image = cv.fromarray(data)
        cv.ShowImage('Depth', image)
        cv.WaitKey(5)

