import pandas as pd

# Function to split an Excel file into multiple Excel files based on sheet names
def split_excel_file(file_path):
    # Load the Excel file
    xls = pd.ExcelFile("./INSUARANCE.xlsx")

    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name, header=0)

        # Drop empty rows
        df.dropna(how='all', inplace=True)

        # Check the first row for empty cells and drop corresponding columns
        df = df.dropna(axis=1, how='all')

        # Save the DataFrame to a new Excel file with the sheet's name
        output_file_name = f"{sheet_name}.xlsx"
        df.to_excel(output_file_name, index=False)
        print(f"Saved sheet {sheet_name} to {output_file_name}")

# Replace 'your_file.xlsx' with the path to your Excel file
split_excel_file('./INSURANCE.xlsx')