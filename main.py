from flask import Flask
from flask_restful import Api

from controllers.v1_port_scan import V1PortScan

app = Flask(__name__)
api = Api(app)

api.add_resource(V1PortScan, "/portScan")

if __name__ == "__main__":
    app.run()
