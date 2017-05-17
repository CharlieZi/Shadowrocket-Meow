#!/usr/bin/python

# Open a file
import sys
import os
import time

class hostDecorator(object):

    def __init__(self):
        self.rawHost = open("HostUpdator/hosts", "r")
        self.baseRules = open("HostUpdator/HostBaseRules.conf","r")
        self.ruleList = open("HostUpdator/Host-list.conf","wb+")
    
    def HostAddressModified(self,LineString):
        tempString = LineString.replace("\n","")
        tempString = tempString.replace(" ","\t")
        StringSplit = tempString.split("\t")
        HostAddress = [StringSplit[0],StringSplit[-1]]
        return HostAddress
    
    def HostAddressFormatforSRules(self,AddressList):
        AddressIP = AddressList[0]
        AddressDomain = AddressList[1]
        AddressString = "%s = %s\n"%(AddressDomain,AddressIP)
        return AddressString

    
    def HostAddrssUpdator(self):
        rawHostLines = self.rawHost.readlines()
        HostUpdateList = []

        for line in rawHostLines[6:]:
            line = self.HostAddressModified(line)
            line = self.HostAddressFormatforSRules(line)
            HostUpdateList.append(line)

        baseLines = self.baseRules.readlines()
        updateTime = ["# Updated at %s\n\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),]

        UpdatedList = baseLines + updateTime + HostUpdateList


        self.ruleList.writelines(UpdatedList)

        self.rawHost.close()
        self.ruleList.close()

        print ("done!")

