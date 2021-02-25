
OBJ = spt3_target.o objdump_init.o
OBJD = spt3_target_d.o objdump_init_d.o
ROOT ?= ~/adl_repo
TESTHEAD = ~/testhead
DEVHEAD = ~/win/tools_spt
CXXFLAGS = -I ${ROOT}/share/binutils/gas -I ${ROOT}/share/binutils/include -I ${ROOT}/share/binutils/bfd -I ${ROOT}/share/binutils/gas/config -I ${ROOT}/share/binutils --std=c++0x -ggdb -g3 -Wall -Wno-deprecated -Wno-unused-label -Wno-unused-but-set-variable -Wno-unused-local-typedefs -D_REENTRANT -DGC_LINUX_THREADS
CXXFLAGS1= -DHAVE_CONFIG_H -D_GNU_SOURCE -I${ROOT}/include -I${ROOT}/share/binutils/opcodes -I${ROOT}/share/binutils/bfd  -I${ROOT}/share/binutils/include -I${ROOT}/share/binutils/intl  -W -Wall -g --std=c++0x  -fPIC 
CXXFLAGS2= -DHAVE_CONFIG_H -D_GNU_SOURCE -I${ROOT}/include -I${ROOT}/share/binutils/gas -I${ROOT}/share/binutils/gas/config -I${ROOT}/share/binutils -I${ROOT}/share/binutils/opcodes -I${ROOT}/share/binutils/bfd -I${ROOT}/share/binutils/include -I${ROOT}/share/binutils/intl  -W -Wall -g --std=c++0x  -fPIC 
SPT3_ADL = spt3_addr.adl spt3_alu.adl spt3_copy.adl spt3_fftb.adl spt3_sort.adl spt3_vmt.adl spt3.adl spt3_cmds.adl spt3_copyb.adl spt3_fft.adl spt3_hist.adl spt3_sortb.adl
CWD = 
SPT_SRCS = as-spt3.cc objdump-spt3.cc

all: $(OBJ)  $(SPT_SRCS)
	#adl2asm $(SPT3_ADL) --no-log-usage --no-a2l --no-ld  --as-libs="$(OBJ)"
	$(CXX)  $(CXXFLAGS1) -O2 -c objdump-spt3.cc -o objdump-spt3.o	
	$(CXX)  $(CXXFLAGS2) -O2 -c as-spt3.cc -o as-spt3.o
	### exploit a gnu ld bug to force a statsi initializer
	$(CXX) -W -Wall -g -O2 --std=c++0x  -fPIC -o objdump-spt3 objdump-spt3.o objdump_init.o -L${ROOT}/share/binutils/binutils -L${ROOT}/share/binutils/bfd -L${ROOT}/share/binutils/opcodes -L${ROOT}/share/binutils/libiberty  -lobjdump -lbfd -lbfd -liberty  -lz -lopcodes
	$(CXX) -o as-spt3 -W -Wall -g -O2 --std=c++0x -fPIC  as-spt3.o -L${ROOT}/share/binutils/gas -L${ROOT}/share/binutils/opcodes -L${ROOT}/share/binutils/bfd -L${ROOT}/share/binutils/intl -L${ROOT}/share/binutils/libiberty objdump-spt3.o  -lgas spt3_target.o -lopcodes -lbfd -liberty  -lz -lgas-gas

$(SPT_SRCS): $(SPT3_ADL)
	make-asm --cpp=g++ spt3.adl --asm --dis --no-dbg --arch-pfx='ppc' --asm-output='as-spt3.cc' --dis-output='objdump-spt3.cc' --hdr-output='instr-info-spt3.h' --log-usage='false'
	
debug: $(OBJD) $(SPT_SRCS)
	#adl2asm $(SPT3_ADL) --no-log-usage --no-a2l --no-ld --no-optimize --verbose --as-libs="$(OBJD)"
	$(CXX)  $(CXXFLAGS1) -O0 -c objdump-spt3.cc -o objdump-spt3_d.o	
	$(CXX)  $(CXXFLAGS2) -O0 -c as-spt3.cc -o as-spt3_d.o
	### exploit a gnu ld bug to force a statsi initializer
	$(CXX) -W -Wall -g -O0 --std=c++0x  -fPIC   -o objdump-spt3 objdump-spt3_d.o objdump_init_d.o -L${ROOT}/share/binutils/binutils -L${ROOT}/share/binutils/bfd -L${ROOT}/share/binutils/opcodes -L${ROOT}/share/binutils/libiberty  -lobjdump -lbfd -lbfd -liberty  -lz -lopcodes
	$(CXX) -o as-spt3 -W -Wall -g -O0 --std=c++0x  -fPIC  as-spt3_d.o -L${ROOT}/share/binutils/gas -L${ROOT}/share/binutils/opcodes -L${ROOT}/share/binutils/bfd -L${ROOT}/share/binutils/intl -L${ROOT}/share/binutils/libiberty objdump-spt3_d.o  -lgas spt3_target_d.o -lopcodes -lbfd -liberty  -lz -lgas-gas

$(OBJ): %.o: %.cpp
	$(CXX) $(CXXFLAGS) -O2 -c $<  -o $@

$(OBJD): %_d.o: %.cpp
	$(CXX) $(CXXFLAGS) -g -O0 -c $<  -o $@

TST_SPT_SRCS = $(sort $(filter-out %_abs.spt3, $(notdir $(wildcard $(TESTHEAD)/bruteforce/*.spt3))))
TST_SPT_ABS_SRCS = $(sort $(notdir $(wildcard $(TESTHEAD)/bruteforce/*_abs.spt3)))


test_it = \
	cd $(1)/bruteforce && \
	for f in $(2); do \
		../as-spt3 $(3) -c $$f -o $$f.o > $$f.err 2>&1 ; \
		if [ ! -s $$f.err ]; then \
			rm $$f.err; \
			../objdump-spt3 -mppc -d -z --prefix-addresses --no-show-raw-insn $$f.o | awk '/0x/ {sub(/0x[0-9a-f][0-9a-f]* /,""); print $$0}' > $$f.dump; \
		else \
			echo "Failed : $$f"; \
		fi; \
	done

gentest:
	cd $(TESTHEAD)/bruteforce && python $(DEVHEAD)/tests/spt3-test.py
	cd $(TESTHEAD)/bruteforce && python $(DEVHEAD)/tests/spt3-test-abs.py

test:
	cp as-spt3 $(TESTHEAD)
	cp objdump-spt3 $(TESTHEAD)
	@$(call test_it,$(TESTHEAD),$(TST_SPT_SRCS),)
	
testabs:
	cp as-spt3 $(TESTHEAD)
	cp objdump-spt3 $(TESTHEAD)
	@$(call test_it,$(TESTHEAD),$(TST_SPT_ABS_SRCS),-I $(DEVHEAD)/inc)
	
testclean:
	rm -rf bruteforce/*

dumps:
	$(ROOT)/bin/adl-dump spt3.adl > listing
	grep Syntax listing | grep DS | sort > dsyntax.list
	grep Syntax listing | grep -v DS | sort > syntax.list
	grep mem syntax.list > new_syntax.list
	grep add_reg syntax.list >> new_syntax.list
	grep -v mem syntax.list | grep -v add_reg | grep -v src_add >> new_syntax.list
	sort -u new_syntax.list > tmp
	mv tmp new_syntax.list

clean:
	rm -f $(OBJ) $(OBJD) as-spt3 objdump-spt3 as-spt3.cc objdump-spt3.cc

