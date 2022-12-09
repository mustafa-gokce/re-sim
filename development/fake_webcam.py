import time
import pyfakewebcam
import numpy as np

"""
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback video_nr=10,11,12 card_label="FakeWebcam1","FakeWebcam2","FakeWebcam2"
sudo modprobe v4l2loopback exclusive_caps=1
sudo v4l2-ctl -d /dev/video10 -c timeout=0
sudo v4l2-ctl -d /dev/video11 -c timeout=0
sudo v4l2-ctl -d /dev/video12 -c timeout=0
ffplay /dev/video10
"""

blue = np.zeros((480, 640, 3), dtype=np.uint8)
blue[:, :, 2] = 255

red = np.zeros((480, 640, 3), dtype=np.uint8)
red[:, :, 0] = 255

camera = pyfakewebcam.FakeWebcam("/dev/video10", 640, 480)

while True:
    camera.schedule_frame(red)
    time.sleep(1 / 30.0)

    camera.schedule_frame(blue)
    time.sleep(1 / 30.0)
