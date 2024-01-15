Summary:	GNU cpio archiving program
Summary(de.UTF-8):	GNU-cpio-Archivierungsprogramm
Summary(es.UTF-8):	Programa de empaquetado cpio de la GNU (usado por el utilitario rpm)
Summary(fr.UTF-8):	Programme d'archivage cpio de GNU
Summary(pl.UTF-8):	Program archwizujący na licencji GNU
Summary(pt_BR.UTF-8):	Programa de empacotamento cpio da GNU (usado pelo utilitário rpm)
Summary(ru.UTF-8):	Архивная программа GNU
Summary(tr.UTF-8):	GNU cpio arşivleme programı
Summary(uk.UTF-8):	Архівна програма GNU
Name:		cpio
Version:	2.15
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	https://ftp.gnu.org/gnu/cpio/%{name}-%{version}.tar.bz2
# Source0-md5:	3394d444ca1905ea56c94b628b706a0b
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	027552f4053477462a09fadc162a5e65
Patch0:		%{name}-info.patch
Patch1:		%{name}-ifdef.patch
URL:		http://www.gnu.org/software/cpio/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.16.5
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

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

%description -l de.UTF-8
GNU cpio kopiert Dateien in oder aus einem CPIO- oder Tar-Archiv.
Archive sind Dateien, die eine Sammlung anderer Dateien und
informationen über sie, wie Dateiname, Besitzer, Zugriffszeiten und
-berechtigungen, enthalten. Das Archiv kann eine andere Datei auf der
Festplatte sein, oder ein Streamerband, oder ein pipe. GNU cpio
unterstützt die archiv-Formate binary, old ASCII, new ASCII, crc, HPUX
binary, HPUX old ASCII, old tar und POSIX.1 tar. Standardmäßig erzeugt
cpio Archive im binary-Format, so daß sie mit älteren cpio-Programmen
kompatibel sind. Beim Extrahieren von Dateien aus Archiven erkennt
cpio das Format automatisch, es kann auch Archive lesen, die auf
Computern mit anderer Byteordnung erzeugt wurden.

%description -l es.UTF-8
cpio copia archivos para dentro o para fuera, o de un "archive" cpio o
tar, que es un archivo que contiene otros archivos, más información
sobre ellos, como su nombre de archivo, dueño y permisos de acceso.
"archive" puede ser otro archivo en el disco, una cinta magnética o un
pipe. cpio posee tres modos de operación.

%description -l fr.UTF-8
cpio copie des fichiers dans ou à partir d'une archive tar ou cpio,
qui est un fichier contenant d'autres fichiers plus des informations
sur ceux-ci, comme leur nom, leur propriétaire, la date et les
permissions. L'archive peut être un autre fichier sur le disque, une
bande ou un tube. cpio possède trois modes de fonctionnement.

%description -l pl.UTF-8
cpio kopiuje pliki do/z archiwum cpio lub tar-a, które jest
pojedynczym zbiorem zawierającym pozostałe pliki wraz z dodatkowymi
informacjami jak np. nazwa, właściciel, czas modyfikacji i prawa
dostępu. Archiwum może być plikiem na dysku, taśmie magnetycznej, albo
potokiem.

%description -l pt_BR.UTF-8
cpio copia arquivos para dentro ou para fora ou de um "archive" cpio
ou tar, que é um arquivo que contém outros arquivos mais informações
sobre eles, como o seu nome de arquivo, dono e permissões de acesso. O
"archive" pode ser outro arquivo no disco, uma fita magnética ou um
pipe. cpio possui três modos de operação.

%description -l ru.UTF-8
cpio копирует файлы в или из архива cpio или tar, который представляет
собой файл, содержащий другие файлы и информацию о них, такую как имя
файла, его хозяин, время создания, права доступа и т.д. Архивом может
быть файл, лента или пайп.

%description -l tr.UTF-8
cpio programı, cpio veya tar arşivlerinden dosya çeker ya da bu
arşivlere dosya koyar. Bu arşivler, dosyaların içeriğinden ve ayrıca
dosyanın adı, sahibi, zaman bilgileri ve erişim hakları gibi
bilgilerden oluşur. Arşiv, disk üzerinde başka bir dosya, manyetik bir
teyp veya bir pipe olabilir.

%description -l uk.UTF-8
cpio копіює файли в або з архіву cpio або tar, який являє собою файл,
що містить інші файли та інформацію про них, таку як ім'я файлу, його
власника, час створення, права доступу і т.і. Архівом може бути файл,
стрічка або пайп.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal} -I m4 -I am
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.cpio-non-english-man-pages

# in PLD rmt is built from tar.spec
%{__rm} $RPM_BUILD_ROOT%{_libexecdir}/rmt
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/rmt.8*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{es,ja}/man1/mt.1*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/cpio
%lang(es) %{_mandir}/es/man1/cpio.1*
%lang(hu) %{_mandir}/hu/man1/cpio.1*
%lang(ja) %{_mandir}/ja/man1/cpio.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/cpio.1*
%{_infodir}/cpio.info*
%{_mandir}/man1/cpio.1*
