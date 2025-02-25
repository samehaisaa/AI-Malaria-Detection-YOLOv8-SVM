import cv2
import numpy as np

def read_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return image

def resize_image(image, size):
    resized_image = cv2.resize(image, size)
    return resized_image

def normalize_image(image):
    normalized_image = image / 255.0
    return normalized_image

def preprocess_image(image_path, size):
    image = read_image(image_path)
    image = resize_image(image, size)
    image = normalize_image(image)
    return image

def save_image(image, save_path):
    cv2.imwrite(save_path, image)

def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def apply_threshold(image, threshold_value):
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresholded_image