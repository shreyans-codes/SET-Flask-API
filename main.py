from flask import Flask
from flask_restful import Api, Resource
from crop_recommend import apiCallFunction

app = Flask(__name__)
api = Api(app)


class Parameters(Resource):

    def get(self, N, P, K, temperature, humidity, pH, rainfall):
        retVal = apiCallFunction(N, P, K, temperature, humidity, pH, rainfall)
        return retVal
        # return {"N": f"Nitrogen In {N}%",
        #         "P": f"Phosphorous In {P}%",
        #         "K": f"Potassium In {K}%",
        #         "Temp": f"Temperature In {temperature}C",
        #         "Hum": f"Humidity In {humidity}%",
        #         "pH": f"Acidity Level In {pH}",
        #         "RF": f"Rainfall In {rainfall}MM"}
        # return "Hello"


api.add_resource(
    Parameters, "/parameters/<float:N>/<float:P>/<float:K>/<float:temperature>/<float:humidity>/<float:pH>/<float:rainfall>")

if __name__ == "__main__":
    app.run(debug=True)
# N,P,K,temp,humidity,ph,rainfall
