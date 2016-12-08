#df = pd.DataFrame(jsonData, columns=['ts','visitor_uuid','visitor_username','visitor_source','visitor_device','visitor_useragent','visitor_ip','visitor_country','visitor_referrer','env_type','env_doc_id','env_adid','event_type','event_readtime','subject_type','env_type','subject_doc_id','subject_page','cause'])
#print(df)

import json
import pandas as pd

jsonData = [] #list for issuu dataset
continents = [] #list for continents
country_To_Continent = [] #list for mapping a country to a continent

def loadfromfile(filename):
    for d in filename:
        jsonData.append(json.loads(d))

    df = pd.DataFrame(jsonData)
    

def loadcontinents(filename):
    for cont in filename:
        continents.append(json.loads(cont))

    return continents

def map_Countries(filename):
    for cont in filename:
        country_To_Continent.append(json.loads(cont))

