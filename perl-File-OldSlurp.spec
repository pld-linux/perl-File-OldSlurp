#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	File
%define		pnam	OldSlurp
Summary:	File::OldSlurp - single call read & write file routines; read directories
Summary(pl.UTF-8):	File::OldSlurp - funkcje odczytu i zapisu za jednym wywołaniem
Name:		perl-File-OldSlurp
Version:	2004.0430
Release:	2
License:	distributable (see README)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bc221d24ff6d0d591ab046e5fe6ac771
URL:		http://search.cpan.org/dist/File-OldSlurp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are quickie routines that are meant to save a couple of lines of
code over and over again. They do not do anything fancy.

This module used to be called File::Slurp. Uri Guttman wrote a version
with more features and more speed, so David Muir Sharnoff (author of
this module) gave the namespace to Uri. However, this version still
has some merit: it is much smaller and thus if speed of complilation
is more important that slurping speed, and you don't need the new
features, then this version is still useful.

%description -l pl.UTF-8
Ten moduł zawiera szybkie funkcje, które mają służyć do zaoszczędzenia
wpisywania tych samych linii kodu wiele razy. Nie robią niczego
fantazyjnego.

Ten moduł nazywał się kiedyś File::Slurp. Uri Guttman napisał wersję z
większymi możliwościami i szybszą, więc David Muir Sharnoff (autor
tego modułu) oddał mu przestrzeń nazw. Jednak ta wersja nadal ma pewne
zalety: jest dużo mniejsza i jeśli szybkość kompilacji ma większe
znaczenie od szybkości pracy, a nie są potrzebne nowe możliwości, ta
wersja nadal ma zastosowanie.

%prep
%setup -q -n %{pdir}-%{pnam}-2004.043

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{perl_vendorlib}/File/OldSlurp.pm
%{_mandir}/man3/*
