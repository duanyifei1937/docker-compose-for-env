 - alert: log-logstash-SOS
    expr: namedprocess_namegroup_num_procs{groupname="map[:/etc/logstash]",hostname="log",instance="10.111.209.191",job="process-exporter"} == 0
    labels:
      service: system
      severity: SOS
    annotations:
      description: "{{ $labels.instance }}   prod-log logstash process 异常退出(panic stdout 无法落盘)"
      
      
# default:

process_names:
  - name: "{{.Comm}}"
    cmdline:
    - '.+'
    
namedprocess_namegroup_num_procs{groupname="java",instance="process-exporter:9256",job="process local"}	



