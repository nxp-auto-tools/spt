#!/usr/bin/env bash

set -e

[ "${ADL_ROOT}" = "" ]           && ADL_ROOT="/workspace/build_tools/adl-3.17.3"
[ "${LIN_CXX}" = "" ]            && LIN_CXX="/opt/gcc-4.8.5/bin/g++"
[ "${LIN_CC}" = "" ]             && LIN_CC="/opt/gcc-4.8.5/bin/gcc"
[ "${CLEANUP_DIRS}" = "" ]       && CLEANUP_DIRS=0

export CC=${LIN_CC}
export CXX=${LIN_CXX}

export ROOT=${ADL_ROOT}

cd tools_spt/dev
make all

cd ..
mkdir -p -m777 SPT3/bin
mkdir -p -m777 SPT3/inc
mkdir -p -m777 SPT3/doc
#copy binaries
cp dev/as-spt3 SPT3/bin/as-spt
cp dev/objdump-spt3 SPT3/bin/objdump-spt
#copy includes directory
cp -r inc/*3.inc SPT3/inc
#copy documentation
cp doc/as-spt3-manual.pdf SPT3/doc
cp doc/'SPT3 mnemonics QuickRef' SPT3/doc
cp doc/gas-manual.pdf SPT3/doc
cp doc/ReadMe.spt3.pdf SPT3/ReadMe.pdf
#prepare artifact
BUILD_DATE=`date +%y%m%d`
zip -q -r SPT_${BUILD_DATE}_linux.zip SPT3
zip -q -r adl_src.zip dev/*.c* dev/*.h
