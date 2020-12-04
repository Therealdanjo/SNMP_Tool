from easysnmp import Session

session = Session(hostname='192.168.1.23', community='public', version=2)

oIDs = ['sysContact', 'sysName', 'sysLocation']


def get_in_list():
    for toSearch in oIDs:
        print(session.get((toSearch, '0')))


get_in_list()
