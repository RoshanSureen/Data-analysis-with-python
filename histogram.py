import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#my libraries
import continents as cont

class displayHistogram:

        # list declaration
        countries = ''
        continents = ''
        browser = ''
        countryList = []
        countryCountList = []
        browserList = []
        browser = {}

        #groups countries and produces the total number of countries for a document
        def groupCountries(self,data):
                self.countries = data.groupby(['env_doc_id','visitor_country']).size().reset_index(name='Count')
                self.countryList = self.countries.visitor_country.values.tolist()
                self.countryCountList = self.countries.Count.values.tolist()
                self.drawHistogram()


        def groupContinents(self,data):
                self.continents = data.groupby(['env_doc_id','visitor_country']).size().reset_index(name='Count')
                #print(self.continents)
                self.countryList = self.continents.visitor_country.values.tolist()
                for index,item in enumerate(self.countryList):
                        self.countryList[index] = cont.nameOfContinent(cont.countryToContinent(item))
                print(self.countryList)
                self.countryCountList = self.continents.Count.values.tolist()
                print(self.countryCountList)
                self.drawHistogram()

        def groupBrowser(self,data):
                self.browser = data.groupby(['env_doc_id', 'visitor_useragent']).size().reset_index(name='Count')
                print(self.browser)
                self.countryList = self.browser.visitor_useragent.values.tolist()
                print(self.countryList)



                # self.countryCountList = self.browser.Count.values.tolist()
                # print(self.countryCountList)
                # self.drawHistogram()


        # creates a histogram
        def drawHistogram(self):
                x = len(self.countryList)
                plt.bar(range(x), self.countryCountList, align='center', alpha=0.4, color='blue')
                plt.xticks(range(x), self.countryList)  # counts.values())
                plt.xlabel('counts')
                plt.title('Number of countries represented')
                plt.show()
