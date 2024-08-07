PREFIX:=/usr/local
all: build
build:
	echo "nothing to build here"
install:
	install -d $(DESTDIR)$(PREFIX)/bin/ $(DESTDIR)$(PREFIX)/lib/ $(DESTDIR)/etc/profile.d/ $(DESTDIR)/usr/lib/rpm/brp-suse.d/
	install -p -m 755 bin/* $(DESTDIR)$(PREFIX)/bin/
	cp -a lib/reproducible-faketools $(DESTDIR)$(PREFIX)/lib/
	install -p -m 644 extra/disorderfs.sh $(DESTDIR)/etc/profile.d/
	install -p -m 755 extra/brp-95-strip-nondeterminism $(DESTDIR)/usr/lib/rpm/brp-suse.d/

roundup:
	git clone https://github.com/SUSE-Cloud/roundup

test:
	make -C tests
