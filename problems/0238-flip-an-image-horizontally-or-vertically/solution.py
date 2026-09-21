import numpy as np

def flip_image(image, direction):
    try:
        image = np.array(image)
        if image.ndim not in [2, 3]:
            return -1
        if image.shape[0] == 0 or image.shape[1] == 0:
            return -1
        if direction == "horizontal":
            result = image[:, ::-1]
        elif direction == "vertical":
            result = image[::-1, :]
        else:
            return -1
        return result.tolist()
    except:
        return -1