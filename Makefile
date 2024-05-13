.PHONY: install test start stop deploy undeploy clean

install:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests

start:
	sh scripts/start_agents.sh

stop:
	sh scripts/stop_agents.sh

deploy:
	sh scripts/deploy.sh

undeploy:
	sh scripts/undeploy.sh

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf build dist .egg-info

# Additional targets can be added below for database setup, linting, etc.