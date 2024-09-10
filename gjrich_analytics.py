
# standard library imports
import csv
import json
import pathlib
from collections import Counter


# external library imports (req venv)
import requests
import pandas as pd


import gjrich_projsetup
import gjrich_utils

# local module imports

'''Objective
Create a Python module that demonstrates skills in fetching data from the web, 
processing it using Python collections, and writing the processed data to different file formats.'''

'''Use try/except/finally and implement exception handling to catch known possible errors and handle them gracefully in at least one of your functions.
'''


Python function with exception handling code example:

def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = pathlib.Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")




'''4. Data Acquisition

Use the requests library to fetch data from specified web APIs or online data sources. This will include JSON, CSV, and plain text data. After a successful fetch, call the appropriate write function to save the data to a file.

Python fetch functions code examples: '''


def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")



'''5. Write Data

Write functions to save content to different file types (e.g., text, CSV, JSON).

Python write functions code examples:'''

def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Excel data saved to {file_path}")



'''6. Process Data and Generate Output

Write functions to read, process, and write results using appropriate Python collections (lists, sets, dictionaries, etc.). 
Demonstrate understanding of each collection data type's characteristics and usage.

Process the fetched data using appropriate Python collections and generate insightful analytics. 
The results of the processing should be formatted and written into text files.'''

'''Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working with text files. 
Analyze text data to generate statistics like 
word count, 
frequency of words, etc., and 
format these findings into a readable text file.'''



'''Function 2. Process CSV Data: Process CSV files with tuples to demonstrate proficiency in working with tabular data. 
Extract and analyze data from CSV files to produce meaningful statistics, summaries, or insights, and save the insights as text files.'''




'''Function 3. Process Excel Data: Extract and analyze data from Excel files 
to produce meaningful statistics, summaries, or insights, and save the insights as text files.'''




'''Function 4. Process JSON Data: Process JSON data with dictionaries to demonstrate proficiency in working with labeled data. 
Parse the JSON data to extract relevant information and present it in a simplified, human-readable text format.'''





''' Main function to demonstrate module capabilities. '''

def main():

    print(f"Name: {yourname_attr.my_name_string}")
    
    # Data Source URLs
    txt_url:str = https://www.gutenberg.org/cache/epub/131/pg131.txt
    csv_url:str = https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2022/Download-data/business-operations-survey-2022-business-finance.csv
    excel_url:str = https://files-faostat.fao.org/production/FS/Descriptions_and_Metadata.xlsx
    json_url:str = https://raw.githubusercontent.com/mledoze/countries/master/countries.json

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')






# conditional script execution
# main function only executes when the script is run directly
# not when imported as a module


if __name__ == '__main__':
    main()