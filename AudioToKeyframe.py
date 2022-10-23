import bpy
import csv
import math
mouth = bpy.data.objects["Mouth"]

FILEPATH = "INSERT_FILEPATH_HERE"
framerate = bpy.context.scene.render.fps

with open(FILEPATH, 'r') as fd:
    reader = csv.reader(fd)
    next(reader, None)
    for kf in reader:
        current_frame = math.floor(float(kf[0])/(1.0/framerate))
        shapekey_index = int(kf[4]) + 1 # shapekey index 0 is the basis, so consider the other shapekeys as one-based indexing
        print(float(kf[0]), current_frame)

        # setting all shapekeys to 0
        for i in range(1,11):
            mouth.active_shape_key_index = i
            mouth.active_shape_key.value = 0
            mouth.active_shape_key.keyframe_insert(data_path='value', frame=current_frame)
        
        if shapekey_index == 0:
            print("Close")
        else:
            mouth.active_shape_key_index = int(kf[4]) + 1
            mouth.active_shape_key.value = 1
            mouth.active_shape_key.keyframe_insert(data_path='value', frame=current_frame)
