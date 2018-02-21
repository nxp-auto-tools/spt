
operands = {
# dummy test values
'adptv_wr' : ["10"],
'blk_dest_inc' : ["32"],
'blk_src_inc' : ["32"],
'cc_im' : ["3"],
'cc_re' : ["2"],
'coef_add' : ["TR_2_0"],
'cond_wr' : ["32"],
'count' : ["32"],
'cs_id' : ["3"],
'cp_mask' : ["0x5a5a5a5a"],
'dest_add' : ["WR_30"],
'dest_add_inc' : ["32"],
'dest_add_O' : ["OR_2_3_0"],
'dsp_val' : ["12345"],
'imm_dat' : ["0xEF12345678"],
'lp_cnt' : ["32"],
'lp_wr' : ["10"],
'mca_inc' : ["32"],
'mem_start_addr_wr' : ["WR_16"],
'mult_coef_add' : ["TR_1_0"],
'mult_s_exp_n_val_addr' : ["WR_45"],
'no_of_taps' : ["5"],
'opram_continuous_addr' : ["32"],
'opram_mem_start_addr' : ["TR_3_2"],
'opram_mem_start_addr_ind' : ["WR_3"],
'opram_skip_addr' : ["32"],
'rel_off' : [".+16"],
'shft_wr' : ["3"],
'sq2s2_im_imdt_value' : ["32"],
'sq2s2_offset_value' : ["32"],
'sq2s2_re_imdt_value' : ["32"],
'sq2s2_shift_value' : ["32"],
'sq2s2_vec_src' : ["32"],
'src_add' : ["OR_1_0_0"],
'src_add_inc' : ["32"],
'src_add_WR' : ["WR_16"],
'src1_add' : ["TR_0_1"],
'src2_add' : ["0x4567"],
'src2_add_wr' : ["WR_2"],
'src3_add' : ["TR_0_3"],
'sysram_continous_addr' : ["32"],
'sysram_mem_start_addr' : ["0x40000000"],
'sysram_skip_addr' : ["32"],
'tap_coef_add' : ["TR_0_5"],
'thld_const' : ["0xa5a5"],
'thld_add' : ["WR_32"],
'tw_add' : ["WR_32"],
'threshold' : ["32"],
'vec_sz' : ["256"],
'vector_len' : ["512"],
'wait_ev' : ["10"],
'wr' : ["WR_5"],
'rpt_cnt' : [ "8191"],
'addr_incr0' : [ "2" ],
'addr_incr1' : [ "4" ],
'addr_incr2' : [ "5" ],
'addr_incr3' : [ "6" ],
'th_id' : [ "3" ],

#real operands
'adptv' : (".noadptv",".adptv"),
'adptv_ofst' : (".bits_0_5", ".bits_6_11", ".bits_12_17", ".bits_18_23", ".bits_24_29", ".bits_30_35", ".bits_36_41", ".bits_42_47"),
'adptv_shft' : (".15down",".23down"),
'bin_sz' : (".16_24bins", ".32bins", ".64bins"),
'bitfld_size' : (".8bits", ".16bits", ".24bits"),
'cond_sel' : (".bit0", ".bit1", ".bit2", ".bit3", ".bit4", ".bit5", ".bit6", ".bit7", ".bit8", ".bit9"),
'cp_type_simple' : (".simple_copy", ".copy_real_pack",".copy_imag_pack",".copy_unpack",".partial_copy_real", ".partial_copy_imag",".partial_copy_r2i",".partial_copy_i2r",".copy_shift"),
'cp_type_threshold' : (".threshold_ge",".threshold_lt", ".threshold_gt"),
'cp_type_thresholdstep' : ( ".threshold_ge_step", ".threshold_gt_step", ".threshold_lt_step"),
'cp_type_trans' : (".transpose_copy", ".transpose_fwd_x8", ".transpose_bck_x8", ".transpose_fwd_x4", ".transpose_bck_x4"),
'cyc_extn' : (".no_cyc_ext", ".cyc_ext"),
'dat_sz' : (".16bits", ".24bits"),
'data_packing' : (".16cmplx",".24cmplx",".24real",".16real",".48bin",".16swap",".16clubbing",".CP4Q",".CP4Q_FMTA",".CP4Q_FMTB",".CP8D_FMTA",".CP8D_FMTB",".CP8D_FMTC",".CP16_FMTA",".CP16_FMTB",".CP16_FMTC",".CP16_FMTD",".CP32_FMTB",".abs_8_untagged",".idx_8_untagged",".idx_sum8_untagged",".abs_8_tagged",".idx_8_tagged",".idx_sum8_tagged",".abs_16_untagged",".idx_16_untagged",".idx_sum16_untagged",".abs_16_tagged",".idx_16_tagged",".idx_sum16_tagged",".abs_24_untagged",".idx_24_untagged",".idx_sum24_untagged",".abs_24_tagged",".idx_24_tagged",".idx_sum24_tagged",".abs_32_untagged",".idx_32_untagged",".idx_sum32_untagged"),
'dest_add_mode' : ("wr", "tr", "or"),
'ev_lvl' : (".low",".high"),
'ev_tr' : (".l0",".l1", ".pos", ".neg"),
'evt_ev' : (".lsb",".bit0",".bit1",".bit2",".bit3",".bit4",".bit5",".bit6",".msb",".bit7"),
'ev_type' : (".cpu", ".int"),
'fft_rnd' : (".round0",".round1",".round2",".round3",".round4",".round5"),
'fft_rnd_rdx2' : (".round1",".round2",".round3",".round4",".round5"),
'gm_preload' : (".no_preload", ".preload"),
'hist_mode' : (".read_store", ".read", ".acc", ".store"),
'ima' : (".imm",".ind"),
'ima2' : (".imm",".ind"),
'in_dattyp' : (".real",".cmplx"),
'in_dattyp_vmt' : (".real",".cmplx"),
'in_dattyp2' : (".real",".cmplx",".log2"),
'in_dattyp2_lm' : (".real .no_tag_in",".cmplx .no_tag_in",".log2 .no_tag_in",".log2 .tag_in"),
'in_pack' : (".in_24real", ".in_24im", ".in_48packed"),
'in_tag' : (".no_tag_in", ".tag_in"),
'init' : (".zero_init",".const_init"),
'ip_pack' : (".in_24real", ".in_24im", ".in_48"),
'jmp_sel' : (".bit0",".bit1",".bit2",".bit3",".bit4", ".bit5",".bit6",".bit7",".bit8",".bit9"),
'jmp_type' : ("",".always", ".cond"),
'loc_n_abs' : (".global_max", ".local_max"),
'maxsn_en' : (".masxn_dis", ".maxsn_en"),
'maxsn_sel' : (".no_maxsn", ".maxsn_16", ".maxsn_8", ".maxsn_4"),
'mca_mod' : (".mod0", ".mod2", ".mod4", ".mod8", ".mod16", ".mod32", ".mod64", ".mod128", ".mod256", ".mod512"),
'modulo_val' : (".mod0", ".mod1", ".mod2", ".mod3", ".mod4", ".mod5", ".mod6", ".mod7", ".mod8", ".mod9", ".mod10", ".mod11", ".mod12", ".mod13", ".mod14", ".mod15", ".mod16", ".mod17", ".mod18", ".mod19", ".mod20", ".mod21", ".mod22", ".mod23", ".mod24"),
'mult_coef_mode' : ("tr", "or"),
'mult_mod' : (".immed",".const",".caddr"),
'mult_mode' : (".const", ".caddr"),
'op_pack' : (".op_off", ".op_on"),
'opram_mem_start_mode' : ("wr", "tr", "or"),
'opsq1' : (".no_sq1", ".sq1"),
'opsq2s1' : (".no_sq2s1", ".abs_sq2s1", ".mag_sq2s1", ".conj_sq2s1"),
'opsq2s2' : (".no_sq2s2", ".shft_sq2s2", ".wr_off_sq2s2", "imm_off_sqs2", ".vec_sq2s2"),
'opsq2s3' : (".no_sq2s3", ".sum_sq2s3"),
'out_mode' : (".tag", ".idx"),
'pack_en' : (".no_pack_real", ".no_pack_im", ".pack"),
'pre_proc' : (".no_pre", ".abs_abs_proc", ".abs_mag_proc"),
'quad_ext' : (".noqext",".qext"),
're_im' : (".im", ".re"),
're_im_coeff' : (".coef_cmplx", ".coef_im", ".coef_re"),
'real_fft' : (".nosplit",".opsplit"),
'repeat' : ("",".no_repeat", ".fft8", ".fft16", ".fft32"),
'repeat2' : ("",".no_repeat", ".fft8", ".fft32"),
'rst_acc' : (".no_rst",".rst_wr"),
'rst_acc_vmt' : (".no_rst", ".rst_sum"),
'rst_n_keep' : (".keep_orig",".reset_values"),
'se' : (".zeropad",".signext"),
'sel_src1_add_mode' : ("wr", "tr", "or"),
'sel_src3_add_mode' : ("wr", "tr", "or"),
'shft' : (".noshift",".shift"),
'shft_ofst' : (".bits_0_5", ".bits_6_11", ".bits_12_17", ".bits_18_23", ".bits_24_29", ".bits_30_35", ".bits_36_41", ".bits_42_47"),
'shft_src' : (".shft_val", ".shft_wr"),
'shft_val' : (".nosft",".shift1",".shift2",".shift3", ".shift4",".shift8"),
'src_add_mode' : ("wr", "tr", "or"),
'src1_add_mode' : ("wr", "tr", "or"),
'src2_add_mode' : ("wr", "tr", "or"),
'sync_async' : (".async",".sync"),
'tag_n_bitfld' : (".packed_bitfld", ".tagged_vect"),
'trace' : (".notrace", ".trace"),
'coherent' : (".nocoherent", ".coherent"),
'thld_cmp' : (".no_thld_cmp", ".thld_cmp"),
'thld_mode' : (".gt_thld", ".ge_thld"),
'trans_type' : (".sysram2opram",".opram2sysram"),
'tw_ovs' : (".noovs",".ovs2",".ovs4",".ovs8",".ovs16",".ovs32",".ovs64",".ovs128",".ovs256",".ovs512"),
'wdog_ev' : (".ev0", ".ev1", ".ev2", ".ev3", ".rcs", ".rfs"),
'wdog_op' : (".start",".stop",".reset",".event"),
'win_type' : (".no_win",".cmplx_win",".real_win_im_tram",".real_win_real_tram"),
'win_type0' : (".cmplx_win",".real_win_im_tram",".real_win_real_tram"),

}

instructions = {
'add.immed' : ["shft modulo_val src_add , src2_add , dest_add"],
'add.reg' : ["shft modulo_val src_add , src2_add_wr , dest_add"],
'add' : ["shft modulo_val src_add , src2_add_wr , dest_add"],
'cmp' : ["src_add , src2_add_wr , dest_add"],
'cmp.immed' : ["src_add , src2_add , dest_add"],
'cmp.reg' : ["src_add , src2_add_wr , dest_add"],
'copy' : ["in_dattyp2 cp_type_simple rst_n_keep vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc"] ,
'copy.ind' : ["in_dattyp2 cp_type_simple rst_n_keep vec_sz src_add_WR , src_add_inc , dest_add_inc"] ,
'copy_n_mask' : ["in_dattyp2 cp_type_simple rst_n_keep vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , cp_mask"] ,
'copy_n_mask.ind' : ["in_dattyp2 cp_type_simple rst_n_keep vec_sz src_add_WR , src_add_inc , dest_add_inc , cp_mask"] ,
'copy.trans' : ["in_dattyp2 cp_type_trans rst_n_keep vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , blk_src_inc , blk_dest_inc"] ,
'copy.trans.ind' : ["in_dattyp2 cp_type_trans rst_n_keep vec_sz src_add_WR , src_add_inc , dest_add_inc , blk_src_inc , blk_dest_inc"] ,
'copy.trans_n_mask' : ["in_dattyp2 cp_type_trans rst_n_keep vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , blk_src_inc , blk_dest_inc , cp_mask"] ,
'copy.trans_n_mask.ind' : ["in_dattyp2 cp_type_trans rst_n_keep vec_sz src_add_WR , src_add_inc , dest_add_inc , blk_src_inc , blk_dest_inc , cp_mask"] ,
'copy.thld' : ["in_dattyp2 cp_type_threshold rst_n_keep pre_proc rst_acc vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , thld_add"] ,
'copy.thld.ind' : ["in_dattyp2 cp_type_threshold rst_n_keep pre_proc rst_acc vec_sz src_add_WR , src_add_inc , dest_add_inc , thld_add"] ,
'copy.thld_n_step' : ["in_dattyp2 cp_type_thresholdstep rst_n_keep pre_proc rst_acc vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , thld_add , thld_const"] ,
'copy.thld_n_step.ind' : ["in_dattyp2 cp_type_thresholdstep rst_n_keep pre_proc rst_acc vec_sz src_add_WR , src_add_inc , dest_add_inc , thld_add , thld_const"] ,
'copy.scat' : ["in_dattyp2 rst_n_keep vec_sz src_add , dest_add_O , tw_add"] ,
'copy.scat.ind' : ["in_dattyp2 rst_n_keep vec_sz src_add_WR , tw_add"] ,
'copy_n_mask.scat' : ["in_dattyp2 rst_n_keep vec_sz src_add , dest_add_O , tw_add , cp_mask"] ,
'copy_n_mask.scat.ind' : ["in_dattyp2 rst_n_keep vec_sz src_add_WR , tw_add , cp_mask"] ,
'copy.clear' : ["vec_sz dest_add_O , cp_mask"] ,
'dsp' : ["dsp_val"],
'evt' : ["ev_type ev_lvl evt_ev"],
'fir' : ["in_dattyp win_type0 init shft_val no_of_taps vec_sz src_add , dest_add_O , tap_coef_add , src_add_inc , dest_add_inc"],
'fir.ind' : ["in_dattyp win_type0 init shft_val no_of_taps vec_sz src_add_WR , tap_coef_add , src_add_inc , dest_add_inc "],
'fir.shift_wr' : ["in_dattyp win_type0 init shft_ofst shft_wr no_of_taps vec_sz src_add , dest_add_O , tap_coef_add , src_add_inc , dest_add_inc"],
'fir.shift_wr.ind' : ["in_dattyp win_type0 init shft_ofst shft_wr no_of_taps vec_sz src_add_WR , tap_coef_add , src_add_inc , dest_add_inc"],
'get' : ["src_add , dest_add"],
'get.ind' : ["src_add_WR"],
'hist' : ["in_dattyp2 pre_proc hist_mode bin_sz pack_en dat_sz vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , threshold"],
'hist.ind' : ["in_dattyp2 pre_proc hist_mode bin_sz pack_en dat_sz vec_sz src_add_WR , src_add_inc , dest_add_inc , threshold"],
'irdx2' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat2 shft_val vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.ind' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat2 shft_val vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.shift_wr' : ["in_dattyp quad_ext tw_ovs repeat2 shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.shift_wr.ind' : ["in_dattyp quad_ext tw_ovs repeat2 shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.adptv' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat2 shft_val adptv_shft adptv_ofst adptv_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.adptv.ind' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat2 shft_val adptv_shft adptv_ofst adptv_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.adptv.shift_wr' : ["in_dattyp quad_ext tw_ovs repeat2 adptv_shft shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx2.adptv.shift_wr.ind' : ["in_dattyp quad_ext tw_ovs repeat2 adptv_shft shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'irdx4' : ["in_dattyp win_type repeat quad_ext tw_ovs fft_rnd shft_val vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , cc_im , cc_re", "mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'irdx4.adptv' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd adptv_shft adptv_ofst adptv_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'irdx4.adptv.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd adptv_shft adptv_ofst adptv_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'irdx4.ind' : [ "in_dattyp win_type repeat quad_ext tw_ovs fft_rnd shft_val vec_sz src_add_WR , src_add_inc , dest_add_inc , cc_im , cc_re", "mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'irdx4.shift' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_val vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'irdx4.shift.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_val vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'irdx4.shift_wr' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc "],
'irdx4.shift_wr.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'jumpa' : ["rel_off"],
'jumpc' : ["cond_sel cond_wr rel_off"],
'loop' : ["lp_cnt"],
'loop.reg' : ["lp_wr"],
'maxs.gm' : ["in_dattyp2 out_mode pre_proc in_pack gm_preload vec_sz src_add , dest_add , src_add_inc , dest_add_inc , thld_add"],
'maxs.gm.ind' : ["in_dattyp2 out_mode pre_proc in_pack gm_preload vec_sz src_add_WR , src_add_inc , dest_add_inc , thld_add"],
'maxs.lm' : ["in_dattyp2_lm out_mode pre_proc cyc_extn in_pack vec_sz src_add , dest_add , src_add_inc , dest_add_inc"],
'maxs.lm.ind' : ["in_dattyp2_lm out_mode pre_proc cyc_extn in_pack vec_sz src_add_WR , src_add_inc , dest_add_inc"],
'maxs.lm.bfld' : ["in_dattyp2_lm pre_proc cyc_extn in_pack vec_sz src_add , dest_add , src_add_inc , dest_add_inc , bitfld_size"],
'maxs.lm.bfld.ind' : ["in_dattyp2_lm pre_proc cyc_extn in_pack vec_sz src_add_WR , src_add_inc , dest_add_inc , bitfld_size"],
'maxs.lmth' : ["in_dattyp2_lm out_mode pre_proc cyc_extn in_pack thld_mode  vec_sz src_add , dest_add , src_add_inc , dest_add_inc , thld_add"],
'maxs.lmth.ind' : ["in_dattyp2_lm out_mode pre_proc cyc_extn in_pack thld_mode  vec_sz src_add_WR , src_add_inc , dest_add_inc , thld_add"],
'maxs.lmth.bfld' : ["in_dattyp2_lm pre_proc cyc_extn in_pack thld_mode  vec_sz src_add , dest_add , src_add_inc , dest_add_inc , thld_add , bitfld_size"],
'maxs.lmth.bfld.ind' : ["in_dattyp2_lm pre_proc cyc_extn in_pack thld_mode vec_sz src_add_WR , src_add_inc , dest_add_inc , thld_add , bitfld_size"],
'maxs.th' : ["in_dattyp2 out_mode pre_proc in_pack thld_mode vec_sz src_add , dest_add , src_add_inc , dest_add_inc , thld_add"],
'maxs.th.ind' : ["in_dattyp2 out_mode pre_proc in_pack thld_mode vec_sz src_add_WR , src_add_inc , dest_add_inc , thld_add"],
'next' : [""],
'pdma' : ["se data_packing trans_type sync_async trace coherent vector_len sysram_mem_start_addr , opram_mem_start_addr , opram_skip_addr , opram_continuous_addr , sysram_skip_addr , sysram_continous_addr"],
'pdma.ind' : ["se data_packing trans_type sync_async trace coherent vector_len sysram_mem_start_addr , opram_mem_start_addr_ind , opram_skip_addr , opram_continuous_addr , sysram_skip_addr , sysram_continous_addr"],
'rdx2' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat real_fft shft_val vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.ind' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat real_fft shft_val vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.shift_wr' : ["in_dattyp quad_ext tw_ovs repeat real_fft shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.shift_wr.ind' : ["in_dattyp quad_ext tw_ovs repeat real_fft shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.adptv' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat real_fft shft_val adptv_shft adptv_ofst adptv_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.adptv.ind' : ["in_dattyp quad_ext tw_ovs fft_rnd_rdx2 repeat real_fft shft_val adptv_shft adptv_ofst adptv_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.adptv.shift_wr' : ["in_dattyp quad_ext tw_ovs repeat real_fft adptv_shft shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx2.adptv.shift_wr.ind' : ["in_dattyp quad_ext tw_ovs repeat real_fft adptv_shft shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc"],
'rdx4' : ["in_dattyp win_type repeat quad_ext tw_ovs fft_rnd shft_val vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , cc_im , cc_re", "mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.adptv' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd adptv_shft adptv_ofst adptv_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.adptv.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd adptv_shft adptv_ofst adptv_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.ind' : [ "in_dattyp win_type repeat quad_ext tw_ovs fft_rnd shft_val vec_sz src_add_WR , src_add_inc , dest_add_inc , cc_im , cc_re", "mult_mode in_dattyp win_type repeat quad_ext tw_ovs fft_rnd vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.shift' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_val vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.shift.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_val vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.shift_wr' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc "],
'rdx4.shift_wr.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.adptv.shift' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_val adptv_shft vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.adptv.shift.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs shft_val adptv_shft vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'rdx4.adptv.shift_wr' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs adptv_shft shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc "],
'rdx4.adptv.shift_wr.ind' : ["mult_mode in_dattyp win_type repeat quad_ext tw_ovs adptv_shft shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'scp' : ["in_dattyp re_im_coeff shft_val no_of_taps vec_sz src_add , dest_add_O , coef_add , src_add_inc , dest_add_inc"],
'scp.ind' : ["in_dattyp re_im_coeff shft_val no_of_taps vec_sz src_add_WR , coef_add , src_add_inc , dest_add_inc"],
'scp.shift_wr' : ["in_dattyp re_im_coeff shft_ofst shft_wr no_of_taps vec_sz src_add , dest_add_O , coef_add , src_add_inc , dest_add_inc"],
'scp.shift_wr.ind' : ["in_dattyp re_im_coeff shft_ofst shft_wr no_of_taps vec_sz src_add_WR , coef_add , src_add_inc , dest_add_inc"],
'sel' : ["re_im wr dest_add src1_add , src2_add_wr , src3_add"],
'set' : ["src_add_WR , dest_add"],
'set.immed' : ["imm_dat , dest_add"],
'set.ind' : ["src_add_WR"],
'stop' : [""],
'repeat' : ["rpt_cnt addr_incr0 , addr_incr1 , addr_incr2 , addr_incr3"],
'sub.immed' : ["shft modulo_val src_add , src2_add , dest_add"],
'sub' : ["shft modulo_val src_add , src2_add_wr , dest_add"],
'sub.reg' : ["shft modulo_val src_add , src2_add_wr , dest_add"],
'thread' : ["th_id"],
'sync' : [""],
'sync.dsp' : [""],
'sync.pdma' : ["cs_id"],
'sync.thread' : ["cs_id"],
'vmt' : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add , dest_add_O , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc"],
'vmt.imm_off_sq2s2'     : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add , dest_add_O , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_re_imdt_value , sq2s2_im_imdt_value"],
'vmt.imm_off_sq2s2.ind' : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add_WR , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_re_imdt_value , sq2s2_im_imdt_value"],
'vmt.ind'               : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add_WR , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc"],
'vmt.shift_sq2s2'       : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add , dest_add_O , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_shift_value"],
'vmt.shift_sq2s2.ind'   : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add_WR , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_shift_value"],
'vmt.vec_sq2s2'         : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add , dest_add_O , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_vec_src"],
'vmt.vec_sq2s2.ind'     : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add_WR , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_vec_src"],
'vmt.wr_off_sq2s2'      : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add , dest_add_O , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_offset_value"],
'vmt.wr_off_sq2s2.ind'  : ["in_dattyp rst_acc_vmt ip_pack op_pack opsq1 opsq2s1 opsq2s3 vec_sz src_add_WR , mult_s_exp_n_val_addr , src_add_inc , dest_add_inc , sq2s2_offset_value"],
'wait.cpu' : ["wait_ev"],
'wait.ext' : ["wait_ev"],
'wait.int' : ["wait_ev"],
'watchdog' : ["ev_tr wdog_op wdog_ev count"],
'win' : ["in_dattyp win_type0 shft_val vec_sz src_add , dest_add_O , src_add_inc , dest_add_inc , cc_im , cc_re", "mult_mode in_dattyp win_type0 shft_val vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'win.ind' : [ "in_dattyp win_type0 shft_val vec_sz src_add_WR , src_add_inc , dest_add_inc , cc_im , cc_re", "mult_mode in_dattyp win_type0 shft_val vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'win.shift_wr.ind' : ["mult_mode in_dattyp win_type0 shft_ofst shft_wr vec_sz src_add_WR , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
'win.shift_wr' : ["mult_mode in_dattyp win_type0 shft_ofst shft_wr vec_sz src_add , dest_add_O , mult_coef_add , src_add_inc , dest_add_inc , mca_mod , mca_inc"],
}

class Writer:
    phyle = None
    test = None
    lines = 0
    count = 0

    def __init__(self, s):
        self.test = s
        self.count = 0

    def close(self):
        self.phyle.close();
        self.lines = 0
        self.phyle = None
        #print "close ", self.test

    def writehdr(self):
        self.phyle.write('.include "tram3.inc"\n.include "oram3.inc"\n.include "wr3.inc"\n')

    def write(self,s):
        if self.lines == 1000:
            self.close()
            #print self.phyle
        if self.phyle is None:
            #print "None ", self.count
            if self.count == 0:
                self.phyle = open(self.test + '.spt3','w')
            else:
                self.phyle = open(self.test + '_' + str(self.count) + '.spt3','w')
                #print self.test, "_", str(self.count)
            self.writehdr()
            self.count = self.count + 1
            self.lines = 1
        self.phyle.write(s);
        self.lines = self.lines + 1
        #print self.test, " ", self.lines

def deep(strg, oprs):
    if (len(oprs) == 0):
        writer.write(strg+'\n')
        return
    op = oprs[0]
    oprs = oprs[1:]
    if op not in operands:
        if op == ',':
            deep(strg + op, oprs)
        else:
#            print(op)
            deep(strg + ' ' + op, oprs)
    else:
        for o in operands[op]:
            deep(strg+' '+o, oprs)

for i in (instructions.keys()):
    writer = Writer(i)
    for s in instructions[i]:
        deep(i , s.split(' '))
    writer.close()
    
