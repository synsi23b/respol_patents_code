from dotenv import load_dotenv
import pymongo
import os

_db = pymongo.MongoClient(os.getenv('MONGOCON')).get_database("patents")

def check_res(res):
    if not res.acknowledged:
        print(res, f"was not acknowledged: {res.acknowledged}")

def check_res_uspert(res):
    print(res, f"\nwas acknowledged: {res.acknowledged}\nnMatched: {res.matched_count}\nnUpserted: {res.upserted_count}\nnModified: {res.modified_count}")

def upsert_patents(datalist):
    ops = [ pymongo.UpdateOne({"_id": x["_id"]}, {'$set': x}, upsert=True) for x in datalist ]
    res = _db["patent"].bulk_write(ops)
    check_res_uspert(res)

def upload_patents(datalist):
    #ops = [ pymongo.({"_id": x["_id"]}, {'$set': x}, upsert=True) for x in datalist ]
    res = _db["patent"].insert_many(datalist)
    check_res(res)

def get_patent(patid):
    return _db["patent"].find_one({"_id" : patid})