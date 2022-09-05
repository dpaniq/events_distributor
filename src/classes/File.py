import csv
import json
from abc import ABC
from os.path import exists

from .Error import Error

class File(ABC):
    
    _error = Error
    
    def __init__(self):
        pass
    
    @staticmethod
    def exist(path):
        return exists(path)

    @staticmethod
    def makeDirectories(path):
        # entry = path.indexOf('events_distributor')
        directories = path.split('/')[:-1]
        print(directories)

    def load(self, fileName, openAs):
        print(fileName)
        return self.__loadFile(fileName, openAs)
    
    def mkOutputDir(self, output):
        pass
        
        # try:
        #     # os.removedirs(f'{self._fileLoader.pwd}/distanation/')
        #     os.mkdir(f'{self._fileLoader.pwd}/day{self._config.day}')
        # except FileNotFoundError or FileExistsError:
        #     print('ok :)')
        # return
    
    def __loadFile(self, path, openAs = None):
        if exists(path):
            if openAs == 'csv':
                return self.__loadAsCSV(path)
            elif openAs == 'json':
                return self.__loadAsJSON(path)

                    # elif openAs == 'csv':
                    #     print('here')
                    #     return self.__loadAsCSV(path)
            # try:
            #     with open(path, newline='') as _file:
            #         if openAs == 'json':
            #             file = json.load(_file)
            #         elif openAs == 'csv':
            #             print('here')
            #             return self.__loadAsCSV(path)
                        
            #         elif openAs == yaml:
            #             file = yaml.load(_file)
            #         else:
            #             print(f'The file {path} (opened as {openAs}) does not exist')
            #             raise Exception('The extension of file is not supported')
            # except FileNotFoundError or FileExistsError:    
            #     print(f'Some file in file loader')
            # finally:
            #     return file
            #     _file.close()
        print(f'The file {path} not exist')
        return None
    
    def __loadAsJSON(self, path):
        with open(path, newline='') as jsonfile:
            print(jsonfile)
            return json.load(jsonfile)
    
    def __loadAsCSV(self, path):
        file = []
        try:
            with open(path, newline='') as csvfile:
                spamreader = csv.reader(csvfile) #  delimiter=' ', quotechar='|'
                for row in spamreader:
                    file.append(row)
        except FileNotFoundError or FileExistsError:
            print(f'Some error in load csv')
        finally:
            print('File loaded successfuly')
            return file
    
    # def saveAsCSV(self, fileName, data):
    #     file = open(f'{fileName}', 'w', newline = '')
    #     with file:   
    #         write = csv.writer(file)
    #         write.writerows(data)
    #         # write.writerows([[1,2], [3,4]])
            
            
            
# os.mkdir
# os.remove()
  
# # Opening JSON file
# f = open('data.json')
  
# # returns JSON object as 
# # a dictionary
# data = json.load(f)
  
# # Iterating through the json
# # list
# for i in data['emp_details']:
#     print(i)
  
# # Closing file
# f.close()
