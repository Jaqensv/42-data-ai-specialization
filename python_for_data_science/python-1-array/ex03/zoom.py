import matplotlib.pyplot as plt


def zoom_image(img):
    """Slice and display the zoomed image."""

    zoom = img[100:500, 300:700]
    zoom = zoom.reshape(400, 400, 1)
    plt.imshow(zoom, cmap="gray")
    plt.show()

    print(f"New shape after slicing: {zoom.shape}")
    print(zoom)
