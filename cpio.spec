Summary:	GNU cpio archiving program
Summary(de):	GNU-cpio-Archivierungsprogramm 
Summary(fr):	Programme d'archivage cpio de GNU
Summary(pl):	Program archwizuj±cy na licencji GNU
Summary(tr):	GNU cpio arþivleme programý
Name:		cpio
Version:	2.4.2
Release:	15
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source:		ftp://prep.ai.mit.edu/pub/gnu/cpio/%{name}-%{version}.tar.gz
Patch0:		cpio-glibc.patch
Patch1:		cpio-mtime.patch
Patch2:		cpio-svr4compat.patch
Patch3:		cpio-info.patch
Patch4:		cpio-glibc21.patch
Patch5:		cpio-longlongdev.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

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
cpio kopiuje pliki do/z archiwum cpio lub tar-a, które jest pojedynczym
zbiorem zawieraj±cym pozosta³e pliki wraz z dodatkowymi
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
chmod u+w configure
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--bindir=/bin \
	--libexecdir=/sbin
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/bin \
	libexecdir=$RPM_BUILD_ROOT/sbin
	
gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/cpio*,%{_mandir}/man1/*} \
	README

%post
/sbin/install-info %{_infodir}/cpio.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/cpio.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /bin/cpio
%{_infodir}/cpio*
%{_mandir}/man1/*

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.4.2-15]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation by Micha³ Kuratczyk <kurkens@polbox.com>.
