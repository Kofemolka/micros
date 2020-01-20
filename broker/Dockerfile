FROM rabbitmq:3-management

RUN rabbitmq-plugins enable --offline rabbitmq_mqtt

ADD rabbitmq.config /etc/rabbitmq/
ADD definitions.json /etc/rabbitmq/
RUN chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.config /etc/rabbitmq/definitions.json

CMD ["rabbitmq-server"]


# COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config

# COPY start.sh .

# CMD ["./start.sh"]