# ELK - Elastic Logstash Kibana (and Beats and more)

## Elasticssearch

Installation:
Follow https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html
usinng
apt-get install elasticsearch

systemmctl start elasticsearch
systemmctl enable elasticsearch
curl http://localhost:9200


For experimentation:

Edit /etc/elasticsearch/elasticsearch.yml
network.host: 0.0.0.0
and also:
discovery.seed_hosts: ["127.0.0.1"]

But this will make the Elasticsearch accessible to everyone.


Map the public IP address of the server to vapiti and then you can access it as:
http://vapiti:9200/


## Kibana

apt-get install kibana

edit /etc/kibana/kibana.yml and add the line:
server.host: 0.0.0.0

systemmctl start kibana
systemmctl enable kibana

Then access as

http://vapiti:5601/

## Auditbeat

Start collecting data (on the same host)
apt-get install auditbeat


