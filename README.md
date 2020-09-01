# Todo
* teste csv_writer function da mit optionalem argument "fieldnames" erweitert
* def merge_lists_w_heads
* Liste aus Konsolenbefehl-Outputs in CSV speichern
* sh int status und sh int X als Liste zusammenführen

* ~~Konsolenbefehle als Funktionen und Variable einbinden~~


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
      * Port
    * counter
  * version
  * inventory
  * cdp
    * neighbors

## Parse-Klasse Aufbau
* Connect
  * SSH2
  * Serial
* Navigate IOS
  * User
    * Show
  * Privileged
  * Configuration
    * Interface 
* Data Input 
  * Read CSV File
* Parse
  * Konsolenbefehl 1
  * Konsolenbefehl 2
  * Kons...
* Process

* Data Output
  * Write CSV File

## Datenformat

{ Hostname : xxx999c001, Datum : YYYY-MM-DD-HH-MM, Befehl: "Show interface status", Output: [][][ {dict_1, dict_2}, {dict_1, dict_2}, {dict_1, dict_2} ] }


# Fragen

## Merge Dictionaries ?

Wie macht man das am besten .....