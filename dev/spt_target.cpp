//
// Extra assembler support for SPT 2.8.
//

#ifndef _MSC_VER
extern "C" {
# include "config.h"
}
#endif

#include <iostream>
#include <stdio.h>

extern "C" {
#  include "as.h"
#  include "bfd/elf-bfd.h"
#  include "bfd/bfd.h"
#  include "bfd/libbfd.h"
#include "bfdver.h"
}

#include "adl-asm-impl.h"
#include "adl-asm-info.h"

using namespace std;

enum SPT_reloc_code {
    R_PPC_ADDR32 = 1,
    R_PPC_REL32 = 26
};

int acb_parse_option(int c,const char *arg)
{
  if (arg != 0L && !strcmp(arg,"version")) {
    /* This output is intended to follow the GNU standards document.  */
    printf (_("GNU assembler %s version: %s\n"), BFD_VERSION_STRING, adl_asm_version.c_str());
    printf (_("Copyright (C) 2014 Free Software Foundation, Inc.\n"));
    printf (_("\
This program is free software; you may redistribute it under the terms of\n\
the GNU General Public License version 3 or later.\n\
This program has absolutely no warranty.\n"));
    printf (_("This assembler was configured for a target of `%s'.\n"),
              "SPT2.8");
    exit(0);
  }

  return 0;
}

bool acb_apply_fix(fixS *fixP, valueT *valP, segT seg ATTRIBUTE_UNUSED)
{
  SPT_reloc_code rtype = (SPT_reloc_code)fixP->fx_r_type;
 
  // Global symbols need an addend of 8 to be added to the relocation. At the
  // point where this function is called, any local symbols are already
  // resolved. So members related to "Symbol" should be NULL for local symbols.
  if ((rtype == R_PPC_REL32)
      && (fixP->fx_addsy || fixP->fx_subsy)) {
      *valP = *valP + 8;
  }

  return false;
}

