%define upstream_name	 XML-RSS
%define upstream_version 1.45

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Creates and updates RSS files
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Test::Manifest)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(HTML::Entities)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
Creates and updates RSS files.
This module supports versions 0.9, 0.91 and 1.0 of RSS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
