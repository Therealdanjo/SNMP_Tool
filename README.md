# SNMPTool 
This is a basic SNMPv2 tool to perform get/set operations
## Installation
* To use the console version of this tool (which is the only one who works at the time of writing this), make sure you have [pysnmp](https://github.com/etingof/pysnmp) installed. To use additional features, you also need to install [pysnmp-mibs](https://github.com/etingof/pysnmp-mibs) 
* After you did all of the above, just download all files in the *src* folder, execute *SNMPTool.py* and enjoy!
* To use the GUI version of this tool, you need to have PyQt5 installed on top of [pysnmp](https://github.com/etingof/pysnmp) and (optionally) [pysnmp-mibs](https://github.com/etingof/pysnmp-mibs). Then, download all files in the *src* folder and execute *SNMPToolGUI.py*

*For more detailed information about every command in the console-based version, type /help when you execute the program!*

#### Warning
For the execution of the program the *venv* folder is not necessary, but I pushed it anyways to have a copy of my virtual environment used py Pycharm

## Functionality
The console-based Tool has the following functionality:
* Get six basic pieces of information via the SNMPv2-MIB and print them to the console ('sysName', 'sysContact', 'sysLocation', 'sysDescr', 'sysUpTime', 'sysServices')
* Perform GET-operations on MIBs which are already precompiled (they are available [here](https://github.com/etingof/pysnmp-mibs)) 
 
   Warning: Some custom MIBs are currently not supported, but I am working on it 
* Perform SET-operations on the same MIBs as the ones supported on GET-requests, and, like GET-requests, it supports all communities

## The GUI
**Warning**: The GUI currently has no logic bound to it (see *Next Steps*)
![alt text](https://github.com/Therealdanjo/SNMP_Tool/blob/master/img/GUI20201217.jpg "GUI updated on 2020-12-17")

## Next Steps
* ~~Adding logic to the GUI (includes rewriting parts of some functions)~~
* Eventually make the GUI prettier (ex. add a logo, modern design)
* Expanding the help page, so that it has help for both the console and GUI-version of the program 
* Eventually scanning a network for available devices via SNMP 
* Eventually add the support for Traps or Informs
