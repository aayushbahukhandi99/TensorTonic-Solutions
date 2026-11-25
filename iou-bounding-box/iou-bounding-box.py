def iou(box_a: list, box_b: list) -> float:
    """
    Returns IoU as a float.
    """
    # Write code here
    xL = max(box_a[0], box_b[0])
    yT = max(box_a[1], box_b[1])
    xR = min(box_a[2], box_b[2])
    yB = min(box_a[3], box_b[3])

    intersection = max(0, xR - xL) * max(0, yB - yT)

    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    union = area_a + area_b - intersection

    return intersection / union if union > 0 else 0.0