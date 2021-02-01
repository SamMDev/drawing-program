class ColorsTextFileManager:

    def __init__(self):
        self.file = open("colors", "r")

    def getColorsAsArray(self):
        arr = self.file.readlines()
        for i in range(len(arr)):
            arr[i] = arr[i].strip()
        self.file.seek(0)
        return arr