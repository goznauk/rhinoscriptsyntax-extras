import rhinoscriptsyntax as rs
import math


def VectorAngleCosine(v1, v2) :
	return rs.VectorDotProduct(rs.VectorUnitize(v1), rs.VectorUnitize(v2))

def VectorAngleSine(v1, v2):
	angleCos = VectorAngleCosine(v1, v2)
	return math.pow(1 - angleCos * angleCos, 1/2)
