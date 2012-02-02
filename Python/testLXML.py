from lxml import etree
import urllib
from functionsUpdateEnviroment import *

#Open and parse local XML
xmlDocument = openAnything('mappingUpdate.xml')
parsedXML = etree.parse( xmlDocument )
xmlDocument.close()

#Open and parse remote XML
remoteXML = openAnything('http://scmartifacts.duncllc.com/orbitzlibs/fqa01.releases.xml')
parsedRemoteXML = etree.parse( remoteXML )
remoteXML.close()

remoteArtifacts = parsedRemoteXML.findall('artifact')

#print etree.tostring(parsedXML)
#for elt in parsedXML.getiterator():
#	print elt.tag


localArtifacts = parsedXML.findall('artifact')
for localArtifact in localArtifacts:
	localName = localArtifact.attrib['name']
	localVersion = localArtifact.attrib['lastUpdate']
	for remoteArtifact in remoteArtifacts:
		if "artifactname" in remoteArtifact.keys():	
			if remoteArtifact.attrib['artifactname'] == localName:
				remoteVersion = remoteArtifact.attrib['version']
				if localVersion < remoteVersion:
					print "Antes: " + remoteArtifact.attrib['artifactname'] + " " + remoteArtifact.attrib['version'] + " " + localVersion + "\n"
					
					tempXML = openAnything(localArtifact.attrib['destination'])
					tempParsedXML = etree.parse(tempXML)
					
					print tempParsedXML.find( "pool/artifact_version")

					print version.text
					
					localArtifact.set ( 'lastUpdate' , remoteVersion )

#Write The mapping XML with the new data
destinationXML = open('mappingUpdate.xml', 'w')
parsedXML.write(destinationXML)
