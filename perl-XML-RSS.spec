%define module	XML-RSS
%define name	perl-%{module}
%define version 1.31
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Creates and updates RSS files
License:	GPL
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Test::Manifest)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(HTML::Entities)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Creates and updates RSS files.
This module supports versions 0.9, 0.91 and 1.0 of RSS.

%prep
%setup -q -n %{module}-%{version}
chmod ogu-x README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


