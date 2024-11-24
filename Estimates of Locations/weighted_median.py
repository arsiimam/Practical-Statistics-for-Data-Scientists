import pandas as pd

#Make a function to calculate weighted Median
def weighted_median(Score, Weight):
   
   #Create a DataFrame
    df = pd.DataFrame({'Score': Score, 'Weight': Weight})
    #Use mergesort to ensure more stable sorting
    df = df.sort_values('Score', kind='mergesort').reset_index(drop=True)

    
# Handle if DataFrame is empty
    if df.empty:
        raise ValueError("Input data is empty.")
    total_weight = df['Weight'].sum()
    if total_weight == 0:
        raise ValueError("Total weight is zero; cannot compute weighted median.")

#Calculate cumulative weight
    df['cumulative_weight'] = df['Weight'].cumsum()
    total_weight = df['Weight'].sum()
    
    # Find the weighted median
    median_row = df[df['cumulative_weight'] >= total_weight / 2].iloc[0]
    
    return median_row['Score']

#Read the csv file
try:
    df = pd.read_csv('data.csv', delimiter=';')
except FileNotFoundError:
    raise FileNotFoundError("The file 'data.csv' was not found.")
except pd.errors.ParserError:
    raise ValueError("Error parsing 'data.csv'. Check the delimiter and file format.")


median = weighted_median(df['Score'], df['Weight'])

print(median)