import csv
# import yaml
import json

from os.path import exists
from src.classes.File import File
from src.classes.Error import Error
from src.utils.path import getExportPath

class Exporter:
    @staticmethod
    def saveCSV(path, data):
        if File.exist(getExportPath()):
            print('👌')
            file = open(getExportPath(path), 'w', newline = '')
            with file:   
                write = csv.writer(file)
                write.writerows(data)
        return None