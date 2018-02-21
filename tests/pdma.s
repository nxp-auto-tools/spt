.include "oram.inc"
.include "wr.inc"
.include "tram.inc"

.section .spt

start:
	pdma     .zeropad .16cmplx    .sysram2opram .sync  16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma     .signext .24cmplx    .opram2sysram .async 16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma     .zeropad .24real     .sysram2opram .sync  16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma     .signext .16real     .opram2sysram .async 16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma     .zeropad .48bin      .sysram2opram .sync  16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma     .signext .16swap     .opram2sysram .async 16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma     .zeropad .16clubbing .opram2sysram .async 16 0x4000000, OR_2_6_7, 4, 4, 8, 8
	pdma.ind .zeropad .48bin      .sysram2opram .sync  16 0x4000000, WR_26,    4, 4, 8, 8

