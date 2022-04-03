%define adw_version 1.6

Summary:        tauOS GTK Themes
Name:           tau-themes
Version:        1.1
Release:        1
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  sassc
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  ninja-build

Requires: tau-themes-adw

%description
A set of GTK Themes for tauOS

%package adw
Summary:        The theme from libadwaita ported to GTK-3
Provides:       adw-gtk3
Provides:       adw-gtk3-git
Conflicts:      adw-gtk3
Conflicts:      adw-gtk3-git

%description adw
The theme from libadwaita ported to GTK-3

%prep
%setup -q

# ADW Setup
git clone --recurse-submodules https://github.com/lassekongo83/adw-gtk3.git

%build

# ADW Build
cd adw-gtk3
git checkout tags/v%{adw_version}
%meson
%meson_build

%install

# ADW Install
cd adw-gtk3
%meson_install

%files

%files adw
%{_datadir}/themes/adw-gtk3/*
%{_datadir}/themes/adw-gtk3-dark/*