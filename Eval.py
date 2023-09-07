from zipfile import *

from RiskTools import useful_functions as rt

import os
import shutil
from PIL.ExifTags import TAGS
from PIL import Image

fromfolder = r'H:\Personal Stuff\Pictures'
tofolder = r'H:\Personal Stuff\Pictures\testfolder'
fromfolder = rt.scrubfldrname(fromfolder)
tofolder     = rt.scrubfldrname(tofolder)

include_subfolders = False

def movefiles(fromfldr:str, tofldr:str, include_subfolder:bool = False):
    for file in os.listdir(fromfldr):
        if is_zipfile(file):
            ZipFile.extractall(file, tofldr)
        elif os.path.isdir(file):
            if os.path.samefile(file, tofldr)== False:
                movefiles(file, tofldr, include_subfolder)
        else:
            shutil.move(f'{fromfldr}{file}', f'{tofldr}{file}')

def getmetadata(folder:str, include_subfolders:str):
    for image in folder:
        pic = Image.open(image)
        exifdata = pic.getexif()
        for tagid in exifdata:
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            print(f'{tagname:25}: {value}')

movefiles(fromfolder, tofolder, True)