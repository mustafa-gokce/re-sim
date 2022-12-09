import simplejpeg
import zmq
import cv2
import numpy


def publish(socket, image, data, flags=0):
    image = simplejpeg.encode_jpeg(image)
    socket.send_json(data, flags | zmq.SNDMORE)
    return socket.send(image, flags)


def subscribe(socket, flags=0, copy=True, track=False):
    data = socket.recv_json(flags=flags)
    image = socket.recv(flags=flags, copy=copy, track=track)
    image = simplejpeg.decode_jpeg(image)
    return data, image


def create_publish_socket(ip, port):
    pub_context = zmq.Context()
    pub_socket = pub_context.socket(zmq.PUB)
    pub_socket.bind("tcp://" + str(ip) + ":" + str(port))
    return pub_socket


def create_subscribe_socket(ip, port):
    sub_context = zmq.Context()
    sub_socket = sub_context.socket(zmq.SUB)
    sub_socket.setsockopt(zmq.SUBSCRIBE, b"")
    sub_socket.connect("tcp://" + str(ip) + ":" + str(port))
    return sub_socket
