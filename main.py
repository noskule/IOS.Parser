from parse import Parse
import test

xyz999c001 = Parse("xyz999c001")
xyz999c002 = Parse("xyz999c002")

## # INPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Read from File  - - - - - - - - - - - - - - - - - - - - - - - -
dictlist = xyz999c001.csv_reader('Test/inventory_read.csv')
# print(dictlist) 

## KONSOLENBEFEHLE # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## show version (all parameters) - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open("Konsole/sh_ver.txt", "r+").read() )
xyz999c001.sh_ver(console_output[1])
# print("sh_ver_var: " + format(xyz999c001.sh_ver_var) )

## show interfaces status - - - - - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open("Konsole/sh_int_stat.txt", "r+").read() )
xyz999c001.sh_int_stat(console_output[1])
xyz999c002.sh_int_stat(console_output[1])
# print("sh_int_stat_var: " + format(xyz999c001.sh_int_stat_var) )

## show interface X - - - - - - - - - - - - - - - - - - - - - - - - 
console_output = xyz999c001.console_output( open("Konsole/sh_int_x.txt", "r+").read() )
xyz999c001.sh_int_x(console_output[1])


## GENERISCHE FUNKTIONEN # # # # # # # # # # # # # # # # # # # # # # # # # # 

## Parse List ( Bsp.: Inventory ) - - - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open( "Konsole/sh_inv.txt", "r+" ).read() )
xyz999c001.sh_inv = xyz999c001.text_list(console_output[1])

## Parse Table (Bsp.: Interface Status) - - - - - - - - - - - - - - - 
console_output = xyz999c001.console_output( open("Konsole/sh_int_stat.txt", "r+").read() )
xyz999c001.sh_int_stat_var = xyz999c001.text_table(console_output[1])

## Liste von Dict Values (Bsp.: Interfaces)
xyz999c001.int_stat_ports_var = xyz999c001.dictlist_values(xyz999c001.sh_int_stat_var, "Port")
#print(xyz999c001.int_stat_ports_var)


## OUTPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

## Write table to CSV-File - - - - - - - - - - - - - - - - - - - - -
#xyz999c001.csv_write_table('Test/console_data_list.csv', console_data_list)

## Write one Dictlist to CSV-File - - - - - - - - - - - - - - - - - - - -
xyz999c001.csv_write_dictlist('Test/devices_settings_2.csv', xyz999c001.sh_int_stat_var)

## Write a list of dictlists to CSV-File - - - - - - - - - - - - - - - - -
list_of_dictlists = [ xyz999c001.sh_int_stat_var, xyz999c002.sh_int_stat_var ]
# print(xyz999c001.sh_int_stat_var)
#print( xyz999c001.listlist_dict_keys( list_of_dictlists ) )
#print(xyz999c002.sh_int_stat_var)
print("---------------------")
print(test.list_of_dictlists)
print("---------------------")
print( xyz999c001.listlist_dict_keys( list_of_dictlists ) )


# print(list_of_dictlists)

## PRINT  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#print(list_of_dictlists)
# Druckt eine Liste von Dictionaries
# for element in list_of_dictlists:
#    for key, value in element.items():
#        print( f"Key  : {key} \nValue: {value}  \n" )

