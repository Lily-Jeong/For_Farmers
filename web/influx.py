import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import certifi

bucket = "ForPROJECT"
org = "cb0eab07a714b4be"
token = "uB7DjgLMtFSL1R4ID7Z509-dx5mol8xXSJOPS6mLjMM_olf137dhu3cURNKz8QOi1dK_HlbedmaoeGrxqwudww=="
url="https://europe-west1-1.gcp.cloud2.influxdata.com/"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org,
   ssl_ca_cert=certifi.where()
)

query_api = client.query_api()

query_h_avg = 'from(bucket:"ForPROJECT")\
|> range(start: -5m)\
|> filter(fn:(r) => r._measurement == "Sensor")\
|> filter(fn:(r) => r.SSID == "KT_GiGA_2G_Wave2_8B8E")\
|> filter(fn:(r) => r._field == "Humidity")\
|> filter(fn:(r) => r.device == "ESP8266")\
|> timedMovingAverage(every: 5m, period: 1h)\
    '
humidity_avg = query_api.query(org=org, query=query_h_avg)
results = []
for table in humidity_avg:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results[0])