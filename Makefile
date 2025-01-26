run-fastapi:
	poetry run uvicorn app.fastapi.app:app --reload

compile-locale:
	find locale -mindepth 2 -type d -name "LC_MESSAGES" | while read -r dir; do \
		lang=$$(basename $$(dirname "$$dir")); \
		msgcat "$$dir"/*.po | msgfmt -o "$$dir/_app.mo" -; \
	done
