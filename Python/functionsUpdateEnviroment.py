def openAnything(source):
	# try to open with urllib (if source is http, ftp, or file URL)
	import urllib
	try: 
		return urllib.urlopen(source)
	except (IOError, OSError):
		pass
	# try to open with native open function (if source is pathname)
	try:           
		return open(source, "w")
	except (IOError, OSError):
		pass     
	# treat source as string
	import StringIO
	return StringIO.StringIO(str(source))

def updateDependencies(remoteArtifact, localArtifact):
	newDependencies = remoteArtifact.findall('config')
        oldDependencies = localArtifact.findall('config_bundle/config')
        for newDependence  in newDependencies:
        	for oldDependence in oldDependencies:
                	if newDependence.attrib['artifactname'] == oldDependence.attrib['name']:
                        	dep = newDependence.attrib['artifactname']
                                new = newDependence.attrib['version']
                                old = oldDependence.attrib['version']
                                if new > old:
                                	print dep + ": " + " old: " + old  + " new: " + new
                                        oldDependence.attrib['version'] = new

