Name:		texlive-etl
Version:	60998
Release:	1
Summary:	Expandable token list operations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etl
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides expandable token list operations for
which expl3's l3tl only has unexpandable variants. These
expandable versions are typically slower than the unexpandable
code. Unlike the l3tl versions, the functions in this module
may contain braces and macro parameter tokens in their
arguments, but as a drawback they cannot distinguish some
tokens and do not consider the character code of group-begin
and group-end tokens. Additionally a general map to token lists
is provided, modelled after the expl3 internal __tl_act:NNNn
but with additional features. The package has no immediate use
for document authors; it only contains expl3 functions intended
for programmers.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/etl
%{_texmfdistdir}/tex/latex/etl
%doc %{_texmfdistdir}/doc/latex/etl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
