import sys
import math

# one home desktop
pathnameto_blender = '/Users/santoshphilip/Documents/coolshadow/github/eppyjuice/eppyjuice'

sys.path.append(pathnameto_blender)


import eppy
import eppy3000.oldeppy
import eppy3000.experimental.listfields as listfields

import poly



fname = '/Users/santoshphilip/Documents/coolshadow/github/eppyjuice/eppyjuice/resources/V9_1/5Zone_IdealLoadsAirSystems_ReturnPlenum1.idf'
idf = eppy.openidf(fname)
epjson = '/Applications/EnergyPlus-9-1-0/Energy+.schema.epJSON'
epj = eppy3000.oldeppy.idf2epj(idf, open(epjson, 'r'))
surfs = epj.epobjects['BuildingSurface:Detailed']
surfaces_pts = [(surf.eppyname, listfields.surf2list(surf)) for surf in surfs]
# surface_pts = surfaces_pts[0]
for surface_pts in surfaces_pts:
    poly.create_apoly(surface_pts[0], surface_pts[1])