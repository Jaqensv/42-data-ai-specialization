import cv2
from zoom import zoom_image


def ft_load(path: str):
    """Loads and returns an image in grayscale."""

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Format not supported")

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Image not found or unreadable")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print(f"The shape of image is: {img.shape}")
    print(img)

    channels = 1 if len(img.shape) == 2 else img.shape[2]

    print(f"Number of channels: {channels}")
    return img


def main():
    """Main calling ft_load and zoom_image."""

    img = ft_load("animal.jpeg")
    zoom_image(img)


if __name__ == "__main__":
    main()
