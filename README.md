# Prueba Backend Merqueo

## How to test
- virtualenv -p python3 env
- source env/bin/activate
- coverage run --source . -m pytest -c test/pytest.ini -vv --disable-warnings

##Coverage
The coverage report will be saved in the htmlcov folder generated for the previous command.
