# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: score.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='score.proto',
  package='NydusNetwork.API.Protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0bscore.proto\x12\x19NydusNetwork.API.Protocol\"\xd3\x01\n\x05Score\x12>\n\nscore_type\x18\x06 \x01(\x0e\x32*.NydusNetwork.API.Protocol.Score.ScoreType\x12\r\n\x05score\x18\x07 \x01(\x05\x12>\n\rscore_details\x18\x08 \x01(\x0b\x32\'.NydusNetwork.API.Protocol.ScoreDetails\";\n\tScoreType\x12\x13\n\x0fScoreType_UNSET\x10\x00\x12\x0e\n\nCurriculum\x10\x01\x12\t\n\x05Melee\x10\x02\"h\n\x14\x43\x61tegoryScoreDetails\x12\x0c\n\x04none\x18\x01 \x01(\x02\x12\x0c\n\x04\x61rmy\x18\x02 \x01(\x02\x12\x0f\n\x07\x65\x63onomy\x18\x03 \x01(\x02\x12\x12\n\ntechnology\x18\x04 \x01(\x02\x12\x0f\n\x07upgrade\x18\x05 \x01(\x02\"B\n\x11VitalScoreDetails\x12\x0c\n\x04life\x18\x01 \x01(\x02\x12\x0f\n\x07shields\x18\x02 \x01(\x02\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x02\"\xf0\n\n\x0cScoreDetails\x12\x1c\n\x14idle_production_time\x18\x01 \x01(\x02\x12\x18\n\x10idle_worker_time\x18\x02 \x01(\x02\x12\x19\n\x11total_value_units\x18\x03 \x01(\x02\x12\x1e\n\x16total_value_structures\x18\x04 \x01(\x02\x12\x1a\n\x12killed_value_units\x18\x05 \x01(\x02\x12\x1f\n\x17killed_value_structures\x18\x06 \x01(\x02\x12\x1a\n\x12\x63ollected_minerals\x18\x07 \x01(\x02\x12\x19\n\x11\x63ollected_vespene\x18\x08 \x01(\x02\x12 \n\x18\x63ollection_rate_minerals\x18\t \x01(\x02\x12\x1f\n\x17\x63ollection_rate_vespene\x18\n \x01(\x02\x12\x16\n\x0espent_minerals\x18\x0b \x01(\x02\x12\x15\n\rspent_vespene\x18\x0c \x01(\x02\x12\x42\n\tfood_used\x18\r \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12H\n\x0fkilled_minerals\x18\x0e \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12G\n\x0ekilled_vespene\x18\x0f \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12\x46\n\rlost_minerals\x18\x10 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12\x45\n\x0clost_vespene\x18\x11 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12O\n\x16\x66riendly_fire_minerals\x18\x12 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12N\n\x15\x66riendly_fire_vespene\x18\x13 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12\x46\n\rused_minerals\x18\x14 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12\x45\n\x0cused_vespene\x18\x15 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12L\n\x13total_used_minerals\x18\x16 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12K\n\x12total_used_vespene\x18\x17 \x01(\x0b\x32/.NydusNetwork.API.Protocol.CategoryScoreDetails\x12H\n\x12total_damage_dealt\x18\x18 \x01(\x0b\x32,.NydusNetwork.API.Protocol.VitalScoreDetails\x12H\n\x12total_damage_taken\x18\x19 \x01(\x0b\x32,.NydusNetwork.API.Protocol.VitalScoreDetails\x12\x42\n\x0ctotal_healed\x18\x1a \x01(\x0b\x32,.NydusNetwork.API.Protocol.VitalScoreDetailsb\x06proto3')
)



_SCORE_SCORETYPE = _descriptor.EnumDescriptor(
  name='ScoreType',
  full_name='NydusNetwork.API.Protocol.Score.ScoreType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ScoreType_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Curriculum', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Melee', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=195,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_SCORE_SCORETYPE)


_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='NydusNetwork.API.Protocol.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score_type', full_name='NydusNetwork.API.Protocol.Score.score_type', index=0,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='NydusNetwork.API.Protocol.Score.score', index=1,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score_details', full_name='NydusNetwork.API.Protocol.Score.score_details', index=2,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCORE_SCORETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=254,
)


_CATEGORYSCOREDETAILS = _descriptor.Descriptor(
  name='CategoryScoreDetails',
  full_name='NydusNetwork.API.Protocol.CategoryScoreDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='none', full_name='NydusNetwork.API.Protocol.CategoryScoreDetails.none', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='army', full_name='NydusNetwork.API.Protocol.CategoryScoreDetails.army', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='economy', full_name='NydusNetwork.API.Protocol.CategoryScoreDetails.economy', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='technology', full_name='NydusNetwork.API.Protocol.CategoryScoreDetails.technology', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='NydusNetwork.API.Protocol.CategoryScoreDetails.upgrade', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=360,
)


_VITALSCOREDETAILS = _descriptor.Descriptor(
  name='VitalScoreDetails',
  full_name='NydusNetwork.API.Protocol.VitalScoreDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='life', full_name='NydusNetwork.API.Protocol.VitalScoreDetails.life', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shields', full_name='NydusNetwork.API.Protocol.VitalScoreDetails.shields', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='energy', full_name='NydusNetwork.API.Protocol.VitalScoreDetails.energy', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=428,
)


_SCOREDETAILS = _descriptor.Descriptor(
  name='ScoreDetails',
  full_name='NydusNetwork.API.Protocol.ScoreDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idle_production_time', full_name='NydusNetwork.API.Protocol.ScoreDetails.idle_production_time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idle_worker_time', full_name='NydusNetwork.API.Protocol.ScoreDetails.idle_worker_time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_value_units', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_value_units', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_value_structures', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_value_structures', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='killed_value_units', full_name='NydusNetwork.API.Protocol.ScoreDetails.killed_value_units', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='killed_value_structures', full_name='NydusNetwork.API.Protocol.ScoreDetails.killed_value_structures', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collected_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.collected_minerals', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collected_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.collected_vespene', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_rate_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.collection_rate_minerals', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_rate_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.collection_rate_vespene', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spent_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.spent_minerals', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spent_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.spent_vespene', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='food_used', full_name='NydusNetwork.API.Protocol.ScoreDetails.food_used', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='killed_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.killed_minerals', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='killed_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.killed_vespene', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lost_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.lost_minerals', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lost_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.lost_vespene', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friendly_fire_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.friendly_fire_minerals', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friendly_fire_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.friendly_fire_vespene', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.used_minerals', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.used_vespene', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_used_minerals', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_used_minerals', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_used_vespene', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_used_vespene', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_damage_dealt', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_damage_dealt', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_damage_taken', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_damage_taken', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_healed', full_name='NydusNetwork.API.Protocol.ScoreDetails.total_healed', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=1823,
)

_SCORE.fields_by_name['score_type'].enum_type = _SCORE_SCORETYPE
_SCORE.fields_by_name['score_details'].message_type = _SCOREDETAILS
_SCORE_SCORETYPE.containing_type = _SCORE
_SCOREDETAILS.fields_by_name['food_used'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['killed_minerals'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['killed_vespene'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['lost_minerals'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['lost_vespene'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['friendly_fire_minerals'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['friendly_fire_vespene'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['used_minerals'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['used_vespene'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['total_used_minerals'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['total_used_vespene'].message_type = _CATEGORYSCOREDETAILS
_SCOREDETAILS.fields_by_name['total_damage_dealt'].message_type = _VITALSCOREDETAILS
_SCOREDETAILS.fields_by_name['total_damage_taken'].message_type = _VITALSCOREDETAILS
_SCOREDETAILS.fields_by_name['total_healed'].message_type = _VITALSCOREDETAILS
DESCRIPTOR.message_types_by_name['Score'] = _SCORE
DESCRIPTOR.message_types_by_name['CategoryScoreDetails'] = _CATEGORYSCOREDETAILS
DESCRIPTOR.message_types_by_name['VitalScoreDetails'] = _VITALSCOREDETAILS
DESCRIPTOR.message_types_by_name['ScoreDetails'] = _SCOREDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Score = _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), dict(
  DESCRIPTOR = _SCORE,
  __module__ = 'score_pb2'
  # @@protoc_insertion_point(class_scope:NydusNetwork.API.Protocol.Score)
  ))
_sym_db.RegisterMessage(Score)

CategoryScoreDetails = _reflection.GeneratedProtocolMessageType('CategoryScoreDetails', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORYSCOREDETAILS,
  __module__ = 'score_pb2'
  # @@protoc_insertion_point(class_scope:NydusNetwork.API.Protocol.CategoryScoreDetails)
  ))
_sym_db.RegisterMessage(CategoryScoreDetails)

VitalScoreDetails = _reflection.GeneratedProtocolMessageType('VitalScoreDetails', (_message.Message,), dict(
  DESCRIPTOR = _VITALSCOREDETAILS,
  __module__ = 'score_pb2'
  # @@protoc_insertion_point(class_scope:NydusNetwork.API.Protocol.VitalScoreDetails)
  ))
_sym_db.RegisterMessage(VitalScoreDetails)

ScoreDetails = _reflection.GeneratedProtocolMessageType('ScoreDetails', (_message.Message,), dict(
  DESCRIPTOR = _SCOREDETAILS,
  __module__ = 'score_pb2'
  # @@protoc_insertion_point(class_scope:NydusNetwork.API.Protocol.ScoreDetails)
  ))
_sym_db.RegisterMessage(ScoreDetails)


# @@protoc_insertion_point(module_scope)