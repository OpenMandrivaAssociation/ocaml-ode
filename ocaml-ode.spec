Name:           ocaml-ode
Version:        0.5
Release:        %mkrel 1.r4
Summary:        OCaml bindings to the Open Dynamics Engine (ODE)
License:        LGPL with exceptions
Group:          Development/Other
URL:            http://www.linux-nantes.org/~fmonnier/OCaml/ODE/
Source0:        http://www.linux-nantes.org/~fmonnier/OCaml/ODE/download/ocamlode-0.5-r4.tar.gz
Patch0:         ocamlode-0.5-r4.dPlaneSpace.patch
Patch1:         ocamlode-0.5-r4.demo_exec.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  ode-devel

%description
This is a set of bindings in Objective Caml for the Open Dynamics Engine,
ODE: http://www.ode.org/.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocamlode-0.5-r4
%patch0 -p0
%patch1 -p0

%build
make all
make doc
mkdir examples
mv drawstuff.ml drawstuff.make demo_*.ml demo_exec.sh examples/

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/ode
ocamlfind install ode META ode.cmi *.{mli,cma,cmxa,cmx,a,so}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE_BSD.txt LICENSE_GPL.txt LICENSE_LGPL.txt CHANGES.txt README.txt
%dir %{_libdir}/ocaml/ode
%{_libdir}/ocaml/ode/META
%{_libdir}/ocaml/ode/*.cma
%{_libdir}/ocaml/ode/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc examples
%{_libdir}/ocaml/ode/*.a
%{_libdir}/ocaml/ode/*.cmxa
%{_libdir}/ocaml/ode/*.cmx
%{_libdir}/ocaml/ode/*.mli

