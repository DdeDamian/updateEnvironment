from lxml import etree
import urllib
from functionsUpdateEnviroment import *
import git

#Open and parse local XML
xmlDocument = openAnything('mappingUpdate.xml')
parsedXML = etree.parse( xmlDocument )
xmlDocument.close()

#Open and parse remote XML
remoteXML = openAnything('http://scmartifacts.duncllc.com/orbitzlibs/fqa01.releases.xml')
parsedRemoteXML = etree.parse( remoteXML )
remoteXML.close()

remoteArtifacts = parsedRemoteXML.findall('artifact')

localArtifacts = parsedXML.findall('artifact')
for localArtifact in localArtifacts:
	localName = localArtifact.attrib['name']
	localVersion = localArtifact.attrib['lastUpdate']
	for remoteArtifact in remoteArtifacts:
		if "artifactname" in remoteArtifact.keys():	
			if remoteArtifact.attrib['artifactname'] == localName:
				remoteVersion = remoteArtifact.attrib['version']
				if localVersion < remoteVersion:
					#Open the XML definition of the artifact in order to parse it.
					tempXML = openAnything(localArtifact.attrib['destination'])
                                        tempParsedXML = etree.parse(tempXML)
                                        tempXML.close()
					#Find de version on the XML and modify for the new one
					artifactVersion = tempParsedXML.find( "artifact_version")
                                        artifactVersion.text = remoteVersion
					print "Artifact changed: " + remoteArtifact.attrib['artifactname'] + " New version: " + remoteArtifact.attrib['version'] + " Old version: " + localVersion + "\n"
					updateDependencies(remoteArtifact, tempParsedXML)
					#Open the XML file to save the changes
					artifactXML = open(localArtifact.attrib['destination'], 'w')	
					tempParsedXML.write(artifactXML)
					localArtifact.set ( 'lastUpdate' , remoteVersion )

#Write The mapping XML with the new data
destinationXML = open('mappingUpdate.xml', 'w')
parsedXML.write(destinationXML)

#Create a link to the git repository and make the commit
repository = git.Git("/home/dvelazquez/orbitz-fabrics/fabric-HDP_POC")
result = repository.execute(["git", "commit", "-a", "-m", "'First script commit'"])
print result
