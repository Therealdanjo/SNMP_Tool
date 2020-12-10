from pysnmp.hlapi import *
from utilities import *


def basic_scan(ip_address):  # scans the basic six information of an IP via SNMP
    oIDs = ['sysName', 'sysContact', 'sysLocation', 'sysDescr', 'sysUpTime', 'sysServices']
    for idToSearch in oIDs:
        iterator = getCmd(SnmpEngine(), CommunityData('public'), UdpTransportTarget((ip_address, 161)),
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
                    if idToSearch == 'sysUpTime':
                        print(idToSearch + ': ' + parseuptime(varBind[1]))
                    else:
                        print(idToSearch + ': ' + str(varBind[1]))


def get(ip_address, mib, mibpath, oid):

    iterator = getCmd(SnmpEngine(), CommunityData('public'), UdpTransportTarget((ip_address, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(mib, oid, 0).addAsn1MibSource('file:///usr/share/snmp', mibpath)))
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:  # SNMP engine errors
        print(errorIndication)
    else:
        if errorStatus:  # SNMP agent errors
            print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex) - 1] if errorIndex else '?'))
        else:
            for varBind in varBinds:  # SNMP response contents
                return oid + ': ' + str(varBind[1])


def set(community, ip_address, mib, mibpath, oid, new_val):
    g = setCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip_address, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(mib, oid, 0).addAsn1MibSource('file:///usr/share/snmp', mibpath), new_val)
               )
    next(g)
