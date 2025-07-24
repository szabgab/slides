import externalapi

def compute(x, y):
    xx = externalapi.remote_compute(x)
    yy = externalapi.remote_compute(y)
    result = (xx+yy) ** 0.5
    return result
