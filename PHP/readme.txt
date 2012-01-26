ENVIRONMENT UPDATER:

We develop this PHP script in order to have a parser of the RSS provided by Yoda. Using the data collected we could update the enviroment in Glu. Next we have a short description of the componnents.

We have 4 main files:

        - updateEnviroment.php: This is the main file, here we call all the functions to reach our goal.
        
        - functionsUpdateEnviroment.php: This file contains all the specific functions that we use in the main file, we use this structure in order to maintain clear the prime code and have the possibility to change or add anything without any troubles.
        
        - mappingUpdate.xml: This file is as important as the rest. Here we have the information  required to achieve the correct update of every artifact. It is compose by several sources, typed as "yodaElement". Everyone of this elements have the following attributes:
                - name: use to find the artifact, is like the key of the object.
                - rssLocation: URL where we find the feed for this artifact.
                - destination: Ubication of the file in the repository.
                - description: A short description of the artifact. (This is optional)
                - lastUpdate: This atribute is use to have a parameter of the last version that the script updated.

        - Git.php: This is the file wich contain the git class and all his functionallity.

The behavior is detailed below:

        - First of all the script fill an array with the artifacts to follow, eventually this could be given as a parameter of the script.
        - For every artifact in the array:
                - It Obtain the full object from the mapping file and take the RSS location.
                - With the location of the feed it search the last update published in Yoda.
                - It verify if the last version is a mayor release and if is later than the one in the mapping file; if this is true it made the update of both files, mapping and environment.
        - Finally commit the changes en the git repository.
