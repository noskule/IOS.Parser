from parse import Parse

xyz999c001 = Parse("xyz999c001")
console_data_list = []

## # INPUT # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Read from File  - - - - - - - - - - - - - - - - - - - - - - - -
dictlist = xyz999c001.csv_reader('Test/inventory_read.csv')
# print(dictlist) 
# console_data_list.append( dictlist )

## GENERISCHE FUNKTIONEN # # # # # # # # # # # # # # # # # # # #

## Parse List ( Inventory ) - - - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open( "Konsole/sh_inv.txt", "r+" ).read().strip() )
console_prompt = console_output[0]
console_data = console_output[1]
#console_data_list.append( xyz999c001.text_list(console_data) )
xyz999c001.sh_inv = xyz999c001.text_list(console_data)
print(xyz999c001.sh_inv)


## Parse Table (interface status) - - - - - - - - - - - - - - - 
console_output = xyz999c001.console_output( open("Konsole/sh_int_stat.txt", "r+").read().strip() )
console_prompt = console_output[0]
console_data = console_output[1]
# console_data_list.append( xyz999c001.text_table(console_data) )


## SPEZIFISCHE FUNKTIIONEN # # # # # # # # # # # # # # # # # # # #

## show version (all parameters) - - - - - - - - - - - - - - - - -
console_output = xyz999c001.console_output( open("Konsole/sh_ver.txt", "r+").read().strip() )
console_prompt = console_output[0]
console_data = console_output[1]
# console_data_list.append( xyz999c001.sh_ver(console_data) )

## show interface X - - - - - - - - - - - - - - - - - - - - - - - - 
string = open("Konsole/sh_int_x.txt", "r+").read()
console_output = xyz999c001.console_output(string)
console_prompt = console_output[0]
console_data = console_output[1]
# console_data_list.append( xyz999c001.sh_int_x(console_data) )


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
# merged_lists = xyz999c001.merge_lists(console_data_list)

# print(merged_lists)
# xyz999c001.csv_write_dictlist('Test/devices_settings_9.csv', merged_lists)
