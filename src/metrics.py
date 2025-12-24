from .color_utils import chroma_from_lab_centers

def neutrality_metrics(centers_lab, weights, tau=20.0):
    chroma = chroma_from_lab_centers(centers_lab)
    mean_chroma = float((weights * chroma).sum())
    neutral_share = float(weights[chroma < tau].sum())
    return mean_chroma, neutral_share