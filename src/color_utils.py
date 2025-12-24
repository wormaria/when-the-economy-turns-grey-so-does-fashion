import numpy as np
import cv2
from sklearn.cluster import MiniBatchKMeans

def bgr_pixels_to_lab(pixels_bgr):
    lab = cv2.cvtColor(pixels_bgr.reshape(-1,1,3), cv2.COLOR_BGR2LAB)
    return lab.reshape(-1,3).astype(np.float32)

def kmeans_palette_lab(pixels_bgr, k=6, seed=0):
    lab = bgr_pixels_to_lab(pixels_bgr)
    km = MiniBatchKMeans(n_clusters=k, random_state=seed, batch_size=2048, n_init="auto")
    labels = km.fit_predict(lab)
    centers = km.cluster_centers_
    counts = np.bincount(labels, minlength=k).astype(np.float32)
    weights = counts / counts.sum()
    return centers, weights

def chroma_from_lab_centers(centers_lab):
    a = centers_lab[:, 1] - 128.0
    b = centers_lab[:, 2] - 128.0
    return np.sqrt(a*a + b*b)
