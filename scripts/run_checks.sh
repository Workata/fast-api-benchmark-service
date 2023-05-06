echo "Check typing with mypy... [command: mypy ./src/]"
mypy ./src/
echo "Format with Black... [command: black ./src/]"
black ./src/
echo "Lint with flake8... [command: flake8 ./src/]"
flake8 ./src/
echo "Test with PyTest... [command: pytest -s ./src/tests/]"
pytest -s ./src/tests/
