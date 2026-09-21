import numpy as np

def rgb_to_grayscale(image):
    try:
        image = np.array(image)
        if image.ndim != 3 or image.shape[2] != 3:
            return -1
        if image.shape[0] == 0 or image.shape[1] == 0:
            return -1
        if np.any(image < 0) or np.any(image > 255):
            return -1
        gray = 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 2]
        return np.rint(gray).astype(int).tolist()
    except:
        return -1