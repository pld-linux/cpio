Summary:     GNU cpio archiving program
Summary(de): GNU-cpio-Archivierungsprogramm 
Summary(fr): Programme d'archivage cpio de GNU
Summary(pl): Program archwizuj±cy GNU
Summary(tr): GNU cpio arþivleme programý
Name:        cpio
Version:     2.4.2
Release:     10
Copyright:   GPL
Group:       Utilities/Archiving
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch1:      cpio-2.4.2-glibc.patch
Patch2:      cpio-2.4.2-mtime.patch
Patch3:      cpio-2.4.2-svr4compat.patch
Prereq:      /sbin/install-info /sbin/rmt
Buildroot:   /tmp/%{name}-%{version}-root

%description
cpio copies files into or out of a cpio or tar archive, which is a
file that contains other files plus information about them, such as
their file name, owner, timestamps, and access permissions.  The
archive can be another file on the disk, a magnetic tape, or a pipe.
cpio has three operating modes.

%description -l de
cpio erstellt Kopien von Dateien in oder von einem cpio- oder tar-
Archiv. Die Dateien enthalten andere Dateien, zusammen mit 
Informationen über diese - etwa den Dateinamen, den Besitzer, 
Zeitstempel und Zugriffsrechte. Das Archiv kann eine andere Datei 
auf der Festplatte, ein Magnetband oder eine Pipe sein. cpio 
arbeitet mit drei Betriebsarten.

%description -l fr
cpio copie des fichiers dans ou à partir d'une archive tar ou cpio,
qui est un fichier contenant d'autres fichiers plus des informations
sur ceux-ci, comme leur nom, leur propriétaire, la date et les permissions.
L'archive peut être un autre fichier sur le disque, une bande ou un tube.
cpio possède trois modes de fonctionnement.

%description -l pl
cpio kopiuje pliki do/z archiwum cpio lub tar-a, które jest pojedyñczym
zbiorem zawieraj±cym zawarto¶æ pozosta³ych plików wraz z dodatkowymi
informacjami jak np. nazwa, w³a¶ciciel, czas modyfikacji i prawa
dostêpu. Archiwum mo¿e byæ plikiem na dysku, ta¶mie magetycznej, albo
potokiem. 

%description -l tr
cpio programý, cpio veya tar arþivlerinden dosya çeker ya da bu arþivlere
dosya koyar. Bu arþivler, dosyalarýn içeriðinden ve ayrýca dosyanýn adý,
sahibi, zaman bilgileri ve eriþim haklarý gibi bilgilerden oluþur. Arþiv,
disk üzerinde baþka bir dosya, manyetik bir teyp veya bir pipe olabilir.

%prep
%setup -q
# patch 0 not applied
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .svr4compat

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr \
	--bindir=/bin \
	--libexecdir=/sbin
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/man/man1}

install -s cpio $RPM_BUILD_ROOT/bin/cpio
install cpio.1 $RPM_BUILD_ROOT/usr/man/man1/cpio.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644, root, root, 755) %doc README
%attr(755, root, root) /bin/cpio
%attr(644, root,  man) /usr/man/man1/cpio.1

%changelog
* Wed Sep 23 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [2.4.2-10]
- added pl translation.

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- Fiddle bindir/libexecdir to get RH install correct.
- Don't include /sbin/rmt -- use the rmt from dump package.
- Don't include /bin/mt -- use the mt from mt-st package.
- Add prereq's

* Tue Jun 30 1998 Jeff Johnson <jbj@redhat.com>
- fix '-c' to duplicate svr4 behavior (problem #438)
- install support programs & info pages

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot
- removed "(used by RPM)" comment in Summary

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- no longer statically linked as RPM doesn't use cpio for unpacking packages
