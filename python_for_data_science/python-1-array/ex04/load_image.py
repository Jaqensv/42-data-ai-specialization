import cv2
from rotate import transpose_image


def ft_load(path: str):
    """Load and return an image in grayscale."""

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Format not supported")

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Image not found or unreadable")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img[150:550, 450:850]

    print(f"The shape of image is: {img.shape}")
    print(img)
    return img


def main():
    """Main calling ft_load and transpose_image."""

    img = ft_load("animal.jpeg")
    transpose_image(img)


if __name__ == "__main__":
    main()
