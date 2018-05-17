import os
import cv2
import glob

path = "captures/"
'''for root, dirs, images in os.walk(path):
    for img in images:
        #print(img)
        image1 = cv2.imread(img)
        #print(image1)
        #log = open(indir + f, 'r')
        log = open(os.path.join(root, img), 'rb')
        print(log)
        cv2.imshow("", image1)'''
filename = "*.jpg"
path = "captures/"+filename
for image in glob.iglob(path):
    #print(image)
    img=cv2.imread(image)
    ace=type(img)
    print(ace)
    print(img)
    cv2.imshow("", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    #os.remove(image)