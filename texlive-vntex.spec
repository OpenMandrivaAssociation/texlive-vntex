Name:		texlive-vntex
Version:	62837
Release:	2
Summary:	Support for Vietnamese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/vietnamese/vntex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX
macros for typesetting documents in Vietnamese. Users of the
fonts (in both Metafont and Adobe Type 1 format) of this bundle
may alternatively use the lm fonts bundle, for which map files
are available to provide a Vietnamese version.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/vntex
%{_texmfdistdir}/fonts/enc/dvips/vntex
%{_texmfdistdir}/fonts/enc/pdftex/vntex
%{_texmfdistdir}/fonts/map/dvips/vntex
%{_texmfdistdir}/fonts/source/vntex
%{_texmfdistdir}/fonts/tfm/vntex
%{_texmfdistdir}/fonts/type1/vntex
%{_texmfdistdir}/fonts/vf/vntex
%{_texmfdistdir}/tex/latex/vntex
%{_texmfdistdir}/tex/plain/vntex
%_texmf_updmap_d/vntex
%doc %{_texmfdistdir}/doc/generic/vntex
#- source
%doc %{_texmfdistdir}/source/generic/vntex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/vntex <<EOF
Map arevvn.map
Map chartervn.map
Map cmbrightvn.map
Map concretevn.map
Map grotesqvn.map
Map txttvn.map
Map urwvn.map
MixedMap vnrother.map
MixedMap vnrtext.map
Map vntopia.map
EOF
