def rescaleFrame(Frame, scale=0.75):

    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(Frame, dimensions, interpolation=cv.INTER_AREA)
