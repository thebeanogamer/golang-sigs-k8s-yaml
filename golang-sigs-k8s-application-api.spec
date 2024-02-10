# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/kubernetes-sigs/application
%global goipath         sigs.k8s.io/application/api
%global forgeurl        https://github.com/kubernetes-sigs/application
Version:                0.8.3

%gometa -f


%global common_description %{expand:
Application metadata descriptor CRD.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md  README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Application metadata descriptor CRD

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/application %{goipath}
for cmd in e2e; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
