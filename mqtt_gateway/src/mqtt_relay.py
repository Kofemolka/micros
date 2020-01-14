from nameko.rpc import rpc
from nameko.events import EventDispatcher
from mqtt_recv import mqtt_recv
from mqtt_send import MqttSend

class MqttRelay:
    name = "mqtt_relay"
    dispatch = EventDispatcher()
    mqtt_send = MqttSend('localhost')

    @rpc
    def publish(self, topic, payload):
        self.mqtt_send.publish(topic, payload)

    @mqtt_recv('localhost')
    def relay_msg(self, topic, payload):
        self.dispatch("mqtt_msg_in", {
            "topic" : topic,
            "payload" : payload
        })