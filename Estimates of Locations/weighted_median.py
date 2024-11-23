import pandas as pd
df = pd.read_csv('data.csv', delimiter=';')


#Make a function to calculate weighted Median
def weighted_median(Score, Weight):
    df = pd.read_csv('data.csv', delimiter=';')
    df = df.sort_values('Score').reset_index(drop=True)
    

    df['cumulative_weight'] = df['Weight'].cumsum()
    total_weight = df['Weight'].sum()
    
    # Find the weighted median
    median_row = df[df['cumulative_weight'] >= total_weight / 2].iloc[0]
    
    return median_row['Score']

median_row = weighted_median(df['Score'], df['Weight'])

print(median_row)