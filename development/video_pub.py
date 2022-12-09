import cv2
import pubsub_utils


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)
    pub = pubsub_utils.create_publish_socket("127.0.0.1", 5555)

    frame = 0
    while True:
        success, image = cap.read()
        if success:
            data = {"frame": frame}
            pubsub_utils.publish(pub, image, data)
            frame += 1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()


if __name__ == "__main__":
    main()
