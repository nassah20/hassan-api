hassan-api
1. Building the API
•	I used Flask, a lightweight Python framework, to create a simple REST API.
•	I defined two endpoints:
o	/students → Returns a list of students and their programs.
o	/subjects → Returns a list of subjects categorized by year.
•	I ran the Flask app locally using:
sh

python app.py
This started the server on http://127.0.0.1:10000.
2. Preparing for Deployment
•	I created a virtual environment (venv) to manage dependencies.
sh

python -m venv venv
venv\Scripts\activate  # For Windows
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
