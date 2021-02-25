//
// Extra assembler support for RISC-V.
//
// This handles stuff like branch transformation and relocations.  Branch
// transformation is required when a branch's target is too far away- the branch
// is negated, then a jump is appended.  That way, the conditional branch avoids
// the jump if the condition doesn't hold, otherwise the jump is taken.
//
// Relaxation handles function calls.  The compiler emits assembler pseudo-ops
// like "call" and "tail".  These are expanded into instruction pairs- auipc and
// jalr.  If the function call is close enough, we can then convert those to
// single jal instructions in the linker.  This requires us to emit pairs of
// relocations- a relax relocation and then the usual high-address relocation.
//
// Most of this code comes from RISC-V binutils.

extern "C" {
#include "as.h"
}

#include <assert.h>
#include <iostream>
#include <unordered_map>

#include "adl-asm-impl.h"
#include "adl-asm-info.h"

using namespace std;
  
static bool set_machine_code(int emc) {
  extern bfd_target powerpc_elf64_vec;
  extern bfd_target powerpc_elf64_le_vec;
  extern bfd_target powerpc_elf32_vec;
  extern bfd_target powerpc_elf32_le_vec;
  ((struct elf_backend_data*)(powerpc_elf64_vec.backend_data))->elf_machine_code = emc;
  ((struct elf_backend_data*)(powerpc_elf64_le_vec.backend_data))->elf_machine_code = emc;
  ((struct elf_backend_data*)(powerpc_elf32_vec.backend_data))->elf_machine_code = emc;
  ((struct elf_backend_data*)(powerpc_elf32_le_vec.backend_data))->elf_machine_code = emc;
  return true;
}


static bool inited, is_ARM = false;
extern bfd *stdoutput;

void acb_after_parse_args()
{
	if (!inited) {
		string str = default_adl_target_format();
		is_ARM = str.find("32")!=std::string::npos;
		inited = set_machine_code(is_ARM?40:183);
	}
}

void acb_setup_finish(struct hash_control *instr_hash,struct adl_field *all_fields,
                                            int num_fields,const reloc_howto_type *relocs,int num_relocs)
{
	gas_assert (stdoutput != 0);
	if (is_ARM) {
		  Elf_Internal_Ehdr * i_ehdrp;	/* ELF file header, internal form.  */
		  i_ehdrp = elf_elfheader (stdoutput);
		  i_ehdrp->e_flags |= 0x05000000;
	}

}


bool acb_apply_fix (fixS *fixP ,valueT *valP ,segT seg ATTRIBUTE_UNUSED)
{ 
int rtype = fixP->fx_r_type;

	if (rtype == 5) {
		fixP->fx_where += 4;
		if (is_ARM)
			fixP->fx_r_type=(bfd_reloc_code_real_type)2;
		else
			fixP->fx_r_type=(bfd_reloc_code_real_type)258;

	}
  return false;
}
