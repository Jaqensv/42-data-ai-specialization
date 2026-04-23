import matplotlib.pyplot as plt
import numpy as np


def transpose_image(img):
    """Transpose and display the zoomed image."""

    rows = len(img)
    cols = len(img[0])

    new_img = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_img[j][i] = img[i][j]

    new_img = np.array(new_img)

    print(f"New shape after Transpose: {new_img.shape}")
    print(new_img)

    plt.imshow(new_img, cmap="gray")
    plt.show()
