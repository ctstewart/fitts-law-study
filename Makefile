.PHONY: build clean

build:
	echo "Hello"
	pyinstaller main.py -y
	cp consent_form.md dist/main/
	zip dist/main.zip dist/main/*

clean:
	rm -rf build/ dist/ __pycache__ main.spec