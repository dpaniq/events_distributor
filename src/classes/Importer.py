import csv
# import yaml
import json
import os
from os.path import exists

from src.classes.File import File
from src.classes.Error import Error
from src.utils.path import getImportPath

class Importer:
    @staticmethod
    def loadJSON(path):
        fullpath = getImportPath(path)
        print(fullpath)
        if File.exist(fullpath):
            print('existttttt')
            try:
                with open(fullpath, newline='') as jsonfile:
                    return json.load(jsonfile)
            except Exception as error:
                Error.throw(1, error, name=Importer.__name__)
        print('no existttttt')
        return None
    
    @staticmethod
    def loadCSV(path):
        fullpath = getImportPath(path)
        if File.exist(fullpath):
            try:
                array = []
                with open(fullpath, newline='') as csvfile:
                    spamreader = csv.reader(csvfile) #  delimiter=' ', quotechar='|'
                    print(spamreader)
                    for row in spamreader:
                        array.append(row)
                    return array
            except Exception as error:
                Error.throw(2, error, name=Importer.__name__)
        return None