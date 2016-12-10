#External Libraries
import json
import pandas as pd

import histogram as hist
import read_json as rj

class firstTask:

    # #list declaration
    # countries = ''
    # continents = ''
    # countryList = []
    # countryCountList = []

    #class contructor
    def __init__(self,path):
        rj.readJson(path)

    #gets all rows of data pertaining to the document id
    def getDocID(self,d_id,data_frame):
        return data_frame.loc[data_frame['env_doc_id'] == d_id]



#main function
if __name__ == '__main__':
    t1 = firstTask('data.txt')
    df_t1 = rj.createDataframe()

    docID = '110322220408-aadc46d7849e4c38bd0392de0e4a7605'
    docID_data = t1.getDocID(docID,df_t1)
    #print(docID_data['visitor_country'])

    hist1 = hist.displayHistogram()
    hist1.groupBrowser(docID_data)