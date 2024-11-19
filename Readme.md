## First Flask Application - Python Flask Application - Simple Flask Application

   Flask Installation URL : https://flask.palletsprojects.com/en/stable/installation/

   1. Install Python and Check Python Version
      URL : https://www.python.org/downloads/ 

   2. Create an virtual environment [ Mac/Linux (or) Windows ]
  
   3. Activate the environment [ Mac/Linux (or) Windows ]

   4. Install Flask

   5. Check the python dependencies 
      $ pip3 freeze

   6. Reference Documentation
      URL : https://flask.palletsprojects.com/en/stable/quickstart/

              (or)

      URL : https://flask.palletsprojects.com/en/stable/  

   7. Transfer the dependencies
      $ pip3 freeze > requirements.txt 
      
   8. Install Dependencies using requirements file
      $ pip3 install -r requirements.txt

==============================
Flask Application First App
==============================

app.py
------
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello World</h1>"

@app.route("/hello")
def hello():
  response = make_response('Hello World\n')
  response.status_code = 202
  response.headers['content-type'] = 'application/octet-stream'
  return response

@app.route("/greet/<name>")
def greet(name):
  return f"Hello! {name}"

# @app.route("/handle_url_params")
# def handle_params():
#   return str(request.args)

@app.route("/handle_url_params")
def handle_params():
  if 'greeting' in request.args.keys() and 'name' in request.args.keys():  
    greeting = request.args.get("greeting")
    name = request.args.get("name")
    return f'{greeting}, {name}'
  else:
    return 'Some parameters are missing'

@app.route("/home", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    return "You made a GET request\n"
  elif request.method == "POST":
    return "You made a POST request\n"
  else:
    return "You will never see this message\n"

if __name__=="__main__":
  app.run(host='0.0.0.0', port=5050, debug=True)




===========================================
 Dockerizing the Python Flask Application
============================================
 
 1. Create Dockerfile in Flask Project Directory 

    $ vi Dockerfile
    
      FROM python:3.10-slim-buster

      WORKDIR /flask-app

      COPY requirements.txt requirements.txt

      RUN pip3 install -r requirements.txt

      COPY . .

      EXPOSE 5050

      CMD ["python3", "run.py"]
 
 2. Build Dockerfile 

    $ docker build --tag first-flask-app . [ dot represents Dockerfile is present current working directory ]

 3. List Docker Images

    $ docker images
    
 4. Run the Docker Image as Docker Container with port mapping
    
    $ docker run -d -p 5050:5050 --name=first-flask-con first-flask-app

 5. List Docker Containers
    
    $ docker ps

 6. Stop Docker Container

    $ docker stop first-flask-con
    
 7. Save the Docker Image as .tar file extension

    $ docker save -o firstflaskapp.tar first-flask-app

 8. To see the firstflaskapp.tar file in which location is saved
    
    $ ls

 9. Upload/Transfer the firstflaskapp.tar into the linux os using "scp" command

    $ scp firstflaskapp.tar <username>@<ip-address/hostname>:<path-linux-os>
    
    Example:
    $ scp firstflaskapp.tar jrao@192.168.0.104:/home/jrao/firstflaskapp.tar
    Enter the Password: ******** [Type the Linux os Password]

 10. To use the docker saved file of firstflaskapp.tar in the linux os 

     $ docker load -i firstflaskapp.tar

     $ docker run -d -p 5050:5050 first-flask-app