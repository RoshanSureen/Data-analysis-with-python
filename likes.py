import read_json as rj

class likes_func:

    readersList = []
    readersDict = {}

    documentList = []
    documentDict = {}
    #class contructor
    def __init__(self,path):
        rj.readJson(path)

    def getDocID(self,d_id,data_frame,column):
        return data_frame.loc[data_frame[column] == d_id]

    def getReaders(self,doc_ID,dataFrame):
        self.readersList = dataFrame['visitor_uuid'].value_counts()
        #print(self.readersList)
        self.readersDict = self.readersList.to_dict()
        print(self.readersDict)

    def getDocuments(self,visitor_ID, dataFrame):
        self.documentList = dataFrame['subject_doc_id'].value_counts()
        #print(self.documentList)
        self.documentDict = self.documentList.to_dict()
        print(self.documentDict)

#main function
if __name__ == '__main__':
    t1 = likes_func('data.txt')
    df_t1 = rj.createDataframe()

    docID = '130313161023-ee03f65a89c7406fa097abe281341b42'
    visitorID = '1d87b7c9c07dc8f8'

    docID_rows = t1.getDocID(docID, df_t1,'subject_doc_id')
    visitorID_rows = t1.getDocID(visitorID,df_t1,'visitor_uuid')

    t1.getReaders(docID,docID_rows)
    t1.getDocuments(visitorID,visitorID_rows)