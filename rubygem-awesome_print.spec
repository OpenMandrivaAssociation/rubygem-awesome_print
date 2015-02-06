%define rbname awesome_print

Summary:	Pretty print Ruby objects with proper indentation and colors
Name:		rubygem-%{rbname}
Version:	1.2.0
Release:	2
License:	GPLv2+
Group:		Development/Ruby
Url:		http://rubygems.org/gems/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
Great Ruby dubugging companion: pretty print Ruby objects to visualize their
structure. Supports Rails ActiveRecord objects via included mixin.

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}/
%{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 1.2.0

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

