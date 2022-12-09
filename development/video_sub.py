import cv2
import pubsub_utils


def main():
    sub = pubsub_utils.create_subscribe_socket("127.0.0.1", 5555)

    while True:
        data, image = pubsub_utils.subscribe(sub)
        cv2.imshow("frame", image)
        # print(data)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
