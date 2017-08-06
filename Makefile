PREFIX:=/usr/local
install:
	install -d $(DESTDIR)$(PREFIX)/bin/ $(DESTDIR)$(PREFIX)/lib/ $(DESTDIR)/etc/profile.d/ $(DESTDIR)/etc/sysctl.d/
	install -p -m 755 bin/* $(DESTDIR)$(PREFIX)/bin/
	install -p -m 644 lib/reproducible-faketools-lib $(DESTDIR)$(PREFIX)/lib/
	install -p -m 644 extra/disorderfs.sh $(DESTDIR)/etc/profile.d/
	echo kernel.randomize_va_space = 0 > $(DESTDIR)/etc/sysctl.d/01-disable-aslr.conf
