from construct import Struct, Union, Const, Computed, Short, Int, this, String, Byte, Optional, Single


color = Struct(
    # A colorStruct represents one color in the palette.
    "chunk_type" / Const(b"\x00\x01"),
    "chunk_length" / Int,  # Four bytes
    "title_length" / Short,  # Two bytes
    "title" / String(this.title_length * 2, encoding="utf-16be"),
    "color_mode" / String(4),  # Four bytes as a string.
    #               # Float  # Total Length       # Twice title length     # title_length+color_mode+swatch_type_index
    "color_values" / Single[(this.chunk_length - (this.title_length * 2) - 2 - 4 - 2) / Single.sizeof()],
    "swatch_type_index" / Short,  # Two bytes
)

end_palette = Struct(
    "chunk_type" / Const(b"\xc0\x02"),
    "chunk_length" / Int,
)

palette = Struct(
    "chunk_type" / Const(b"\xc0\x01"),
    "chunk_length" / Int,
    "title_length" / Short,
    "title" / String(this.title_length * 2, encoding="utf-16be"),
    "colors" / color[1:],
    "_end" / end_palette,
)


header = Struct(
    "datatype" / Const(b"ASEF"),
    "major_version" / Short,
    "minor_version" / Short,
    "bugfix_version" / Short,
    "chunk_count" / Short,
)


ase_file = Struct(
    "header" / header,
    "data" / Union(0, "palette" / Optional(palette), "colors" / Optional(color[1:]))
)
