#coding=utf-8
import sys
import os.path
#import Image
if __name__ == '__main__':


    BASE_PATH="./data/generate/"
    SEPARATOR=";"
    label = 0
    for dirpath, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirpath, subdirname)
            #print subject_path
            for filename in os.listdir(subject_path):
                image_filename = subject_path + "/"+ filename
                #print(image_filename)
                #img=Image.open(image_filename)
                ##  img=img.resize((92,112))
                #img.show()
                abs_path = "%s/%s" % (subject_path, filename)
                print("%s%s%d"%(abs_path,SEPARATOR, label))
                # print("%s"%(abs_path))
            label = label + 1