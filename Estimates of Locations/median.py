import pandas as pd

#Impport dataset from data.csv using pandas DafaFrame

df = pd.read_csv('data.csv',delimiter=";")

#Median Using pandas .median() functions
#Pandas doesn't short the data before calculate the median, its identify the middle value based on underlying data. It makes the algorithm more efficient
median_score = df['Score'].median()
print("Media sing .median() Function: ", median_score)

#Median manual calculation
#1. Define the function
def calculate_median(data):
    #1. Sort the data
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    #2. Find the middle Value.
    # If the length of data is odd, pick yhe middle element directly
    if n % 2 == 1:
        median = sorted_data[n //2] 
        
    #Ifthe length of data is even, calculate the average of the two middle element
    else:
        middle1 = sorted_data[n // 2 -1]
        middle2 = sorted_data[n // 2]
        median = (middle1 + middle2)/2
     
    return median

#Print the result
median = calculate_median(df['Score'])
print("Median using manual formula: ",median)

#Apply The Subject filter
filtered_median = calculate_median(df[df['Subject'] == 'Math']['Score'])
print("Median using filtered subject Math: ",filtered_median)

#Dynamics Filter
filter_category = 'English' #You can change this input into any value inside Subject Category

dynamic_Filter_median = calculate_median(df[df['Subject'] == filter_category]['Score'])
print("Median of the subject ",filter_category, "is: ", dynamic_Filter_median) 