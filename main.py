from Host import Host
import parse
import test

xyz999c001 = Host("xyz999c001")
xyz999c002 = Host("xyz999c002")

## # INPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Read from File  - - - - - - - - - - - - - - - - - - - - - - - -
dictlist = parse.csv_reader('Test/inventory_read.csv')
# print(dictlist) 

## KONSOLENBEFEHLE # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## show version (all parameters) - - - - - - - - - - - - - - - - -
console_output = parse.console_output( open("Konsole/sh_ver.txt", "r+").read() )
xyz999c001.sh_ver(console_output[1])
# print("sh_ver_var: " + format(xyz999c001.sh_ver_var) )

## show interfaces status - - - - - - - - - - - - - - - - - - - - -
console_output = parse.console_output( open("Konsole/sh_int_stat.txt", "r+").read() )
xyz999c001.sh_int_stat(console_output[1])
xyz999c002.sh_int_stat(console_output[1])
# print("sh_int_stat_var: " + format(xyz999c001.sh_int_stat_var) )
# print("sh_int_stat_var: " + format(xyz999c002.sh_int_stat_var) )

## show interface X - - - - - - - - - - - - - - - - - - - - - - - - 
console_output = parse.console_output( open("Konsole/sh_int_x.txt", "r+").read() )
xyz999c001.sh_int_x(console_output[1])


## GENERISCHE FUNKTIONEN # # # # # # # # # # # # # # # # # # # # # # # # # # 

## Parse List ( Bsp.: Inventory ) - - - - - - - - - - - - - - - - - - -
console_output = parse.console_output( open( "Konsole/sh_inv.txt", "r+" ).read() )
xyz999c001.sh_inv = parse.text_list(console_output[1])

## Parse Table (Bsp.: Interface Status) - - - - - - - - - - - - - - - 
console_output = parse.console_output( open("Konsole/sh_int_stat.txt", "r+").read() )
xyz999c001.sh_int_stat_var = parse.text_table(console_output[1])

## Liste von Dict Values (Bsp.: Interfaces)
xyz999c001.int_stat_ports_var = parse.dictlist_values(xyz999c001.sh_int_stat_var, "Port")
#print(xyz999c001.int_stat_ports_var)


## OUTPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

## Write table to CSV-File - - - - - - - - - - - - - - - - - - - - -
#parse.csv_write_table('Test/console_data_list.csv', console_data_list)

## Write one Dictlist to CSV-File - - - - - - - - - - - - - - - - - - - -
parse.csv_write_dictlist('Test/devices_settings_2.csv', xyz999c001.sh_int_stat_var)

## Write a list of dictlists to CSV-File - - - - - - - - - - - - - - - - -
list_of_dictlists = [ xyz999c001.sh_int_stat_var, xyz999c002.sh_int_stat_var ]
list_of_dictlists_merged = parse.merge_lists(list_of_dictlists)
list_of_dictlists_keys = parse.listlist_dict_keys( list_of_dictlists )
parse.csv_write_dictlist('Test/list_of_dictlists_5.csv', list_of_dictlists_merged, list_of_dictlists_keys)

# print(list_of_dictlists)

## PRINT  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#print(list_of_dictlists)
# Druckt eine Liste von Dictionaries
# for element in list_of_dictlists:
#    for key, value in element.items():
#        print( f"Key  : {key} \nValue: {value}  \n" )

