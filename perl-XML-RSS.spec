%define upstream_name	 XML-RSS
%define upstream_version 1.49

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Creates and updates RSS files
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

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


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.490.0-1mdv2011.0
+ Revision: 654383
- update to new version 1.49

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.480.0-1mdv2011.0
+ Revision: 539088
- update to 1.48

* Wed Dec 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.470.0-1mdv2010.1
+ Revision: 475399
- update to 1.47

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.460.0-1mdv2010.1
+ Revision: 460777
- update to 1.46

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.450.0-1mdv2010.0
+ Revision: 410631
- update to 1.45

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.440.0-1mdv2010.0
+ Revision: 408247
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.44-1mdv2010.0
+ Revision: 370250
- update to new version 1.44

* Tue Jan 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.43-1mdv2009.1
+ Revision: 328900
- update to new version 1.43

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-1mdv2009.1
+ Revision: 324522
- update to new version 1.42

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.41-1mdv2009.1
+ Revision: 311966
- update to new version 1.41

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-1mdv2009.1
+ Revision: 309316
- update to new version 1.40

* Fri Nov 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2009.1
+ Revision: 307435
- update to new version 1.38

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.37-1mdv2009.1
+ Revision: 305756
- update to new version 1.37

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2009.1
+ Revision: 292361
- update to new version 1.36

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.33-2mdv2009.0
+ Revision: 268882
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.33-1mdv2009.0
+ Revision: 217102
- update to new version 1.33

* Sat Feb 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2008.1
+ Revision: 164622
- update to new version 1.32

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.31-1mdv2008.0
+ Revision: 46232
- 1.31


* Sat Jan 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.22-1mdv2007.0
+ Revision: 104840
- 1.22

* Wed Jan 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2007.1
+ Revision: 103642
- fix build dependencies
- fix build dependencies

  + Olivier Thauvin <nanardon@mandriva.org>
    - 1.21
    - Import perl-XML-RSS

* Thu Mar 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.10-1mdk
- 1.10

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.05-2mdk
- Rebuild, fix URL, change description, add tests

* Tue Aug 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.05-1mdk
- 1.05
- Update description

* Thu Apr 22 2004 Michael Scherer <misc@mandrake.org> 1.04-1mdk
- New release 1.04
- [DIRM]

