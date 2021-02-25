/*
 * Copyright 2018-2021 NXP
 * SPDX-License-Identifier: GPL-3.0+
 */

//
// Extra disassembler support for SPT3.1.
//

extern "C" {
# include "config.h"
}

#include "dis-asm.h"


void disassemble_init_adl (struct disassemble_info * info) 
{
   info->skip_zeroes = 16;
}

