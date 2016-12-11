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

    #get all readers of one document
    def getReaders(self,doc_ID,dataFrame):
        self.readersList = dataFrame['visitor_uuid'].value_counts()
        self.readersDict = self.readersList.to_dict()
        print(self.readersDict)

    #get all documents read by one person
    def getDocuments(self,visitor_ID, dataFrame):
        self.documentList = dataFrame['subject_doc_id'].value_counts()
        self.documentDict = self.documentList.to_dict()
        print(self.documentDict)

#main function
def task5(documetID,visitor_ID):
    t1 = likes_func('data.txt')
    df_t1 = rj.createDataframe()

    docID = documetID
    visitorID = visitor_ID

    docID_rows = t1.getDocID(docID, df_t1,'subject_doc_id')
    visitorID_rows = t1.getDocID(visitorID,df_t1,'visitor_uuid')

    t1.getReaders(docID,docID_rows)
    t1.getDocuments(visitorID,visitorID_rows)