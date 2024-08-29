Name:		texlive-zref-clever
Version:	72097
Release:	1
Summary:	Clever LaTeX cross-references based on zref
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zref-clever
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-clever.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-clever.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-clever.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a user interface for making LaTeX
cross-references which automates some of their typical
features, thus easing their input in the document and improving
the consistency of typeset results. A reference made with
\zcref includes a "name" according to its "type", and lists of
multiple labels can be automatically sorted and compressed into
ranges when due. The reference format is highly and easily
customizable, both globally and locally. The package is based
on zref's extensible referencing system.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/zref-clever
%{_texmfdistdir}/tex/latex/zref-clever
%doc %{_texmfdistdir}/doc/latex/zref-clever

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
