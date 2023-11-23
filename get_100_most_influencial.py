import pandas as pd
from pathlib import Path

dpath = Path(__file__).resolve().parent / "data"

DATA_ROWS = 2000

df = pd.read_csv( dpath / "patent_text_measures.txt" )

print(df.columns)

# largest_word = df.nlargest(DATA_ROWS, "new_word_reuse")
# largest_word.to_csv(dpath / "new_word_reuse.csv")

# largest_bigram = df.nlargest(DATA_ROWS, "new_bigram_reuse")
# largest_bigram.to_csv(dpath / "new_bigram_reuse.csv")

# largest_trigram = df.nlargest(DATA_ROWS, "new_trigram_reuse")
# largest_trigram.to_csv(dpath / "new_trigram_reuse.csv")

# largest_comb = df.nlargest(DATA_ROWS, "new_word_comb_reuse")
# largest_comb.to_csv(dpath / "new_word_comb_reuse.csv")

# backward_cosine = df.nlargest(DATA_ROWS, "backward_cosine")
# backward_cosine.to_csv(dpath / "backward_cosine.csv")

# forward_cosine = df.nlargest(DATA_ROWS, "forward_cosine")
# forward_cosine.to_csv(dpath / "forward_cosine.csv")

df["forward_div_backward_cousine"] = df["forward_cosine"].div(df["backward_cosine"].values)

forward_div_backward_cousine =  df.nlargest(DATA_ROWS, "forward_div_backward_cousine")
forward_div_backward_cousine = forward_div_backward_cousine.reindex(columns=[
    'patent', "forward_div_backward_cousine", 'forward_cosine', 'backward_cosine', 
    'new_word', 'new_word_reuse', 'new_bigram', 'new_bigram_reuse', 'new_trigram',
    'new_trigram_reuse', 'new_word_comb', 'new_word_comb_reuse',  
    ])

forward_div_backward_cousine.to_csv(dpath / "forward_div_backward_cousine.csv")