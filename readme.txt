This project helps you create random human poses and generate their rgbd data.

1) generatePoses.py : Run this script in makehuman. It will generate different variations from basic poses.

2) generateViews.py : Run this script in blender. It will render rgbd images of poses from different camera views. It will also generate rgb images with body parts segmented and labeled in the form of different colors. Open Blender from commandline in order to see print statements and errors from this script.

3) basicPose.mhm : Put this file in input_poses directory under base directory poseSamples. It is the basic pose
from which variations will be generated. Make sure this human model has default skeleton. Any other skeleton type will break the createPose script.

4) camera_positions.txt : Put this file in input_files folder under base directory poseSamples. It contains parameters for controlling various camera orientations.

5) pose_parameters.txt : Put this file in input_files folder under base directory poseSamples. It contains various human parameters that can be modelled.

6) camera_properties.txt : This file lets you set different camera parameters like focal lenght, sensor size etc. Put this file in the input_files folder.

7) vertex_groups.txt : This file defines a mapping between vertiex groups and their correspoding color depiction. Put this file in the input_files folder. Following rgb values are currently used :
   Torso            : 0,255,0
   Head             : 0,0,255
   Upper left arm   : 255,0,0
   Upper right arm  : 100,0,0
   Lower left arm   : 255,0,255
   Lower right arm  : 100,0,100
   Upper left leg   : 255,255,0
   Upper right leg  : 100,100,0
   Lower left leg   : 0,255,255
   Lower right leg  : 0,100,100
   
8) output file format : 
    RGB images : human_<pose variation number>_<image type>_<camera view number>.png        : human_0_rgb_3.png
    Depth data : human_<pose variation number>_<image type>_<camera view number>_0001.exr   : human_0_depth_3_0001.exr

Create a following directory structure and change the paths in both the scripts accordingly. Put files from
inputData into appropriate folders before running the scripts.

poseSamples
├── dae_files
│   ├── human_0.dae
│   ├── human_1.dae
│   ├── pose9.dae
│   └── textures
│       └── brown_eye.png
├── input_files
│   ├── camera_positions.txt
│   └── pose_parameters.txt
├── input_poses
│   ├── basepose.mhm
│   └── basepose.thumb
├── mhx2
│   ├── human_0.mhx2
│   ├── human_1.mhx2
│   ├── myfile.mhx12
│   ├── pose1.mhx12
│   ├── pose2.mhx2
│   ├── sumit.mhx2
│   └── textures
│       ├── brown_eye.png
│       ├── female_casualsuit01_ao.png
│       ├── female_casualsuit01_diffuse.png
│       ├── female_casualsuit01_normal.png
│       ├── male_casualsuit02_ao.png
│       ├── male_casualsuit02_diffuse.png
│       └── male_casualsuit02_normal.png
├── posed_mh
│   ├── human_0.mhm
│   └── human_1.mhm
├── readme.txt
├── render_data
│   ├── human_0_rgb_0.png
│   ├── human_0_rgb_1.png
│   ├── human_0_rgb_2.png
│   ├── human_0_rgb_3.png
│   ├── human_0_rgbd_00001.png
│   ├── human_0_rgbd_10001.png
│   ├── human_0_rgbd_20001.png
│   ├── human_0_rgbd_30001.png
│   ├── human_1_rgb_0.png
│   ├── human_1_rgb_1.png
│   ├── human_1_rgb_2.png
│   ├── human_1_rgb_3.png
│   ├── human_1_rgbd_00001.png
│   ├── human_1_rgbd_10001.png
│   ├── human_1_rgbd_20001.png
│   ├── human_1_rgbd_30001.png
│   ├── pose9_rgb_0.png
│   ├── pose9_rgb_1.png
│   ├── pose9_rgb_2.png
│   ├── pose9_rgb_3.png
│   ├── pose9_rgbd_00001.png
│   ├── pose9_rgbd_10001.png
│   ├── pose9_rgbd_20001.png
│   └── pose9_rgbd_30001.png
└── textures
    ├── brown_eye.png
    ├── female_casualsuit01_ao.png
    ├── female_casualsuit01_diffuse.png
    └── female_casualsuit01_normal.png
