PREFIX:=/usr/local
BINS=date hostname uname
install:
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -p -m 755 $(BINS) $(DESTDIR)$(PREFIX)/bin/
