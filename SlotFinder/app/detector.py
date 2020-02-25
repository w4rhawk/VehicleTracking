import cv2
import numpy as np

class detection:
    def __init__(self):
        self.config="yolov3.cfg"
        self.weights="yolov3.weights"
        self.classes_="yolov3.txt"
        self.looping=True
        self.show_window=True

    def get_output_layers(self,net):
        
        layer_names = net.getLayerNames()
        
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        return output_layers


    def draw_prediction(self,img, class_id, confidence, x, y, x_plus_w, y_plus_h,classes,COLORS):

        label = str(classes[class_id])

        color = COLORS[class_id]

        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

        cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

      
     
    def detect(self):
        # reads frames from a video 
        image = cv2.imread("image.png") 
        count=0
        Width = image.shape[1]
        Height = image.shape[0]
        scale = 0.00392

        classes = None

        with open(self.classes_, 'r') as f:
            classes = [line.strip() for line in f.readlines()]

        COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

        net = cv2.dnn.readNet(self.weights, self.config)

        blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

        net.setInput(blob)

        outs = net.forward(self.get_output_layers(net))

        class_ids = []
        confidences = []
        boxes = []
        conf_threshold = 0.5
        nms_threshold = 0.4


        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])


        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

        for i in indices:
            i = i[0]
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            self.draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h),classes,COLORS)
            count=count+1

        cv2.imshow("object detection", image)

        cv2.waitKey();
        
        
        cv2.imwrite("object-detection.jpg", image)
        cv2.destroyAllWindows()
        return count
