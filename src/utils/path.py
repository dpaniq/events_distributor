import os

def getImportPath(path):
    return f"{os.getcwd()}/_imports/{path}"

def getExportPath(path):
    return f"{os.getcwd()}/_exports/{path}"