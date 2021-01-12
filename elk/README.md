# ELK - Elastic Logstash Kibana (and Beats and more)


Installation:
Follow https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

systemmctl start elasticsearch
curl http://localhost:9200


For experimentation:

Edit /etc/elasticsearch/elasticsearch.yml
network.host: 0.0.0.0
and also:
discovery.seed_hosts: ["127.0.0.1"]

But this will make the Elasticsearch accessible to everyone.

