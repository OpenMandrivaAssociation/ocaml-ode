Name:           ocaml-ode
Version:        0.5r4
Release:        2
Summary:        OCaml bindings to the Open Dynamics Engine (ODE)
License:        LGPL with exceptions
Group:          Development/Other
URL:            http://www.linux-nantes.org/~fmonnier/OCaml/ODE/
Source0:        http://www.linux-nantes.org/~fmonnier/OCaml/ODE/download/ocamlode-0.5-r4.tar.gz
Patch0:         ocamlode-0.5-r4.dPlaneSpace.patch
Patch1:         ocamlode-0.5-r4.demo_exec.patch
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
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
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/ode
ocamlfind install ode META ode.cmi *.{mli,cma,cmxa,cmx,a,so}

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



%changelog
* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 0.5-1.r4mdv2010.0
+ Revision: 415930
- import ocaml-ode


