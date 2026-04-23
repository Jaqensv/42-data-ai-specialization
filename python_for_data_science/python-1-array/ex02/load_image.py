import cv2
from numpy import ndarray as array


def ft_load(path: str) -> array:

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Format not supported")

    img = cv2.imread(path, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Image not found or unreadable")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(f"The shape of image is: {img.shape}")

    return img
