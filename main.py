import pandas as pd
import os
from zipfile import ZipFile


# Code
def combineData(inputZipFilePath):
   dirname = os.path.dirname(inputZipFilePath)
   outputCsvFilePath = os.path.join(dirname, 'Combined')
   df_combined = pd.DataFrame()

   with ZipFile(inputZipFilePath, 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall()
       listOfFileNames = zipObj.namelist()
       result = list(filter(lambda x: (x.find("Combined") > -1), listOfFileNames))
       df_combined["Source IP"] = None
       df_combined["Environment"] = None
       if len(result) > 0:
           df_combined = pd.read_csv(result[0])
           outputCsvFilePath = result[0]

       for fileName in listOfFileNames:
           if fileName.endswith('.csv'):
               if fileName.find("Combined") == -1:
                   df_others = pd.read_csv(fileName);
                   df_temp = pd.DataFrame()
                   df_temp['Source IP'] = df_others['Source IP']
                   df_temp['Environment'] = os.path.basename(fileName)[:-4]
                   # append to df_combined
                   df_combined = df_combined.append(df_temp, ignore_index=True)

       df_combined['Environment'] = df_combined['Environment'].apply(
           lambda x: 'Asia Prod' if (x.find("Asia Prod") > -1) else x)
       df_combined = df_combined.drop_duplicates()
       df_combined = df_combined.sort_values("Source IP")

   # Writing the final output to Combined.csv
   # print(df_combined)
   df_combined.to_csv(outputCsvFilePath, index=False)
   # ouput written to combined.csv file
   # print(outputCsvFilePath)
   return outputCsvFilePath
