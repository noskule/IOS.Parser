# Todo

* Konsolenbefehle / Output als Objekte einbinden

## Bugs

* ~~parse.text_table() trennt Spalten nicht immer richtig~~


# Datenstruktur

## Cisco IOS Befehls-Hirarchie 

* User EXEC Commands
* Privileged EXEC Commands
  * Global Configuration Commands
    * Interface Commands
    * Routing Engine Commands
    * Line Commands 

## Befehle fürs Parsing
* show
    * interface
        * status
        * counter
    * version
    * inventory

## Aufbau

* Connect
  * SSH2
  * Serial
* Navigate IOS
  * User
    * Shows
  * Privileged
  * Configuration
    * Interface 
* Data Input 
  * Read CSV File
* Parse
  * Text Table
  * Text List
  * Special Commands
* Process

* Data Output
  * Write CSV File

## Datenformat

{ Hostname : xxx999c001, Datum : YYYY-MM-DD-HH-MM, Befehl: "Show interface status", Output: [][][ {dict_1, dict_2}, {dict_1, dict_2}, {dict_1, dict_2} ] }

### Hostname:

Hostname, erreichbar übers Netz.

### Befehl:

* user
  * show
    * ...  
* en
  * int
  * rout
  * line

### Output:



# Fragen

## Merge Dictionaries ?

Wie macht man das am besten .....