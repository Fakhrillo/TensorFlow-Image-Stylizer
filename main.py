from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Load pre-trained model
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# tf.get_logger().setLevel('ERROR') # If you see the Warning messages do not worry, they do not affect the output, use this if it's necessary, it'll get rid of the warnings

def tensor_to_image(tensor):
    tensor = np.array(tensor * 255, dtype=np.uint8)
    return Image.fromarray(tensor[0])

def load_image(image_path, max_res=512):
    with Image.open(image_path) as img:
        scale = max_res / max(img.size)
        img = img.resize((int(img.width * scale), int(img.height * scale)))
        img = np.array(img) / 255.0
    return tf.convert_to_tensor(img, dtype=tf.float32)[tf.newaxis, ...]

content_image = load_image("media/target.jpg")
style_image = load_image("media/reference4.jpg")

tensor_to_image(hub_model(content_image, style_image)[0]).show()