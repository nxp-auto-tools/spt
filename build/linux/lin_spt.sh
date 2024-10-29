#!/usr/bin/env bash

set -e

[ "${ADL_ROOT}" = "" ]           && ADL_ROOT="/opt/adl-3.24.7"
[ "${LIN_CXX}" = "" ]            && LIN_CXX="/usr/bin/g++"
[ "${LIN_CC}" = "" ]             && LIN_CC="/usr/bin/gcc"
[ "${CLEANUP_DIRS}" = "" ]       && CLEANUP_DIRS=0

export CC=${LIN_CC}
export CXX=${LIN_CXX}

SPT_VER=3.8

export ROOT=${ADL_ROOT}
export SPT_BIN=SPT${SPT_VER}

cd tools_spt/dev
make all

cd ..
mkdir -p -m777 $SPT_BIN/bin
mkdir -p -m777 $SPT_BIN/inc
mkdir -p -m777 $SPT_BIN/doc

#copy binaries
cp dev/as-spt${SPT_VER} $SPT_BIN/bin/as-spt
cp dev/objdump-spt${SPT_VER} $SPT_BIN/bin/objdump-spt

#copy SPT3.1 asm porting utility
cp util/linux/port-asm3.1 $SPT_BIN/bin

#copy include directory
cp -r inc/*.inc $SPT_BIN/inc

#copy documentation
cp doc/as-spt${SPT_VER}-manual.pdf $SPT_BIN/doc
cp doc/spt${SPT_VER}-mnemonics-quickref.txt $SPT_BIN/doc
cp doc/gas-manual.pdf $SPT_BIN/doc
cp doc/readme.pdf $SPT_BIN/readme.pdf

#prepare artifact
BUILD_DATE=`date +%y%m%d`
zip -q -r SPT${SPT_VER}_${BUILD_DATE}_linux.zip $SPT_BIN
zip -q -r adl_src.zip dev/*.c* dev/*.h
