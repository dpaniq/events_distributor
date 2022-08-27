import os
import re

from random import choice, shuffle
from pprint import pprint

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

class Distributor:
    # Private

    
    # Protected
    _config = None
    _fileLoader = None
    
    
    # Public
    segments = {}
    final = {} 
    
    def __init__(self, config, fileLoader):
        # _loadConfig
        self._config = config
        self._fileLoader = fileLoader
    

    
    def start(self):
        self.loadEventFile()
        self.cleanSegmentsName()
        self.distributeProjectsBySegment()
        self.export()
    
    def loadEventFile(self):
        eventFile = self._fileLoader.load(self._config.event, 'csv')
        # print(eventFile)

        # Read file
        if (eventFile):
            # Add only segment and project columns. Reversy it
            projectsAndSegments = []
            for row in eventFile:
                projectsAndSegments.append(row[2:4][::-1])
                # pprint(row[2:4][::-1])

            # Take last enter of project
            # Remove all registration on event before
            projects = {}
            for project, segment in projectsAndSegments:
                projects[project] = segment
            # pprint(projects)
            
            # Grouping by segment
            segments = {}
            for project, segment in projects.items():
                if segment not in segments:
                    segments[segment] = []
                    
                # For one segment project must be twice
                segments[segment].append(project)
                segments[segment].append(project)
            # pprint(segments)
            self.segments = segments
    
    def cleanSegmentsName(self):
        cleanedSegments = {}
        for segment in self.segments.keys():
            cleanedSegments[re.sub('[\'\`"]', '', segment)] = self.segments[segment]
        self.segments = cleanedSegments
        # pprint(self.segments)
        
    """
        [
            ['project', 'project', 'project'],
            ['project', 'project', 'project'],
            ['project', 'project', 'project'],
            ['project', 'project', 'project'] [row]
                                    [column]
        ]
    """
    # Project distributing       
    def distributeProjectsBySegment(self):
        distributor = {}
        
        for segmentName in self.segments.keys():
            pass
            segmentConfig = next((segConf for segConf in self._config.segments if segConf['name'] == segmentName), None)
            if not segmentConfig:
                continue
            # pprint(segmentConfig)
            
            # Ok, segment have name, columns, rows. What next?
            rows = []
            projectTransit = {}
            print(segmentName, segmentConfig['rows'], segmentConfig['columns'])
            for row in range(segmentConfig['rows']):
                columns = []
                for col in range(segmentConfig['columns']):
                    print(f'rows=[{row}] col=[{col}]')
                    if len(self.segments[segmentName]) < 0:
                        break
                    
                    """
                    Problem: 
                    One project cannot be in a similar row or column

                    any   [some1] any
                    [some2]  any  [some2]
                    any   [some1] any
                    
                    """
                    shuffle(self.segments[segmentName])
                    for projectName in self.segments[segmentName]:
                        # ProjectName first entry
                        if projectName not in projectTransit:
                            projectTransit[projectName] = {"row": row, "col": col}
                            self.segments[segmentName].remove(projectName) # delete one of project from segment
                            columns.append(projectName)
                            break
                           
                        # ProjectName second entry
                        elif projectTransit[projectName]['row'] != row and projectTransit[projectName]['col'] != col:
                            del projectTransit[projectName]
                            self.segments[segmentName].remove(projectName) # delete one of project from segment
                            columns.append(projectName)
                            if projectName not in projectTransit:
                                projectTransit[projectName] = {"row": row, "col": col}
                            else:
                                del projectTransit[projectName]
                            

                rows.append(columns)
            # print(segmentName)
            pprint(len(rows))
            pprint(rows)
            self.final[segmentName] = rows
        # pprint(self.final)
        
    # Export files
    def export(self):
        # self._fileLoader.mkOutputDir(self._config['output'])
        for segmentName, data in self.final.items():
            self._fileLoader.saveAsCSV(f'_exports/{segmentName}.csv', data)
            # file = open(f'output/{key}.csv', 'w', newline = '')
            # with file:   
            #     write = csv.writer(file)
            #     write.writerows(generateCSV[key])
                # for row in generateCSV[key]:
                #   write.writerows([row])
    

# firstKey = list(generateCSV.keys())[0]

# # print(generateCSV[firstKey])
# # [['asdasd', ...], [], []]

# for key, values in generateCSV.items():
      
#   file = open(f'{key}.csv', 'w', newline = '')
#   with file:   
#       write = csv.writer(file)
#       write.writerows(generateCSV[key])
#       # for row in generateCSV[key]:
#       #   write.writerows([row])
 
# opening the csv file in 'w+' mode

 
# writing the data into the file



# import pandas as pd

# df = pd.DataFrame(generateCSV)      
# df.to_excel('./teams.xlsx')


# firstKey = (generateCSV.keys())[0]
# with open('file.csv', 'w', newline='') as csvfile:
#   spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  
#   for row in generateCSV[firstKey]:
#     spamwriter.writerow(row)
  
