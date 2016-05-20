
cimport cython

from libc.math cimport sin, cos

@cython.boundscheck(False)
cdef ellipse_c(float[:,::1] im, int m, int n, float x, float y, float a, float b, float phi, float val, bint add):
    cdef int i,j
    cdef float sa = sin(phi)
    cdef float ca = cos(phi)
    cdef float rx,ry,iy,jx
    if add:
        for i in range(m):
            iy = (2.*i)/(m-1) - 1.
            for j in range(n):
                jx = (2.*j)/(n-1) - 1.
                rx = ca*(jx-x) - sa*(iy-y)
                ry = sa*(jx-x) + ca*(iy-y)
                if (rx/a)*(rx/a) + (ry/b)*(ry/b) <= 1:
                    im[i,j] += val
    else:
        for i in range(m):
            iy = (2.*i)/(m-1) - 1.
            for j in range(n):
                jx = (2.*j)/(n-1) - 1.
                rx = ca*(jx-x) - sa*(iy-y)
                ry = sa*(jx-x) + ca*(iy-y)
                if (rx/a)*(rx/a) + (ry/b)*(ry/b) <= 1:
                    im[i,j] = val

def ellipse(im, x=None, y=None, a=None, b=None, phi=None, val=None, add=False):
    if None in [x, y, a, b, phi, val]:
        raise ValueError()
    ny, nx = im.shape
    ellipse_c(im, ny, nx, x, y, a, b, phi, val, add)

cdef square_c(float[:,::1] im, int m, int n, float x, float y, float w, float h, float phi, float val, bint add):
    cdef int i,j
    cdef float l,r,t,b
    l = x-w/2.
    r = x+w/2.
    t = y-h/2.
    b = y+h/2.
    cdef float sa = sin(phi)
    cdef float ca = cos(phi)
    if add:
        for i in range(m):
            for j in range(n):
                rx = ca*(j-x) - sa*(i-y)
                ry = sa*(j-x) + ca*(i-y)
                if rx>l and rx<r and ry>t and ry<b:
                    im[i,j] += val
    else:
        for i in range(m):
            for j in range(n):
                rx = ca*(i-x) - sa*(j-y)
                ry = sa*(i-x) + ca*(j-y)
                if rx>l and rx<r and ry>t and ry<b:
                    im[i,j] = val

def square(im, x=None, y=None, w=None, h=None, phi=None, val=None, add=False):
    if None in [x, y, w, h, phi, val]:
        raise ValueError()
    ny, nx = im.shape
    square_c(im, ny, nx, x, y, w, h, phi, val, add)


