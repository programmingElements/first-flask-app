from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
  technology_name = "Python Flask"
  app_name = "First Application"
  topics = ["Jinja2", "Redirects & Errors", "Routing", "Rendering Templates", "Sessions", "Message Flashing", "Logging"]
  feature_flask = "Flask Features"
  features = ["modular", "extensible", "lightweight", "restful", "jinja", "secure cookies", "friendly ecosystem"]
  items = ["Python", "Java", "Javascript", "Go", "C", "C++", "Swift", "Dot", "C#", "PHP"]
  return render_template("/index.html", technology_name=technology_name, app_name=app_name, topics=topics, feature_flask=feature_flask, features=features, items=items)

@app.route("/home")
def home():
  return render_template("/home.html")

@app.route("/about")
def about():
  status = "single"
  return render_template("/about.html", status=status)

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.template_filter("reverse_word")
def rev_word(s):
  return " ".join(s.split(" ")[::-1])

@app.template_filter("repeat")
def repeat_times(s, times=2):
  return s * times

@app.template_filter("alter_case")
def alternate_case(s):
  return "".join([ c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s) ])