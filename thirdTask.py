import read_json as rj

class firstTask:

    #class contructor
    def __init__(self,path):
        rj.readJson(path)

    def readers(self,data_frame):
        data_frame = data_frame.groupby(['visitor_uuid', 'event_readtime']).sum().reset_index()
        data_frame = data_frame[data_frame.event_readtime.notnull()]

        data_frame = data_frame.sort_values(['event_readtime'], ascending=0)
        data_frame = data_frame.head(10)
        return data_frame


#main function
if __name__ == '__main__':
    t1 = firstTask('data.txt')
    df_t1 = rj.createDataframe()

    new_df = t1.readers(df_t1)
    print(new_df)