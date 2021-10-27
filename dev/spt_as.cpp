//
// Copyright 2020-2021 NXP
// SPDX-License-Identifier: GPL-3.0+
//

//
// Extra assembler support for SPT3.4.
//

#ifndef _MSC_VER
extern "C" {
 #include "as.h"
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

static bool is_32bit_ARM = false;

static int arm32_jump_reloc;
static int arm64_jump_reloc;
static int arm32_pdma_reloc;
static int arm64_pdma_reloc;

// We want to store the BFD code, not the HOWTO type.
static int get_reloc(const string &rname,const adl_reloc_name *relocs_by_index,
                     int num_relocs_by_index, const reloc_howto_type *relocs) {
  for (int i = 0; i != num_relocs_by_index; ++i) {
    reloc_howto_type *howto = &relocs[relocs_by_index[i].index];
    if (howto->name && howto->name == rname) {
      return relocs_by_index[i].code;
    }
  }

  as_fatal("Could not find relocation %s\n",rname.c_str());
  return -1;
}

void acb_setup_finish(struct hash_control *instr_hash, struct adl_field *all_field,
	              int num_fields, const reloc_howto_type *relocs,
	              int num_relocs, const adl_reloc_name *relocs_by_index,
                      int num_relocs_by_index) {
  gas_assert(stdoutput != 0);
  if (is_32bit_ARM) {
    Elf_Internal_Ehdr * i_ehdrp;	/* ELF file header, internal form.  */
    i_ehdrp = elf_elfheader(stdoutput);
    i_ehdrp->e_flags |= 0x05000000;
  }

  // Lookup relocations by name.
  arm32_jump_reloc = get_reloc("R_ARM_REL32_NOI",relocs_by_index,num_relocs_by_index,relocs);
  arm64_jump_reloc = get_reloc("R_AARCH64_PREL32",relocs_by_index,num_relocs_by_index,relocs);
  arm32_pdma_reloc = get_reloc("R_ARM_ABS32_NOI",relocs_by_index,num_relocs_by_index,relocs);
  arm64_pdma_reloc = get_reloc("R_AARCH64_ABS32",relocs_by_index,num_relocs_by_index,relocs);

  // Explicitly enable right shifts to be signed. Fix for CMPMISC-267.
  expr_signed_right_shift = 1;
}

void acb_after_parse_args()
{
  static bool inited;
  if (!inited) {
    string str = default_adl_target_format();
    is_32bit_ARM = str.find("32") != std::string::npos;
    inited = 1;
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
  int rtype = fixP->fx_r_type;
  if ((rtype == arm64_pdma_reloc || rtype == arm32_pdma_reloc)
      && !strcmp(seg->name, ".text")) {
    if (is_32bit_ARM)
      fixP->fx_r_type = (bfd_reloc_code_real_type)arm32_pdma_reloc;
    else
      fixP->fx_r_type = (bfd_reloc_code_real_type)arm64_pdma_reloc;
  }

  if ((rtype == arm64_jump_reloc || rtype == arm32_jump_reloc)
      && !strcmp(seg->name, ".text")) {
    if (is_32bit_ARM)
      fixP->fx_r_type = (bfd_reloc_code_real_type)arm32_jump_reloc;
    else
      fixP->fx_r_type = (bfd_reloc_code_real_type)arm64_jump_reloc;
  }

  // Place of relocation is 32bit away from the instruction boundary. Since
  // this is a PC relative relocation, the resolved value will always point
  // to the start of destination instruction and calculated from the origin
  // instruction boundary. So add the offset from the relocation to the
  // instruction boundary as an addend.
  if (rtype == arm64_jump_reloc || rtype == arm32_jump_reloc)
    *valP = *valP + 4;

  return false;
}

// Generate a reloc for a fixup. This is mostly a clone of the standard function
// tc_gen_reloc. The only difference is that the relocation for BFD_RELOC_32 is
// renamed to R_AARCH64_ABS32. Since R_AARCH64_ABS32 is being used as relocation
// for PDMA instruction, the same cannot be used as an alias for BFD_RELOC_32
// elsewhere. Hence when BFD_RELOC_32 gets generated elsewhere, its renamed to
// SPT/AARCH64 specific R_AARCH64_ABS32.
arelent *acb_gen_reloc (asection *seg ATTRIBUTE_UNUSED,fixS *fixp)
{
  arelent *reloc;
  bfd_reloc_code_real_type rtype = fixp->fx_r_type;

  if (is_32bit_ARM == false) {
    // 2 is BFD_RELOC_32
    if (rtype == 2)
      rtype = (bfd_reloc_code_real_type)arm64_pdma_reloc;
  }

  reloc = (arelent *) xmalloc (sizeof (arelent));

  reloc->sym_ptr_ptr = (asymbol **) xmalloc (sizeof (asymbol *));
  *reloc->sym_ptr_ptr = symbol_get_bfdsym (fixp->fx_addsy);
  reloc->address = fixp->fx_frag->fr_address + fixp->fx_where;
  reloc->howto = bfd_reloc_type_lookup (stdoutput, rtype);
  if (reloc->howto == (reloc_howto_type *) NULL) {
      AS_BAD_WHERE (fixp->fx_file, fixp->fx_line,
                    _("reloc %d not supported by object file format"),
                    (int) fixp->fx_r_type);
      return NULL;
  }
  reloc->addend = fixp->fx_addnumber;

  return reloc;
}

