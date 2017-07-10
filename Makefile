PREFIX:=/usr/local
install:
	install -d $(DESTDIR)$(PREFIX)/bin/ $(DESTDIR)$(PREFIX)/lib/ $(DESTDIR)/etc/profile.d/
	install -p -m 755 bin/* $(DESTDIR)$(PREFIX)/bin/
	install -p -m 644 extra/disorderfs.sh $(DESTDIR)/etc/profile.d/
	install -p -m 644 lib/reproducible-faketools-lib $(DESTDIR)$(PREFIX)/lib/
