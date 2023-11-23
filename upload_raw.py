from db import upload_patents
import csv
import sys

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


def upload(patents):
    for p in patents:
        p["_id"] = int(p["patent"])
        del p["patent"]
        del p["claims"]
    upload_patents(patents)


with open("./data/patent_txt_raw.csv", newline='', encoding='Latin1') as inf:
    dicread = csv.DictReader(inf)
    patents = []
    for row in dicread:
        patents.append(row)
        if len(patents) == 1000:
            upload(patents)
            patents = []
    print("Final upload len ", len(patents))
    if patents:
        upload(patents)
            