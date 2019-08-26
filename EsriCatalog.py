
import os
import csv
import datetime


CSV_FNAME = 'EsriCatalog.csv'

# Test values
# mxd0 = 'C:\\Data\\stdv_viz.mxd'
# lyrs0 = {'C:\\TestPath\\Documents\\BRCS\\Data\\BRCS_GDB.gdb\\Union': 'Union', 'C:\\TestPath\\Documents\\BRCS\\NHD_H_Michigan_GDB.gdb\\WBD\\WBDHU10': 'WBDHU10'}
#
# mxd1 = 'C:\\Data\\Traces.mxd'
# lyrs1 = {'C:\\TestPath\\Documents\\BRCS\\StreamTraces.gdb\\BRCS_Downstream170515': 'BRCS_Downstream170515', 'C:\\TestPath\\Documents\\BRCS\\StreamTraces.gdb\\BRCS_Upstream170515': 'BRCS_Upstream170515'}
#
# mxd2 = 'C:\\Data\\MI_NHD.mxd'
# lyrs2 = {'C:\\Data\\NHD_H_Michigan_GDB.gdb\\Hydro_GeoRef\\Barrier_MI': 'Barrier_MI', 'C:\\Data\\NHD_H_Michigan_GDB.gdb\\Hydro_GeoRef\\NHDFlowline_3078': 'NHDFlowline_3078', 'C:\\Data\\NHD_H_Michigan_GDB.gdb\\Hydro_GeoRef\\Hydro_GeoRef_Net_Junctions': 'Hydro_GeoRef_Net_Junctions'}
#
# mxd3 = 'C:\\Data\\MapWithoutGDB.mxd'
# lyrs3 = {'C:\\TestPath\\Documents\\BRCS\\Map_Without_GDB\\No_GDB_Data\\No_GDB_Test_Data': 'No_GDB_Test_Data'}

# Create a function write_csv(mxd, lyrs)
def write_csv(mxd, lyrs):
    lyrs_lst = lyrs.keys()
    for k in lyrs_lst:
        gdb_path = gdb_parent(k)
        os.chdir(gdb_path)
        f_path = '{}\\{}'.format(gdb_path, CSV_FNAME)
        if os.path.exists(f_path):
            with open(CSV_FNAME, 'a') as csv_f:
                csv_f.write('{},{},{},{}\n'.format(mxd, lyrs[k], k, datetime.datetime.now()))
        else:
            with open(CSV_FNAME, 'w') as csv_f:
                csv_f.write('Map Document,Layer Name,Data Source,Date Accessed\n')
                csv_f.write('{},{},{},{}\n'.format(mxd, lyrs[k], k, datetime.datetime.now()))

# File Geodatabases appear as a directory but cannot be used in the same way.
# Find the parent directory for a gdb using:
def gdb_parent(path):
    gdbIdx = path.find('.gdb')
    if gdbIdx == -1:
        return os.path.dirname(path)
    else:
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
# write_csv(mxd0, lyrs0)
# write_csv(mxd1, lyrs1)
# write_csv(mxd2, lyrs2)
# write_csv(mxd3, lyrs3)

# print '{}\\{}'.format(gdb_parent('C:\\TestPath\\Documents\\BRCS\\StreamTraces.gdb\\BRCS_Downstream170515'), CSV_FNAME)
