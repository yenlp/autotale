def clamp(v, min, max):
    if v < min:
        v = min
    if v > max:
        v = max
    return v

def lerp(a, b, t):
    return a * (1 - t) + b * t