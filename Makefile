test:
	pytest -s -v test/test_parser.py --doctest-modules --cov stock_pandas --cov-config=.coveragerc --cov-report term-missing

lint:
	flake8 stock_pandas

fix:
	autopep8 --in-place --aggressive -r stock_pandas

install:
	pip install -r requirements.txt -r test-requirements.txt

report:
	codecov

build: stock_pandas
	rm -rf dist
	python setup.py sdist bdist_wheel

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

.PHONY: test
