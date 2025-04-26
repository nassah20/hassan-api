API Overview
Building the API
I used Flask, a lightweight Python framework, to create a simple REST API. The API exposes two main endpoints:
    
    - /students → Returns a list of students and their programs.
    - /subjects → Returns a list of subjects categorized by year.
    
    To run the Flask app locally, I used the following command:
    
     bash
    python app.py
     
    
    This started the server, and you could access the API on http://13.60.254.240:5000.
Preparing for Deployment
To prepare the API for deployment, I created a virtual environment (venv) to manage dependencies:
    
    For Linux/macOS:
    bash
    python -m venv venv
    source venv/bin/activate

    I then installed Flask inside the virtual environment:
    
    bash
    pip install flask

    To save the dependencies, I generated a requirements.txt file:
    
     bash
    pip freeze > requirements.txt
     

Deploying the API
I used AWS to deploy the API. The process included the following steps:
    
    1.   Pushing the code to GitHub  :
    
     bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin <repository_url>
    git push -u origin main
     
    
    2.   Deploying to AWS  :
    - Created an EC2 instance on AWS.
    - SSH'd into the EC2 instance and set up the environment.
    - Ran the Flask app with the following command:
    
     bash
    python app.py
     
    
    The API was made available at http://13.60.254.240:5000.
Docker & Containerization
Dockerizing the API
To containerize the API, I used Docker to create isolated environments for the application. Below are the essential steps for Dockerizing the app:
    
    1.   Creating a Dockerfile  :
    The Dockerfile contains instructions to build a Docker image for the Flask API. Here’s an example Dockerfile:
    
     dockerfile
        Use the official Python image from Docker Hub
    FROM python:3.8-slim
    
        Set the working directory inside the container
    WORKDIR /app
    
        Copy the local code to the container
    COPY . /app
    
        Install dependencies from the requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt
    
        Expose the port the app will run on
    EXPOSE 5000
    
        Define the command to run the app
    CMD ["python", "app.py"]
     
    
    2.   Creating a Docker Compose File  :
    I used Docker Compose to manage multiple containers, such as the Flask app and the MySQL database.
    
     yaml
    version: '3'
    services:
      flask-api:
        build: .
        ports:
          - "5000:5000"
        depends_on:
          - db
        environment:
          - FLASK_APP=app.py
          - MYSQL_HOST=db
          - MYSQL_USER=root
          - MYSQL_PASSWORD=yourpassword
          - MYSQL_DB=hassanDB
    
      db:
        image: mysql:5.7
        environment:
          - MYSQL_ROOT_PASSWORD=root
          - MYSQL_DATABASE=hassanDB
        ports:
          - "3306:3306"
     
    
    3.   Building and Running the Docker Containers  :
    
    To build and start the containers using Docker Compose:
    
     bash
    docker-compose up --build
     
    
    The Flask API will be available at http://localhost:5000, and the MySQL database will be available at port 3306.
Bash Scripts Directory
1. health_check.sh: Monitoring the System
Purpose: Monitors the system's resource usage and checks API availability.
    
    - Checks CPU, memory, and disk usage.
    - Verifies if the web server (e.g., Apache) is running.
    - Tests the /students and /subjects API endpoints using curl.
    - Logs output to /var/log/server_health.log.
    - Adds warnings if disk space is low or an endpoint fails.
2. backup_api.sh: Backup the API
Purpose: Backs up the API project files and the MySQL database.
    
    - Compresses the API project directory into /home/ubuntu/backups.
    - Dumps the MySQL database into an SQL file.
    - Deletes backups older than 7 days.
    - Logs the results to /var/log/backup.log.
3. update_server.sh: Automate Server and API Updates
Purpose: Automates updates for the server and the API.
    
    - Runs apt update and apt upgrade for system packages.
    - Pulls the latest API code from GitHub.
    - Restarts the web server (Apache).
    - Logs output to /var/log/update.log.
    - If git pull fails, it logs the error and skips the restart.
How to Use the Scripts
Before running any script, ensure the script has execute permissions:
    
     bash
    chmod +x health_check.sh
    chmod +x backup_api.sh
    chmod +x update_server.sh
     

Common Docker Issues and Solutions
Issue 1: MySQL Container Not Starting
  Problem  : The MySQL container fails to start, showing an error like:
    
     bash
    [ERROR] [Entrypoint]: Database is uninitialized and password option is not specified
     
    
      Solution  : This happens when the MYSQL_ROOT_PASSWORD environment variable is not set. Ensure that the environment variable is properly defined in the docker-compose.yml file:
    
     yaml
    db:
      image: mysql:5.7
      environment:
        - MYSQL_ROOT_PASSWORD=root
        - MYSQL_DATABASE=hassanDB
     

Issue 2: Flask API Container Exiting with Code 1
  Problem  : The Flask API container exits immediately after starting, usually due to missing environment variables or dependencies.
    
      Solution  : Check the logs of the Flask container using:
    
     bash
    docker logs <container_name>
     
    
    Ensure that all required environment variables are set and that the application can access the MySQL database correctly.
Issue 3: Ports Not Exposed Properly
  Problem  : The API or database is not accessible from the host machine.
    
      Solution  : Ensure that the correct ports are exposed in the docker-compose.yml file:
    
     yaml
    ports:
      - "5000:5000"       For Flask API
      - "3306:3306"       For MySQL
     
URLS
1.	PUBLIC ADDRESS: http://13.60.254.240:5000 
2.	GITHUB REPOSITORY: https://github.com/your-username/hassan-api
3.	DOCKER HUB LINK: https://hub.docker.com/repositories/nassah20  
