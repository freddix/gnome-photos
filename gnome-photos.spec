Summary:	Access, organize and share your photos with GNOME
Name:		gnome-photos
Version:	3.7.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-photos/3.7/%{name}-%{version}.tar.xz
# Source0-md5:	022065ec136f3892c36932432d472245
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libgdata-devel
BuildRequires:	liboauth-devel
BuildRequires:	libtool
BuildRequires:	libzapojit-devel
BuildRequires:	pkg-config
BuildRequires:	tracker-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	hicolor-icon-theme
Requires:	tracker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-photos

%description
Photos is an application to access, organize and share your photos
with GNOME 3.0

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-photos
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-photos
%{_desktopdir}/gnome-photos.desktop
%{_iconsdir}/hicolor/*/*/*.png

