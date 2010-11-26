from freenect import runloop
from zmqnect import ADDR, context
import zmq

pub_socket = context.socket(zmq.PUB)
pub_socket.bind(ADDR)

def call_back(socket, channel):
    def cb(dev, data, timestamp):
        socket.send("%s %s" % (channel, data))
    return cb

def run():
    runloop(call_back(pub_socket, "depth"), call_back(pub_socket, "rgb"))



