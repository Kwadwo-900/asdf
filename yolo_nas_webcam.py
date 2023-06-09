import cv2
import torch
from super_gradients.training import models
from super_gradients.common.objects_names import Models

model = models.get(Models.YOLO_N, pretrained_weights = 'coco')

model = model.to("cuda" if torch.cuda.is_available() else "cpu")

model.predict_webcam()