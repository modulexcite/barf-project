#! /usr/bin/env python

from barf.barf import BARF

if __name__ == "__main__":
    #
    # Open file
    #
    barf = BARF("../../samples/bin/branch4.x86")

    #
    # Translate to REIL
    #
    print("[+] Translating: x86 -> REIL -> SMT...")

    for addr, asm_instr, reil_instrs in barf.translate():
        print("0x{0:08x} : {1}".format(addr, asm_instr))

        for reil_instr in reil_instrs:
            print("{0:14}{1}".format("", reil_instr))

            try:
                # Some instructions cannot be translate to SMT, i.e,
                # UNKN, UNDEF, JCC. In those cases, an exception is
                # raised.
                smt_exprs = barf.smt_translator.translate(reil_instr)

                for smt_expr in smt_exprs:
                    print("{0:16}{1}".format("", smt_expr))
            except:
                pass
