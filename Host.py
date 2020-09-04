import csv
import parse, IOS_Param

class Host:
    '''Ein Parser für CISCO IOS Konsolen Output'''

    def __init__(self, hostname='XXX###c###' ):
        """Initialize name and age attributes."""
        self.hostname = hostname
        self.sh_ver_var = ""
        self.sh_int_stat_var = ""
        self.int_stat_ports_var = ""


    ## KONSOLENBEFEHLE # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def sh_ver(self, text):
        '''Returns a dictionary List of parameters from the "show version" command '''
        parameter_dictlist = []
        parameter_dict_name = parse.key_value_name( text, IOS_Param.sh_ver_sep_text )
        parameter_dictlist.append(parameter_dict_name)
        parameter_dict_dopp = parse.key_value_doppelpunkt( text, IOS_Param.sh_ver_sep_dopp )
        parameter_dictlist.append(parameter_dict_dopp)
        parameter_dict_version = self.sh_ver_version(text)
        parameter_dictlist.append(parameter_dict_version)
        parameters = parse.merge_dict_list(parameter_dictlist)
        self.sh_ver_var = parameters

    def sh_int_stat(self,console_data):
        '''Returns a dictionary List of parameters from the show interface status command'''
        table_data = parse.text_table(console_data)
        self.sh_int_stat_var = table_data


    ## KONSOLENBEFEHLE - HILFSFUNKTIONEN # # # # # # # # # # # # # # # # # # #

    def sh_ver_version(self, text):
        ''' Returns the version of the IOS installation'''
        parameter_dict = {}
        keys = ["Version ", "RELEASE SOFTWARE "]
        for line in text.split('\n'):
            if "Cisco IOS Software, " in line:
                parameterlist = line.split(',')
                for element in parameterlist:
                    for key in keys:
                        if key in element:
                            parameter_dict[key.strip()] = element.replace(key, "").strip()
        return parameter_dict

    def sh_int_x(self, text):
        '''Gibt ein Dict mit allen interface Parametern zurück'''
        parameterstring = text.split('\n', 1)[1].replace(',', '\n').replace(';', '\n')
        parameter_dict = parse.key_value_name_first( parameterstring, IOS_Param.sh_int_x_text )
        return parameter_dict


