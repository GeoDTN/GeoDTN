""" ex_moebius.py - define a Moebius strip point cloud

  Define a Moebius strip pointcloud

"""
import numpy as np

def moebius_strip( nu=800, nv=100 ):
    """ Return a Moebius strip point cloud

      Return a numpy array with shape [nu*nv, 3] containing floating point coordinates
      of a Moebius strip. See also: http://en.wikipedia.org/wiki/Moebius_strip

      Optional arguments:
        nu = discretization of the u parameter (should be about 8*nv)
        nv = discretization of the v parameter

    """
    urange = [ 0.0, 2.0*np.pi ]
    vrange = [ 0.0, 2.0 ]
    ustep = (urange[1]-urange[0])/float(nu)
    vstep = (vrange[1]-vrange[0])/float(nv)
    i, u = 0, 0.0   #i inizialize two variables at the same time: it's common in python!
    points = np.empty([nu*nv, 3])
    for _ in xrange(nu):
        v = -1.0    # _ --> ignore the counter!!!
        for _ in xrange(nv):
            points[i,0] = ( 1.0+(v/2.0)*np.cos(u/2.0) ) * np.cos(u);
            points[i,1] = ( 1.0+(v/2.0)*np.cos(u/2.0) ) * np.sin(u);
            points[i,2] = (v/2.0) * np.sin(u/2.0);
            v += vstep
            i += 1
        u += ustep
    return points