start:
	docker-compose up
install:
	pip install -r requirements.txt
connector:
	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @debezium_connector/mysql.json
	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @debezium_connector/postgresql.json
seeding:
	python src/seeding_data.py
stop:
	docker-compose down