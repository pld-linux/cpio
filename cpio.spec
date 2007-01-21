Summary:	GNU cpio archiving program
Summary(de):	GNU-cpio-Archivierungsprogramm
Summary(es):	Programa de empaquetado cpio de la GNU (usado por el utilitario rpm)
Summary(fr):	Programme d'archivage cpio de GNU
Summary(pl):	Program archwizuj±cy na licencji GNU
Summary(pt_BR):	Programa de empacotamento cpio da GNU (usado pelo utilitário rpm)
Summary(ru):	áÒÈÉ×ÎÁÑ ÐÒÏÇÒÁÍÍÁ GNU
Summary(tr):	GNU cpio arþivleme programý
Summary(uk):	áÒÈ¦×ÎÁ ÐÒÏÇÒÁÍÁ GNU
Name:		cpio
Version:	2.7
Release:	2
License:	GPL v2+
Group:		Applications/Archiving
Source0:	ftp://ftp.gnu.org/gnu/cpio/%{name}-%{version}.tar.bz2
# Source0-md5:	69ad6cb3d288aafe5f969f68d9fd0fb7
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	027552f4053477462a09fadc162a5e65
Patch0:		%{name}-info.patch
Patch1:		%{name}-locale.patch
Patch2:		%{name}-CAN_2005_111.patch
Patch3:		%{name}-link.patch
URL:		http://www.gnu.org/software/cpio/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gettext-devel >= 0.16
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

%description -l de
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

%description -l es
cpio copia archivos para dentro o para fuera, o de un "archive" cpio o
tar, que es un archivo que contiene otros archivos, más información
sobre ellos, como su nombre de archivo, dueño y permisos de acceso.
"archive" puede ser otro archivo en el disco, una cinta magnética o un
pipe. cpio posee tres modos de operación.

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
dostêpu. Archiwum mo¿e byæ plikiem na dysku, ta¶mie magnetycznej, albo
potokiem.

%description -l pt_BR
cpio copia arquivos para dentro ou para fora ou de um "archive" cpio
ou tar, que é um arquivo que contém outros arquivos mais informações
sobre eles, como o seu nome de arquivo, dono e permissões de acesso. O
"archive" pode ser outro arquivo no disco, uma fita magnética ou um
pipe. cpio possui três modos de operação.

%description -l ru
cpio ËÏÐÉÒÕÅÔ ÆÁÊÌÙ × ÉÌÉ ÉÚ ÁÒÈÉ×Á cpio ÉÌÉ tar, ËÏÔÏÒÙÊ ÐÒÅÄÓÔÁ×ÌÑÅÔ
ÓÏÂÏÊ ÆÁÊÌ, ÓÏÄÅÒÖÁÝÉÊ ÄÒÕÇÉÅ ÆÁÊÌÙ É ÉÎÆÏÒÍÁÃÉÀ Ï ÎÉÈ, ÔÁËÕÀ ËÁË ÉÍÑ
ÆÁÊÌÁ, ÅÇÏ ÈÏÚÑÉÎ, ×ÒÅÍÑ ÓÏÚÄÁÎÉÑ, ÐÒÁ×Á ÄÏÓÔÕÐÁ É Ô.Ä. áÒÈÉ×ÏÍ ÍÏÖÅÔ
ÂÙÔØ ÆÁÊÌ, ÌÅÎÔÁ ÉÌÉ ÐÁÊÐ.

%description -l tr
cpio programý, cpio veya tar arþivlerinden dosya çeker ya da bu
arþivlere dosya koyar. Bu arþivler, dosyalarýn içeriðinden ve ayrýca
dosyanýn adý, sahibi, zaman bilgileri ve eriþim haklarý gibi
bilgilerden oluþur. Arþiv, disk üzerinde baþka bir dosya, manyetik bir
teyp veya bir pipe olabilir.

%description -l uk
cpio ËÏÐ¦À¤ ÆÁÊÌÉ × ÁÂÏ Ú ÁÒÈ¦×Õ cpio ÁÂÏ tar, ÑËÉÊ Ñ×ÌÑ¤ ÓÏÂÏÀ ÆÁÊÌ,
ÝÏ Í¦ÓÔÉÔØ ¦ÎÛ¦ ÆÁÊÌÉ ÔÁ ¦ÎÆÏÒÍÁÃ¦À ÐÒÏ ÎÉÈ, ÔÁËÕ ÑË ¦Í'Ñ ÆÁÊÌÕ, ÊÏÇÏ
×ÌÁÓÎÉËÁ, ÞÁÓ ÓÔ×ÏÒÅÎÎÑ, ÐÒÁ×Á ÄÏÓÔÕÐÕ ¦ Ô.¦. áÒÈ¦×ÏÍ ÍÏÖÅ ÂÕÔÉ ÆÁÊÌ,
ÓÔÒ¦ÞËÁ ÁÂÏ ÐÁÊÐ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
