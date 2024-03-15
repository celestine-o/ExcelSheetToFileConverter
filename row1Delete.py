import os
import pandas as pd

# Set the folder path where your Excel files are located
folder_path = './files'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):  # Check if the file is an Excel file
        file_path = os.path.join(folder_path, filename)
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, header=None)
        # Print the DataFrame to see the data
        print(f'Data from {filename} before modification:')
        print(df)
        
        # Check if the DataFrame has more than one row
        if len(df.index) > 1:
        # Check if the first row contains 'Unnamed' or NaN and set new headers if true
            if df.iloc[0, 0] == 'Unnamed: 0' or pd.isnull(df.iloc[0, 0]):
                new_header = df.iloc[1]  # Take the second row for the header
                
                df = df[2:]  # Take the data less the header row
                df.columns = new_header  # Set the new header
                
                df.reset_index(drop=True, inplace=True)  # Reset the index to start with 0
                print(df)
            else:
                print(f'File {filename} does not have enough rows to set a new header.')
                continue  # Skip to the next file

        
        # Save the DataFrame back to Excel, overwriting the original file
        df.to_excel(file_path, index=False)
        
        print('First row deleted from all Excel files in the folder.')