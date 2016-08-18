import rhinoscriptsyntax as rs
import math

def SurfaceMidDomain(surface) :
    u = rs.SurfaceDomain(surface, 0)
    u = (u[1]+u[0])/2
    v = rs.SurfaceDomain(surface, 1)
    v = (v[1]+v[0])/2
    return (u,v)

def SurfaceMidPoint(surface) :
    u,v = getMidDomain(surface)
    return rs.EvaluateSurface(surface, u, v)
