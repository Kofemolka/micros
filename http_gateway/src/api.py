from flask import Flask, Blueprint, request, jsonify, abort
from auth import auth

from nameko.standalone.rpc import ClusterRpcProxy

#TODO 
# separate API class per entity
class ApiModule():

    def __init__(self, app, config):
        self.blueprint = Blueprint("api.v1", __name__, url_prefix="/api/v1")

        self.blueprint.add_url_rule('/core/find_by_plate',
            'api_core_find_by_plate', self.core_find_by_plate, methods=['GET'])

        self.blueprint.add_url_rule('/mqtt/publish',
            'api_mqtt_publish', self.mqtt_publish, methods=['POST'])

        app.register_blueprint(self.blueprint)

        self.broker_uri = {
            'AMQP_URI' : config.broker["uri"]
        }        

    # @auth.login_required
    def core_find_by_plate(self):
        plate = request.args.get("plate")
        if not plate: abort(400, "[plate] param is missing")
                
        with ClusterRpcProxy(self.broker_uri) as cluster_rpc:
            res = cluster_rpc.booking.find_by_plate_number(plate)
            return res

    # @auth.login_required
    def mqtt_publish(self):
        topic = request.args.get("topic")
        if not topic: abort(400, "[topic] param is missing")

        payload = request.args.get("payload")
        if not payload: abort(400, "[payload] param is missing")
                
        with ClusterRpcProxy(self.broker_uri) as cluster_rpc:
            res = cluster_rpc.mqtt_relay.publish(topic, payload)
            return res