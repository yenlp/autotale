def clamp(v, min, max):
    if v < min:
        v = min
    if v > max:
        v = max
    return v