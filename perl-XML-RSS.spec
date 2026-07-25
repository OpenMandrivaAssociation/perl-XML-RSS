%define upstream_name	 XML-RSS
%define upstream_version 1.65

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Creates and updates RSS files

License:	GPL
Group:		Development/Perl
Url:		https://github.com/shlomif/perl-XML-RSS
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-RSS-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Test::Manifest)
BuildRequires:	perl(DateTime::Format::W3CDTF)
BuildRequires:	perl(DateTime::Format::Mail)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(HTML::Entities)
BuildArch:	noarch

%description
Creates and updates RSS files.
This module supports versions 0.9, 0.91 and 1.0 of RSS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod ogu-x README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML



