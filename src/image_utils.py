import numpy as np
import cv2

def center_crop(img_bgr, crop_frac=0.60):
    h, w = img_bgr.shape[:2]
    ch, cw = int(h * crop_frac), int(w * crop_frac)
    y0 = (h - ch) // 2
    x0 = (w - cw) // 2
    return img_bgr[y0:y0+ch, x0:x0+cw]

def sample_pixels_from_mask(img_bgr, mask, n=12000, seed=0):
    rng = np.random.default_rng(seed)
    ys, xs = np.where(mask > 0)
    if len(xs) == 0:
        return None
    idx = rng.choice(len(xs), size=min(n, len(xs)), replace=False)
    return img_bgr[ys[idx], xs[idx], :]

def sample_pixels_full(img_bgr, n=12000, seed=0):
    rng = np.random.default_rng(seed)
    flat = img_bgr.reshape(-1, 3)
    idx = rng.choice(len(flat), size=min(n, len(flat)), replace=False)
    return flat[idx]