import read_json as rj

class thirdTask:

    #class contructor
    def __init__(self,path):
        rj.readJson(path)

    def top_readers(self,data_frame):
        data_frame = data_frame.groupby(['visitor_uuid', 'event_readtime']).sum().reset_index()
        data_frame = data_frame[data_frame.event_readtime.notnull()]

        data_frame = data_frame.sort_values(['event_readtime'], ascending=0)
        data_frame = data_frame.head(10)
        return data_frame


#main function
def taskThree():
    t1 = thirdTask('data.txt')
    df_t1 = rj.createDataframe()

    new_df = t1.top_readers(df_t1)
    return new_df
