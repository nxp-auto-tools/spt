#ifndef _sptInstruction
#define _sptInstruction



#include <iostream>
#include <string>
#include <cstdint>
#include <list>

//#include "sptDataTypes.h"
//#include "sptInternals.h"

#define SPT1 0
#define SPT2 1
#define SPT2_5 2
#define SPT3 3


#define OPCODE_SET 1
#define OPCODE_GET 2
#define OPCODE_ADD 3
#define OPCODE_STOP 4
#define OPCODE_LOOP 5
#define OPCODE_NEXT 6
#define OPCODE_SYNC 7
#define OPCODE_WAIT 8
#define OPCODE_EVT 9
#define OPCODE_WATCHDOG 0x0A
#define OPCODE_SUB 0x0B
#define OPCODE_CMP 0x0C
#define OPCODE_JUMP 0x0D
#define OPCODE_SEL 0x0E

#define OPCODE_REPEAT 0x0F
#define OPCODE_THREAD 0x10

#define OPCODE_WIN 0x21
#define OPCODE_RDX4 0x22
#define OPCODE_RDX2 0x23
#define OPCODE_HIST 0x24
#define OPCODE_COPY 0x25
#define OPCODE_VMT 0x26
#define OPCODE_MAXS 0x27
#define OPCODE_PDMA 0x28
#define OPCODE_FIR 0x29
#define OPCODE_SCP 0x2A
#define OPCODE_IRDX4 0x2B
#define OPCODE_IRDX2 0x2C
//SPT3 instructions
#define OPCODE_SORT 0x2D
#define OPCODE_DSP 0x2E
#define OPCODE_WINB 0x31
#define OPCODE_RDX4B 0x32
#define OPCODE_RDX2B 0x33
#define OPCODE_COPYB 0x35
#define OPCODE_MAXSB 0x37

#define OPCODE_FIRB 0x39
#define OPCODE_SCPB 0x3A
#define OPCODE_IRDX4B 0x3B
#define OPCODE_IRDX2B 0x3C
#define OPCODE_SORTB 0x3D

typedef unsigned char byte;
//typedef unsigned long long   uint64_t;

#define BUF_SZ 200
#define ATTRIBUTE_UNUSED
#define INSN_ unsigned x0, unsigned x1, unsigned x2, unsigned x3
#define INSN_F insn[0], insn[1], insn[2], insn[3]
#define SP " "

class sptInstruction{

protected:
	unsigned int  insn[4];
	static int lEndian ;
	char disasmBuffer[20];
	char outbuff[BUF_SZ];
	
public:
	static bool bigendian;
	static void setEndian(bool value){
		bigendian = value;
	};
	static sptInstruction * create(unsigned  * ins, int type);
	static int sptType ;
	static const int size = 16;
	sptInstruction(unsigned  * ins);
	virtual char * disassemble(void) = 0;
	//virtual int execute(void) = 0;
	static   char * getBIns(INSN_, char * insName);
	static unsigned char getInd(INSN_);
	static unsigned char getChrp(INSN_);
	static unsigned char getShift(INSN_);
	static unsigned char getSrc(INSN_);

	static char * getSrcAddWr(INSN_);
	static char * getSrc2Add(INSN_);
	static char * getSrcAdd(INSN_);
	static char * getSrc1Add(INSN_);
	static char * getSrc3Add(INSN_);
	static char * getThldAdd(INSN_);
	static char * getImmDat(INSN_); 
	static char * getDestAdd(INSN_);
	static  char * get_in_dattyp_s(INSN_);
	static char * getModVal(INSN_);
	static char * get_shift_val(INSN_);
	static char * getShift_s(INSN_);
	static char *getMultCoefAdd(INSN_);
	static char * getMcaMode(INSN_);
	static char * getShftOffset(INSN_);
	static char * getFftRnd(INSN_);
	static char * getTwOvs(INSN_);
		
};

class sptSetInstruction :public sptInstruction{
public:
	sptSetInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptGetInstruction :public sptInstruction{
public:
	sptGetInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptAddInstruction :public sptInstruction{
public:
	sptAddInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptCopyInstruction :public sptInstruction{
public:
	sptCopyInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptDspInstruction :public sptInstruction{
public:
	sptDspInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptStopInstruction :public sptInstruction{
public:
	sptStopInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptLoopInstruction :public sptInstruction{
public:
	sptLoopInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptNextInstruction :public sptInstruction{
public:
	sptNextInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptSyncInstruction :public sptInstruction{
public:
	sptSyncInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptWaitInstruction :public sptInstruction{
public:
	sptWaitInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptSubInstruction :public sptInstruction{
public:
	sptSubInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptCmpInstruction :public sptInstruction{
public:
	sptCmpInstruction(unsigned  * ins);
	char * disassemble(void);
};


class sptEvtInstruction :public sptInstruction{
public:
	sptEvtInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptFirInstruction :public sptInstruction{
public:
	sptFirInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptHistInstruction :public sptInstruction{
public:
	sptHistInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptIrdx2Instruction :public sptInstruction{
public:
	sptIrdx2Instruction(unsigned  * ins);
	char * disassemble(void);
};

class sptIrdx4Instruction :public sptInstruction{
public:
	sptIrdx4Instruction(unsigned  * ins);
	char * disassemble(void);
};

class sptJumpInstruction :public sptInstruction{
public:
	sptJumpInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptMaxsInstruction :public sptInstruction{
public:
	sptMaxsInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptPdmaInstruction :public sptInstruction{
public:
	sptPdmaInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptSelInstruction :public sptInstruction{
public:
	sptSelInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptScpInstruction :public sptInstruction{
public:
	sptScpInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptSortInstruction :public sptInstruction{
public:
	sptSortInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptRdx2Instruction :public sptInstruction{
public:
	sptRdx2Instruction(unsigned  * ins);
	char * disassemble(void);
};

class sptRdx4Instruction :public sptInstruction{
public:
	sptRdx4Instruction(unsigned  * ins);
	char * disassemble(void);
};


class sptRepeatInstruction :public sptInstruction{
public:
	sptRepeatInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptThreadInstruction :public sptInstruction{
public:
	sptThreadInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptVmtInstruction :public sptInstruction{
public:
	sptVmtInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptWatchdogInstruction :public sptInstruction{
public:
	sptWatchdogInstruction(unsigned  * ins);
	char * disassemble(void);
};


class sptWinInstruction :public sptInstruction{
public:
	sptWinInstruction(unsigned  * ins);
	char * disassemble(void);
};

class sptDummyInstruction :public sptInstruction{
public:
	sptDummyInstruction(unsigned  * ins);
	char * disassemble(void);
};

#endif
