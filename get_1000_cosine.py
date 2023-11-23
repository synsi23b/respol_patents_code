import pandas as pd
from pathlib import Path
from db import get_patent

dpath = Path(__file__).resolve().parent / "data"

DATA_ROWS = 2000

df = pd.read_csv( dpath / "patent_text_measures.txt" )

df["forward_div_backward_cousine"] = df["forward_cosine"].div(df["backward_cosine"].values)

cos_large = df.nlargest(DATA_ROWS, "forward_div_backward_cousine")
cos_small = df.nsmallest(DATA_ROWS, "forward_div_backward_cousine")


def write_out(frame:pd.DataFrame, filename:str):
    frame = frame.reindex(columns=[
        'patent', "title", "abstract", "forward_div_backward_cousine", 'forward_cosine', 'backward_cosine', 
        'new_word', 'new_word_reuse', 'new_bigram', 'new_bigram_reuse', 'new_trigram',
        'new_trigram_reuse', 'new_word_comb', 'new_word_comb_reuse',  
        ])
    frame.to_csv(dpath / filename)


def add_title_abstract(df):
    patents = [ get_patent(x) for x in df["patent"]]
    df["title"] = [ x["title"] for x in patents]
    df["abstract"] = [ x["abstract"] for x in patents]


#cos_large = cos_large.apply(add_title_abstract, axis=1, result_type="expand")
add_title_abstract(cos_large)
add_title_abstract(cos_small)


write_out(cos_large, "largest_cosine.csv")
write_out(cos_small, "smallest_cousine.csv")
