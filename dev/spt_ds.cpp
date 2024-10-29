//
// Copyright 2024 NXP
// SPDX-License-Identifier: GPL-3.0+
//

//
// Extra disassembler support for SPT3.8.
//

extern "C" {
# include "config.h"
}

#include "dis-asm.h"


void disassemble_init_adl (struct disassemble_info * info)
{
   info->skip_zeroes = 16;
}

