serve:
	 python3 -m uvicorn --reload --host 127.0.0.1 --port 8080 srv:app

test:
	curl -X 'POST' \
        'http://127.0.0.1:8080/' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{"content": "Hello world!"}'
