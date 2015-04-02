Summary:	Hawaii desktop
Name:		task-hawaii
Version:	0.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
BuildArch:	noarch
Requires:	hawaii-icon-themes >= %{version}
Requires:	hawaii-wallpapers >= %{version}
Requires:	hawaii-widget-styles >= 0.2.0
Requires:	hawaii-shell >= %{version}
Requires:	hawaii-terminal >= 0.2.0
Requires:	hawaii-system-preferences >= %{version}
Requires:	hawaii-eyesight >= 0.1.2
#Requires:	xkeyboard-config
Requires:	x11-data-xkbdata
Requires:	qtaccountsservice
Requires:	qtconfiguration
#Requires:	qtwayland
#Requires:	greenisland
Requires:	desktop-common-data

%description
Hawaii desktop environment meta package.

%files
