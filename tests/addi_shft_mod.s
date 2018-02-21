.include "wr.inc"

	.section .spt
start:
	add.immed.noshift.mod16 WR_0, 15, WR_0
	add.immed.shift.mod24 WR_0, 15, WR_0
	add.immed .mod24 WR_0, 15, WR_0

