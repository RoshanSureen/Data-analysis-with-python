import histogram as hist
import read_json as rj

class secondTask:

    browsers = {}
    #class contructor
    def __init__(self,path):
        rj.readJson(path)

#main function
def taskTwo():
    t1 = secondTask('data.txt')
    df_t1 = rj.createDataframe()

    hist1 = hist.displayHistogram()
    hist1.groupBrowser(df_t1)