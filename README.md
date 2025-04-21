hassan-api
1. Building the API
•	I used Flask, a lightweight Python framework, to create a simple REST API.
•	I defined two endpoints:
o	/students → Returns a list of students and their programs.
o	/subjects → Returns a list of subjects categorized by year.
•	I ran the Flask app locally using:
sh

python app.py
This started the server on http://216.24.57.252
2. Preparing for Deployment
•	I created a virtual environment (venv) to manage dependencies.
sh

python -m venv venv
venv\Scripts\activate  
For Windows
•	Installed Flask inside the environment:
sh

pip install flask
•	Saved dependencies in a requirements.txt file:
sh

pip freeze > requirements.txt
3. Deploying the API
I chose Render (or any other platform) for deployment. The process included:
•	Pushing the code to GitHub
sh

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <ir-github-repo-url>
git push -u origin main
•	Connecting GitHub to Render
o	Logged into Render.
o	Created a new Web Service.
o	Selected the GitHub repository.
o	Set the Start Command:
sh

gunicorn app:app
o	Clicked Deploy.

bash_scripts Directory

This directory contains three main scripts:

 1. health_check.sh
 Purpose: Monitors the system's resource usage and checks API availability.
 Functions:
  - Checks CPU, memory, and disk usage
  - Verifies the web server (e.g., Apache) is running
  - Tests `/students` and `/subjects` API endpoints using `curl`
  - Logs output to `/var/log/server_health.log`
  - Adds warnings if disk space is low or an endpoint fails

  2.backup_api.sh
   Purpose: Backs up the API project files and database.
   Functions:
  - Compresses the API project directory into `/home/ubuntu/backups`
  - Dumps the MySQL database into an SQL file
  - Deletes backups older than 7 days
  - Logs results to `/var/log/backup.log`

3.update_server.sh
Purpose: Automates server and API updates.
Functions
  - Runs `apt update` and `apt upgrade` for system packages
  - Pulls the latest API code from GitHub
  - Restarts the web server (Apache)
  - Logs output to `/var/log/update.log`
  - If `git pull` fails, it logs the error and skips the restart

 How to Use the Scripts
 1. Set Execute Permissions
Before running any script, you must make it executable:

bash
chmod +x health_check.sh
chmod +x backup_api.sh
chmod +x update_server.sh
