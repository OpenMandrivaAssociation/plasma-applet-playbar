%define oname playbar
%define debug_package	%{nil}

Name:           plasma-applet-%{oname}
Version:        0.7.1
Release:        1
Summary:        Control your favorite media player
License:        GPLv3+
Group:          Graphical desktop/KDE
Url:            https://github.com/audoban/PlayBar
Source:         PlayBar-%{version}.tar.gz

BuildRequires:  kdelibs4-devel >= 4.11

Requires:       kdebase4-runtime 


%description
MPRIS2 client written in QML for Plasma KDE.

Features:
- Customizable global shortcuts
- Media Player Control in bar
- You can control multiple players
- Very configurable

%prep
%setup -q -n PlayBar-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang plasma_applet_%{oname}


%files 
%doc README.md CHANGELOG.md LICENSE
%{_kde_services}/*.desktop
%{_kde_appsdir}/plasma/plasmoids/
%{_kde_appsdir}/plasma/services/%{oname}service.operations
%{_kde_libdir}/kde4/plasma_engine_%{oname}.so
%lang(es) %{_kde_datadir}/locale/es/LC_MESSAGES/plasma_applet_playbar.mo
%lang(ru) %{_kde_datadir}/locale/ru/LC_MESSAGES/plasma_applet_playbar.mo


