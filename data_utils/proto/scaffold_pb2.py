# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scaffold.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scaffold.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0escaffold.proto\"\x1a\n\x06LsAtom\x12\x10\n\x08idx_atom\x18\x01 \x03(\x05\"i\n\x0cTupMolLsatom\x12\x0f\n\x07idx_mol\x18\x01 \x01(\x05\x12\x18\n\x07ls_atom\x18\x02 \x01(\x0b\x32\x07.LsAtom\x12\x16\n\x05ls_nh\x18\x03 \x01(\x0b\x32\x07.LsAtom\x12\x16\n\x05ls_np\x18\x04 \x01(\x0b\x32\x07.LsAtom\"6\n\x0eLsDicmollsatom\x12$\n\rdic_mol_atoms\x18\x01 \x03(\x0b\x32\r.TupMolLsatom\"\x8b\x01\n\rDicScaffoldLs\x12\x35\n\x0cidx_scaffold\x18\x08 \x03(\x0b\x32\x1f.DicScaffoldLs.IdxScaffoldEntry\x1a\x43\n\x10IdxScaffoldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.LsDicmollsatom:\x02\x38\x01\"[\n\x08\x44icSmIdx\x12\"\n\x05sm_sc\x18\x07 \x03(\x0b\x32\x13.DicSmIdx.SmScEntry\x1a+\n\tSmScEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"[\n\x08\x44icIdxSm\x12\"\n\x05sm_sc\x18\x07 \x03(\x0b\x32\x13.DicIdxSm.SmScEntry\x1a+\n\tSmScEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8a\x01\n\x08\x44icIdxLs\x12\x36\n\x0fsmiles_scaffold\x18\x08 \x03(\x0b\x32\x1d.DicIdxLs.SmilesScaffoldEntry\x1a\x46\n\x13SmilesScaffoldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.LsDicmollsatom:\x02\x38\x01\x62\x06proto3')
)




_LSATOM = _descriptor.Descriptor(
  name='LsAtom',
  full_name='LsAtom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_atom', full_name='LsAtom.idx_atom', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=44,
)


_TUPMOLLSATOM = _descriptor.Descriptor(
  name='TupMolLsatom',
  full_name='TupMolLsatom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_mol', full_name='TupMolLsatom.idx_mol', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ls_atom', full_name='TupMolLsatom.ls_atom', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ls_nh', full_name='TupMolLsatom.ls_nh', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ls_np', full_name='TupMolLsatom.ls_np', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=151,
)


_LSDICMOLLSATOM = _descriptor.Descriptor(
  name='LsDicmollsatom',
  full_name='LsDicmollsatom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dic_mol_atoms', full_name='LsDicmollsatom.dic_mol_atoms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=207,
)


_DICSCAFFOLDLS_IDXSCAFFOLDENTRY = _descriptor.Descriptor(
  name='IdxScaffoldEntry',
  full_name='DicScaffoldLs.IdxScaffoldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DicScaffoldLs.IdxScaffoldEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DicScaffoldLs.IdxScaffoldEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=349,
)

_DICSCAFFOLDLS = _descriptor.Descriptor(
  name='DicScaffoldLs',
  full_name='DicScaffoldLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_scaffold', full_name='DicScaffoldLs.idx_scaffold', index=0,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DICSCAFFOLDLS_IDXSCAFFOLDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=349,
)


_DICSMIDX_SMSCENTRY = _descriptor.Descriptor(
  name='SmScEntry',
  full_name='DicSmIdx.SmScEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DicSmIdx.SmScEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DicSmIdx.SmScEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=399,
  serialized_end=442,
)

_DICSMIDX = _descriptor.Descriptor(
  name='DicSmIdx',
  full_name='DicSmIdx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sm_sc', full_name='DicSmIdx.sm_sc', index=0,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DICSMIDX_SMSCENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=442,
)


_DICIDXSM_SMSCENTRY = _descriptor.Descriptor(
  name='SmScEntry',
  full_name='DicIdxSm.SmScEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DicIdxSm.SmScEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DicIdxSm.SmScEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=535,
)

_DICIDXSM = _descriptor.Descriptor(
  name='DicIdxSm',
  full_name='DicIdxSm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sm_sc', full_name='DicIdxSm.sm_sc', index=0,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DICIDXSM_SMSCENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=535,
)


_DICIDXLS_SMILESSCAFFOLDENTRY = _descriptor.Descriptor(
  name='SmilesScaffoldEntry',
  full_name='DicIdxLs.SmilesScaffoldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DicIdxLs.SmilesScaffoldEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DicIdxLs.SmilesScaffoldEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=676,
)

_DICIDXLS = _descriptor.Descriptor(
  name='DicIdxLs',
  full_name='DicIdxLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='smiles_scaffold', full_name='DicIdxLs.smiles_scaffold', index=0,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DICIDXLS_SMILESSCAFFOLDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=676,
)

_TUPMOLLSATOM.fields_by_name['ls_atom'].message_type = _LSATOM
_TUPMOLLSATOM.fields_by_name['ls_nh'].message_type = _LSATOM
_TUPMOLLSATOM.fields_by_name['ls_np'].message_type = _LSATOM
_LSDICMOLLSATOM.fields_by_name['dic_mol_atoms'].message_type = _TUPMOLLSATOM
_DICSCAFFOLDLS_IDXSCAFFOLDENTRY.fields_by_name['value'].message_type = _LSDICMOLLSATOM
_DICSCAFFOLDLS_IDXSCAFFOLDENTRY.containing_type = _DICSCAFFOLDLS
_DICSCAFFOLDLS.fields_by_name['idx_scaffold'].message_type = _DICSCAFFOLDLS_IDXSCAFFOLDENTRY
_DICSMIDX_SMSCENTRY.containing_type = _DICSMIDX
_DICSMIDX.fields_by_name['sm_sc'].message_type = _DICSMIDX_SMSCENTRY
_DICIDXSM_SMSCENTRY.containing_type = _DICIDXSM
_DICIDXSM.fields_by_name['sm_sc'].message_type = _DICIDXSM_SMSCENTRY
_DICIDXLS_SMILESSCAFFOLDENTRY.fields_by_name['value'].message_type = _LSDICMOLLSATOM
_DICIDXLS_SMILESSCAFFOLDENTRY.containing_type = _DICIDXLS
_DICIDXLS.fields_by_name['smiles_scaffold'].message_type = _DICIDXLS_SMILESSCAFFOLDENTRY
DESCRIPTOR.message_types_by_name['LsAtom'] = _LSATOM
DESCRIPTOR.message_types_by_name['TupMolLsatom'] = _TUPMOLLSATOM
DESCRIPTOR.message_types_by_name['LsDicmollsatom'] = _LSDICMOLLSATOM
DESCRIPTOR.message_types_by_name['DicScaffoldLs'] = _DICSCAFFOLDLS
DESCRIPTOR.message_types_by_name['DicSmIdx'] = _DICSMIDX
DESCRIPTOR.message_types_by_name['DicIdxSm'] = _DICIDXSM
DESCRIPTOR.message_types_by_name['DicIdxLs'] = _DICIDXLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LsAtom = _reflection.GeneratedProtocolMessageType('LsAtom', (_message.Message,), dict(
  DESCRIPTOR = _LSATOM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:LsAtom)
  ))
_sym_db.RegisterMessage(LsAtom)

TupMolLsatom = _reflection.GeneratedProtocolMessageType('TupMolLsatom', (_message.Message,), dict(
  DESCRIPTOR = _TUPMOLLSATOM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:TupMolLsatom)
  ))
_sym_db.RegisterMessage(TupMolLsatom)

LsDicmollsatom = _reflection.GeneratedProtocolMessageType('LsDicmollsatom', (_message.Message,), dict(
  DESCRIPTOR = _LSDICMOLLSATOM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:LsDicmollsatom)
  ))
_sym_db.RegisterMessage(LsDicmollsatom)

DicScaffoldLs = _reflection.GeneratedProtocolMessageType('DicScaffoldLs', (_message.Message,), dict(

  IdxScaffoldEntry = _reflection.GeneratedProtocolMessageType('IdxScaffoldEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICSCAFFOLDLS_IDXSCAFFOLDENTRY,
    __module__ = 'scaffold_pb2'
    # @@protoc_insertion_point(class_scope:DicScaffoldLs.IdxScaffoldEntry)
    ))
  ,
  DESCRIPTOR = _DICSCAFFOLDLS,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:DicScaffoldLs)
  ))
_sym_db.RegisterMessage(DicScaffoldLs)
_sym_db.RegisterMessage(DicScaffoldLs.IdxScaffoldEntry)

DicSmIdx = _reflection.GeneratedProtocolMessageType('DicSmIdx', (_message.Message,), dict(

  SmScEntry = _reflection.GeneratedProtocolMessageType('SmScEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICSMIDX_SMSCENTRY,
    __module__ = 'scaffold_pb2'
    # @@protoc_insertion_point(class_scope:DicSmIdx.SmScEntry)
    ))
  ,
  DESCRIPTOR = _DICSMIDX,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:DicSmIdx)
  ))
_sym_db.RegisterMessage(DicSmIdx)
_sym_db.RegisterMessage(DicSmIdx.SmScEntry)

DicIdxSm = _reflection.GeneratedProtocolMessageType('DicIdxSm', (_message.Message,), dict(

  SmScEntry = _reflection.GeneratedProtocolMessageType('SmScEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICIDXSM_SMSCENTRY,
    __module__ = 'scaffold_pb2'
    # @@protoc_insertion_point(class_scope:DicIdxSm.SmScEntry)
    ))
  ,
  DESCRIPTOR = _DICIDXSM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:DicIdxSm)
  ))
_sym_db.RegisterMessage(DicIdxSm)
_sym_db.RegisterMessage(DicIdxSm.SmScEntry)

DicIdxLs = _reflection.GeneratedProtocolMessageType('DicIdxLs', (_message.Message,), dict(

  SmilesScaffoldEntry = _reflection.GeneratedProtocolMessageType('SmilesScaffoldEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICIDXLS_SMILESSCAFFOLDENTRY,
    __module__ = 'scaffold_pb2'
    # @@protoc_insertion_point(class_scope:DicIdxLs.SmilesScaffoldEntry)
    ))
  ,
  DESCRIPTOR = _DICIDXLS,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:DicIdxLs)
  ))
_sym_db.RegisterMessage(DicIdxLs)
_sym_db.RegisterMessage(DicIdxLs.SmilesScaffoldEntry)


_DICSCAFFOLDLS_IDXSCAFFOLDENTRY._options = None
_DICSMIDX_SMSCENTRY._options = None
_DICIDXSM_SMSCENTRY._options = None
_DICIDXLS_SMILESSCAFFOLDENTRY._options = None
# @@protoc_insertion_point(module_scope)