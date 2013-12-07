# revision 30579
# category Package
# catalog-ctan /language/vietnamese/vntex
# catalog-date 2013-05-19 14:33:40 +0200
# catalog-license other-free
# catalog-version 3.2
Name:		texlive-vntex
Version:	3.2
Release:	7
Summary:	Support for Vietnamese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/vietnamese/vntex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vntex.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/vntex/chartervn/bchb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/chartervn/bchbi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/chartervn/bchr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/chartervn/bchri8v.afm
%{_texmfdistdir}/fonts/afm/vntex/grotesqvn/ugqb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/fplrc8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uagd8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uagdo8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uagk8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uagko8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ubkd8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ubkdi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ubkl8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ubkli8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ucrb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ucrbo8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ucrr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/ucrro8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uhvb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uhvbo8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uhvr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uhvro8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uncb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uncbi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uncr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uncri8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uplb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uplbi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uplr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uplri8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/utmb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/utmbi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/utmr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/utmri8v.afm
%{_texmfdistdir}/fonts/afm/vntex/urwvn/uzcmi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/vntopia/putb8v.afm
%{_texmfdistdir}/fonts/afm/vntex/vntopia/putbi8v.afm
%{_texmfdistdir}/fonts/afm/vntex/vntopia/putr8v.afm
%{_texmfdistdir}/fonts/afm/vntex/vntopia/putri8v.afm
%{_texmfdistdir}/fonts/enc/dvips/vntex/t5.enc
%{_texmfdistdir}/fonts/enc/pdftex/vntex/t5d.enc
%{_texmfdistdir}/fonts/enc/pdftex/vntex/t5uni.enc
%{_texmfdistdir}/fonts/map/dvips/vntex/arevvn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/chartervn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/cmbrightvn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/concretevn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/grotesqvn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/txttvn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/urwvn.map
%{_texmfdistdir}/fonts/map/dvips/vntex/vnrother.map
%{_texmfdistdir}/fonts/map/dvips/vntex/vnrtext.map
%{_texmfdistdir}/fonts/map/dvips/vntex/vntopia.map
%{_texmfdistdir}/fonts/source/vntex/vnr/vnaccent.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnacomp.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnb10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbase.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx5.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx6.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx7.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbx9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbxsl10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnbxti10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vncligtb.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vncode.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vncombac.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vncsc.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vncsc10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vndothook.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vndunh10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnecomp.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnff10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnfi10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnfib8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnicomp.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vniligtb.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnitt10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlacc.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlai.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlar.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnldi.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnldr.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlei.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnler.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlii.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlir.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnloi.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlor.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlui.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlur.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlyi.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnlyr.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnminus.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnmligtb.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnocomp.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr17.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr5.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr6.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr7.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnr9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnrligtb.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnrm.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnroman.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnsl10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnsl12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnsl8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnsl9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnsltt10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnss10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnss12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnss17.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnss8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnss9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssbx10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssdc10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssi10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssi12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssi17.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssi8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssi9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssq8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnssqi8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vntcsc10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vntextit.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnti10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnti12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnti7.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnti8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnti9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vntt10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vntt12.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vntt8.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vntt9.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnu10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuacc.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuar.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnucomp.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnudr.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuer.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuir.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuor.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuur.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnuyr.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnvtt10.mf
%{_texmfdistdir}/fonts/source/vntex/vnr/vnycomp.mf
%{_texmfdistdir}/fonts/tfm/vntex/arevvn/favb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/arevvn/favbi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/arevvn/favr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/arevvn/favri8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchbi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchri8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/chartervn/bchro8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbr10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbr17.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbr8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbr9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbrbx10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbrsl10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbrsl17.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbrsl8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmbrsl9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmsltl10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/cmbrightvn/vncmtl10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/concretevn/vncccsc10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/concretevn/vnccr10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/concretevn/vnccsl10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/concretevn/vnccti10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/grotesqvn/ugqb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/grotesqvn/ugqbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/txttvn/txbtt8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/txttvn/txbttsc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/txttvn/txbttsl8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/txttvn/txtt8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/txttvn/txttsc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/txttvn/txttsl8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/fplrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uagd8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uagdc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uagdo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uagk8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uagkc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uagko8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubkd8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubkdc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubkdi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubkdo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubkl8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubklc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubkli8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ubklo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ucrb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ucrbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ucrbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ucrr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ucrrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/ucrro8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uhvb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uhvbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uhvbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uhvr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uhvrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uhvro8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncbi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncri8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uncro8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplbi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplri8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uplro8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmbi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmri8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/utmro8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/urwvn/uzcmi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnb10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx5.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx6.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx7.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbx9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnbxti10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vncsc10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vndunh10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnff10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnfi10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnfib8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnitt10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr17.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr5.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr6.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr7.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnr9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnsl10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnsl12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnsl8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnsl9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnsltt10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnss10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnss12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnss17.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnss8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnss9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssbx10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssdc10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssi10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssi12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssi17.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssi8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssi9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssq8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnssqi8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vntcsc10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnti10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnti12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnti7.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnti8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnti9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vntt10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vntt12.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vntt8.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vntt9.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnu10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vnr/vnvtt10.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putb8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putbc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putbi8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putbo8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putr8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putrc8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putri8v.tfm
%{_texmfdistdir}/fonts/tfm/vntex/vntopia/putro8v.tfm
%{_texmfdistdir}/fonts/type1/vntex/arevvn/ArevSans-Bold-T5.pfb
%{_texmfdistdir}/fonts/type1/vntex/arevvn/ArevSans-BoldOblique-T5.pfb
%{_texmfdistdir}/fonts/type1/vntex/arevvn/ArevSans-Oblique-T5.pfb
%{_texmfdistdir}/fonts/type1/vntex/arevvn/ArevSans-Roman-T5.pfb
%{_texmfdistdir}/fonts/type1/vntex/chartervn/bchb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/chartervn/bchbi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/chartervn/bchr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/chartervn/bchri8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbr10.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbr17.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbr8.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbr9.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbrbx10.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbrsl10.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbrsl17.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbrsl8.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmbrsl9.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmsltl10.pfb
%{_texmfdistdir}/fonts/type1/vntex/cmbrightvn/vncmtl10.pfb
%{_texmfdistdir}/fonts/type1/vntex/concretevn/CMConcrete8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/concretevn/CMConcreteItalic8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/concretevn/CMConcreteSlanted8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/concretevn/CMConcreteSmallCaps8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/grotesqvn/ugqb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/txttvn/txbtt8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/txttvn/txbttsc8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/txttvn/txtt8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/txttvn/txttsc8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/fplrc8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uagd8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uagdo8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uagk8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uagko8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ubkd8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ubkdi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ubkl8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ubkli8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ucrb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ucrbo8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ucrr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/ucrro8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uhvb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uhvbo8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uhvr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uhvro8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uncb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uncbi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uncr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uncri8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uplb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uplbi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uplr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uplri8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/utmb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/utmbi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/utmr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/utmri8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/urwvn/uzcmi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnb10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx5.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx6.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx7.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbx9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbxsl10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnbxti10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vncsc10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vndunh10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnff10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnfi10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnfib8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnitt10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr17.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr5.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr6.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr7.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnr9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnsl10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnsl12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnsl8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnsl9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnsltt10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnss10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnss12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnss17.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnss8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnss9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssbx10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssdc10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssi10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssi12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssi17.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssi8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssi9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssq8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnssqi8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vntcsc10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnti10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnti12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnti7.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnti8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnti9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vntt10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vntt12.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vntt8.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vntt9.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnu10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vnr/vnvtt10.pfb
%{_texmfdistdir}/fonts/type1/vntex/vntopia/putb8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/vntopia/putbi8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/vntopia/putr8v.pfb
%{_texmfdistdir}/fonts/type1/vntex/vntopia/putri8v.pfb
%{_texmfdistdir}/fonts/vf/vntex/chartervn/bchbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/chartervn/bchrc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uagdc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uagkc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/ubkdc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/ubklc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/ucrbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/ucrrc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uhvbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uhvrc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uncbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uncrc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uplbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/uplrc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/utmbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/urwvn/utmrc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/vntopia/putbc8v.vf
%{_texmfdistdir}/fonts/vf/vntex/vntopia/putrc8v.vf
%{_texmfdistdir}/tex/latex/vntex/dblaccnt.sty
%{_texmfdistdir}/tex/latex/vntex/mcviscii.def
%{_texmfdistdir}/tex/latex/vntex/pd1supp.def
%{_texmfdistdir}/tex/latex/vntex/swpvntex.sty
%{_texmfdistdir}/tex/latex/vntex/t5bch.fd
%{_texmfdistdir}/tex/latex/vntex/t5ccr.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmbr.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmdh.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmfib.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmfr.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmr.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmss.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmssq.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmtl.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmtt.fd
%{_texmfdistdir}/tex/latex/vntex/t5cmvtt.fd
%{_texmfdistdir}/tex/latex/vntex/t5enc.def
%{_texmfdistdir}/tex/latex/vntex/t5enc.dfu
%{_texmfdistdir}/tex/latex/vntex/t5fav.fd
%{_texmfdistdir}/tex/latex/vntex/t5fnc.fd
%{_texmfdistdir}/tex/latex/vntex/t5fpl.fd
%{_texmfdistdir}/tex/latex/vntex/t5futs.fd
%{_texmfdistdir}/tex/latex/vntex/t5mak.fd
%{_texmfdistdir}/tex/latex/vntex/t5mdbch.fd
%{_texmfdistdir}/tex/latex/vntex/t5mdput.fd
%{_texmfdistdir}/tex/latex/vntex/t5mdugm.fd
%{_texmfdistdir}/tex/latex/vntex/t5pag.fd
%{_texmfdistdir}/tex/latex/vntex/t5pbk.fd
%{_texmfdistdir}/tex/latex/vntex/t5pcr.fd
%{_texmfdistdir}/tex/latex/vntex/t5phv.fd
%{_texmfdistdir}/tex/latex/vntex/t5pnc.fd
%{_texmfdistdir}/tex/latex/vntex/t5ppl.fd
%{_texmfdistdir}/tex/latex/vntex/t5ptm.fd
%{_texmfdistdir}/tex/latex/vntex/t5ptmom.fd
%{_texmfdistdir}/tex/latex/vntex/t5put.fd
%{_texmfdistdir}/tex/latex/vntex/t5pxr.fd
%{_texmfdistdir}/tex/latex/vntex/t5txr.fd
%{_texmfdistdir}/tex/latex/vntex/t5txtt.fd
%{_texmfdistdir}/tex/latex/vntex/t5uag.fd
%{_texmfdistdir}/tex/latex/vntex/t5ubk.fd
%{_texmfdistdir}/tex/latex/vntex/t5ucr.fd
%{_texmfdistdir}/tex/latex/vntex/t5ugq.fd
%{_texmfdistdir}/tex/latex/vntex/t5uhv.fd
%{_texmfdistdir}/tex/latex/vntex/t5unc.fd
%{_texmfdistdir}/tex/latex/vntex/t5upl.fd
%{_texmfdistdir}/tex/latex/vntex/t5utm.fd
%{_texmfdistdir}/tex/latex/vntex/t5uzcm.fd
%{_texmfdistdir}/tex/latex/vntex/tcvn.def
%{_texmfdistdir}/tex/latex/vntex/varioref-vi.sty
%{_texmfdistdir}/tex/latex/vntex/vietnam.sty
%{_texmfdistdir}/tex/latex/vntex/viscii.def
%{_texmfdistdir}/tex/latex/vntex/vncaps.tex
%{_texmfdistdir}/tex/latex/vntex/vntex.sty
%{_texmfdistdir}/tex/latex/vntex/vps.def
%{_texmfdistdir}/tex/plain/vntex/dblaccnt.tex
%{_texmfdistdir}/tex/plain/vntex/t5code.tex
%{_texmfdistdir}/tex/plain/vntex/vntexinfo.tex
%_texmf_updmap_d/vntex
%doc %{_texmfdistdir}/doc/generic/vntex/INSTALL
%doc %{_texmfdistdir}/doc/generic/vntex/ReleaseNotes.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vn-fonts-print.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vn-fonts.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vn-min-print.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vn-min.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vntex-man-print.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vntex-man.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vntex-print.pdf
%doc %{_texmfdistdir}/doc/generic/vntex/vntex-update-maps
%doc %{_texmfdistdir}/doc/generic/vntex/vntex.pdf
#- source
%doc %{_texmfdistdir}/source/generic/vntex/GPL.txt
%doc %{_texmfdistdir}/source/generic/vntex/LGPL.txt
%doc %{_texmfdistdir}/source/generic/vntex/LICENSE-utopia.txt
%doc %{_texmfdistdir}/source/generic/vntex/LPPL.txt
%doc %{_texmfdistdir}/source/generic/vntex/Makefile
%doc %{_texmfdistdir}/source/generic/vntex/README.vntopia
%doc %{_texmfdistdir}/source/generic/vntex/doc/ReleaseNotes.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/abbr.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/test-accents.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vn-fonts-print.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vn-fonts.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vn-min-print.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vn-min.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vntex-man-print.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vntex-man.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vntex-print.tex
%doc %{_texmfdistdir}/source/generic/vntex/doc/vntex.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/Makefile
%doc %{_texmfdistdir}/source/generic/vntex/tests/README
%doc %{_texmfdistdir}/source/generic/vntex/tests/adventor-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/adventor-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/arevvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/arevvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/bonum-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/bonum-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/chartervn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/chartervn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/chorus-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/chorus-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/classicovn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/classicovn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/cmbrightvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/cmbrightvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/comicsansvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/comicsansvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/concretevn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/concretevn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/cursor-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/cursor-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/garamondvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/garamondvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/grotesqvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/grotesqvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/heros-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/heros-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/mscore-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/mscore-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/pagella-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/pagella-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/schola-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/schola-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5antt-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5antt-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5cyklop-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5cyklop-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5gentium-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5gentium-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5iwona-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5iwona-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5kurier-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5kurier-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5lm-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/t5lm-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/termes-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/termes-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-accents.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-babel.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-captions.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-plain-tcx.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-plain.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-tcvn.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-utf8.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-vietnam-tcx.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-vietnam.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/test-viscii.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/txttvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/txttvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/urwvn-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/urwvn-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/vnr-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/vnr-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/vnsample.cls
%doc %{_texmfdistdir}/source/generic/vntex/tests/vntopia-sample.tex
%doc %{_texmfdistdir}/source/generic/vntex/tests/vntopia-test.tex
%doc %{_texmfdistdir}/source/generic/vntex/vntex.dtx
%doc %{_texmfdistdir}/source/generic/vntex/vntex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

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
