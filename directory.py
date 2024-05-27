class Directory:
    def __init__(self, directoryName, ramaProcedencia = None, path = ""):
        self.ramaProcedencia = ramaProcedencia
        self.directoryName = directoryName
        self.subDirectories = []
        self.files = []
        self.path = path + "/" + directoryName

    def makeDirectory(self, directoryName): 
        
        for directory in self.subDirectories:
            if directory.directoryName == directoryName:
                return None
    
        newDirectory = Directory(directoryName, self, self.path)
        self.subDirectories.append(newDirectory)

        return newDirectory
        

    def changeDirectory(self, directoryName):
        if directoryName == "..":
            return self.ramaProcedencia
        if directoryName == ".":
            return self
        for subDirectory in self.subDirectories:
            if subDirectory.directoryName == directoryName:
                return subDirectory
        return None
    
    def removeDirectory(self, directoryName):
        for subDirectory in self.subDirectories:
            if subDirectory.directoryName == directoryName:
                self.subDirectories.remove(subDirectory)
                return True
        return False

    def autoComplete(self, name):
        for subDirectory in self.subDirectories:
            if subDirectory.directoryName.startswith(name):
                return subDirectory.directoryName
        return None
    
    def createFile(self, fileName):
        for file in self.files:
            if file == fileName:
                return None
        self.files.append(fileName)
        return fileName
    
    def remove(self, name):
        for file in self.files:
            if file == name:
                self.files.remove(file)
                return True
        for subDirectory in self.subDirectories:
            if subDirectory.directoryName == name:
                self.subDirectories.remove(subDirectory)
                return True
        return False
        
