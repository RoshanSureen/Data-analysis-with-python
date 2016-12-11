import argparse
import firstTask as t1
import secondTask as t2
import thirdTask as t3
import likes as t5

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="provide arguments as <taskID> <documentID> for only task 1 and 2. "
                                                 "<visitorID> will be included for task 5 ")
    parser.add_argument('typeID', help='choose between any number from 1-5',type=int)
    parser.add_argument('docID', help='ID of the document',type=str)
    parser.add_argument('visitID', help='ID of the visitor', type=str)

    args = parser.parse_args()
    document_uuid = args.docID
    visitor_uuid = args.visitID

    if args.typeID == 1:
        t1.taskOne(document_uuid,1)
    elif args.typeID == 2:
        t1.taskOne(document_uuid,2)
    elif args.typeID == 3:
        t2.taskTwo()
    elif args.typeID == 4:
        df_to_print = t3.taskThree()
        print(df_to_print[['visitor_uuid','event_readtime']])
    elif args.typeID == 5:
        t5.task5(document_uuid,visitor_uuid)