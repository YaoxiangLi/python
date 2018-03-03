import os
import re
from tqdm import tqdm
import pandas as pd

# Define I/O at the very beginning
# xlrd, openpyxl are required modules for this program
PATH = './'
INPUT = '09re_practice_data.xlsx'
OUTPUT = 'cleaned_data.xlsx'


def loadExcel(path, excel, sheet):
    """
    Load an excel file to a pandas dataframe
    path: the location of the excel file
    excel: the excel file name
    sheet: name of the spread sheet
    """
    os.chdir(path)
    print('\nThe current working directory is:', os.getcwd())
    return pd.read_excel(excel, sheet)


def saveExcel(path, excel, sheet, df):
    """
    Save a pandas dataframe to an excel
    package 'openpyxl' is required for this method
    path: the location of the excel file
    excel: the excel file name
    sheet: name of the spread sheet
    df: the name of the pandas dataframe
    """
    os.chdir(path)
    writer = pd.ExcelWriter(excel)
    df.to_excel(writer, sheet_name=sheet)
    writer.save()
    print('\nSuccessfully saved to excel!')


def main():
    # Loading the data
    data = loadExcel(PATH, INPUT, 'Sheet2')
    print('data:', data)

    # Selecting the column to be cleaned
    names = data['房产名称']
    print('strings:', names)

    # \地\下\室\负\夹 to Unicode \u5730\u4e0b\u5ba4\u8d1f\u5939
    # Created a regular expression instance that include all
    # Chinese characters without "\地\下\室\负\夹"
    pattern = re.compile(
        u'[\u4e00-\u4e0a\u4e0c-\u5729\u5731-\u5938\u5940-\u5ba3\u5ba5-\u8d1e\u8d20-\u9fa5]')

    # Initialized a empty pandas dataframe 'df' to hold the processed data
    # with column name 'A'
    df = pd.DataFrame(columns=['A'])

    # Start cleaning!
    print('\n Start cleaning Chinese characters by regular expression:')
    for name in tqdm(names):
        df.loc[name] = pattern.sub('', name)
    print('\n Remove the extra letter:')
    for name in tqdm(names):
        df['A'].loc[name] = df['A'].loc[name][1:]

    # Save to a excel file
    saveExcel(PATH, OUTPUT, 'Sheet1', df)


if __name__ == '__main__':
    main()
