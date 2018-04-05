#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bindrcpp
Version  : 0.2.2
Release  : 5
URL      : https://cran.r-project.org/src/contrib/bindrcpp_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bindrcpp_0.2.2.tar.gz
Summary  : An 'Rcpp' Interface to Active Bindings
Group    : Development/Tools
License  : MIT
Requires: R-bindrcpp-lib
Requires: R-Rcpp
Requires: R-bindr
Requires: R-plogr
BuildRequires : R-Rcpp
BuildRequires : R-bindr
BuildRequires : R-plogr
BuildRequires : clr-R-helpers

%description
that call a C++ function.

%package lib
Summary: lib components for the R-bindrcpp package.
Group: Libraries

%description lib
lib components for the R-bindrcpp package.


%prep
%setup -q -c -n bindrcpp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522356459

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522356459
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bindrcpp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bindrcpp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bindrcpp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bindrcpp|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bindrcpp/DESCRIPTION
/usr/lib64/R/library/bindrcpp/INDEX
/usr/lib64/R/library/bindrcpp/LICENSE
/usr/lib64/R/library/bindrcpp/Meta/Rd.rds
/usr/lib64/R/library/bindrcpp/Meta/features.rds
/usr/lib64/R/library/bindrcpp/Meta/hsearch.rds
/usr/lib64/R/library/bindrcpp/Meta/links.rds
/usr/lib64/R/library/bindrcpp/Meta/nsInfo.rds
/usr/lib64/R/library/bindrcpp/Meta/package.rds
/usr/lib64/R/library/bindrcpp/NAMESPACE
/usr/lib64/R/library/bindrcpp/NEWS.md
/usr/lib64/R/library/bindrcpp/R/bindrcpp
/usr/lib64/R/library/bindrcpp/R/bindrcpp.rdb
/usr/lib64/R/library/bindrcpp/R/bindrcpp.rdx
/usr/lib64/R/library/bindrcpp/help/AnIndex
/usr/lib64/R/library/bindrcpp/help/aliases.rds
/usr/lib64/R/library/bindrcpp/help/bindrcpp.rdb
/usr/lib64/R/library/bindrcpp/help/bindrcpp.rdx
/usr/lib64/R/library/bindrcpp/help/paths.rds
/usr/lib64/R/library/bindrcpp/html/00Index.html
/usr/lib64/R/library/bindrcpp/html/R.css
/usr/lib64/R/library/bindrcpp/include/bindrcpp.h
/usr/lib64/R/library/bindrcpp/include/bindrcpp_RcppExports.h
/usr/lib64/R/library/bindrcpp/include/bindrcpp_types.h
/usr/lib64/R/library/bindrcpp/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bindrcpp/libs/bindrcpp.so
/usr/lib64/R/library/bindrcpp/libs/bindrcpp.so.avx2
/usr/lib64/R/library/bindrcpp/libs/bindrcpp.so.avx512
