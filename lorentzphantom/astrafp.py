import astra
import numpy as np
def fp(im, ang):
    proj_geom = astra.create_proj_geom('parallel', 1.0, im.shape[0], np.array([ang,0]))
    vol_geom = astra.create_vol_geom(im.shape)
    pid = astra.create_projector('cuda',proj_geom,vol_geom)
    w = astra.OpTomo(pid)
    fpim = w*im
    astra.projector.delete(pid)
    return fpim[0:im.shape[0]]
