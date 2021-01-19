import statistics
import skimage
from skimage import io
import skimage.measure
import numpy as np
import os
import sys
import csv

# Open directory
path = input("Folder containing images : ")
filePath = input("Name of csv file that will be created : ")
dirs = os.listdir(path)
print("files in the directory:", len(dirs))

# Main array
L = []

# Loop
for file in dirs:
    img = io.imread(path+'/'+file)
    entropy = skimage.measure.shannon_entropy(img)

    # This is the maths behind, cf Shannon
    # marg = np.histogramdd(np.ravel(img), bins = 256)[0]/img.size
    # marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    # entropy = -np.sum(np.multiply(marg, np.log2(marg)))

    L.append([file, entropy])

# CSV commands
with open(filePath, 'w', newline='') as F:
    F_writer = csv.writer(F, delimiter=',')
    F_writer.writerows(L)
    print("CSV SAVED")

# ---- PATHS ----
imageDirPath = './FormatedImages/'
nbImages = int(input("Number of images to keep : "))

with open(filePath) as csvDataFile:
    csvList = list(csv.reader(csvDataFile))
    print("Reading file ", filePath)

    # Get median
    medianIndex = len(csvList) / 2

    # Put all img to remove in an array
    imgFilesToRemove = []
    for i in range(len(csvList)):
        if i < medianIndex-nbImages/2 or i > medianIndex + nbImages/2:
            imgFilesToRemove.append(csvList[i][0])
    
    # Delete images
    for img in imgFilesToRemove:
        os.remove(imageDirPath + img)
    print("Deleted a total of ", len(imgFilesToRemove), " images in ", imageDirPath)
