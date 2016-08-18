import rhinoscriptsyntax as rs
import scriptcontext
import math

def SurfaceMidDomain(surface_id) :
    """Returns the mid domain of a surface 
    Parameters:
      surface_id = the surface's identifier
    Returns:
      tuple of the mid domain u, v on success
    Example:
      import rsextras as rsext
      srf = rs.GetObject("Select a surface", rs.filter.surface)
      if rs.IsSurface(srf):
        print rsext.SurfaceMidDomain(srf)	
    See Also:
      
    """
    surface = rs.coercesurface(surface_id, True)
    u = rs.SurfaceDomain(surface, 0)
    u = (u[1]+u[0])/2
    v = rs.SurfaceDomain(surface, 1)
    v = (v[1]+v[0])/2
    if u is None or v is None :
        return scriptcontext.errorhandler()
    return (u,v)

def SurfaceMidPoint(surface_id) :
    """Returns the point of mid domain of a surface 
    Parameters:
      surface_id = the surface's identifier
    Returns:
      point of the mid domain of a surface on success
    Example:
      import rsextras as rsext
      srf = rs.GetObject("Select a surface", rs.filter.surface)
      if rs.IsSurface(srf):
        print rsext.SurfaceMidPoint(srf)	
    See Also:
      
    """
    surface = rs.coercesurface(surface_id, True)
    u,v = getMidDomain(surface)
    es = rs.EvaluateSurface(surface, u, v)
    if es is None :
        return scriptcontext.errorhandler()
    return es
