%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Goofey
Summary:	Net::Goofey perl module
Summary(pl):	Modu³ perla Net::Goofey
Name:		perl-Net-Goofey
Version:	1.4
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Text-LineEditor
Requires:	perl-Text-LineEditor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Goofey - implementation of a simple Goofey client in Perl.

%description -l pl
Net::Goofey - implementacja prostego klienta Goofey w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README perlgoofey
%{perl_vendorlib}/Net/Goofey.pm
%{_mandir}/man3/*
