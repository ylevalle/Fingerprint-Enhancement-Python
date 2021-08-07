from .utils import ridge_segment, ridge_orient, ridge_freq, ridge_filter


def image_enhance(img):
    blksze = 16
    thresh = 0.1
    # normalise the image and find a ROI
    normim, mask = ridge_segment(img, blksze, thresh)

    gradientsigma = 1
    blocksigma = 7
    orientsmoothsigma = 7
    # find orientation of every pixel
    orientim = ridge_orient(normim, gradientsigma,
                            blocksigma, orientsmoothsigma)

    blksze = 38
    windsze = 5
    minWaveLength = 5
    maxWaveLength = 15
    # find the overall frequency of ridges
    freq, medfreq = ridge_freq(
        normim, mask, orientim, blksze, windsze, minWaveLength, maxWaveLength)

    freq = medfreq * mask
    kx = 0.65
    ky = 0.65
    # create gabor filter and do the actual filtering
    newim = ridge_filter(normim, orientim, freq, kx, ky)

    return(newim < -3)
