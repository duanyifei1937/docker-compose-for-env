# filebeat

* pipelining
Configures number of batches to be sent asynchronously to logstash while waiting for ACK from logstash. Output only becomes blocking once number of `pipelining` batches have been written. Pipelining is disabled if a value of 0 is configured. The default value is 2.


# logstash.instance * pipeline.worker * pipeline.batch.size * filebeat.pipelining(2) *  ~= filebeat.queue * 1/2


1 * 2 * 2500 * 2 = 10000