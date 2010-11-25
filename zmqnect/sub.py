import cv
import numpy as np
import zmq
from time import sleep
from zmqnect import ADDR, context

#depth_socket = context.socket(zmq.SUB)
#rgb_socket = context.socket(zmq.SUB)
#depth_socket.connect(ADDR)
#rgb_socket.connect(ADDR)
#depth_socket.setsockopt(zmq.SUBSCRIBE, 'depth')
#rgb_socket.setsockopt(zmq.SUBSCRIBE, 'rgb')

def get_depth_array(data):
    arr = np.fromstring(data, dtype=np.uint16)
    arr.resize((480, 640))
    return arr

def get_rgb_array(data):
    arr = np.fromstring(data, dtype=np.uint8)
    arr.resize((480, 640, 3))
    return arr

cv.NamedWindow('RGB')


def run_rgb():
    rgb_socket = context.socket(zmq.SUB)
    rgb_socket.connect(ADDR)
    rgb_socket.setsockopt(zmq.SUBSCRIBE, 'rgb')
    sleep(0.5)
    while True:
        data = get_rgb_array(rgb_socket.recv())
        image = cv.CreateImageHeader((data.shape[1], data.shape[0]),
                                 cv.IPL_DEPTH_8U,
                                 3)
        # Note: We swap from RGB to BGR here
        cv.SetData(image, data[:, :, ::-1].tostring(),
                   data.dtype.itemsize * 3 * data.shape[1])
        cv.ShowImage('RGB', image)
        cv.WaitKey(5)

def run_depth():
    depth_socket = context.socket(zmq.SUB)
    depth_socket.connect(ADDR)
    depth_socket.setsockopt(zmq.SUBSCRIBE, 'depth')
    sleep(0.5)
    while True:
        data = get_depth_array(depth_socket.recv())
        data -= np.min(data.ravel())
        data *= 65536 / np.max(data.ravel())
        image = cv.CreateImageHeader((data.shape[1], data.shape[0]),
                                     cv.IPL_DEPTH_16U,
                                     1)
        cv.SetData(image, data.tostring(),
                   data.dtype.itemsize * data.shape[1])
        cv.ShowImage('Depth', image)
        cv.WaitKey(5)

