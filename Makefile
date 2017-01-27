PREFIX:=/usr/local
BINS=date hostname uname
install:
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -p -m 755 $(BINS) $(DESTDIR)$(PREFIX)/bin/
	install -p -m 644 reproducible-faketools-lib $(DESTDIR)$(PREFIX)/bin/
