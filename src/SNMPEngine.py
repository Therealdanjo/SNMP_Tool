from pysnmp.hlapi import *
from utilities import *


def basic_scan(ip_address):  # scans the basic six information of an IP via SNMP
    oIDs = ['sysName', 'sysContact', 'sysLocation', 'sysDescr', 'sysUpTime', 'sysServices']
    retstr = ''
    for idToSearch in oIDs:
        iterator = getCmd(SnmpEngine(), CommunityData('public'), UdpTransportTarget((ip_address, 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', idToSearch, 0)))
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:  # SNMP engine errors
            return errorIndication
        else:
            if errorStatus:  # SNMP agent errors
                return '%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex) - 1] if errorIndex else '?')
            else:
                for varBind in varBinds:  # SNMP response contents
                    if idToSearch == 'sysUpTime':
                        retstr += idToSearch + ': ' + parseuptime(varBind[1]) + '\n'
                    else:
                        retstr += idToSearch + ': ' + str(varBind[1]) + '\n'

    retstr = retstr[:-2]    # Removes the last \n from the return string
    return retstr


def get(community, ip_address, mib, mibpath, oid):
    iterator = getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip_address, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(mib, oid, 0).addAsn1MibSource('file:///usr/share/snmp', mibpath)))
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:  # SNMP engine errors
        return errorIndication
    else:
        if errorStatus:  # SNMP agent errors
            return '%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex) - 1] if errorIndex else '?')
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
