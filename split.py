import os
import shutil

train = open(os.path.abspath('ImageSets/train.txt'))
val = open(os.path.abspath('ImageSets/val.txt'))
list_train = train.read().splitlines()
list_val = val.read().splitlines()
for i in list_train:
    shutil.move('data_im/data_object_image_2/training/image_2/'+i+'.png','DATA_DIR/training/image_2/'+i+'.png')
    shutil.move('data_im/data_object_velodyne/training/velodyne/'+i+'.bin','DATA_DIR/training/velodyne/'+i+'.bin')
    shutil.move('data_im/training/label_2/'+i+'.txt','DATA_DIR/training/label_2/'+i+'.txt')

for i in list_val:
    shutil.move('data_im/data_object_image_2/training/image_2/'+i+'.png','DATA_DIR/validation/image_2/'+i+'.png')
    shutil.move('data_im/data_object_velodyne/training/velodyne/'+i+'.bin','DATA_DIR/validation/velodyne/'+i+'.bin')
    shutil.move('data_im/training/label_2/'+i+'.txt','DATA_DIR/validation/label_2/'+i+'.txt')
