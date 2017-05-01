#!/usr/bin/python

# Open a file
import sys
import os



rawHost = open("HostUpdator/hosts", "r")
baseRules = open("HostUpdator/HostBaseRules.conf","r")
ruleList = open("HostUpdator/Host-list.conf","wb+")







def HostAddressModified(LineString):
    tempString = LineString.replace("\n","")
    tempString = tempString.replace(" ","\t")
    StringSplit = tempString.split("\t")
    HostAddress = [StringSplit[0],StringSplit[-1]]
    return HostAddress


def HostAddressFormatforSRules(AddressList):
    AddressIP = AddressList[0]
    AddressDomain = AddressList[1]
    AddressString = "%s = %s\n"%(AddressDomain,AddressIP)
    return AddressString




rawHostLines = rawHost.readlines()
HostUpdateList = []

for line in rawHostLines[6:]:
    line = HostAddressModified(line)
    line = HostAddressFormatforSRules(line)
    HostUpdateList.append(line)

# print HostUpdateList

baseLines = baseRules.readlines()
UpdatedList = baseLines + HostUpdateList

# print UpdatedList

ruleList.writelines(UpdatedList)


rawHost.close()
ruleList.close()

print ("done!")