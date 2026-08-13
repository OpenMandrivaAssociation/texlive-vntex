%global tl_name vntex
%global tl_revision 79618
%global tl_version 3.2.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Support for Vietnamese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/vietnamese/vntex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX macros for
typesetting documents in Vietnamese. Users of the fonts (in both
Metafont and Adobe Type 1 format) of this bundle may alternatively use
the lm fonts bundle, for which map files are available to provide a
Vietnamese version.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from vntex:
Map arevvn.map
Map chartervn.map
Map cmbrightvn.map
Map concretevn.map
Map grotesqvn.map
Map txttvn.map
Map urwvn.map
Map vntopia.map
MixedMap vnrother.map
MixedMap vnrtext.map
TL_DROPIN_EOF
