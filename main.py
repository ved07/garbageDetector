from flask import Flask, render_template, redirect, url_for, request
import random
app = Flask(__name__,template_folder='templates')


@app.route('/', methods=["POST","GET"])
def index():
  if request.method == "POST":
    image=request.files["file"]
    image.filename = "main" + ".jpg"
    filepath = image.filename
    print(filepath)
    image.save(filepath)
    
    return redirect(url_for("test",poop=image))
  else:
   return render_template("home.html")


@app.route('/mission/')
def mission():
    return render_template("mission.html")

@app.route('/Applications/')
def progUses():
    return render_template("ProgramUses.html")
@app.route("/<poop>")
def test(poop):
    return f"<p>{poop}</p>"
@app.route('/predict/')
def predict():
  from convNet import model as conv
  Net = conv()
  Net.oneHotEncode()
  Net.setupData()
  Net.setupModel()
  print(Net.predict('main.jpg'))
  print(Net.decodeOneHot())
  
  
if __name__ == "__main__": 
  # Makes sure this is the main process
	app.run(debug=True, # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000))
    #port = 5000  # Randomly select the port the machine hosts on. 
  