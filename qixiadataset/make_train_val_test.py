import os
import random

trainval_percent = 0.7
train_percent = 0.6
xmlfilepath = '/home/smallchild/data/VOCdevkit/qixiadataset/Annotations'
txtsavepath = '/home/smallchild/data/VOCdevkit/qixiadataset/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('/home/smallchild/data/VOCdevkit/qixiadataset/ImageSets/Main/trainval.txt', 'w')
ftest = open('/home/smallchild/data/VOCdevkit/qixiadataset/ImageSets/Main/test.txt', 'w')
ftrain = open('/home/smallchild/data/VOCdevkit/qixiadataset/ImageSets/Main/train.txt', 'w')
fval = open('/home/smallchild/data/VOCdevkit/qixiadataset/ImageSets/Main/val.txt', 'w')

i=0
for i in list:
    i += 1
    name=total_xml[i][:-4]+"\n"
    #print name
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest .close()

print i


# for i  in list:
#     name=total_xml[i][:-4]+'\n'
#     if i in trainval:
#         ftrainval.write(name)
#         if i in train:
#             ftrain.write(name)
#         else:
#             fval.write(name)
#     else:
#         ftest.write(name)
#
# ftrainval.close()
# ftrain.close()
# fval.close()
# ftest .close()
