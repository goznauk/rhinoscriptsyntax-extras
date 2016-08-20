import rhinoscriptsyntax as rs
import math


def VectorAngleCosine(v1, v2) :
	return rs.VectorDotProduct(rs.VectorUnitize(v1), rs.VectorUnitize(v2))

def VectorAngleSine(v1, v2) :
	angleCos = VectorAngleCosine(v1, v2)
	return math.pow(1 - angleCos * angleCos, 1/2)

def VectorInternalDivision(vector1, vector2, ratio1, ratio2) :
    vector1 = rs.coerce3dvector(vector1)
    vector2 = rs.coerce3dvector(vector2)
    
    return rs.VectorDivide(rs.VectorAdd(rs.VectorScale(vector1, ratio2), rs.VectorScale(vector2, ratio1)), ratio1+ratio2)

def VectorAngleDivision(vector1, vector2, angle1, angle2) :
    return VectorInternalDivision(vector1, vector2, math.sin(angle1), math.sin(angle2))