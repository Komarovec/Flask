from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

ANIMALS = {
	"dog": {"weight": 13, "sound": "bark", "id": "dog"},
	"cow": {"weight": 130, "sound": "moo", "id": "cow"}
}

class AnimalsResource(Resource):
	def get(self, id=None):
		if(id):
			return ANIMALS.get(id)

		return list(ANIMALS.values())


api.add_resource(AnimalsResource, "/v1/animals", endpoint="animals_list")
api.add_resource(AnimalsResource, "/v1/animals/<string:id>", endpoint="animals_detail")

if __name__ == "__main__":
	app.run()
