from xml.dom import minidom
import urllib
from functionsUpdateEnviroment import *


#artifactsArray = ['orbitz-host-apollo-hotel', 'orbitz-host-hbe', 'orbitz-host-het', 'orbitz-host-hse', 'orbitz-host-pegasus', 'orbitz-host-sort', 'orbitz-host-tbs-txn', 'orbitz-host-gash-us', 'orbitz-host-gta', 'orbitz-host-hilton', 'orbitz-host-pdn', 'orbitz-host-tbs-shop']
artifactsArray = ['orbitz-host-gta', 'orbitz-host-hilton', 'orbitz-host-tbs-shop']

#Abrir xml local
xmlDocument = openAnything('test.xml')
parsedXML = minidom.parse(xmlDocument)
xmlDocument.close()

root = parsedXML.childNodes[2]
artifacts = root.childNodes

for artifactNode in artifacts:
	artifactNode.childNodes


#for artifact in artifactsArray:
#	node = artifacts.getElementsByTagName(name)
#	print node[0].toxml()

print artifacts.toxml()

#Abrir xml remoto
#remoteXML = openAnything('http://scmartifacts.duncllc.com/orbitzlibs/fqa01.releases.xml')
#parsedRemoteXML = minidom.parse(remoteXML)
#remoteXML.close()





#print parsedXML.toxml()
#print parsedRemoteXML.toxml()
