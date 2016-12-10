import histogram as hist
import read_json as rj

class firstTask:

    #class contructor
    def __init__(self,path):
        rj.readJson(path)

    #gets all rows of data pertaining to the document id
    def getDocID(self,d_id,data_frame):
        return data_frame.loc[data_frame['subject_doc_id'] == d_id]

#main function
def taskTwo():
    t1 = firstTask('data.txt')
    df_t1 = rj.createDataframe()

    hist1 = hist.displayHistogram()
    hist1.groupBrowser(df_t1)