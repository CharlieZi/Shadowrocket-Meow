# Open a file
import sys
import os
import time
import urllib2
import re
import datetime

class hostCollector(object):


    def __init__(self):
        pass

    def urlToNameConvertor(self,urlList):
        fileNameList = []
        for url in urlList:      
            fileName = "HostUpdator/"+url.split("/")[3] + "_" + url.split("/")[-1]
            fileNameList = fileNameList + [fileName]
        return fileNameList



    def fileDownloader(self,urlList):
        for url in urlList:      
            Url  = urllib2.urlopen(url)
            fileName = "HostUpdator/"+url.split("/")[3] + "_" + url.split("/")[-1]
            File = open(fileName, 'wb')
            meta = Url.info()
            fileSize = int(meta.getheaders("Content-Length")[0])
            print "Downloading: %s Bytes: %s" % (fileName, fileSize)

            fileSizeDl = 0
            blockSize = 8192

            while True:
                buffer = Url.read(blockSize)
                if not buffer:
                    break
                fileSizeDl += len(buffer)
                File.write(buffer)

                # status = r"%10d  [%3.2f%%]" % (fileSizeDl, fileSizeDl * 100. / fileSize)
                # status = status + chr(8)*(len(status)+1) + "\n"
                # print status,
            
            File.close()
        print "Host files downloaded! "

    def timeStampDetector(self, fileName):
        hostFile = open(fileName,"r") 
        hostHeader = hostFile.readlines()[0:5]
        pattern = re.compile('\d{4}-\d{2}-\d{2}.*')
        pattern2 = re.compile('\d{4}\d{2}\d{2}\d{2}\d{2}.*')
        for wordlist in hostHeader:
            tempList = re.split(" |=",wordlist)
            for word in tempList:
                if pattern.match(word):
                    hostPubDate = datetime.datetime.strptime(word.replace("\n",""), '%Y-%m-%d')
                    break
                if pattern2.match(word):
                    hostPubDate = datetime.datetime.strptime(word.replace("\n",""), '%Y%m%d%H%M')
                    break
        hostFile.close()
        return hostPubDate

    def hoseCommentWashAsList(self,fileName):
        HostAddress = []
        hostFile = open(fileName,"r") 
        hostFileLines = hostFile.readlines()
        for line in hostFileLines:
            if line[0] == "#":
                pass
            else:
                line = line.replace("\n","")
                line = line.replace(" ","\t")
                line = line.split("\t")
                HostAddress = HostAddress + [[line[0],line[-1],self.timeStampDetector(fileName)]]
        hostFile.close()
        return HostAddress

    def hostfileCombineAsList(self, urlList):
        fileNameList = self.urlToNameConvertor(urlList)
        totalHostFile = []
        submittedNum = 1
        for file in fileNameList:
            print("washing " + file)
            washedHostFile = self.hoseCommentWashAsList(file)
            totalHostFile = totalHostFile + washedHostFile
            print("%s/%s")%(submittedNum,len(fileNameList))
            submittedNum = submittedNum + 1
            
        return totalHostFile

    def hostDuplicatRemoveAsList(self, totalHostFile):
        finalHostList = [totalHostFile[0]]
        for entry in totalHostFile:

            host_domain = entry[1]
            host_ip = entry[0]
            host_updatedTime = entry[2]


            lengthCountNum = 0
            for item in finalHostList:
                # print item
                if host_domain == item[1]:
                    if host_updatedTime <= item[2]:
                        break
                    else:
                        finalHostList.remove(item)
                        finalHostList += [entry]
                        break
                else:
                    lengthCountNum += 1
                

                if lengthCountNum == len(finalHostList):
                    finalHostList += [entry]

                    
    

        return finalHostList      

    def rawHostFormatorAsList(self, HostList):
        formatedHostList =[]
        for item in HostList:
            hostString = "%s\t%s\n"%(item[1],item[0])
            formatedHostList = formatedHostList + [hostString]  

        return formatedHostList     
                        
    def rawHostFileWirtor(self, urlList):
        combinedHostList = self.hostfileCombineAsList(urlList)
        # print combinedHostList
        finalHostList = self.hostDuplicatRemoveAsList(combinedHostList)
        formatedHostList = self.rawHostFormatorAsList(finalHostList)
        rawHost = open("HostUpdator/hosts", "w+")
        
        rawHost.writelines(formatedHostList)
        # print formatedHostLists

        rawHost.close()



# urlList = [
#     # "https://raw.githubusercontent.com/CharlieZi/Shadowrocket-Meow/master/hosts",
#     # "https://raw.githubusercontent.com/CharlieZi/Host-Collector/master/hostIPScanResult",
#     # "https://raw.githubusercontent.com/racaljk/hosts/master/hosts",
#     # "https://raw.githubusercontent.com/sy618/hosts/master/FQ",
#     "https://raw.githubusercontent.com/vokins/yhosts/master/hosts",
#     "https://raw.githubusercontent.com/vokins/yhosts/master/hosts",
#     ]
# hostCollect = hostCollector()
# hostCollect.fileDownloader(urlList)
# hostCollect.rawHostFileWirtor(urlList)



