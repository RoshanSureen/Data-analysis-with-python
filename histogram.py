import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#my libraries
import continents as cont

class displayHistogram:


    # list declaration
    countries = ''
    continents = ''
    xaxis_List = []
    yaxis_List = []

    main_browsers = ["Opera", "Dalvik", "Safari", "Chrome", 'Trident', 'Mozilla']

    userAgentdata = ''

    #groups countries and produces the total number of countries for a document
    def groupCountries(self,data):
            self.countries = data.groupby(['subject_doc_id','visitor_country']).size().reset_index(name='Count')

            self.xaxis_List = self.countries.visitor_country.values.tolist()
            self.yaxis_List = self.countries.Count.values.tolist()

            self.drawHistogram()

    def groupContinents(self,data):
            self.continents = data.groupby(['subject_doc_id','visitor_country']).size().reset_index(name='Count')
            self.xaxis_List = self.continents.visitor_country.values.tolist()

            for index,item in enumerate(self.xaxis_List):
                    self.xaxis_List[index] = cont.nameOfContinent(cont.countryToContinent(item))
            print(self.xaxis_List)

            self.yaxis_List = self.continents.Count.values.tolist()
            print(self.yaxis_List)
            self.drawHistogram()

    def groupBrowser(self,data):
            self.userAgentData = data['visitor_useragent'].value_counts()
            dict_browser = self.userAgentData.to_dict()
            top_Browsers = {}

            for browser in self.main_browsers:
                for key,value in dict_browser.items():
                    if browser in key:
                        if browser in top_Browsers:
                            top_Browsers[browser] = top_Browsers[browser] + value
                        else:
                            top_Browsers[browser] = value
            print(top_Browsers)

            for k,v in top_Browsers.items():
                self.xaxis_List.append(k)
                self.yaxis_List.append(v)
            self.drawHistogram()

    # creates a histogram
    def drawHistogram(self):
            x = len(self.xaxis_List)
            plt.bar(range(x), self.yaxis_List, align='center', alpha=0.4, color='blue')

            plt.xticks(range(x), self.xaxis_List)  # counts.values())
            plt.title('Number of countries represented')

            plt.show()
