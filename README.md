# CS6760 Group 7 - Password Manager

## Before you start
By: Ke

We are using PostgresSQL Database in Docker container to store passwords. 
To set up a new Docker container, with PostgreSQL installed, you need to do several steps:
1. Install Docker on your machine
   - Install Docker on a Mac instructions can be found [here](https://docs.docker.com/desktop/install/mac-install/). Windows installation instructions can be found [here](https://docs.docker.com/desktop/install/windows-install/).
2. Create a Postgres database from Docker Image
   - Create a `Dockerfile` in the root directory of the project. The `Dockerfile` should contain the following:
     ```
     FROM postgres
     ENV POSTGRES_PASSWORD dbpassword
     ENV POSTGRES_DB password_manager
     COPY password_db.sql /docker-entrypoint-initdb.d/
     ```
     And then run 
     ```
     docker build -t my-password-manager-db ./
     ``` 
     to build the Docker image and give it a name of `my-password-manager-db`.
     We can run it as a container by doing the following:
      ```
      docker run --name my-password-manager-container -p 5432:5432 -d my-password-manager-db
      ```
     


