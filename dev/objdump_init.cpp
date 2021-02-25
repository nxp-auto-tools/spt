extern "C" void set_machine(const char *);
static class adl_objdump_set_machine {
public: adl_objdump_set_machine() { set_machine("ppc"); }
} adl_objdump_set_machine;


