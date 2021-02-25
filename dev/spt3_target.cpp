//
// Extra assembler support for SPT3.1.
//
#ifndef _MSC_VER
extern "C" {
# include "config.h"
}
#endif

#include <iostream>
#include <stdio.h>

extern "C" {
 #include "as.h"
 #include "bfdver.h"
}


#include "adl-asm-impl.h"
#include "adl-asm-info.h"

using namespace std;

enum SPT_reloc_code {
  R_ARM_ABS32_NOI = 55,
  R_ARM_REL32_NOI = 56,
  R_AARCH64_ABS32 = 258,
  R_AARCH64_PREL32 = 261
};

static bool inited, is_32bit_ARM = false;
extern bfd *stdoutput;

extern "C" bfd_target powerpc_elf64_vec;
extern "C" bfd_target powerpc_elf64_le_vec;
extern "C" bfd_target powerpc_elf32_vec;
extern "C" bfd_target powerpc_elf32_le_vec;

static bool set_machine_code(int emc) {
  ((struct elf_backend_data*)(powerpc_elf64_vec.backend_data))->elf_machine_code = emc;
  ((struct elf_backend_data*)(powerpc_elf64_le_vec.backend_data))->elf_machine_code = emc;
  ((struct elf_backend_data*)(powerpc_elf32_vec.backend_data))->elf_machine_code = emc;
  ((struct elf_backend_data*)(powerpc_elf32_le_vec.backend_data))->elf_machine_code = emc;
  return true;
}

void acb_setup_finish(struct hash_control *instr_hash,
                      struct adl_field *all_field,
	              int num_fields, const reloc_howto_type *relocs,
	              int num_relocs)
{
  gas_assert(stdoutput != 0);
  if (is_32bit_ARM) {
    Elf_Internal_Ehdr * i_ehdrp;	/* ELF file header, internal form.  */
    i_ehdrp = elf_elfheader(stdoutput);
    i_ehdrp->e_flags |= 0x05000000;
  }
}

void acb_after_parse_args()
{
  if (!inited) {
    string str = default_adl_target_format();
    is_32bit_ARM = str.find("32") != std::string::npos;
    inited = set_machine_code(is_32bit_ARM ? 40 : 183);
  }
}

bool acb_apply_fix(fixS *fixP, valueT *valP, segT seg ATTRIBUTE_UNUSED)
{
  // Relocation for pdma instuction for 32bit arch should ideally be
  // R_ARM_ABS32. But unfortunately the enum value of this relocation
  // clashes with the adl native relocation BFD_RELOC_32, resulting
  // in buggy behaviour where BFD_RELOC_32 is used - like in debug sections.
  // So to avoid the clash, choose a different 32bit ARM relocation with a
  // similar behaviour. If there is no thumb code or overflow checking is
  // not relevant, both R_ARM_ABS32 and R_ARM_ABS32_NOI behave in a similar
  // manner.
  SPT_reloc_code rtype = (SPT_reloc_code)fixP->fx_r_type;
  if ((rtype == R_AARCH64_ABS32 || rtype == R_ARM_ABS32_NOI)
      && !strcmp(seg->name, ".text")) {
    if (is_32bit_ARM)
      fixP->fx_r_type = (bfd_reloc_code_real_type)R_ARM_ABS32_NOI;
    else
      fixP->fx_r_type = (bfd_reloc_code_real_type)R_AARCH64_ABS32;
  }

  // Place of relocation is 32bit away from the instruction boundary. Since
  // this is a PC relative relocation, the resolved value will always point
  // to the start of destination instruction and calculated from the origin
  // instruction boundary. So add the offset from the relocation to the
  // instruction boundary as an addend.
  if (rtype == R_AARCH64_PREL32 || rtype == R_ARM_REL32_NOI)
    *valP = *valP + 4;

  return false;
}

int acb_parse_option(int c, const char *arg)
{
  if (arg != 0L && !strcmp(arg, "version")) {
    /* This output is intended to follow the GNU standards document.  */
    printf(_("GNU assembler %s version %s for SPT3.1\n"), BFD_VERSION_STRING, adl_asm_version.c_str());
    printf(_("Copyright (C) 2014 Free Software Foundation, Inc.\n"));
    printf(_("This program is free software; you may redistribute it under\n\
the terms of the GNU General Public License version 3 or later.\n\
This program has absolutely no warranty.\n"));
    exit(0);
  }

  return 0;
}

