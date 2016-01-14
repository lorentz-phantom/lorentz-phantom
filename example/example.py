import lorentzphantom
import numpy as np

oplist = [
        {'op':'define','shape':'ellipse','id':0,'x':0,'y':0,'a':0.1,'b':0.2,'phi':0,'val':1},
        {'op':'define','shape':'ellipse','id':1,'x':-0.5,'y':-0.5,'a':0.4,'b':0.1,'phi':0,'val':0.5},
        {'op':'define','shape':'ellipse','id':2,'x':-0.5,'y':0.5,'a':0,'b':0,'phi':0,'val':0.75},
        {'op':'adjust','id':0,'var':'x','new_val':0.7,'t_start':0,'t_end':1},
        {'op':'adjust','id':0,'var':'y','new_val':0.7,'t_start':0,'t_end':1},
        {'op':'adjust','id':1,'var':'phi','new_val':2*np.pi,'t_start':0,'t_end':1},
        {'op':'adjust','id':2,'var':'a','new_val':0.3,'t_start':0.1,'t_end':0.25},
        {'op':'adjust','id':2,'var':'b','new_val':0.3,'t_start':0.1,'t_end':0.25},
        {'op':'adjust','id':2,'var':'a','new_val':0,'t_start':0.75,'t_end':0.9},
        {'op':'adjust','id':2,'var':'b','new_val':0,'t_start':0.75,'t_end':0.9},
        ]

imgs =  lorentzphantom.generate.imagelist(oplist, np.linspace(0,1,25),(256,256))
import pylab as pl
pl.gray()
for img in imgs:
    pl.imshow(img)
    pl.show()
