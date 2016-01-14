from . import shapes
try:
    from . import astrafp
except ImportError:
    pass
import numpy as np

def imagelist(oplist, tsteps, shape):
    nt = len(tsteps)
    tsteps = np.array(tsteps)

    print tsteps
    par_list = []
    shape_list = []

    for op in oplist:
        if op['op']=='define':
            par = {key:op[key] for key in op if not (key=='op' or key=='id')}
            shape_list.insert(op['id'],par)

            pard = {}
            for key in par:
                if not key=='shape':
                    pard[key] = np.ones(nt)*par[key]
            par_list.insert(op['id'],pard)
        elif op['op']=='adjust':
            cl = par_list[op['id']][op['var']]
            l = np.argmax(tsteps>=op['t_start'])
            r = np.argmax(tsteps>=op['t_end'])
            print l,r
            cl[l:r] = np.interp(tsteps[l:r], [op['t_start'],op['t_end']], [cl[l-1],op['new_val']])
            cl[r-1:] = op['new_val']
    print shape_list
    imgs = np.zeros((nt,shape[0],shape[1]))
    for i in range(nt):
        for j,shp in enumerate(shape_list):
            for key in shp:
                if not key=='shape':
                    shp[key] = par_list[j][key][i]
            shapes.addshape(imgs[i],**shp)
    return imgs

def fp(oplist, tsteps, angs, shape, fpfunc=None):
    imgs = imagelist(oplist, tsteps, shape)
    if fpfunc==None:
        fpfunc = astrafp.fp
    p = np.zeros((len(angs),shape[0]))
    for i,ang in enumerate(angs):
        p[i] = fpfunc(imgs[i],ang)
    return p

