import pymongo
import pandas as pd
import json

client=pymongo.MongoClient("mongodb+srv://Sandeep:Sandeep011@cluster0.i2b4kej.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH="C:/Users/nehak/OneDrive/Desktop/app/aps_failure_training_set1.csv"

DATABASE_NAME='Sandeep'
COLLECTION_NAME="Aps-sensor"


if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)