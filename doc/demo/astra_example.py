import sys
sys.path.insert(0,'../')
import lorentzphantom
import numpy as np
import json
import astra

fl = open('example_phantom.json','r')
strg = fl.read()
fl.close()

oplist = json.loads(strg)

ang = np.linspace(0,np.pi,256,False)
sz = 256

fp,imgs = lorentzphantom.generate.fp(oplist,np.linspace(0,1,len(ang)),ang,(sz,sz), fpfunc=lorentzphantom.forwproj.astrafp)
fp = astra.add_noise_to_sino(fp,10**3)

proj_geom = astra.create_proj_geom('parallel',1.0,sz,ang)
vol_geom = astra.create_vol_geom(sz)
pid = astra.create_projector('cuda',proj_geom,vol_geom)

w = astra.OpTomo(pid)

rec = w.reconstruct('FBP_CUDA',fp,iterations=1)

import pylab as pl
pl.gray()
pl.imshow(fp)
pl.show()
pl.imshow(rec)
pl.show()
pl.imshow(imgs[0]+imgs[-1])
pl.show()
