
SPT.2017.EAR2 tools – November 20th, 2017

This release contains the tools, manuals and examples for the Signal Processing Toolbox SPT3 implementation. Note that SPT3 is source and binary incompatible with previous SPT versions.

Include files

inc/oram3.inc
inc/tram3.inc
inc/wr3.inc

define macros for the standard sources and destinations, the address map of SPT3 is different than SPT 1, 2 and 2.5 and require distinct includes.

Objdump

Since the SPT commands live in their own sections objdump needs to have the -D option specified to force disassembling the .spt section, the -r embeds the relocation information in the disassembly output.

Invocation
Spt3 supports 32 and 64 bits ARM ABIs:

* -a32 generates an ARM object file
* -a64 generates an AARch64 object file

The GNU assembler reference manual describes other options.

Known Issues

Bug fixes
The COPY instruction used the SPT 2 syntax in EAR1.
The MAXS instruction .lmth mode wasn’t supported in EAR1.
