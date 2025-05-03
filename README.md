1. Project Initialization , We began by setting up a React frontend project and initializing the Git repository. Dependencies such as `react-scripts` and `react` were installed using npm.
2. Dockerization , A `Dockerfile` was created in the frontend directory to containerize the application. A `.dockerignore` file was also created to prevent unnecessary files like `node_modules` from being included in the Docker image.
3. Running Docker Locally , The image was built using `docker build -t frontend .`, and containers were run on different ports to ensure functionality using `docker run -p 3000 ,3000 frontend` and `docker run -p 3001 ,3000 frontend`.
4. Version Control with GitHub , The project was pushed to GitHub at the following URL , https ,//github.com/nassah20/hassan-api/tree/master. Due to secret scanning protection, detected secrets were removed from the commit history using `git filter-repo`.
5. Docker Hub Deployment , The Docker image was tagged and pushed to Docker Hub at , https ,//hub.docker.com/repositories/nassah20. This allows remote access and sharing of the image.
6. AWS EC2 Deployment , The application was deployed and tested on an AWS EC2 instance. Public access is available via the IP address , http://13.60.254.240:3000.
LINKS USED
• GitHub Repository , https://github.com/nassah20/hassan-api/tree/master
• Docker Hub Repository , https://hub.docker.com/repositories/nassah20
• Public Frontend URL (EC2) , http://13.60.254.240 :3000
