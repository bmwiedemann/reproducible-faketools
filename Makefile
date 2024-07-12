PREFIX:=/usr/local
install:
	install -d $(DESTDIR)$(PREFIX)/bin/ $(DESTDIR)$(PREFIX)/lib/ $(DESTDIR)/etc/profile.d/
	install -p -m 755 bin/* $(DESTDIR)$(PREFIX)/bin/
	cp -a lib/reproducible-faketools $(DESTDIR)$(PREFIX)/lib/
	install -p -m 644 extra/disorderfs.sh $(DESTDIR)/etc/profile.d/

roundup:
	git clone https://github.com/SUSE-Cloud/roundup

test:
	cd tests && ./roundup.sh
