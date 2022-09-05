import os
import re

from random import choice, shuffle
from pprint import pprint

from .Configurator import Configurator
from .Importer import Importer
from .Exporter import Exporter
from .Error import Error

class Distributor:
    # Private
    __error = Error('Distributor')
    
    # Public
    cfg = None
    events = {}
    final = {}
    
    def __init__(self):
        self.cfg = Configurator()
        # try:
        #     self.cfg = Configurator()
        #     print(self.cfg)
        # except Exception as error:
        #     Error.throw(1, error, name=Distributor.__name__)
            
    
    def start(self):
        # event = self.cfg['event']
        # if not event:
        #     return False
        # table = self.loadEventTable(event)
        # segments = self.reduceSegments(table)
        # cleanedSegments = self.cleanSegmentsName(segments)
        # distributed = self.distributeProjectsBySegment(cleanedSegments, self.cfg)
        # self.export(distributed)
        pass
            
    
    
    @staticmethod
    def loadEventTable(event):
        return Importer.loadCSV(event['name'] + '.csv')
    
    @staticmethod        
    def export(event):
        print('1')
        for segmentName, data in event:
            Exporter.saveCSV(f'{segmentName}.csv', data)
        
    @staticmethod
    def cleanSegmentsName(segments):
        cleanedSegments = {}
        for segment in segments.keys():
            cleanedSegments[re.sub('[\'\`"]', '', segment)] = segments[segment]
        return cleanedSegments
    
    @staticmethod
    def reduceSegments(table):
        if not table:
            return None
    
        projectsAndSegments = []
        for row in table:
            # Add only segment and project columns. Reversy it
            projectsAndSegments.append(row[2:4][::-1])
            # pprint(row[2:4][::-1])

        # Take last enter of project. Remove all registration on event before
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
        return segments
        
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
    def distributeProjectsBySegment(segments, config):
        for segmentName in segments.keys():
            segmentConfig = next((segmentConfig for segmentConfig in config['segments'] if segmentConfig['name'] == segmentName), None)
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
                    if len(segments[segmentName]) < 0:
                        break
                    
                    """
                    Problem: 
                    One project cannot be in a similar row or column

                    Wrong
                    any   [some1] any
                    [some2]  any  [some2]
                    any   [some1] any
                    
                    """
                    shuffle(segments[segmentName])
                    for projectName in segments[segmentName]:
                        # ProjectName first entry
                        if projectName not in projectTransit:
                            projectTransit[projectName] = {"row": row, "col": col}
                            segments[segmentName].remove(projectName) # delete one of project from segment
                            columns.append(projectName)
                            break
                           
                        # ProjectName second entry
                        elif projectTransit[projectName]['row'] != row and projectTransit[projectName]['col'] != col:
                            del projectTransit[projectName]
                            segments[segmentName].remove(projectName) # delete one of project from segment
                            columns.append(projectName)
                            if projectName not in projectTransit:
                                projectTransit[projectName] = {"row": row, "col": col}
                            else:
                                del projectTransit[projectName]
                            

                rows.append(columns)
            pprint(len(rows))
            pprint(rows)
            
            return {segmentName: rows}

  
