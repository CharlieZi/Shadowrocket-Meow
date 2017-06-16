#!/usr/bin/python

# Open a file
import sys
import os
import time
import datetime
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/HostUpdator"
sys.path.insert(0,currentdir) 



from HostCollector import hostCollector
from HostFormatModifier import hostDecorator


class HostUpdator(object):
    def init(self):
        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/HostUpdator"
        sys.path.insert(0,currentdir) 

        from HostCollector import hostCollector
        from HostFormatModifier import hostDecorator
    def HostUpdateWithUrl(self,urlList):
        hostCollect = hostCollector()
        hostCollect.fileDownloader(urlList)
        hostCollect.rawHostFileWirtor(urlList)

        print("host collection done!")

        hostDecorat = hostDecorator()
        hostDecorat.HostAddrssUpdator()

        print("output for shadowrocket-rules done!")


        hostListconf = open("HostUpdator/Host-list.conf","r")
        hostListconfFile = hostListconf.readlines()
        hostListconfPub = open("Host-list.conf","w+")
        hostListconfPub.writelines(hostListconfFile)
        hostListconf.close()
        hostListconfPub.close()

        print("Host-list.conf copied")





urlList = [
    "https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/hosts",
    # "https://raw.githubusercontent.com/racaljk/hosts/master/hosts",
    # "https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts",
    # "https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts-ad",
    # "https://raw.githubusercontent.com/sy618/hosts/master/dnsmasq/hosts",
    ]

HostUpdateFlow = HostUpdator()
HostUpdateFlow.HostUpdateWithUrl(urlList)