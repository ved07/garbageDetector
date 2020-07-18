from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CLImage
# Instantiate a new Clarifai app by passing in your API key.
app = ClarifaiApp(api_key='dad6ee7ee71e4a98a2c747bc25fd69a4')
model = app.public_models.general_model
model.model_version = 'aa7f35c01e0642fda5cf400f543e7c40'
response = model.predict_by_filename("bottle.jpg")
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
