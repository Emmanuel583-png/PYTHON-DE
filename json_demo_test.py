import json

pipeline_config = {
    "api_name" : "weather_service",
    "timeout_seconds" : "30",
    "endpoints" : ["/current", "/forecast", "/historical"],
    "retry_enabled" : True
}

with open("config.json", "w") as file:
    json.dump(pipeline_config,file, indent=4)

with open("config.json", "r") as file:
    data =json.load(file)
    print(f"pipeline {data['api_name']} uses timeout {data['timeout_seconds']} with {len(data['endpoints'])} endpoints ")
