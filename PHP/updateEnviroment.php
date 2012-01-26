<?php

include "functionsUpdateEnviroment.php";
include_once('Git.php');

$artifactsArray = array('orbitz-host-apollo-hotel', 'orbitz-host-hbe', 'orbitz-host-het', 'orbitz-host-hse', 'orbitz-host-pegasus', 'orbitz-host-sort', 'orbitz-host-tbs-txn', 'orbitz-host-gash-us', 'orbitz-host-gta', 'orbitz-host-hilton', 'orbitz-host-pdn', 'orbitz-host-tbs-shop');

$changes = "Updated artifacts: ";

foreach ($artifactsArray as $artifactName){
	$artifactNode = getMappedArtifact($artifactName);
	$feed = $artifactNode['rssLocation'];
	$lastUpdateNode = getLastFeed($feed);
	$currentVersion = getFeedVersion($lastUpdateNode['title']);
	$previusVersion = $artifactNode['lastUpdate'];
	echo $lastUpdateNode['title'] . " " . $previusVersion . " " . $currentVersion . "\n";
	if ( nonBeta($currentVersion) && strnatcmp($previusVersion, $currentVersion) < 0){
		setVersionMapping($previusVersion, $currentVersion); 
		setVersionEnvironment($artifactNode['destination'], $previusVersion, $currentVersion);
		$changes = $changes . $artifactName . "-" . $currentVersion . " ";
	}
}
#$repository = Git::open('/home/dvelazquez/orbitz-fabrics/fabric-HDP_POC');
#$repository -> commit($changes);
echo "git commit -a -m ".$changes . "\n";
?>
