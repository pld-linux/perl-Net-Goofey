%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Net-Goofey perl module
Summary(pl):	Modu³ perla Net-Goofey
Name:		perl-Net-Goofey
Version:	0.9
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Goofey-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

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
%doc README.gz client.pl

%{perl_sitelib}/Net/Goofey.pm
%{perl_sitearch}/auto/Net/Goofey

%{_mandir}/man3/*
