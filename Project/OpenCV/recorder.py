import cv2
import os

index = 1

while True:
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("camera", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        break
    elif k % 256 == 32:
        name = "image{}.png".format(index)
        image = "img/image{}.png".format(index)
        cv2.imwrite(image, frame)
        print("{} written".format(name))
        index += 1

    cam.release()

path = 'img/'
file_list = os.listdir(path)

for file in file_list:
    image = cv2.imread(path+file)
    cv2.imshow('image', image)
    os.remove(path+file)
    cv2.waitKey(0)

cv2.destroyAllWindows()
