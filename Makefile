.PHONY: install-dependencies isort black flake8

install-dependencies:
	python -m pip install --upgrade pip
	pip install isort black flake8

isort:
	isort --skip venv --skip tesseract --skip "auth compiled" --skip "utils/Crypto" --skip-glob "*__pycache__*" .

black:
	black . --exclude 'venv|tesseract|auth compiled|utils/Crypto|__pycache__'

compile:
	nuitka --clang --mingw64 --onefile --follow-imports --windows-icon-from-ico=.\Item_Gem.ico --remove-output --output-filename=Bot --windows-company-name=Unknown --windows-product-version=1.0 --onefile-tempdir-spec=C:\Users\Default\AppData\Local\Temp\bot_unknown .\app.py

publish:
	py ./utils/publish/change_language.py
	make compile
	py utils/publish/publish.py
	py utils/publish/change_language.py true
	make compile
	py utils/publish/publish.py true

test: isort black
