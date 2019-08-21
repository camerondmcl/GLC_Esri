# The proposed function will have two inputs:
#   1) Map Document path
#   2) dictionary containing {dataSource: name} for each layer
#
# For each unique parent directory path, add or append to a file named 'EsriCatalog.csv'

import os
import csv
import datetime


CSV_FNAME = 'EsriCatalog.csv'

# Test values
mxd0 = 'C:\\Data\\stdv_viz.mxd'
lyrs0 = {'C:\\TestPath\\Documents\\BRCS\\Data\\BRCS_GDB.gdb\\Union': 'Union', 'C:\\TestPath\\Documents\\BRCS\\NHD_H_Michigan_GDB.gdb\\WBD\\WBDHU10': 'WBDHU10'}

mxd1 = 'C:\\Data\\Traces.mxd'
lyrs1 = {'C:\\TestPath\\Documents\\BRCS\\StreamTraces.gdb\\BRCS_Downstream170515': 'BRCS_Downstream170515', 'C:\\TestPath\\Documents\\BRCS\\StreamTraces.gdb\\BRCS_Upstream170515': 'BRCS_Upstream170515'}

mxd2 = 'C:\\Data\\MI_NHD.mxd'
lyrs2 = {'C:\\Data\\NHD_H_Michigan_GDB.gdb\\Hydro_GeoRef\\Barrier_MI': 'Barrier_MI', 'C:\\Data\\NHD_H_Michigan_GDB.gdb\\Hydro_GeoRef\\NHDFlowline_3078': 'NHDFlowline_3078', 'C:\\Data\\NHD_H_Michigan_GDB.gdb\\Hydro_GeoRef\\Hydro_GeoRef_Net_Junctions': 'Hydro_GeoRef_Net_Junctions'}

# Create a function write_csv(mxd, lyrs)
def write_csv(mxd, lyrs):
    lyrs_lst = lyrs.keys()
    with open(CSV_FNAME, 'a+') as csv_f:
        try:
            #runs if the CSV already existed (and therefore already has the header)
            csv.reader(csv_f).next()
            for k in lyrs_lst:
                csv_f.write('{},{},{},{}\n'.format(mxd, lyrs[k], k, datetime.datetime.now()))
        except StopIteration:
            #runs if the CSV was just created and doesn't have the header yet)
            csv_f.write('Map Document,Layer Name,Data Source,Date Accessed\n')
            for k in lyrs_lst:
                csv_f.write('{},{},{},{}\n'.format(mxd, lyrs[k], k, datetime.datetime.now()))

# File Geodatabases appear as a directory but cannot be used in the same way.
# Find the parent directory for a gdb using:
def gdb_parent(path):
    gdbIdx = path.find('.gdb')
    gdbPartial = path[:gdbIdx]
    return os.path.dirname(gdbPartial)

# Format the EsriCatalog.csv using the following fields:
#   Map Document, Layer Name, Data Source, Date Accessed
#
#   Map Document - Full path of the .mxd file
#   Layer Name - Layer name from the dictionary input
#   Data Source - Full path of the dataset from the dictionary input
#   Date Accessed - timestamp (now)

#testing write_csv
write_csv(mxd0, lyrs0)
write_csv(mxd1, lyrs1)
write_csv(mxd2, lyrs2)
