from core import G
import os

"""
You need to create a model with default skeleton
for running this script.
"""

BASE_DIR="/home/sumit/Desktop/poseSamples/"
EXPORT_DIR=BASE_DIR+"dae_files/"
POSED_DIR=BASE_DIR+"posed_mh/"
POSE_PARAMETER_FILE=os.path.join(BASE_DIR, "input_files/pose_parameters.txt")
INPUT_DIR = os.path.join(BASE_DIR, "input_poses/")
LOAD_HUMAN_PATH=BASE_DIR+"input_poses/basicPose.mhm"
NUMBER_OF_VARIATIONS=2
EXPORTER_NAME = 'Collada (dae)'
VALID_FILE_EXTENSION = '.mhm'
#increment step for this variable is number of variations
START_INDEX_FOR_FILE_NAME = 0*NUMBER_OF_VARIATIONS

"""
Reads data from file
"""
def read_file(file_path):
    lines=[]
    file_obj=open(file_path, "r")
    for line in file_obj:
        lines.append(line.strip())
    return lines


"""
Exports file to blender acceptable format
"""
def export(human, file_name, export_dir, exporter_name):
    # don't change the defination of filename function
    def filename(file_ext):
        file_path=export_dir+file_name+"."+file_ext
        return file_path

    #mhx2Exporter=G.app.files.export.getExporter('MakeHuman Exchange (mhx2)')
    mhx2Exporter=G.app.files.export.getExporter(exporter_name)
    mhx2Exporter.export(human, filename)

"""
Generate random values for human parameters
"""
def generate_random_variations(params):
    from random import Random
    rand=Random()
    human_params={}
    for param in params:
        print(param)
        if param == 'gender':
            human_params[param]=rand.randint(0, 1)
        else:
            human_params[param]=rand.random()
    if human_params['gender'] == 0 and human_params['age'] < 0.2:
        human_params['breastsize'] = human_params['age']
    return human_params

"""
Load a human and set its parameters
"""
def create_human(human_params,load_human_path):
    G.app.loadHumanMHM(load_human_path)
    human = G.app.selectedHuman
    #human.resetToRestPose()
    human.setAge(human_params['age'])
    human.setAsian(human_params['asianVal'])
    human.setAfrican(human_params['africanVal'])
    human.setCaucasian(human_params['caucasianVal'])
    human.setGender(human_params['gender'])
    human.setHeight(human_params['height'])
    human.setMuscle(human_params['muscle'])
    human.setWeight(human_params['weight'])
    human.setBreastSize(human_params['breastsize'])
    return human


"""
This method generates pose variations from base pose
"""
def generate_poses(human, human_name):
    from bvh import BVH
    import matrix as m
    skeleton=human.skeleton
    bones=skeleton.getBones()
    b=BVH()
    b.fromSkeleton(skeleton, None, False)
    anim=b.createAnimationTrack(skeleton, name=human_name)
    rotmatrix=m.rotx(30)
    change=rotmatrix[:3, :4]
    for boneNr in range(len(bones)):
        boneName=bones[boneNr].name
        animData=anim.data[boneNr]
        if boneName == "upperarm02.L":
            anim.data[boneNr]=change

    human.addAnimation(anim)
    human.setActiveAnimation(anim.name)
    human.refreshPose()
    return human


"""
This method saves the automatically generated posed
models in mhm format.
"""
def save_model(human, human_name, posed_dir):
    file_name=os.path.join(posed_dir, human_name+".mhm")
    human.save(file_name, human_name)


"""
For validating file extension
"""
def validate_file(file_name, extensions):
    if file_name.endswith(extensions):
        return True
    return False

"""
This is the main method of the script
"""
params=read_file(POSE_PARAMETER_FILE)
fileNames=os.listdir(INPUT_DIR)
for fileName in fileNames:
    print(fileName)
    if validate_file(fileName, VALID_FILE_EXTENSION):
        LOAD_HUMAN_PATH = os.path.join(INPUT_DIR,fileName)
        for i in range(START_INDEX_FOR_FILE_NAME, NUMBER_OF_VARIATIONS+START_INDEX_FOR_FILE_NAME):
            human_params=generate_random_variations(params)
            human=create_human(human_params,LOAD_HUMAN_PATH)
            human_name="human_"+str(i)
            human=generate_poses(human, human_name)
            save_model(human, human_name, POSED_DIR)
            export(human, human_name, EXPORT_DIR, EXPORTER_NAME)
