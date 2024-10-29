#!/bin/bash

# Generate spt_copyb.adl
echo -e "//\n// Generated using gen_instb.sh\n//" > spt_copyb.adl
sed -e '/./{H;$!d;}' -e 'x;/instrfield/d;' spt_copy.adl >> spt_copyb.adl
sed -i 's/NAME/NAMEB/g; s/COPY/COPYB/g; s/copy/copyb/g' spt_copyb.adl
sed -i 's/opcode(0x25)/opcode(0x35)/g' spt_copyb.adl

# Generate spt_fftb.adl
echo -e "//\n// Generated using gen_instb.sh\n//" > spt_fftb.adl
sed -e '/./{H;$!d;}' -e 'x;/instrfield\|error/d;' spt_fft.adl >> spt_fftb.adl
sed -i 's/spt_fft/spt_fftb/g' spt_fftb.adl
sed -i 's/win/winb/g; s/opcode(0x21)/opcode(0x31)/g' spt_fftb.adl
sed -i 's/rdx4/rdx4b/g; s/opcode(0x22)/opcode(0x32)/g; s/opcode(0x2b)/opcode(0x3b)/g' spt_fftb.adl
sed -i 's/rdx2/rdx2b/g; s/opcode(0x23)/opcode(0x33)/g; s/opcode(0x2c)/opcode(0x3c)/g' spt_fftb.adl
sed -i 's/fir/firb/g; s/opcode(0x29)/opcode(0x39)/g' spt_fftb.adl
sed -i 's/scp/scpb/g; s/opcode(0x2a)/opcode(0x3a)/g' spt_fftb.adl
# Revert renaming of fields
sed -i 's/fft_rnd_rdx2b/fft_rnd_rdx2/g; s/winb_type/win_type/g; s/scpb_coef_add/scp_coef_add/g' spt_fftb.adl
sed -i 's/win_type_winb/win_type_win/g; s/R_winb_/R_win_/g; s/R_rdx_rnd0_winb/R_rdx_rnd0_win/g' spt_fftb.adl
sed -i 's/R_scpb_/R_scp_/g' spt_fftb.adl

# Generate spt_sortb.adl
echo -e "//\n// Generated using gen_instb.sh\n//" > spt_sortb.adl
sed -e '/./{H;$!d;}' -e 'x;/instrfield\|illegal/d;' spt_sort.adl >> spt_sortb.adl
sed -i 's/opcode(0x27)/opcode(0x37)/g; s/opcode(0x2D)/opcode(0x3D)/g' spt_sortb.adl
sed -i 's/sort/sortb/g; s/maxs/maxsb/g; s/SORT/SORTB/g; s/MAXS/MAXSB/g' spt_sortb.adl
# Revert renaming of fields
sed -i 's/maxsbn_sel/maxsn_sel/g; s/sortb_type/sort_type/g; s/sortb_rank/sort_rank/g; s/cyc_inc_sortb/cyc_inc_sort/g' spt_sortb.adl
sed -i 's/R_sortb_/R_sort_/g; s/R_maxsb_/R_maxs_/g' spt_sortb.adl
