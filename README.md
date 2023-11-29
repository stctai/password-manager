# CS6760 Group 7 - Password Manager

## Setting Up
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

3. Intall the the packages listed in the requirements.txt file with the specified versions
   Run this command in this project terminal
      ```
      pip install -r requirements.txt
      ```
   This command reads the requirements.txt file and installs the specified packages along with their versions.


## How to Use
By: Minjie

After you start the app on your local machine through 
   ```
   python main.py
   ```
   , you will be prompt to type in the master password. By default, for the simplicity, we use general "password" as the master password.

Once you are sucessfully authenticated, you will be provided with three choices:
   1. Create new password.
   2. Find all sites and apps connected to an email.
   3. Find a password for a site or app.

After all the operations you want to make, you can press Q to quit the application safely.


## Encryption for Security
The program uses Fernet library for the encrpytion and decryption of the password stored into the database. The Fernet library is a Python library for symmetric (also known as "secret key") authenticated cryptography. Here are some reasons why we chose the Fernet library over other options:

1. Simplicity:
   - Fernet provides a high-level, easy-to-use interface for symmetric key encryption and decryption.
   - Generating keys and encrypting/decrypting data with Fernet is straightforward, making it a good choice for developers who want a simple and effective solution.
2. Security:
   - Fernet uses AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode for encryption, providing strong security.
   - It also includes HMAC (Hash-based Message Authentication Code) to ensure the integrity of the encrypted data. This helps prevent tampering with the encrypted data.
3. Key Management:
   - Fernet handles key management automatically. We don't need to worry about key generation, distribution, or rotation; Fernet takes care of these aspects for us.
   - This simplifies the implementation and reduces the risk of key mismanagement, which is a common source of security vulnerabilities.
4. Python Standard Library Integration:
   - Fernet is part of the cryptography library in Python, which is actively maintained and widely used. This integration with the Python standard library makes it a convenient choice for projects that want to leverage existing Python modules.
