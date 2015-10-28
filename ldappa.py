#!/usr/bin/env python

import os.path
from config import Config

import bonsai


def main():
    conf = Config(os.path.expanduser('~/.ldapparc'))['monitor']

    client = bonsai.LDAPClient(conf['url'])
    client.set_credentials("SIMPLE", (conf['binddn'], conf['password']))
    connection = client.connect()

    result = connection.search('cn=Bytes,cn=Statistics,cn=monitor', 0, '', ['+'])
    nBytes = result[0]['monitorCounter'][0]

    result = connection.search('cn=Entries,cn=Statistics,cn=monitor', 0, '', ['+'])
    nEntries = result[0]['monitorCounter'][0]
    
    result = connection.search('cn=Total,cn=Connections,cn=monitor', 0, '', ['+'])
    totalConnections = result[0]['monitorCounter'][0]

    result = connection.search('cn=Current,cn=Connections,cn=monitor', 0, '', ['+'])
    currentConnections = result[0]['monitorCounter'][0]

    result = connection.search('cn=Max File Descriptors,cn=Connections,cn=monitor', 0, '', ['+'])
    maxDescriptors = result[0]['monitorCounter'][0]

    connection.close()

    print()
    print("Connections:")
    print("  Max descr:", maxDescriptors)
    print("  Current:", currentConnections)
    print("  Total:", totalConnections)
    print()
    print("Statistics:")
    print("  Bytes:", nBytes)
    print("  Entries:", nEntries)

if __name__ == "__main__":
    main()
