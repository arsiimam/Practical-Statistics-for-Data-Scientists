import pandas as pd

#Make a function to calculate weighted Median
def weighted_median(Score, Weight):
   
   #Create a DataFrame
    df = pd.DataFrame({'Score': Score, 'Weight': Weight})
    df = df.sort_values('Score').reset_index(drop=True)
    

    df['cumulative_weight'] = df['Weight'].cumsum()
    total_weight = df['Weight'].sum()
    
    # Find the weighted median
    median_row = df[df['cumulative_weight'] >= total_weight / 2].iloc[0]
    
    return median_row['Score']

#Read the csv file
df = pd.read_csv('data.csv', delimiter=';')
median = weighted_median(df['Score'], df['Weight'])

print(median)