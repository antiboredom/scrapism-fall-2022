import cv2
import sys

paths = sys.argv[1:]

for img in paths:
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("Found {} Faces in {}.".format(len(faces), img))

    i = 0
    for (x, y, w, h) in faces:
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w]
        outname = "{}_face_{}_.jpg".format(img, str(i).zfill(4))
        cv2.imwrite(outname, roi_color)
        i += 1

    # status = cv2.imwrite('faces_detected.jpg', image)
    # print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
