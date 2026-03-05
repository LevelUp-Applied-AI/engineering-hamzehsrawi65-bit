\# Docker Notes — Day 9



\## Docker Version



Docker was initially not available inside WSL until Docker Desktop integration was configured.



WSL output:



The command 'docker' could not be found in this WSL 2 distro.

We recommend to activate the WSL integration in Docker Desktop settings.





\## Hello World Test



Command:



docker run hello-world



Output:



Hello from Docker!

This message shows that your installation appears to be working correctly.



To generate this message, Docker took the following steps:

1\. The Docker client contacted the Docker daemon.

2\. The Docker daemon pulled the "hello-world" image from Docker Hub.

3\. The Docker daemon created a container from that image.

4\. The Docker daemon streamed the output to the Docker client.





\## Postgres Container



\### Pull Postgres Image



Command:



docker pull postgres:15-alpine



Output:



Status: Downloaded newer image for postgres:15-alpine

docker.io/library/postgres:15-alpine





\### Run Postgres Container



Command used:



docker run -d --name pg-prework -e POSTGRES\_PASSWORD=prework -p 5432:5432 postgres:15-alpine



Container ID returned:



e52f0872baa37820cfd2a94f8a58b9ec8a29658cea87d3198f49a1ad6c8a7a34





\### Verify Running Container



Command:



docker ps



Output shows container running:



pg-prework   postgres:15-alpine   Up   0.0.0.0:5432->5432/tcp





\## Startup Logs



Command:



docker logs pg-prework



Important confirmation line found:



LOG:  database system is ready to accept connections





\## Stop and Restart Container



Stop container:



docker stop pg-prework



Output:



pg-prework





Restart container:



docker restart pg-prework



Output:



pg-prework





Logs after restart confirm startup again:



LOG:  database system is ready to accept connections





\## Issues Encountered



1\. Docker command was not initially available inside WSL.

&nbsp;  This was resolved by enabling Docker Desktop WSL integration.



2\. A container name conflict occurred because `pg-prework`

&nbsp;  already existed. The issue was resolved by using the

&nbsp;  existing container instead of creating a new one.

