import json

class srtMakerFromText(object):
    """
    Speech2Text API Response >> .txt >> .SRT
    """
    def __init__(self, textFile):
        self.text = textFile
        self.fname = self.text[:-4]+ 'SRT'

    textPieces = []
    timeRanges = []

    def _getPieces(self):
        """
        Open the file and then
        Store the chunks of text as a list of tuples
        """

        with open(self.text, 'r') as f:
            _reader = f.read()
            _read = json.loads(_reader)
            print("{} successfully read".format(self.text))

            n = len(_read['results'])
            print("There are {} chunks".format(n))
            for i in range(n):
                self.textPieces.append(_read['results'][i]['alternatives'][0]['transcript'])
                self.timeRanges.append((_read['results'][i]['alternatives'][0]['timestamps'][0][1], _read['results'][i]['alternatives'][0]['timestamps'][-1][-1]))
            return(list(zip(self.textPieces, self.timeRanges)))

    def _makeFile(self):
        """
        Create a list of blocks of text for the .SRT file
        First line is the chunk number
        Second line is the time interval
        Third line is the text
        Fourth line is \n
        """

        pieces = self._getPieces()
        nChunks = len(pieces)
        tempChunk = []
        for i in range(nChunks):
            # line one
            tempChunk.append(str(i+1)+"\n")

            # line two- This code will help me in future versions of code for video translation project

            # line three
            tempChunk.append(str(pieces[i][0])+"\n")

            # line four
            tempChunk.append("\n")
        print(len(tempChunk))
        return tempChunk

    def writeFile(self):
        myLines = self._makeFile()
        with open(self.fname, 'w') as f:
            f.writelines(myLines)
            print("{} written \n".format(self.fname))
'''
# Runn this code if you want to test this calss alone, anyway this code will be called from Convert.py
# The input will contain JSON text files which generated from last step Convert.py
json_from_IBM_Watson_dir = "/Users/latlab/Desktop/AudioToText/2_Output_Files/"


list_of_files = glob.glob(json_from_IBM_Watson_dir + "*.text")
for (finel_number, f_Name) in enumerate(list_of_files):
    writer = srtMakerFromText(f_Name).writeFile()
'''