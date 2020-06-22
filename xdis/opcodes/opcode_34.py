# (C) Copyright 2017, 2020 by Rocky Bernstein
"""
CPython 3.4 bytecode opcodes

This is a like Python 3.4's opcode.py with some classification
of stack usage.
"""

from xdis.opcodes.base import (
    def_op,
    finalize_opcodes,
    format_CALL_FUNCTION_pos_name_encoded,
    format_MAKE_FUNCTION_arg,
    format_extended_arg,
    free_op,
    init_opdata,
    rm_op,
    update_pj3,
)

import xdis.opcodes.opcode_33 as opcode_33

version = 3.4
python_implementation = "CPython"

l = locals()

init_opdata(l, opcode_33, version)

# These are removed since Python 3.3
rm_op(l, "STORE_LOCALS", 69)

# These are new since Python 3.3
free_op(l, "LOAD_CLASSDEREF", 148)

update_pj3(globals(), l)

opcode_arg_fmt = {
    "CALL_FUNCTION": format_CALL_FUNCTION_pos_name_encoded,
    "CALL_FUNCTION_KW": format_CALL_FUNCTION_pos_name_encoded,
    "CALL_FUNCTION_VAR_KW": format_CALL_FUNCTION_pos_name_encoded,
    "MAKE_FUNCTION": format_MAKE_FUNCTION_arg,
    "EXTENDED_ARG": format_extended_arg,
}

opcode_extended_fmt = {
    "MAKE_FUNCTION": opcode_33.extended_format_MAKE_FUNCTION,
}

finalize_opcodes(l)
