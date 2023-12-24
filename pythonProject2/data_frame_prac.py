import pandas as pd
import matplotlib.pyplot as plt


data = {
    'SSN': [123, 445, 551, 872],
    'Name': ['Anna', 'Bob', 'John', 'Mike'],
    'Age': [20, 43, 82, 23],
    'Height': [176, 165, 187, 192],
    'Gender': ['f', 'm', 'm', 'm']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)
# print(df.T) #transpose

# print(df['Name'].iloc[0:2]) #ILOC

# df.Age.hist()
# plt.show()

print(df.count() )