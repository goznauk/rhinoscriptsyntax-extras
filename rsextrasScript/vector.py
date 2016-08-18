import rhinoscriptsyntax as rs
import math


def VectorAngleCosine(v1, v2) :
	return rs.VectorDotProduct(rs.VectorUnitize(v1), rs.VectorUnitize(v2))
