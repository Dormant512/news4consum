import pandas as pd
import sys
import os

date_args = [str(i) for i in sys.argv[1:]] #YYYY, MM, DD, YYYY, MM, DD
df = pd.DataFrame(data={'date': [], 'title': []})
list_news = ['fontanka', 'gazeta-spb', 'lenta', 'rbc', 'spb-mk']

for item in list_news:
    filename = f"./SCRAPED-DATA/{item}{'-'.join(date_args)}.csv"
    cur_df = pd.read_csv(filename, sep='\t', on_bad_lines='skip')
    df = pd.concat([df, cur_df], ignore_index=True)
    
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file '{filename}' does not exist.") 

df.sort_values(by=['date'], inplace=True, ignore_index=True)
write_name = f"./SCRAPED-DATA/NEWS-{'-'.join([str(i) for i in date_args])}.csv"
df.to_csv(write_name, sep='\t', index=False)
