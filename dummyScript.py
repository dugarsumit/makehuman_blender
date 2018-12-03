from core import G
from bvh import BVH
import numpy as np
import matrix as m

human = G.app.selectedHuman
skeleton = human.skeleton
bones = skeleton.getBones()
file = open("/home/sumit/Desktop/testfile.txt","r+")
b = BVH()
b.fromSkeleton(skeleton,None,False)
anim = b.createAnimationTrack(skeleton, name="test")
newData = []
change = np.zeros((3,4))
change[0][0] = 1.0
change[1][1] = 1.0
change[2][2] = 1.0
change[2][3] = 0.0
#change[1][3] = 10
#rotmatrix = m.rotz(-30)
#change = rotmatrix[:3,:4]
rotmatrix = m.rotx(-30)
change = rotmatrix[:3,:4]

for boneNr in range(len(bones)):
    boneName = bones[boneNr].name
    animData = anim.data[boneNr]
    if boneName == "upperarm02.L":
        pass # <--- here "animData" holds info about the rotations for bone "upperarm02.L" and can be modified
        anim.data[boneNr] = change
        newData.append(change)
    else:
        newData.append(animData)
    file.write(str(animData)+"\n")

newData = np.array(newData)
human.addAnimation(anim)
human.setActiveAnimation(anim.name)
human.refreshPose()
# setRotationX(xrot)
#
# Sets the rotation around the X axis for the model, where 0.0 is frontal projection.
# Rotation is set in degrees from -180.0 to +180.0 (these two extremes are equal)

xrot = MHScript.setRotationX(0)
file.write(str(xrot)+"\n")

file.close()