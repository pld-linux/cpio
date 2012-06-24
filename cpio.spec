Summary:	GNU cpio archiving program
Summary(de):	GNU-cpio-Archivierungsprogramm 
Summary(fr):	Programme d'archivage cpio de GNU
Summary(pl):	Program archwizuj�cy na licencji GNU
Summary(tr):	GNU cpio ar�ivleme program�
Name:		cpio
Version:	2.4.2
Release:	15
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narz�dzia/Archiwizacja
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
Informationen �ber diese - etwa den Dateinamen, den Besitzer, 
Zeitstempel und Zugriffsrechte. Das Archiv kann eine andere Datei 
auf der Festplatte, ein Magnetband oder eine Pipe sein. cpio 
arbeitet mit drei Betriebsarten.

%description -l fr
cpio copie des fichiers dans ou � partir d'une archive tar ou cpio,
qui est un fichier contenant d'autres fichiers plus des informations
sur ceux-ci, comme leur nom, leur propri�taire, la date et les permissions.
L'archive peut �tre un autre fichier sur le disque, une bande ou un tube.
cpio poss�de trois modes de fonctionnement.

%description -l pl
cpio kopiuje pliki do/z archiwum cpio lub tar-a, kt�re jest pojedynczym
zbiorem zawieraj�cym pozosta�e pliki wraz z dodatkowymi
informacjami jak np. nazwa, w�a�ciciel, czas modyfikacji i prawa
dost�pu. Archiwum mo�e by� plikiem na dysku, ta�mie magetycznej, albo
potokiem. 

%description -l tr
cpio program�, cpio veya tar ar�ivlerinden dosya �eker ya da bu ar�ivlere
dosya koyar. Bu ar�ivler, dosyalar�n i�eri�inden ve ayr�ca dosyan�n ad�,
sahibi, zaman bilgileri ve eri�im haklar� gibi bilgilerden olu�ur. Ar�iv,
disk �zerinde ba�ka bir dosya, manyetik bir teyp veya bir pipe olabilir.

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
* Sat May 29 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.4.2-15]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation by Micha� Kuratczyk <kurkens@polbox.com>.
