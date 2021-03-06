from SNMPEngine import *

print('Hi, welcome to the SNMPTool!\nIf you need help, type /help\nTo quit, type /quit')
while True:
    cmd = input()
    if cmd == '/help':
        print('Opening in default webbrowser...')
        openhelp()
    if cmd == '/basicinfo':
        print('Please input the IP you want to scan:')
        ip = input()
        print('***Results***')
        print(basic_scan(ip))
        print('********')
    if cmd == '/get':
        print('Please input your IP:')
        ip = input()
        print('Please enter the community name:')
        community = input()
        print('Please enter the path to your MIB:')
        mibaddr = 'file:///' + input()
        print('Please enter the OID:')
        oid = input()

        tempname = mibaddr.split('/')
        mibname = tempname[-1]

        print('***Result***')
        if not checkemptystrings(community, ip, mibname, mibaddr, oid):
            print(get(community, ip, mibname, mibaddr, oid))
        else:
            print('Sorry, you have to enter every required field in order to get an element.\nPlease try again!')
        print('********')

    if cmd == '/set':
        print('Please input your IP:')
        ip = input()
        print('Please enter the path to your MIB:')
        mibaddr = input()
        print('Please enter the community:')
        community = input()
        print('Please enter the OID:')
        oid = input()
        print('Please enter the new Value:')
        new_val = input()

        tempname = mibaddr.split('/')
        mibname = tempname[-1]

        print('********')
        if not checkemptystrings(ip, mibname, mibaddr, oid):
            set(community, ip, mibname, mibaddr, oid, new_val)
            print('The new value <' + new_val + '> was successfully set!')
        else:
            print('Sorry, you have to enter every required field in order to set an element.\nPlease try again!')
        print('********')
    if cmd == '/scan':
        print("Please enter the Network IP:")
        ip = input()
        print("Please enter the subnet mask:")
        subnet = input()
        print('********')
        if not checkemptystrings(ip, subnet):
            print('Started network scan on ' + ip + "/" + subnet)
            res = scan(ip, subnet)
            formatted = 'Available Devices:\n'
            for i in res:
                formatted += i + '\n'
            formatted = formatted[:-1]  # Removes last \n
            print(formatted)
        else:
            print("Sorry, you have to enter every value to scan a network\nPlease try again!")
        print('********')

    if cmd == '/quit':
        exit(0)
