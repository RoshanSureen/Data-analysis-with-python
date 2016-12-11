import read_json as rj
import histogram as hist

class first_Task:

    #class contructor
    def __init__(self,path):
        rj.readJson(path)

    #gets all rows of data pertaining to the document id
    def getDocID(self,d_id,data_frame):
        return data_frame.loc[data_frame['subject_doc_id'] == d_id]



#main function
def taskOne(docID,type):
    t1 = first_Task('data.txt')
    df_t1 = rj.createDataframe()

    doc_ID = docID
    docID_data = t1.getDocID(doc_ID,df_t1)

    hist1 = hist.displayHistogram()

    if type == 1:
        hist1.groupCountries(docID_data)
    else:
        hist1.groupContinents(docID_data)