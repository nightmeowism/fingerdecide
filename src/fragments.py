import random
import cv2


def make_fragment(img, min_frac=0.5, max_frac=0.7):
    """Return a random, slightly blurred piece of a grayscale fingerprint image."""
    h, w = img.shape
    fh = int(h * random.uniform(min_frac, max_frac))
    fw = int(w * random.uniform(min_frac, max_frac))
    top = random.randint(0, h - fh)
    left = random.randint(0, w - fw)
    return cv2.GaussianBlur(img[top:top + fh, left:left + fw], (3, 3), 0)