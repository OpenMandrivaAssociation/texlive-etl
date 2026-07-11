%global tl_name etl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Expandable token list operations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides expandable token list operations for which expl3's
l3tl only has unexpandable variants. These expandable versions are
typically slower than the unexpandable code. Unlike the l3tl versions,
the functions in this module may contain braces and macro parameter
tokens in their arguments, but as a drawback they cannot distinguish
some tokens and do not consider the character code of group-begin and
group-end tokens. Additionally a general map to token lists is provided,
modelled after the expl3 internal __tl_act:NNNn but with additional
features. The package has no immediate use for document authors; it only
contains expl3 functions intended for programmers.

