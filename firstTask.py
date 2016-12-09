#External Libraries
import json
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

jsonData = []

class firstTask:

    #list declaration
    countries = ''
    countryList = []
    countryCountList = []

    #class contructor
    def __init__(self,path):
        with open(path) as data:
            for d in data:
                jsonData.append(json.loads(d))

    #creates a panda dataframe
    def createDataframe(self,data):
        df = pd.DataFrame(data,columns=['ts','visitor_uuid','visitor_username','visitor_source','visitor_device',
         'visitor_useragent','visitor_ip','visitor_country','visitor_referrer',
         'env_type','env_doc_id','env_adid','event_type','event_readtime','subject_type',
         'env_type','subject_doc_id','subject_page','cause'])
        return df

    #gets all rows of data pertaining to the document id
    def getDocID(self,d_id,data_frame):
        return data_frame.loc[data_frame['env_doc_id'] == d_id]

    #groups countries and produces the total number of countries for a document
    def groupCountries(self,data):
        self.countries = data.groupby(['env_doc_id','visitor_country']).size().reset_index(name='Count')
        self.countryList = self.countries.visitor_country.values.tolist()
        self.countryCountList = self.countries.Count.values.tolist()

    #creates a histogram
    def drawHistogram(self):
        x = len(self.countryList)
        plt.bar(range(x), self.countryCountList, align='center', alpha=0.4, color='blue')
        plt.xticks(range(x), self.countryList)  # counts.values())
        plt.xlabel('counts')
        plt.title('Number of countries represented')
        plt.show()

#main function
if __name__ == '__main__':
    t1 = firstTask('data.txt')
    df_t1 = t1.createDataframe(jsonData)

    docID = '100608165922-d5c05908b7044d97a13a952e808ccba7'
    docID_data = t1.getDocID(docID,df_t1)
    print(docID_data['visitor_country'])

    t1.groupCountries(docID_data)
    t1.drawHistogram()