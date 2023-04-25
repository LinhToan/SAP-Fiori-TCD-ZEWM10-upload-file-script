import pandas as pd
from datetime import datetime

lot_history = pd.read_csv(r'C:\Users\l619072\Downloads\2HQI\2HQI Inventory Report - Copy.csv')
# lot_history = lot_history.fillna(0)
lot_history.head()

current_date = datetime.now().strftime('%m/%d/%Y')
current_time = datetime.now().time().strftime("%H:%M %p")

recon_list = [] # It's easier to build up a list and then create the dataframe
counter = 0 # Index for recon_list because we only want to increment recon_list's index if we reach a new batch number.

for index,row in lot_history.iterrows():
    if len(recon_list) == 0: # If test is empty, then initialize the process
        recon_list.append([current_date, current_time, '2HQI', lot_history['Item Code'][index], '(blank)', lot_history['P I D'][index], 'F', '(blank)', lot_history['OH_QTY'][index], 'CV', lot_history['ON_WGT_N'][index], 'A100'])
        continue
    if row[1] == recon_list[counter][5] and row[0] == recon_list[counter][3]: # If row's batch number matches recon_list's current batch number.
        recon_list[counter][8] += row[2] # sum CV
        recon_list[counter][10] += row[3] # sum LB
    else: # If we hit a new batch, then increment recon_list's index and create new row for new batch.
        counter += 1
        recon_list.append([current_date, current_time, '2HQI', lot_history['Item Code'][index], '(blank)', lot_history['P I D'][index], 'F', '(blank)', lot_history['OH_QTY'][index], 'CV', lot_history['ON_WGT_N'][index], 'A100'])
        
df = pd.DataFrame(recon_list, columns = ['Snapshot Date', 'Snapshot Time', 'Plant ID', 'Product Code', 'Product Description', 'Batch Number', 'Stock Type', 'Pallet ID', 'Available Qty.', 'UOM', 'Weight(Mandatory)', 'Stor.Loc'])

# Export dataframe as excel
file_name = '2HQI ZEWM10 upload.xlsx'
df.to_excel(file_name, index=False)
print('DataFrame is successfully exported as an excel file!')