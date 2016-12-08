import json
import pandas as pd

jsonData = []
with open('data.txt') as data:
    for d in data:
        jsonData.append(json.loads(d))

df = pd.DataFrame(jsonData, columns=['ts','visitor_uuid','visitor_username','visitor_source','visitor_device','visitor_useragent','visitor_ip','visitor_country','visitor_referrer','env_type','env_doc_id','env_adid','event_type','event_readtime','subject_type','env_type','subject_doc_id','subject_page','cause'])
#print(df)

print(df['visitor_country'])