import sys
sys.path.insert(0,'../')
import lorentzphantom
import numpy as np
import json
import tomopy

fl = open('example_phantom.json','r')
strg = fl.read()
fl.close()

oplist = json.loads(strg)

ang = np.linspace(0,np.pi,256,False)
sz = 256

fp,imgs = lorentzphantom.generate.fp(oplist,np.linspace(0,1,len(ang)),ang,(sz,sz), fpfunc=lorentzphantom.forwproj.tomopyfp)

rec = tomopy.recon(np.expand_dims(fp,1),ang,algorithm='gridrec')

import pylab as pl
pl.gray()
pl.imshow(fp)
pl.show()
pl.imshow(rec[0])
pl.show()
pl.imshow(imgs[0]+imgs[-1])
pl.show()
