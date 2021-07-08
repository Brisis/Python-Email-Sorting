import re
import pandas as pd

#read emails csv
data = pd.read_csv('unsorted_emails.csv')

#get first column of data only
df = data.iloc[:,0]

#flatten column to get list of emails
#Url list initialization
Input = df.values.flatten()
#Python code to sort the URL in the list based on the top-level domain.

#Function to sort in tld order
def tld(Input):
	return Input.split('@')[-1]

#Using sorted and calling function
Output = sorted(Input,key=tld)

# save to a new csv file
pd.DataFrame(Output).to_csv("sorted_emails.csv", header=None, index=None)

#Printing output
print("sorted email list")
print(Output)
