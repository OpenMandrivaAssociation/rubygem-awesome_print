%define oname awesome_print

Summary:    Pretty print Ruby objects with proper indentation and colors
Name:       rubygem-%{oname}
Version:    1.2.0
Release:	1
Group:      Development/Ruby
License:    GPLv2+
URL:        http://github.com/michaeldv/awesome_print
Source0:    http://rubygems.org/gems/awesome_print-1.2.0.gem
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
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean

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
