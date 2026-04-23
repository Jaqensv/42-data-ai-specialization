import cv2
import matplotlib.pyplot as plt


def ft_load(path: str):
    """Load and return a color filtered image."""

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Format not supported")

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Image not found or unreadable")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.title("Figure VIII.1: Original")
    plt.show()

    print(f"The shape of image is: {img.shape}")
    print(img)
    return img
