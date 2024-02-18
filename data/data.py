import os
import pandas as pd

# # Set the path to the folder containing your CSV files
# folder_path = './'

# # Get a list of all CSV files in the folder
# csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# # Initialize an empty DataFrame to store the combined data
# combined_data = pd.DataFrame()

# # Loop through each CSV file and append its data to the combined DataFrame
# for csv_file in csv_files:
#     file_path = os.path.join(folder_path, csv_file)
#     data = pd.read_csv(file_path)
#     combined_data = pd.concat([combined_data, data], ignore_index=True)


import pandas as pd

# # Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Define the rules for updating the "Target Starting pos" column
# def update_target_starting_pos(value):
#     if value in [400, 700]:
#         return 150
#     elif value in [800, 300]:
#         return 250
#     elif value in [900, 200]:
#         return 350
#     elif value in [1000, 100]:
#         return 450
#     else:
#         return value

# # Apply the rules to the "Target Starting pos" column
# df['Target Starting x Position (px)'] = df['Target Starting x Position (px)'].apply(update_target_starting_pos)

# # Save the updated DataFrame back to the Excel file
# df.to_excel(excel_file_path, index=False)

# print("Update completed successfully.")

# Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Define the sizes
# sizes = [80, 120, 160, 200]

# # Calculate the mean time of completion for each size
# for size in sizes:
#     mask = df['Target Size (px)'] == size
#     mean_time = df.loc[mask, 'Time (ms)'].mean()
#     df.loc[mask, 'MT'] = mean_time

# # Save the updated DataFrame back to the Excel file
# df.to_excel(excel_file_path, index=False)

# print("Update completed successfully.")


# # Calculate the standard deviation for the 'Time of Completion' column
# std_deviation = df['Time (ms)'].std()

# # Add a new column 'STD' for standard deviation
# df['STD'] = std_deviation

# # Calculate the number of standard deviations each row is from the mean
# df['Num of STDs'] = (df['Time (ms)'] - df['MT']) / std_deviation

# # Filter out rows where the number of standard deviations is above 3
# df_filtered = df[df['Num of STDs'].abs() <= 3]

# # Save the filtered DataFrame back to the Excel file
# df_filtered.to_excel(excel_file_path, index=False)

# # Print the standard deviation to the console
# print("Standard Deviation:", std_deviation)

# # Print the standard deviation to the console
# print("Standard Deviation:", std_deviation)

# print("Update completed successfully.")

# import pandas as pd
# import numpy as np
# import math

# # Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Define the calculation for the 'ID' column
# def calculate_id(row):
#     target_starting_pos = row['Target Starting x Position (px)']
#     target_size = row['Target Size (px)']

#     # Avoid division by zero by adding 1 to the denominator
#     expression = target_starting_pos / (target_size + 1)

#     # Calculate the logarithm of log(base2)
#     id_value = math.ceil(np.log2(expression)) + 1
    
#     return id_value

# # Add a new column 'ID' to the DataFrame
# df['ID'] = df.apply(calculate_id, axis=1)

# # Save the updated DataFrame back to the Excel file
# df.to_excel(excel_file_path, index=False)

# print("Update completed successfully.")
# import pandas as pd
# import numpy as np
# import math

# # Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)


# # Calculate the 'IP' column
# df['IP'] = df['ID'] / (df['MT'] / 1000)

# # Save the updated DataFrame back to the Excel file
# df.to_excel(excel_file_path, index=False)

# print("Update completed successfully.")

# import pandas as pd
# import matplotlib.pyplot as plt

# # Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Create a scatter plot with 'ID' on the X-axis and 'MT' on the Y-axis
# plt.scatter(df['ID'], df['MT'])

# # Add labels and title
# plt.xlabel('ID')
# plt.ylabel('MT')
# plt.title('Scatter Plot of ID vs MT')

# # Show the plot
# plt.show()
# import pandas as pd

# # Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Display unique values and their counts for 'MT'
# mt_counts = df['MT'].value_counts()
# print(mt_counts)

# import pandas as pd

# # Specify the path for the combined Excel file
# excel_file_path = 'file.xlsx'

# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Calculate the mean time of completion for each separate configuration
# mean_times = df.groupby(['Target Starting x Position (px)', 'Target Size (px)'])['Time (ms)'].transform('mean')

# # Add a new column 'MT' with the corresponding mean times
# df['MT'] = mean_times

# # Save the updated DataFrame to the original Excel file
# df.to_excel(excel_file_path, index=False)

# print("Mean times added as a new column 'MT' for each row and saved to the original Excel file.")

# # Display the unique mean times
# unique_mean_times = mean_times.unique()
# print("Unique mean times for each configuration:")
# print(unique_mean_times)

#
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Specify the path for the combined Excel file
excel_file_path = 'file.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Calculate the mean time of completion for each separate configuration
mean_times = df.groupby(['Target Starting x Position (px)', 'Target Size (px)'])['Time (ms)'].transform('mean')

# Add a new column 'MT' with the corresponding mean times
df['MT'] = mean_times

# Create a scatter plot with 'ID' on the X-axis and 'MT' on the Y-axis
sns.scatterplot(x='ID', y='MT', data=df)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(df['ID'], df['MT'])

# Plot the linear regression line
sns.lineplot(x=df['ID'], y=slope * df['ID'] + intercept, color='red')

# Display the equation and R-squared value on the plot
equation = f'y = {slope:.4f}x + {intercept:.4f}'
r_squared = f'R-squared: {r_value**2:.4f}'
plt.text(0.5, 0.9, equation, fontsize=10, transform=plt.gca().transAxes)
plt.text(0.5, 0.85, r_squared, fontsize=10, transform=plt.gca().transAxes)

# Show the plot
plt.show()

