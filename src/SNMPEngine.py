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
    if not errorIndication:  # SNMP engine errors
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


def scan(ip_address, subnet):
    ip_splits = ip_address.split('.')
    subnet_range_from = int(ip_splits[2])
    ip_range_from = 1
    ip_range_to = 2
    subnet_range_to = subnet_range_from + 1
    if subnet == '30':
        ip_range_to = 3
    elif subnet == '29':
        ip_range_to = 7
    elif subnet == '28':
        ip_range_to = 15
    elif subnet == '27':
        ip_range_to = 31
    elif subnet == '26':
        ip_range_to = 63
    elif subnet == '25':
        ip_range_to = 127
    elif subnet == '24':
        ip_range_to = 255
    elif subnet == '23':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 2
    elif subnet == '22':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 3
    elif subnet == '21':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 4
    elif subnet == '20':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 5
    elif subnet == '19':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 6
    elif subnet == '18':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 7
    elif subnet == '17':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 8
    elif subnet == '16':
        ip_range_to = 256
        subnet_range_to = subnet_range_from + 9
    else:
        return 'Subnet not supported :('

    available_ips = []
    for i in range(subnet_range_from, subnet_range_to):
        for j in range(ip_range_from, ip_range_to):
            current_ip = "%d.%d.%d.%d" % (int(ip_splits[0]), int(ip_splits[1]), i, j)

            iterator = getCmd(SnmpEngine(), CommunityData('public'), UdpTransportTarget((current_ip, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)))
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            if not errorIndication:  # if not SNMP engine errors
                if not errorStatus:  # if not SNMP agent errors
                    available_ips.append(current_ip)    # If no error is shown, the IP is added to the available IPs
        if i == subnet_range_from:
            ip_range_from -= 1  # begins from .0 after the first "network"
        if i == (subnet_range_to - 1):
            ip_range_to -= 1    # theoretically removes the .255 address from the last "network"

    return available_ips
