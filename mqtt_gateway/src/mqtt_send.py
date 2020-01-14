from nameko.extensions import DependencyProvider
import paho.mqtt.client as mqtt

class MqttSend(DependencyProvider):
    def __init__(self, addr, port=1883, **kwargs):
        self.addr = addr
        self.port = port
        super(MqttSend, self).__init__(**kwargs)

    def setup(self):
        self.client = mqtt.Client()
        self.client.connect(self.addr, self.port, 60)
        
        self.container.spawn_managed_thread(
            self.client.loop_forever(), identifier="MqttSend.run"
        )

    def get_dependency(self, worker_ctx):

        def publish(topic, payload):            
            msg_info = self.client.publish(topic, payload)
            msg_info.wait_for_publish()

        return publish