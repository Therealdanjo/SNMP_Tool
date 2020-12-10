from pysnmp.hlapi import *

oIDs = ['sysContact', 'sysName', 'sysLocation']


def search_in_list():  # Basic Function that gets and prints multiple values from a list
    for idToSearch in oIDs:
        iterator = getCmd(SnmpEngine(), CommunityData('public'), UdpTransportTarget(('192.168.1.23', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', idToSearch, 0)))
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:  # SNMP engine errors
            print(errorIndication)
        else:
            if errorStatus:  # SNMP agent errors
                print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex) - 1] if errorIndex else '?'))
            else:
                for varBind in varBinds:  # SNMP response contents
                    print(varBind[1])


search_in_list()
