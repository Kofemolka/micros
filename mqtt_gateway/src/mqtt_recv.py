from nameko.extensions import Entrypoint
import paho.mqtt.client as mqtt

class MqttRecv(Entrypoint):
    def __init__(self, addr, port=1883, **kwargs):
        self.addr = addr
        self.port = port
        super(MqttRecv, self).__init__(**kwargs)

    def setup(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.addr, self.port, 60)

    def start(self):
        self.container.spawn_managed_thread(
            self.client.loop_forever(), identifier="MqttRecv.run"
        )    

    def on_connect(self, client, userdata, flags, rc):
        print("MqttRecv:Connected with result code "+str(rc))

        self.client.subscribe("device/#")

    def on_message(self, client, userdata, msg):
        print("MqttRecv: on_message - ", msg.topic, msg.payload)
        args = (msg.topic, str(msg.payload))
        kwargs = {}

        self.container.spawn_worker(
            self, args, kwargs
        )

mqtt_recv = MqttRecv.decorator