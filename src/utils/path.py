import os

def getImportPath(path):
    return f"{os.getcwd()}/_imports/{path}"

def getExportPath(path= None):
    return f"{os.getcwd()}/_exports/{path}" if path else f"{os.getcwd()}/_exports/"