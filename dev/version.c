#include <stdio.h>
#include <string.h>
extern "C" {
#  include "as.h"
#  include "bfd/elf-bfd.h"
#  include "bfd/bfd.h"
#  include "bfd/libbfd.h"
#include "bfdver.h"
}

#define __NO_RNUMBER__

#include "adl-asm-impl.h"
#include "adl-asm-info.h"
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