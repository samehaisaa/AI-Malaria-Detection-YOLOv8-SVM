import torch
from PIL import Image

import torchvision.transforms as transforms

def load_model(model_path):
    """
    Load a PyTorch model from a given path.
    """
    model = torch.load(model_path)
    model.eval()
    return model

def preprocess_image(image_path, input_size):
    """
    Preprocess the input image for the model.
    """
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize(input_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0)
    return image

def predict(model, image_tensor):
    """
    Make a prediction using the model and preprocessed image tensor.
    """
    with torch.no_grad():
        outputs = model(image_tensor)
    return outputs

def load_and_predict(model_path, image_path, input_size=(224, 224)):
    """
    Load the model, preprocess the image, and make a prediction.
    """
    model = load_model(model_path)
    image_tensor = preprocess_image(image_path, input_size)
    outputs = predict(model, image_tensor)
    return outputs