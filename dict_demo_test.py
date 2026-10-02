pipeline_config: dict[str, int] = {"batch_size": 500, "db_name": "production_db"}

retries: int = pipeline_config.get("retry_attempt", 3)

pipeline_config["status"] = "ACTIVE"

for key,value in pipeline_config.items():
    print(f"KEY: {key} | VALUE: {value}")

print(f"\n safely retried retries: {retries}")

