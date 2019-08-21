 Movie_Rating_Task
 This utility will let you know the rating of movies.
 Requirements Log in to your docker account
 commands
This will pull the image where the script is present
docker pull yaths/imdb_test:docker
# get the image id
docker images
# run the image as a container
docker run -ti -d [imageid]
Get the container id
docker ps
Get inside container to execute script
docker exec -it [containerid] /bin/bash
python python_docker.py titanic
Movie Name is ==>['titanic']
Rotten Tomatoes Ratings -->89%
Error Handled
Movie name not found
No Ratings are present
