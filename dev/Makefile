
ROOT ?= /opt/adl-3.24.4_patch
TESTHEAD = ~/testhead
DEVHEAD = ~/win/tools_spt

AS_OBJ = spt_as.o
DISAS_OBJ = spt_ds.o
AS_OBJD = spt_as_d.o
DISAS_OBJD = spt_ds_d.o
OBJ = $(AS_OBJ) $(DISAS_OBJ)
OBJD = $(AS_OBJD) $(DISAS_OBJD)

INCLUDE_PATH = -I ${ROOT}/share/binutils/gas -I ${ROOT}/share/binutils/include -I ${ROOT}/share/binutils/bfd -I ${ROOT}/share/binutils/gas/config -I ${ROOT}/share/binutils
CXXFLAGS = --std=c++0x -Wall -Wno-deprecated -Wno-unused-label -Wno-unused-but-set-variable -Wno-unused-local-typedefs -D_REENTRANT -DGC_LINUX_THREADS
ADL_FLAG = --static

SPT_ADL = spt_addr.adl spt_alu.adl spt_copy.adl spt_sort.adl spt_vmt.adl spt.adl spt_cmds.adl spt_fft.adl spt_hist.adl
SPT_BIN = as-spt3.5 objdump-spt3.5

SPT_VER = $(shell date '+%Y.%-m.%-d')

all: clean rel

rel: ADL_FLAG += --as-libs="$(AS_OBJ)" --dis-libs="$(DISAS_OBJ)" --optimize=3 --no-dbg
rel: $(OBJ)  $(SPT_BIN)

debug: clean dbg

dbg: ADL_FLAG += --as-libs="$(AS_OBJD)" --dis-libs="$(DISAS_OBJD)" --dbg --no-optimize
dbg: $(OBJD) $(SPT_BIN)

verbose: ADL_FLAG += --verbose
verbose: clean rel

$(SPT_BIN): $(SPT_ADL)
	${ROOT}/bin/adl2asm --elf-machine-code-32=40  --elf-machine-code-64=183 --arch-le-name=spt-le --arch-name=spt --arch-print-name="spt" -I=. spt.adl --no-log-usage --no-warn-redefine \
        --asm --dis --cleanup=none --no-a2l --no-ld --bprefix=${ROOT}/share/binutils $(ADL_FLAG) --build-locally --model-base=spt3.5 --banner-msg="SPT 3.5 assembler tools version $(SPT_VER)"

$(OBJ): %.o: %.cpp
	$(CXX) $(INCLUDE_PATH) $(CXXFLAGS) -O3 -c $<  -o $@

$(OBJD): %_d.o: %.cpp
	$(CXX) $(INCLUDE_PATH) $(CXXFLAGS) -ggdb -g3 -g -O0 -c $<  -o $@

dumps:
	$(ROOT)/bin/adl-dump spt.adl > listing
	grep Syntax listing | grep DS | sort > dsyntax.list
	grep Syntax listing | grep -v DS | sort > syntax.list
	grep mem syntax.list > new_syntax.list
	grep add_reg syntax.list >> new_syntax.list
	grep -v mem syntax.list | grep -v add_reg | grep -v src_add >> new_syntax.list
	sort -u new_syntax.list > tmp
	mv tmp new_syntax.list

clean:
	rm -f $(OBJ) $(OBJD) $(SPT_BIN) as-spt3.5.* objdump-spt3.5.* instr-info-spt3.5.h

