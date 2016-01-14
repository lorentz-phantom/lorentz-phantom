import numpy as np

def ellipse(im, x=None, y=None, a=None, b=None, phi=None, val=None, add=False):
    if None in [x, y, a, b, phi, val]:
        raise ValueError()
    ny, nx = im.shape
    my, mx = np.mgrid[-1:1:complex(0,ny),-1:1:complex(0,nx)]
    sa = np.sin(phi)
    ca = np.cos(phi)
    rx = ca*(mx-x) - sa*(my-y)
    ry = sa*(mx-x) + ca*(my-y)
    ell = (rx/a)**2 + ((ry)/b)**2 <= 1
    if add:
        im[ell] += val
    else:
        im[ell] = val


def addshape(im, shape=None, **options):
    func = globals()[shape]
    func(im, **options)

