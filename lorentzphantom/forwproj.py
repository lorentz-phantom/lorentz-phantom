
try:
    import astra
except ImportError:
    pass

try:
    import tomopy
except ImportError:
    pass

import numpy as np

def tomopyfp(im, ang):
    fp = tomopy.project(np.expand_dims(im,0),ang).flatten()
    fps = len(fp)
    return fp[fps//2-im.shape[0]//2:fps//2-im.shape[0]//2+im.shape[0]]

def astrafp_cpu(im, ang):
    return astrafp(im, ang, prj='line')

def astrafp(im, ang, prj='cuda'):
    proj_geom = astra.create_proj_geom('parallel', 1.0, im.shape[0], np.array([ang,0]))
    vol_geom = astra.create_vol_geom(im.shape)
    pid = astra.create_projector(prj,proj_geom,vol_geom)
    w = astra.OpTomo(pid)
    fpim = w*im
    astra.projector.delete(pid)
    return fpim[0:im.shape[0]]
