Name:           byacc
Version:        20100216
Release:        1
Summary:        LALR(1) parser generator
Group:          Development/Languages/C and C++
License:        SUSE-Public-Domain
Url:            http://invisible-island.net/byacc/byacc.html
Source:         http://invisible-island.net/datafiles/release/byacc.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Berkeley Yacc is a LALR(1) parser generator. It has been made as compatible as
possible with AT&T Yacc and it accepts any input specification that conforms to
the AT&T Yacc documentation. In contrast to bison, it is written to avoid
dependencies upon a particular compiler.

%prep
%setup

%build
# without --with-warnings several functions will not be marked with gcc's
# noreturn attribute and produce warnings when $RPM_OPT_FLAGS contains -Wall
%configure --with-warnings
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_bindir}/yacc %{buildroot}%{_bindir}/byacc

%remove_docs

%files
%defattr(-,root,root,-)
%{_bindir}/byacc

%changelog
