Summary:	GNU cpio archiving program
Summary(de):	GNU-cpio-Archivierungsprogramm 
Summary(fr):	Programme d'archivage cpio de GNU
Summary(pl):	Program archwizuj�cy na licencji GNU
Summary(tr):	GNU cpio ar�ivleme program�
Name:		cpio
Version:	2.4.2
Release:	17
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
Patch6:		cpio-DESTDIR.patch
Patch7:		cpio-stdout.patch
Patch8:		cpio-emptylink.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives are
files which contain a collection of other files plus information about them,
such as their file name, owner, timestamps, and access permissions.  The
archive can be another file on the disk, a magnetic tape, or a pipe.  GNU
cpio supports the following archive formats: binary, old ASCII, new ASCII,
crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1 tar.  By default, cpio
creates binary format archives, so that they are compatible with older cpio
programs.  When it is extracting files from archives, cpio automatically
recognizes which kind of archive it is reading and can read archives created
on machines with a different byte-order.

Install cpio if you need a program to manage file archives.

%description -l de
GNU cpio kopiert Dateien in oder aus einem CPIO- oder Tar-Archiv. Archive
sind Dateien, die eine Sammlung anderer Dateien und informationen �ber sie,
wie Dateiname, Besitzer, Zugriffszeiten und -berechtigungen, enthalten. Das
Archiv kann eine andere Datei auf der Festplatte sein, oder ein
Streamerband, oder ein pipe. GNU cpio unterst�tzt die archiv-Formate binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar und POSIX.1
tar. Standardm��ig erzeugt cpio Archive im binary-Format, so da� sie mit
�lteren cpio-Programmen kompatibel sind. Beim Extrahieren von Dateien aus
Archiven erkennt cpio das Format automatisch, es kann auch Archive lesen,
die auf Computern mit anderer Byteordnung erzeugt wurden.

%description -l fr
cpio copie des fichiers dans ou � partir d'une archive tar ou cpio,
qui est un fichier contenant d'autres fichiers plus des informations
sur ceux-ci, comme leur nom, leur propri�taire, la date et les permissions.
L'archive peut �tre un autre fichier sur le disque, une bande ou un tube.
cpio poss�de trois modes de fonctionnement.

%description -l pl
cpio kopiuje pliki do/z archiwum cpio lub tar-a, kt�re jest pojedynczym
zbiorem zawieraj�cym pozosta�e pliki wraz z dodatkowymi informacjami jak np.
nazwa, w�a�ciciel, czas modyfikacji i prawa dost�pu. Archiwum mo�e by�
plikiem na dysku, ta�mie magetycznej, albo potokiem.

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
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
LDFLAGS="-s"; export LDFLAGS 
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT 
	
gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/cpio*,%{_mandir}/man1/*} \
	README

%post
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /bin/cpio
%{_infodir}/cpio*
%{_mandir}/man1/cpio.*
