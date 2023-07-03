all: writeup

writeup: writeup.sh
	@if echo $$PATH | grep -q $$HOME/opt/bin; then \
		install $< ~/opt/bin/$@; \
    else \
        echo '~/opt/binを$$PATHに追加してください。'; \
	fi

clean:
	rm ~/opt/bin/writeup
