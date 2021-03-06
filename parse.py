import csv, IOS_Param



## GENERISCHE FUNKTIONEN # # # # # # # # # # # # # # # # # # # # # # # # # # 

def text_list(inventory_string):
    '''Parst eine Textliste wie "show inventory" und erstellt eine Liste mit Dictionaries.'''
    inventory_string = inventory_string.replace('\"', '')
    inventory_list = inventory_string.split("\n\n\n")                  # Listelemente generieren (Modulliste) """
    for modul in inventory_list:
        dictlist = []
        for modul in inventory_list :
            modul = modul.replace("\n", ',')                           # Neue Zeile in Komma umwandeln """
            modul = [element.strip() for element in modul.split(',')]  # Listelemente genereieren (Modulelement) """
            modul_dict = {}                                            # Module String in Dictionary """
            for element in modul :
                element.strip()
                element = [element.strip() for element in element.split(':')]
                modul_dict[element[0]] = element[1]
            dictlist.append(modul_dict)
    return dictlist

def text_table(console_data):
    ''' Parst Textlisten wie "show interfaces status" und erstellt eine Liste aus Dictionaries.'''
    
    ## Tabellenkopf und Tabellendaten trennen
    splitstring = console_data.split('\n',1 )
    tablehead = splitstring[0]
    tabledata = splitstring[1]

    ## Wandelt String in Dict um { Zeichenindex : Name, ... }
    col_dict = text_table_colhead ( tablehead )
    # print ( "coldict: " + format ( col_dict ) )
    
    ## Wandelt Zeilen in Liste um
    rowlist = tabledata.split ('\n')

    ## Wandelt String jeder Zeile in Dict um
    table_data = text_table_data ( col_dict, rowlist )
    # print ( "table_data:\n" + format ( table_data ) )
    return table_data

def text_table_colhead(colhead):
    '''Wandelt den Tabellenkopf in Dict um { Zeichenindex : Name, ... } '''
    stringindex = 0
    chartype = "space"
    col_dict = {}
    col_index_next = 0
    col_name_next = "space"
    for char in colhead:
        if char.isspace() == False:    # it's a char
            if chartype == "space":        # wecchsel von space nach char, neuer Spaltenname
                col_index_next = stringindex
                col_name_next = ""
            col_name_next = col_name_next + char
            chartype = "char"
        else:                           # itf's a space 
            if chartype == "char":          # wechsel von char nach space, ende Spaltenname
                col_dict[col_index_next] = col_name_next

            chartype = "space"         
        stringindex += 1
    return col_dict        

def text_table_data(coldict, stringlist):
    ''' Wandelt String jeder Daten-Zeile in Liste'''
    col_index = list ( coldict.keys() )
    iteration = 0
    for index in col_index:       
        if index != 0:
            col_index[iteration] = index - 1
        iteration += 1
    col_head = list ( coldict.values() )
    table_row_max_lenght = len( max(stringlist , key = len) )
    col_index.append(table_row_max_lenght)
    rowlist =[]
    for row in stringlist:
        coldict = {}
        for i in range( len(col_index)-1 ) :
            element = row[ col_index[i] : col_index[i+1] ]
            coldict[col_head[i]] = element.strip()
        rowlist.append(coldict) 
    return rowlist


## CSV  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def csv_reader(file):
    '''Reads a CSV-File and returns a dictionary list'''
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        table = []
        for row in csv_reader:
            if row_count == 0:
                keys = row
                row_count += 1
            else:
                dictlist = {}
                element_count = 0
                for element in row:
                    dictlist[keys[element_count]] = element
                    element_count += 1 
                table.append(dictlist)
                row_count += 1                                
        return table

def csv_write_table(file, table):
    '''Writes a List of Lists to a CSV-File the first list being the fieldnames'''
    with open(file, mode='w') as csv_file:
        fieldnames = table[0]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        #print("fieldnames: " + format(fieldnames) )
        for row in table:
            #print("row: " + format(row) )
            writer.writerow(row)

def csv_write_dictlist(  file, dictlist, fieldnames="" ):
    '''Writes a list of dictionary to a csv file.'''
    if fieldnames  == "":
        fieldnames = {k for d in dictlist for k in d.keys()}
    with open(file, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writeheader()
        for row in dictlist:
            writer.writerow(row)


## TOOLS # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def console_output(data):
    """ Returns a list ( two elements ) with the console prompt and console output """
    data = data.split('\n', 1)
    data[0] = data[0].strip() 
    data[1] = data[1].strip()
    return data

def merge_dict_list(list_of_dicts):
    '''Merges a list of dictionaries '''
    new_dict = {k:v for list_item in list_of_dicts for (k,v) in list_item.items()}
    return new_dict

def merge_dict_lists(lists_of_dictlists ):
    '''Merges lists of dictlist to one list of dicts '''
    '''
    * pop first element of each list and extract the keys
    * merge the lists into a new list
    * add the keys to the first element in the new list
    * return the list 
    '''
    pass


def merge_lists(lists_of_lists):
    '''Fasst eine Liste aus Listen zu einer Liste zusammen'''
    merged_lists = []
    for li in lists_of_lists:
        merged_lists += li
    return merged_lists

def key_value_name(text, parameterlist) :
    '''Searches Lines for parameters and splits key and value when no seperator is used'''
    parameter_dict = {}
    linelist = text.split('\n')
    for line in linelist :
        for parameter in parameterlist :
            if parameter in line :
                line = line.split( parameter, 1 )
                parameter_dict[parameter.replace(":","").strip()] = line[1].strip()
    return parameter_dict

def key_value_name_first(text, parameterlist) :
    '''Searches Lines for parameters and splits key and value when key is first and value is second in line and writes a dictionary'''
    parameter_dict = {}
    linelist = [line.strip() for line in text.split('\n')]
    for parameter in parameterlist :
        i = 0
        while i <= len(linelist)-1 :
            if parameter in linelist[i] :
                line = linelist.pop(i)
                value = line.replace(parameter, "").strip()
                parameter_dict[parameter] = value
            i += 1
    return parameter_dict

def key_value_doppelpunkt(text, parameterlist) :
    '''Searches Lines for parameters and splits key and value when key is first and separator is ":" '''
    parameter_dict = {}
    for line in text.split('\n') :
        for parameter in parameterlist :
            if parameter in line :
                parameter_dict[parameter.strip()] = line.split(":", 1 )[1].strip()
    return parameter_dict

def list_dict_keys(dictlist):
    '''Returns a list of dictionary keys from a list of dictionaries.'''
    return list({k for d in dictlist for k in d.keys()})

def listlist_dict_keys(list_of_dictlists):
    '''Returns a list of dictionary keys from a list of a list of dictionaries.'''
    keys = []
    merged_lists = []
    for dictlist in list_of_dictlists:
        merged_lists = merged_lists + dictlist 
    keys = keys + list({k for d in merged_lists for k in d.keys()})
    return keys    

def dictlist_values(dictlist, key):
    '''From a dictlist returns a list of values of a given key'''
    valuelist = []
    for dict in dictlist:
        valuelist.append(dict[key])
    return valuelist

