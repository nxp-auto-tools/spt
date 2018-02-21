.include "oram.inc"
.include "wr.inc"
.include "tram.inc"

.extern	spt_sram

.section .spt

start:
	pdma .zeropad .16cmplx .sysram2opram .sync 16 spt_sram+4, OR_2_6_7, 4, 4, 8, 8
	pdma .signext .24cmplx .opram2sysram .async 16 spt_sram, OR_2_6_7, 4, 4, 8, 8
	pdma .zeropad .24real .sysram2opram .sync 16 spt_sram, OR_2_6_7, 4, 4, 8, 8
	pdma .signext .16real .opram2sysram .async 16 spt_sram, OR_2_6_7, 4, 4, 8, 8
	pdma .zeropad .48bin .sysram2opram .sync 16 spt_sram, OR_2_6_7, 4, 4, 8, 8
	pdma .signext .16cmplx .opram2sysram .async 16 spt_sram, OR_2_6_7, 4, 4, 8, 8
	pdma.ind .zeropad .48bin .sysram2opram .sync 16 spt_sram, WR_26, 4, 4, 8, 8

