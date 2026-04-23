import matplotlib.pyplot as plt
import cv2


def ft_invert(array):
    """Inverts the color of the image received."""

    filter_array = array.copy()
    y_len = len(filter_array)
    x_len = len(filter_array[0])
    for y in range(y_len):
        for x in range(x_len):
            filter_array[y, x][0] = 255 - filter_array[y, x][0]
            filter_array[y, x][1] = 255 - filter_array[y, x][1]
            filter_array[y, x][2] = 255 - filter_array[y, x][2]

    plt.imshow(filter_array)
    plt.title("Figure VIII.2: Invert")
    plt.show()

    return filter_array


def ft_red(array):
    """Applies a red filter on the image received."""

    filter_array = array.copy()
    y_len = len(filter_array)
    x_len = len(filter_array[0])
    for y in range(y_len):
        for x in range(x_len):
            filter_array[y, x][1] = 0
            filter_array[y, x][2] = 0

    plt.imshow(filter_array)
    plt.title("Figure VIII.3: Red")
    plt.show()

    return filter_array


def ft_green(array):
    """Applies a green filter on the image received."""

    filter_array = array.copy()
    y_len = len(filter_array)
    x_len = len(filter_array[0])
    for y in range(y_len):
        for x in range(x_len):
            filter_array[y, x][0] = 0
            filter_array[y, x][2] = 0

    plt.imshow(filter_array)
    plt.title("Figure VIII.4: Green")
    plt.show()

    return filter_array


def ft_blue(array):
    """Applies a blue filter on the image received."""

    filter_array = array.copy()
    y_len = len(filter_array)
    x_len = len(filter_array[0])
    for y in range(y_len):
        for x in range(x_len):
            filter_array[y, x][0] = 0
            filter_array[y, x][1] = 0

    plt.imshow(filter_array)
    plt.title("Figure VIII.5: Blue")
    plt.show()

    return filter_array


def ft_grey(array):
    """Applies a grey filter on the image received."""

    filter_array = array.copy()
    filter_array = cv2.cvtColor(filter_array, cv2.COLOR_RGB2GRAY)

    plt.imshow(filter_array, cmap="gray")
    plt.title("Figure VIII.6: Grey")
    plt.show()

    return filter_array
