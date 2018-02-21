.include "tram.inc"
.include "oram.inc"
.include "wr.inc"

.section .spt

start:
     win .real 16 OR_2_3_1,OR_3_3_1,1,2,16,16,.nosft
     win.ind .real 16 WR_1, 1, 2, 16, 16, .nosft

     win .cmplx .const 20 OR_1_2_3, OR_1_1_1, WR_4, 16,16, .mod2, 8, .shift1
     win.ind .cmplx .const 20 WR_2, WR_4, 16,16, .mod2, 8, .shift2

     rdx4 .cmplx .fft16 .win .noqext .ovs32 0 20 OR_1_2_3, OR_1_1_1, 1, 2, 16,16, .shift1
     rdx4.ind .cmplx .fft16 .win .noqext .ovs32 0 20 WR_1, 1, 2, 16,16, .shift1

     rdx4 .cmplx .fft16 .win .noqext .caddr .ovs32 0 20 OR_1_2_3, OR_1_1_1, WR_4, 16,16, .mod4, 16, .shift1
     rdx4.ind .cmplx .fft16 .win .noqext .caddr .ovs32 0 20 WR_1, WR_4, 16,16, .mod4, 16, .shift1

     rdx4.adptv .cmplx .fft16 .win .noqext .caddr .ovs32 .bits_18_23 .15down WR_4 0 20 OR_1_2_3, OR_1_1_1, WR_4, 16,16, .mod4, 16, .shift1
     rdx4.ind.adptv .cmplx .fft16 .win .noqext .caddr .ovs32 .bits_24_29 .15down WR_4 0 20 WR_1, WR_4, 16,16, .mod4, 16, .shift1

     rdx2 .cmplx .nosplit .noqext .ovs16 0 20 OR_1_2_3, OR_1_1_1, WR_5, 16,16, .shift4
     rdx2.ind .cmplx .opsplit .qext .noovs 0 20 WR_1, WR_5, 16,16, .shift3

     rdx2.adptv .cmplx .nosplit .noqext .ovs16 .bits_30_35 .15down WR_4 0 20 OR_1_2_3, OR_1_1_1, WR_5, 16,16, .shift4
     rdx2.ind.adptv .cmplx .opsplit .qext .noovs .bits_42_47 .15down WR_4 0 20 WR_1, WR_5, 16,16, .shift3

     fir .cmplx .init 0 20 OR_1_2_3, OR_1_1_1, WR_5, 16,16, .shift4
     fir.ind .cmplx .noinit 0 20 WR_1, WR_5, 16,16, .shift3
