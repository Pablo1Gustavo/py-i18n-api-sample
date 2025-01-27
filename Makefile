run-fastapi:
	poetry run uvicorn app.fastapi.app:app --reload --port 8080

run-flask:
	poetry run flask --app app.flask.app run --reload --port 8080

compile-locale:
	find locale -mindepth 2 -type d -name "LC_MESSAGES" | while read -r dir; do \
		lang=$$(basename $$(dirname "$$dir")); \
		msgcat "$$dir"/*.po | msgfmt -o "$$dir/_app.mo" -; \
	done
