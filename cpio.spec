Summary:	GNU cpio archiving program
Summary(de):	GNU-cpio-Archivierungsprogramm 
Summary(fr):	Programme d'archivage cpio de GNU
Summary(pl):	Program archwizuj±cy na licencji GNU
Summary(tr):	GNU cpio arþivleme programý
Name:		cpio
Version:	2.4.2
Release:	23
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://prep.ai.mit.edu/pub/gnu/cpio/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-mtime.patch
Patch2:		%{name}-svr4compat.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-glibc21.patch
Patch5:		%{name}-longlongdev.patch
Patch6:		%{name}-DESTDIR.patch
Patch7:		%{name}-stdout.patch
Patch8:		%{name}-emptylink.patch
Patch9:		%{name}-errorcode.patch
Patch10:	%{name}-gethostname_is_in_libc_aka_no_libnsl.patch
Patch11:	%{name}-man.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
GNU cpio copies files into or out of a cpio or tar archive. Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions. The archive can be another file on the disk, a magnetic
tape, or a pipe. GNU cpio supports the following archive formats:
binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old
tar and POSIX.1 tar. By default, cpio creates binary format archives,
so that they are compatible with older cpio programs. When it is
extracting files from archives, cpio automatically recognizes which
kind of archive it is reading and can read archives created on
machines with a different byte-order.

%description -l de
GNU cpio kopiert Dateien in oder aus einem CPIO- oder Tar-Archiv.
Archive sind Dateien, die eine Sammlung anderer Dateien und
informationen über sie, wie Dateiname, Besitzer, Zugriffszeiten und
-berechtigungen, enthalten. Das Archiv kann eine andere Datei auf
der Festplatte sein, oder ein Streamerband, oder ein pipe. GNU cpio
unterstützt die archiv-Formate binary, old ASCII, new ASCII, crc, HPUX
binary, HPUX old ASCII, old tar und POSIX.1 tar. Standardmäßig erzeugt
cpio Archive im binary-Format, so daß sie mit älteren cpio-Programmen
kompatibel sind. Beim Extrahieren von Dateien aus Archiven erkennt
cpio das Format automatisch, es kann auch Archive lesen, die auf
Computern mit anderer Byteordnung erzeugt wurden.

%description -l fr
cpio copie des fichiers dans ou à partir d'une archive tar ou cpio,
qui est un fichier contenant d'autres fichiers plus des informations
sur ceux-ci, comme leur nom, leur propriétaire, la date et les
permissions. L'archive peut être un autre fichier sur le disque, une
bande ou un tube. cpio possède trois modes de fonctionnement.

%description -l pl
cpio kopiuje pliki do/z archiwum cpio lub tar-a, które jest
pojedynczym zbiorem zawieraj±cym pozosta³e pliki wraz z dodatkowymi
informacjami jak np. nazwa, w³a¶ciciel, czas modyfikacji i prawa
dostêpu. Archiwum mo¿e byæ plikiem na dysku, ta¶mie magetycznej, albo
potokiem.

%description -l tr
cpio programý, cpio veya tar arþivlerinden dosya çeker ya da bu
arþivlere dosya koyar. Bu arþivler, dosyalarýn içeriðinden ve ayrýca
dosyanýn adý, sahibi, zaman bilgileri ve eriþim haklarý gibi
bilgilerden oluþur. Arþiv, disk üzerinde baþka bir dosya, manyetik bir
teyp veya bir pipe olabilir.

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
%patch9 -p1
%patch10 -p1
%patch11 -p1
chmod -R a+Xr,u+Xw .

%build
autoconf
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT 
	
gzip -9nf README

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /bin/cpio
%{_infodir}/cpio*
%{_mandir}/man1/cpio.*
