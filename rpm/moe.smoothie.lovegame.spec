# SPDX-FileCopyrightText: 2026 Smooth-E
# SPDX-License-Identifier: GPL-3.0-or-later

Name:       moe.smoothie.lovegame

%define _buildhost Aurora Build Engine

# >> macros
# << macros
%define __provides_exclude_from ^%{_datadir}/.*$

Summary:    36 вопросов
Version:    1.2.2
Release:    1
Group:      Amusements/Games
License:    GPL-3.0-or-later
URL:        https://codeberg.org/salty-smoothie/aurora-lovegame
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(auroraapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Узнайте друга друга получше, отвечая на эти личные вопросы.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5  \
    VERSION=%{version} \
    RELEASE=%{release}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%defattr(644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
