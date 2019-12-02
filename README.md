# docker-compose-for-env
use docker-compose build dev and stage environment
使用docker-compose启动测试服务环境，不依赖物理机；


## ELK
* docker-compose build elk stage env

### reference:
* https://www.elastic.co/guide/en/elasticsearch/reference/7.4/docker.html
* https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html


### issue
测试volume不支持local path: 
- ./es_data:/usr/share/elasticsearch/data

* links
单向link

* logstash xpack
[2019-11-13T10:27:30,787][ERROR][logstash.licensechecker.licensereader] Unable to retrieve license information from license server {:message=>"No Available connections"}



* 匹配到panic 重定向到文件

* 增加以下十行到文件
