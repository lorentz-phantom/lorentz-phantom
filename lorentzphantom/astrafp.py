import astra

def fp(im, ang):
    proj_geom = astra.create_proj_geom('parallel', 1.0, im.shape[0], np.array([ang,0]))
    vol_geom = astra.create_vol_geom(im.shape)
    w = astra.OpTomo('cuda',proj_geom,vol_geom)
    fpim = w*im
    return w[0:im.shape[0]]
