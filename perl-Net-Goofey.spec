%include	/usr/lib/rpm/macros.perl
Summary:	Net-Goofey perl module
Summary(pl):	Modu� perla Net-Goofey
Name:		perl-Net-Goofey
Version:	1.4
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Goofey-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Text-LineEditor
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Text-LineEditor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Goofey - implementation of a simple Goofey client in Perl.

%description -l pl
Net-Goofey - implementacja prostego klienta Goofey w Perlu.

%prep
%setup -q -n Net-Goofey-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/Goofey
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz perlgoofey

%{perl_sitelib}/Net/Goofey.pm
%{perl_sitearch}/auto/Net/Goofey

%{_mandir}/man3/*
