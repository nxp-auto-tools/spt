#!/bin/sh

# Generate spt3_copyb.adl
echo -e "//\n// Generated using gen_instb.sh\n//" > spt3_copyb.adl
sed -e '/./{H;$!d;}' -e 'x;/instrfield/d;' spt3_copy.adl >> spt3_copyb.adl
sed -i 's/NAME/NAMEB/g; s/COPY/COPYB/g; s/copy/copyb/g' spt3_copyb.adl
sed -i 's/opcode(0x25)/opcode(0x35)/g' spt3_copyb.adl

# Generate spt3_fftb.adl
echo -e "//\n// Generated using gen_instb.sh\n//" > spt3_fftb.adl
sed -e '/./{H;$!d;}' -e 'x;/instrfield\|error/d;' spt3_fft.adl >> spt3_fftb.adl
sed -i 's/spt3_fft/spt3_fftb/g' spt3_fftb.adl
sed -i 's/win/winb/g; s/opcode(0x21)/opcode(0x31)/g' spt3_fftb.adl
sed -i 's/rdx4/rdx4b/g; s/opcode(0x22)/opcode(0x32)/g; s/opcode(0x2b)/opcode(0x3b)/g' spt3_fftb.adl
sed -i 's/rdx2/rdx2b/g; s/opcode(0x23)/opcode(0x33)/g; s/opcode(0x2c)/opcode(0x3c)/g' spt3_fftb.adl
sed -i 's/fir/firb/g; s/opcode(0x29)/opcode(0x39)/g' spt3_fftb.adl
sed -i 's/scp/scpb/g; s/opcode(0x2a)/opcode(0x3a)/g' spt3_fftb.adl
# Revert renaming of fields
sed -i 's/fft_rnd_rdx2b/fft_rnd_rdx2/g; s/winb_type/win_type/g; s/scpb_coef_add/scp_coef_add/g' spt3_fftb.adl

# Generate spt3_sortb.adl
echo -e "//\n// Generated using gen_instb.sh\n//" > spt3_sortb.adl
sed -e '/./{H;$!d;}' -e 'x;/instrfield\|illegal/d;' spt3_sort.adl >> spt3_sortb.adl
sed -i 's/opcode(0x27)/opcode(0x37)/g; s/opcode(0x2D)/opcode(0x3D)/g' spt3_sortb.adl
sed -i 's/sort/sortb/g; s/maxs/maxsb/g; s/SORT/SORTB/g; s/MAXS/MAXSB/g' spt3_sortb.adl
# Revert renaming of fields
sed -i 's/maxsbn_sel/maxsn_sel/g; s/sortb_type/sort_type/g; s/sortb_rank/sort_rank/g' spt3_sortb.adl
