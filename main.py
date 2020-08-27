from parse import Parse

xyz999c001 = Parse("xyz999c001")
console_data_list = []

## # INPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Read from File  - - - - - - - - - - - - - - - - - - - - - - - -
dictlist = xyz999c001.csv_reader('Test/inventory_read.csv')
# print(dictlist) 
# console_data_list.append( dictlist )

## GENERISCHE FUNKTIONEN # # # # # # # # # # # # # # # # # # # #

## Parse List ( Bsp.: Inventory ) - - - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open( "Konsole/sh_inv.txt", "r+" ).read() )
xyz999c001.sh_inv = xyz999c001.text_list(console_output[1])

## Parse Table (Bsp.: Interface Status) - - - - - - - - - - - - - - - 
console_output = xyz999c001.console_output( open("Konsole/sh_int_stat.txt", "r+").read() )
xyz999c001.sh_int_stat_var = xyz999c001.text_table(console_output[1])

## Liste von Dict Values (Bsp.: Interfaces)
print(xyz999c001.sh_int_stat)
# xyz999c001.sh_int_stat_ports = xyz999c001.dictlist_values(xyz999c001.sh_int_stat, "Port")
# print(xyz999c001.sh_int_stat_ports)

## SPEZIFISCHE FUNKTIIONEN # # # # # # # # # # # # # # # # # # # #

## show version (all parameters) - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open("Konsole/sh_ver.txt", "r+").read() )
xyz999c001.sh_ver(console_output[1])
print("sh_ver_var: " + format(xyz999c001.sh_ver_var) )

## show interface X - - - - - - - - - - - - - - - - - - - - - - - - 
console_output = xyz999c001.console_output( open("Konsole/sh_int_x.txt", "r+").read() )
xyz999c001.sh_int_x(console_output[1])

## show interfaces status - - - - - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open("Konsole/sh_int_stat.txt", "r+").read() )
xyz999c001.sh_int_stat(console_output[1])
print("sh_int_stat_var: " + format(xyz999c001.sh_int_stat_var) )


## OUTPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

## PRINT  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#print(console_data_list)
# Druckt eine Liste von Dictionaries
#for console_data in console_data_list:
#    for key, value in console_data.items():
#        print( f"Key  : {key} \nValue: {value}  \n" )



## Write table to CSV-File - - - - - - - - - - - - - - - - - - - - -
#xyz999c001.csv_write_table('Test/console_data_list.csv', console_data_list)


## Write Dictlist to CSV-File - - - - - - - - - - - - - - - - - - - -
xyz999c001.csv_write_dictlist('Test/devices_settings_9.csv', xyz999c001.sh_int_stat_var)

