Name:           ros-melodic-igvc-self-drive-gazebo-plugins
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS igvc_self_drive_gazebo_plugins package

Group:          Development/Libraries
License:        BSD2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-gazebo-ros
Requires:       ros-melodic-gazebo-ros-pkgs
Requires:       ros-melodic-hector-gazebo-plugins
Requires:       ros-melodic-hector-models
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-gazebo-ros
BuildRequires:  ros-melodic-roscpp

%description
Gazebo plugins for IGVC Self-Drive simulator

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Sat Oct 06 2018 Micho Radovnikovich <mtradovn@oakland.edu> - 0.1.3-0
- Autogenerated by Bloom

* Sat Oct 06 2018 Micho Radovnikovich <mtradovn@oakland.edu> - 0.1.2-0
- Autogenerated by Bloom

* Sat Oct 06 2018 Micho Radovnikovich <mtradovn@oakland.edu> - 0.1.1-0
- Autogenerated by Bloom

* Sat Sep 29 2018 Micho Radovnikovich <mtradovn@oakland.edu> - 0.1.0-0
- Autogenerated by Bloom

