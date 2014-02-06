%global cartridgedir %{_libexecdir}/openshift/cartridges/zend
%global frameworkdir %{_libexecdir}/openshift/cartridges/zend

Name:    openshift-origin-cartridge-zend
Version: 1.1.8
Release: 1%{?dist}
Summary: Zend Server cartridge
Group:   Development/Languages
License: ASL 2.0
URL:     https://openshift.redhat.com
Source0: %{name}-%{version}.tar.gz

Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

Requires: rubygem-builder
# Zend Server 5.6
Requires: zend-server-php-5.3 >= 5.6.0-11
Requires: php-5.3-mongo-zend-server
Requires: php-5.3-imagick-zend-server
Requires: php-5.3-uploadprogress-zend-server
Requires: php-5.3-java-bridge-zend-server
Requires: php-5.3-optimizer-plus-zend-server
Requires: php-5.3-zend-extensions
Requires: php-5.3-extra-extensions-zend-server
Requires: php-5.3-loader-zend-server
# Zend Server 6.x
Requires: zend-server-php-5.4 >= 5.6.0-11

Obsoletes: openshift-origin-cartridge-zend-5.6

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Zend Server cartridge for openshift.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%clean
%__rm -rf %{buildroot}

%post
# Zend Server 5.6
%__cp -rf %{cartridgedir}/versions/5.6/configuration/shared-files/usr/local/zend/* /usr/local/zend/
#configure /sandbox/zend dir
sh %{cartridgedir}/versions/5.6/rpm/zend_configure_filesystem.sh
# Zend Server 6.x
cp -rf %{cartridgedir}/versions/6.1/configuration/shared-files/usr/local/zend-server-6-php-5.4/* /usr/local/zend-server-6-php-5.4/

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.adoc
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Fri Jan 24 2014 Adam Miller <admiller@redhat.com> 1.1.8-1
- Removing Obsolete flag until bug 1054654 is fixed (lnader@redhat.com)

* Thu Jan 23 2014 Adam Miller <admiller@redhat.com> 1.1.7-1
- Bump up cartridge versions (bparees@redhat.com)

* Fri Jan 17 2014 Adam Miller <admiller@redhat.com> 1.1.6-1
- Merge pull request #2271 from bparees/cart_data_cleanup
  (dmcphers+openshiftbot@redhat.com)
- remove unnecessary cart-data variable descriptions (bparees@redhat.com)

* Thu Jan 16 2014 Adam Miller <admiller@redhat.com> 1.1.5-1
- obsolete zend-5.6 (vvitek@redhat.com)

* Thu Jan 09 2014 Troy Dawson <tdawson@redhat.com> 1.1.4-1
- Bug 1033581 - minor update and adding comment (bleanhar@redhat.com)
- Bug 1033581 - Zend's jenkins_shell_command.erb was effectively the same as
  the stock jenkins-client script (bleanhar@redhat.com)

* Fri Dec 20 2013 Adam Miller <admiller@redhat.com> 1.1.3-1
- Zend display-name has duplicates (ccoleman@redhat.com)

* Mon Dec 16 2013 Adam Miller <admiller@redhat.com> 1.1.2-1
- Updates to the Zend Server new app page, originally from VojtechVitek Convert
  zend logo to base64 (sgoodwin@redhat.com)

* Thu Dec 12 2013 Adam Miller <admiller@redhat.com> 1.1.1-1
- bump_minor_versions for sprint 38 (admiller@redhat.com)
- remove Zend's extra files needed by binary RPM from cartridge codebase
  (vvitek@redhat.com)

* Fri Dec 06 2013 Troy Dawson <tdawson@redhat.com> 1.0.2-1
- fix secondary carts failures due to zend-6.1 LD_LIBRARY_PATH
  (vvitek@redhat.com)
- fix zend-6.1 date.timezone warnings (vvitek@redhat.com)
- fix zend-6.1 Java Bridge user UUID (vvitek@redhat.com)
- fix zend PEAR and PECL extensions (vvitek@redhat.com)
- Merge pull request #2194 from bparees/zend_max
  (dmcphers+openshiftbot@redhat.com)
- Bump up cartridge versions. (mrunalp@gmail.com)
- bug 1035214:  MaxClients/ServerLimit in httpd config of zend-6.1 is 5 instead
  of 60 (bparees@redhat.com)

* Wed Dec 04 2013 Adam Miller <admiller@redhat.com> 1.0.1-1
- add ORACLE_* vars to zend-6.1 (vvitek@redhat.com)
- Merge pull request #2198 from VojtechVitek/bug_1035605
  (dmcphers+openshiftbot@redhat.com)
- fix zend-6.1 watchdog failure (vvitek@redhat.com)
- Merge pull request #2195 from VojtechVitek/bug_1034626
  (dmcphers+openshiftbot@redhat.com)
- fix zend-6.1 app status (vvitek@redhat.com)
- fix Zend Server 6.1 control message flooding (vvitek@redhat.com)
- Fix for bug 1034596 remove links that point to openshift.redhat.com
  (sgoodwin@redhat.com)
- various zend clean-up (vvitek@redhat.com)
- fix zend client_result message (vvitek@redhat.com)
- enable zend-6.1 cartridge version (vvitek@redhat.com)
- fix processed_templates in zend managed_files (vvitek@redhat.com)
- add Zend Cartridge Guide instead of default README (vvitek@redhat.com)
- add Zend Server 6.1 files (vvitek@redhat.com)
- remove extra slashes from Apache config file (vvitek@redhat.com)
- move template repo to the shared usr/ dir (vvitek@redhat.com)
- prepare zend cartridge dir for new versions (vvitek@redhat.com)
- remove obsolete lib/util file (vvitek@redhat.com)
- Remove Open Sans since we're not including it externally, make font stack
  consistent with our site, set line-height (sgoodwin@redhat.com)
- Revision to zend start page. (sgoodwin@redhat.com)
- bump_minor_versions for sprint 37 (admiller@redhat.com)

* Thu Nov 14 2013 Adam Miller <admiller@redhat.com> 0.8.3-1
- Merge pull request #2158 from pmorie/latest-versions
  (dmcphers+openshiftbot@redhat.com)
- Bumping cartridge versions for 2.0.36 (pmorie@gmail.com)

* Wed Nov 13 2013 Adam Miller <admiller@redhat.com> 0.8.2-1
- Bug 1014793 - Added 'wait_for_pid_file' function to Bash SDK
  (mfojtik@redhat.com)

* Thu Nov 07 2013 Adam Miller <admiller@redhat.com> 0.8.1-1
- Correct zend cartridge status output (andy.goldstein@gmail.com)
- bump_minor_versions for sprint 36 (admiller@redhat.com)

* Thu Oct 31 2013 Adam Miller <admiller@redhat.com> 0.7.9-1
- Bump cartridge versions for 2.0.35 (pmorie@gmail.com)

* Tue Oct 29 2013 Adam Miller <admiller@redhat.com> 0.7.8-1
- Merge pull request #2053 from BanzaiMan/dev/hasari/bz1021042
  (dmcphers+openshiftbot@redhat.com)
- Bug 1021042 (asari.ruby@gmail.com)

* Mon Oct 28 2013 Adam Miller <admiller@redhat.com> 0.7.7-1
- Bug 1021472: Correctly migrate cart dependency dirs (ironcladlou@gmail.com)

* Thu Oct 24 2013 Adam Miller <admiller@redhat.com> 0.7.6-1
- Merge pull request #2033 from ncdc/master (dmcphers+openshiftbot@redhat.com)
- Jenkins fixes (andy.goldstein@gmail.com)

* Wed Oct 23 2013 Adam Miller <admiller@redhat.com> 0.7.5-1
- bump version to get around tag conflict (admiller@redhat.com)
- bump version to get around tag conflict (admiller@redhat.com)
- Update Zend jenkins shell command (andy.goldstein@gmail.com)
- Bug 1012295 - Added dependecy_dirs to managed_files.yml for zend
  (mfojtik@redhat.com)
- Fix cartridge dependency dir paths in upgrades (andy.goldstein@gmail.com)
- Bug 1020188 (andy.goldstein@gmail.com)
- Bug 1012295 - Create the HOMEDIR/.drush directory (mfojtik@redhat.com)
- Update Zend Jenkins script to match the rest (andy.goldstein@gmail.com)
- Merge pull request #1978 from fotioslindiakos/latest_versions_master
  (dmcphers+openshiftbot@redhat.com)
- Updated cartridge versions (fotios@redhat.com)
- More command consistency (dmcphers@redhat.com)
- Upgrade script for zend (pmorie@gmail.com)
- Change zend to use $OPENSHIFT_DEPENDENCIES_DIR (pmorie@gmail.com)

* Wed Oct 23 2013 Adam Miller <admiller@redhat.com>
- bump version to get around tag conflict (admiller@redhat.com)
- Update Zend jenkins shell command (andy.goldstein@gmail.com)
- Bug 1012295 - Added dependecy_dirs to managed_files.yml for zend
  (mfojtik@redhat.com)
- Fix cartridge dependency dir paths in upgrades (andy.goldstein@gmail.com)
- Bug 1020188 (andy.goldstein@gmail.com)
- Bug 1012295 - Create the HOMEDIR/.drush directory (mfojtik@redhat.com)
- Update Zend Jenkins script to match the rest (andy.goldstein@gmail.com)
- Merge pull request #1978 from fotioslindiakos/latest_versions_master
  (dmcphers+openshiftbot@redhat.com)
- Updated cartridge versions (fotios@redhat.com)
- More command consistency (dmcphers@redhat.com)
- Upgrade script for zend (pmorie@gmail.com)
- Change zend to use $OPENSHIFT_DEPENDENCIES_DIR (pmorie@gmail.com)

* Tue Sep 24 2013 Troy Dawson <tdawson@redhat.com> 0.7.1-1
- suppress zend control client_messages (vvitek@redhat.com)
- bump_minor_versions for sprint 34 (admiller@redhat.com)

* Thu Sep 12 2013 Adam Miller <admiller@redhat.com> 0.6.3-1
- Merge pull request #1896 from ironcladlou/dev/cart-version-bumps
  (dmcphers+openshiftbot@redhat.com)
- Cartridge version bumps for 2.0.33 (ironcladlou@gmail.com)
- fix Zend hot_deploy on Jenkins (vvitek@redhat.com)

* Fri Sep 06 2013 Adam Miller <admiller@redhat.com> 0.6.2-1
- Fix bug 1004899: remove legacy subscribes from manifests (pmorie@gmail.com)

* Thu Aug 08 2013 Adam Miller <admiller@redhat.com> 0.6.1-1
- Merge pull request #1793 from jwhonce/bug/985514
  (dmcphers+openshiftbot@redhat.com)
- Bug 985514 - Update CartridgeRepository when mcollectived restarted
  (jhonce@redhat.com)
- bump_minor_versions for sprint 32 (admiller@redhat.com)

* Wed Jul 31 2013 Adam Miller <admiller@redhat.com> 0.5.4-1
- Update cartridge versions for Sprint 31 (jhonce@redhat.com)

* Mon Jul 29 2013 Adam Miller <admiller@redhat.com> 0.5.3-1
- Bug 982738 (dmcphers@redhat.com)

* Wed Jul 24 2013 Adam Miller <admiller@redhat.com> 0.5.2-1
- Remove 'Group-Overrides' from zend cart manifest file, its a no-op.
  (rpenta@redhat.com)

* Fri Jul 12 2013 Adam Miller <admiller@redhat.com> 0.5.1-1
- bump_minor_versions for sprint 31 (admiller@redhat.com)

* Wed Jul 10 2013 Adam Miller <admiller@redhat.com> 0.4.3-1
- Bug 968252: Clean up old marker README files (ironcladlou@gmail.com)

* Tue Jul 02 2013 Adam Miller <admiller@redhat.com> 0.4.2-1
- Bug 976921: Move cart installation to %%posttrans (ironcladlou@gmail.com)
- remove v2 folder from cart install (dmcphers@redhat.com)

* Tue Jun 25 2013 Adam Miller <admiller@redhat.com> 0.4.1-1
- bump_minor_versions for sprint 30 (admiller@redhat.com)

* Fri Jun 21 2013 Adam Miller <admiller@redhat.com> 0.3.4-1
- Criteria for incompatible vs. compatible change: - Did "control start"
  change? - Did you create new files? (jhonce@redhat.com)

* Tue Jun 18 2013 Adam Miller <admiller@redhat.com> 0.3.3-1
- Merge pull request #1639 from ironcladlou/bz/974923
  (dmcphers+openshiftbot@redhat.com)
- Various cleanup (dmcphers@redhat.com)
- Bug 974923: Fix inaccurate Cart-Data env var references
  (ironcladlou@gmail.com)

* Mon Jun 17 2013 Adam Miller <admiller@redhat.com> 0.3.2-1
- First pass at removing v1 cartridges (dmcphers@redhat.com)
- fix zend apachectl symlink (vvitek@redhat.com)
- Merge pull request #1508 from ironcladlou/dev/v2carts/manifest-defaults
  (dmcphers+openshiftbot@redhat.com)
- Make Initial-Build-Required default to false (ironcladlou@gmail.com)
- Fix Zend apachectl deployment settings (vvitek@redhat.com)

* Thu May 30 2013 Adam Miller <admiller@redhat.com> 0.3.1-1
- bump_minor_versions for sprint 29 (admiller@redhat.com)

* Thu May 30 2013 Adam Miller <admiller@redhat.com> 0.2.7-1
- add zend php binary to env PATH variable (vvitek@redhat.com)

* Fri May 24 2013 Adam Miller <admiller@redhat.com> 0.2.6-1
- Merge pull request #1452 from VojtechVitek/zend_disable_oci_extension
  (dmcphers+openshiftbot@redhat.com)
- disable Zend PHP PDO-OCI extension (vvitek@redhat.com)

* Thu May 23 2013 Adam Miller <admiller@redhat.com> 0.2.5-1
- Merge pull request #1446 from ironcladlou/bz/966255
  (dmcphers+openshiftbot@redhat.com)
- Bug 966255: Remove OPENSHIFT_INTERNAL_* references from v2 carts
  (ironcladlou@gmail.com)

* Wed May 22 2013 Adam Miller <admiller@redhat.com> 0.2.4-1
- Bug 962662 (dmcphers@redhat.com)
- Bug 965537 - Dynamically build PassEnv httpd configuration
  (jhonce@redhat.com)
- Fix but 964348 (pmorie@gmail.com)

* Mon May 20 2013 Dan McPherson <dmcphers@redhat.com> 0.2.3-1
- Bug 963494 - Zend cartridges cannot be created (jhonce@redhat.com)

* Thu May 16 2013 Adam Miller <admiller@redhat.com> 0.2.2-1
- locking fixes and adjustments (dmcphers@redhat.com)
- Merge pull request #1367 from fotioslindiakos/locked_files
  (dmcphers+openshiftbot@redhat.com)
- WIP Cartridge Refactor -- Cleanup spec files (jhonce@redhat.com)
- Added erb processing to managed_files.yml (fotios@redhat.com)
- Card online_runtime_297 - Allow cartridges to use more resources
  (jhonce@redhat.com)
- Card online_runtime_297 - Allow cartridges to use more resources
  (jhonce@redhat.com)

* Wed May 08 2013 Adam Miller <admiller@redhat.com> 0.2.1-1
- bump_minor_versions for sprint 28 (admiller@redhat.com)

* Mon May 06 2013 Adam Miller <admiller@redhat.com> 0.1.11-1
- Merge pull request #1301 from VojtechVitek/zend_bug_fixes
  (dmcphers+openshiftbot@redhat.com)
- Warn users to set Zend Server Console password (vvitek@redhat.com)
- Improve Zend control client_* messages (vvitek@redhat.com)
- Update Zend license key/serial (vvitek@redhat.com)
- fix /ZendServer GUI Console (vvitek@redhat.com)

* Fri May 03 2013 Adam Miller <admiller@redhat.com> 0.1.10-1
- cleanup (dmcphers@redhat.com)
- Converted metadata/{locked_files,snapshot*}.txt (fotios@redhat.com)

* Thu May 02 2013 Adam Miller <admiller@redhat.com> 0.1.9-1
- fix zend configuration (vvitek@redhat.com)

* Tue Apr 30 2013 Adam Miller <admiller@redhat.com> 0.1.8-1
- Merge pull request #1268 from VojtechVitek/zend-v2-setup-install
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #1269 from rmillner/v2_misc_fixes
  (dmcphers+openshiftbot@redhat.com)
- Add health mapping to Zend. (rmillner@redhat.com)
- fix zend v2 setup/install (vvitek@redhat.com)

* Mon Apr 29 2013 Adam Miller <admiller@redhat.com> 0.1.7-1
- Bug 957073 (dmcphers@redhat.com)

* Thu Apr 25 2013 Adam Miller <admiller@redhat.com> 0.1.6-1
- zend work (dmcphers@redhat.com)

* Thu Apr 25 2013 Dan McPherson <dmcphers@redhat.com> 0.1.5-1
- 

* Thu Apr 25 2013 Dan McPherson <dmcphers@redhat.com> 0.1.4-1
- 

* Wed Apr 24 2013 Dan McPherson <dmcphers@redhat.com> 0.1.3-1
- new package built with tito

* Wed Apr 24 2013 Vojtech Vitek (V-Teq) <vvitek@redhat.com>
- Zend v2 init (vvitek@redhat.com)

* Tue Apr 23 2013 Vojtech Vitek (V-Teq) <vvitek@redhat.com>
- init package built with tito

