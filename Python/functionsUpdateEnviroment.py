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
