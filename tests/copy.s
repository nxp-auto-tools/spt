.include "oram.inc"
.include "wr.inc"
.include "tram.inc"

.section .spt

start:
	copy .real .simple_copy .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .cmplx .transpose_copy .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .log2 .copy_real_pack .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .cmplx .copy_unpack .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .real .partial_copy_real .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .log2 .partial_copy_imag .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .real .partial_copy_r2i .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .cmplx .partial_copy_i2r .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .real .copy_clear .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy .log2 .copy_shift .keep_orig 30 TR_4_5, OR_2_6_7, 4, 4, 8, 8, 0x5a
	copy.ind .real .copy_real_pack .reset_values 30 wr_26, 4, 4, 8, 8, 0x5a

