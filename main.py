from flask import Flask, render_template, redirect, url_for, request
import random
app = Flask(__name__,template_folder='templates')


@app.route('/', methods=["POST","GET"])
def index():
  if request.method == "POST":
    image=request.files["file"]
    image.filename = "poop" + ".jpg"
    filepath = image.filename
    print(filepath)
    image.save(filepath)

    """
    # Instantiate a new Clarifai app by passing in your API key.
    app = ClarifaiApp(api_key='dad6ee7ee71e4a98a2c747bc25fd69a4')
    model = app.public_models.general_model
    model.model_version = 'aa7f35c01e0642fda5cf400f543e7c40'
    response = model.predict_by_filename(".jpg")
    print(response["outputs"][0]["data"]["concepts"])
    poop = response["outputs"][0]["data"]["concepts"]

    recyclable = False
    for element in poop:
        if (element["name"] == "recycling") and (element["value"]>=0.75):
            recyclable = True
    if recyclable:
        print("yep, its a recyclable")
    else:
        print("nope, into the trash")
    """
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

if __name__ == "__main__": 
  # Makes sure this is the main process
	app.run(debug=True, # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000))
    #port = 5000  # Randomly select the port the machine hosts on. 
  