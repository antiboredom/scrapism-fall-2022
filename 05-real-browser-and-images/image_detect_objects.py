import cv2
import numpy as np
import sys
import time
import os

# Load yolo
def load_yolo():
    print(os.path.abspath("yolov3.cfg"))
    net = cv2.dnn.readNet(
        os.path.abspath("yolov3.weights"), os.path.abspath("yolov3.cfg"), "darknet"
    )
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layers_names = net.getLayerNames()
    output_layers = [layers_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    return net, classes, colors, output_layers


def load_image(img_path):
    # image loading
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    return img, height, width, channels


def detect_objects(img, net, outputLayers):
    blob = cv2.dnn.blobFromImage(
        img,
        scalefactor=0.00392,
        size=(320, 320),
        mean=(0, 0, 0),
        swapRB=True,
        crop=False,
    )
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs


def get_box_dimensions(outputs, height, width):
    boxes = []
    confs = []
    class_ids = []
    for output in outputs:
        for detect in output:
            scores = detect[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > 0.3:
                center_x = int(detect[0] * width)
                center_y = int(detect[1] * height)
                w = int(detect[2] * width)
                h = int(detect[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)
    return boxes, confs, class_ids


def draw_labels(boxes, confs, colors, class_ids, classes, img):
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
    cv2.imshow("Image", img)


def extract_objects(boxes, confs, colors, class_ids, classes, img):
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            roi_color = img[y : y + h, x : x + w]
            outname = "{}_{}_{}_.jpg".format(img, str(i).zfill(4))
            cv2.imwrite(outname, roi_color)
            # cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # cv2.putText(img, label, (x, y - 5), font, 1, color, 1)


def image_detect(img_paths, target=None):
    model, classes, colors, output_layers = load_yolo()
    for img_path in img_paths:
        image, height, width, channels = load_image(img_path)
        blob, outputs = detect_objects(image, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)

        indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
        for i in range(len(boxes)):
            if i in indexes:
                try:
                    label = str(classes[class_ids[i]])
                    if target is not None and target != label:
                        continue
                    x, y, w, h = boxes[i]
                    x = max(0, x)
                    y = max(0, y)
                    print(label, x, y, w, h)
                    roi_color = image[y : y + h, x : x + w]
                    outname = "{}_{}_{}_.jpg".format(img_path, label, str(i).zfill(4))
                    cv2.imwrite(outname, roi_color)
                except Exception as e:
                    continue


if __name__ == "__main__":
    # change TARGET to be one of the object classes found in coco.names to taget just that object type
    # for example:
    # TARGET = "person"
    # or, to grab everything set it to be None like so:
    # TARGET = None
    TARGET = None
    image_detect(sys.argv[1:], TARGET)
