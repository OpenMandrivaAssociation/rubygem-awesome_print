%define oname awesome_print

Summary:    Pretty print Ruby objects with proper indentation and colors
Name:       rubygem-%{oname}
Version:    0.4.0
Release:	2
Group:      Development/Ruby
License:    GPLv2+
URL:        http://github.com/michaeldv/awesome_print
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(rspec) >= 2.5.0
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Great Ruby dubugging companion: pretty print Ruby objects to visualize their
structure. Supports Rails ActiveRecord objects via included mixin.

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/init.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/rails/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Wed Sep 07 2011 Alexander Barakin <abarakin@mandriva.org> 0.4.0-1
+ Revision: 698560
- imported package rubygem-awesome_print

* Wed Dec 01 2010 Rémy Clouard <shikamaru@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 604597
- import rubygem-awesome_print

