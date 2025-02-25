# template: foreman_plugin

%global gem_name foreman_google
%global plugin_name google
%global foreman_min_version 3.13.0

Name: rubygem-%{gem_name}
Version: 3.0.5
Release: 1%{?foremandist}%{?dist}
Summary: Google Compute Engine plugin for the Foreman
License: GPLv3
URL: https://github.com/theforeman/foreman_google
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Foreman 3.5 dropped the gce compute provider and this is the replacement
Obsoletes: foreman-gce < 3.5.0-1

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildRequires: rubygem(google-apis-compute_v1) = 0.54.0
BuildRequires: rubygem(google-cloud-compute) = 0.5.0
BuildRequires: rubygem(google-protobuf) = 3.24.3
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 12.0.1
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: (npm(react-intl) >= 2.8.0 with npm(react-intl) < 3.0.0)
# end package.json dependencies BuildRequires

%description
Google Compute Engine plugin for the Foreman.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Tue Feb 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.5-1
- Update to 3.0.5

* Thu Feb 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.4-1
- Update to 3.0.4

* Sun Nov 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.2-1
- Update to 3.0.2

* Fri Sep 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.0-1
- Update to 3.0.0

* Tue May 07 2024 Evgeni Golov - 2.0.1-2
- Rebuild for Webpack asset compression

* Sun Apr 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.1-1
- Update to 2.0.1

* Wed Jan 31 2024 Evgeni Golov - 2.0.0-2
- Rebuild for Webpack 5

* Sun Dec 31 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.0.0-1
- Update to 2.0.0

* Wed May 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.0.4-1
- Update to 1.0.4

* Mon Feb 06 2023 Leos Stejskal <lstejska@redhat.com> 1.0.3-1
- Update to 1.0.3

* Tue Jan 31 2023 Leos Stejskal <lstejska@redhat.com> 1.0.2-1
- Update to 1.0.2

* Thu Jan 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.0.1-1
- Update to 1.0.1

* Mon Nov 07 2022 Leos Stejskal <lstejska@redhat.com> 1.0.0-1
- Update to 1.0.0

* Mon Oct 31 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.2-2
- Mark as a replacement for foreman-gce

* Thu Oct 06 2022 Leos Stejskal <lstejska@redhat.com> 0.0.2-1
- Update to 0.0.2

* Thu Oct 06 2022 Leos Stejskal <lstejska@redhat.com> 0.0.1-1
- Add rubygem-foreman_google generated by gem2rpm using the foreman_plugin template

