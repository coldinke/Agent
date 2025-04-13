
lint:
	flake8 main.py ./examples --count --ignore=W503 --max-line-length=127 --statistics
	mypy main.py

clean:
	rm -rf __pycache__
