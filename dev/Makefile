
OBJ = spt3_reloc.o 
SPTI = sptInstruction.o
ROOT = ~/SPT/adl-3.16.20
CXXFLAGS = -I $(ROOT)/external/binutils-adl/gas -I $(ROOT)/external/binutils-adl/include -I $(ROOT)/external/binutils-adl/bfd -I $(ROOT)/external/binutils-adl/gas/config -I $(ROOT)/external/binutils-adl --std=c++0x -ggdb -g3 -Wall -Wno-deprecated -Wno-unused-label -Wno-unused-but-set-variable -Wno-unused-local-typedefs -D_REENTRANT -DGC_LINUX_THREADS
CXXFLAGS1= -DHAVE_CONFIG_H -D_GNU_SOURCE -I/usr/local/include -I/usr/local/share/binutils/opcodes -I/usr/local/share/binutils/bfd  -I/usr/local/share/binutils/bfd  -I/usr/loccal/share/binutils/include -I/usr/local/share/binutils/intl  -W -Wall -g -O2 --std=c++0x  -fPIC 
SPT3_ADL = spt3.0-GM.adl

$(OBJ) : 
	$(CXX) $(CXXFLAGS) -c spt3_reloc.c  -o spt3_reloc.o
	g++ $(CXXFLAGS1) -c sptInstruction.cpp -o sptInstruction.o 

all: $(OBJ)
	adl2asm $(SPT3_ADL) --no-log-usage --no-a2l --no-ld  --as-libs=$(OBJ)

