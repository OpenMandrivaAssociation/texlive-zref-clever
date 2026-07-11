%global tl_name zref-clever
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Clever LaTeX cross-references based on zref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zref-clever
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-clever.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-clever.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-clever.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(oberdiek)
Requires:	texlive(zref)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a user interface for making LaTeX cross-references
which automates some of their typical features, thus easing their input
in the document and improving the consistency of typeset results. A
reference made with \zcref includes a "name" according to its "type",
and lists of multiple labels can be automatically sorted and compressed
into ranges when due. The reference format is highly and easily
customizable, both globally and locally. The package is based on zref's
extensible referencing system.

