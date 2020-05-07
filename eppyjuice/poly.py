# Copyright (c) 2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""draw a polygon in blender"""
import bpy
import math

def create_apoly(objname, points):
    myvertex = points
    myfaces = []

    # -------------------------------------
    # Create all Faces
    # -------------------------------------
    pointorder = tuple(list(range(len(points))))
    myface = [pointorder, ]
    myfaces.extend(myface)


    mymesh = bpy.data.meshes.new(objname)

    myobject = bpy.data.objects.new(objname, mymesh)

    bpy.context.collection.objects.link(myobject)

    # Generate mesh data
    mymesh.from_pydata(myvertex, [], myfaces)
    # Calculate the edges
    mymesh.update(calc_edges=True)

    return myobject
    
def main(fname=None):
    
    h = 10
    w = 3
    points = [(0, 0, 0), (-w / 2., 0, h / 2.),  (0, 0, h), (w, 0, h), (w, 0, 0)]
    aplane = create_apoly("Awesome_object", points)
    if fname:
        bpy.ops.wm.save_as_mainfile(filepath=fname)

if __name__ == '__main__':
    fname = '/Users/santoshphilip/Documents/coolshadow/github/eppyjuice/eppyjuice/a.blend'
    fname = None
    main(fname)