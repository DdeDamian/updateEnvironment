<?php

function getMappedArtifact($artifact){
#This function searches a given artifact from our mapping xml and returned all the data. 
	
	$doc = new DOMDocument(); #Se crea el DOMDocument donde se volcara el xml
	$doc->load("mappingUpdate.xml");
	$arrFeeds = array();
	foreach ($doc->getElementsByTagName('source') as $node) {
		$itemRSS = array ( 
		'name' => $node->getElementsByTagName('name')->item(0)->nodeValue,
		'rssLocation' => $node->getElementsByTagName('rssLocation')->item(0)->nodeValue,
		'destination' => $node->getElementsByTagName('destination')->item(0)->nodeValue,
		'description' => $node->getElementsByTagName('description')->item(0)->nodeValue,
		'lastUpdate' => $node->getElementsByTagName('lastUpdate')->item(0)->nodeValue,
		);
		if ( $itemRSS["name"] == $artifact ){
			return $itemRSS;
		}
		array_push($arrFeeds, $itemRSS);
	}
	die ("Error: Artifact not found\n");
}

function getLastFeed($feed){
#This function take the last update from a given RSS feed

	$doc = new DOMDocument(); #Se crea el DOMDocument donde se volcara el xml
	$doc->load($feed); #Se obtiene el XML del RSS Feed correspondiente
	$node = $doc->getElementsByTagName('entry')->item(0);
	$itemRSS = array ( 
	'id' => $node->getElementsByTagName('id')->item(0)->nodeValue,
	'link' => $node->getElementsByTagName('link')->item(0)->nodeValue,
	'title' => $node->getElementsByTagName('title')->item(0)->nodeValue,
	'published' => $node->getElementsByTagName('published')->item(0)->nodeValue,
	'updated' => $node->getElementsByTagName('updated')->item(0)->nodeValue,
	'summary' => $node->getElementsByTagName('summary')->item(0)->nodeValue,
    	);
	return $itemRSS;
}

function nonBeta($currentVersion){
#This function check if the given version is or not a beta version. If isn't a beta return true.

return !preg_match("*-*", $currentVersion);

}

function getFeedVersion($title){
#This function extract the current version from the title provided by the RSS feed.

$parts = explode(" ", $title);
return $parts[1];

}

function setVersionEnvironment($path, $previusVersion, $currentVersion){
#This function change the current version number for the last version number on the environment.

$tempFile = file_get_contents($path);

$modFile = str_replace($previusVersion, $currentVersion, $tempFile);

file_put_contents($path, $modFile);

}

function setVersionMapping($previusVersion, $currentMappedVersion){
#REVISAR ESTA FUNCION! POR QUE ESTA BIEN, PERO PUEDE PASAR QUE 2 ARTEFACTOS TENGAN LA MISMA VERSION!
#CONVIENE BUSCAR POR ARTEFACTO Y CAMBIAR SU VERSION!
$path = "mappingUpdate.xml";

$tempFile = file_get_contents($path);

$modFile = str_replace($previusVersion, $currentMappedVersion, $tempFile);

file_put_contents($path, $modFile);

}

?>
