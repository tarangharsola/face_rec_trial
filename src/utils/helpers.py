def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_image(image):
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def save_processed_image(image, save_path):
    import cv2
    cv2.imwrite(save_path, image)

def draw_rectangle(image, coordinates, color=(0, 255, 0), thickness=2):
    import cv2
    x, y, w, h = coordinates
    return cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)