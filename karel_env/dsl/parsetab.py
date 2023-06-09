
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'C_LBRACE C_RBRACE DEF ELSE E_LBRACE E_RBRACE FRONT_IS_CLEAR IF IFELSE INT I_LBRACE I_RBRACE LEFT_IS_CLEAR MARKERS_PRESENT MOVE M_LBRACE M_RBRACE NOT NO_MARKERS_PRESENT PICK_MARKER PUT_MARKER REPEAT RIGHT_IS_CLEAR RUN R_LBRACE R_RBRACE STAT TURN_LEFT TURN_RIGHT WHILE W_LBRACE W_RBRACEprog : DEF RUN M_LBRACE stmt M_RBRACEstmt : while\n                | repeat\n                | stmt_stmt\n                | action\n                | if\n                | ifelse\n        stmt_stmt : stmt stmt\n        if : IF C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE\n        ifelse : IFELSE C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE ELSE E_LBRACE stmt E_RBRACE\n        while : WHILE C_LBRACE cond C_RBRACE W_LBRACE stmt W_RBRACE\n        repeat : REPEAT cste R_LBRACE stmt R_RBRACE\n        cond : cond_without_not\n                | NOT C_LBRACE cond_without_not C_RBRACE\n        cond_without_not : FRONT_IS_CLEAR\n            | LEFT_IS_CLEAR\n            | RIGHT_IS_CLEAR\n            | MARKERS_PRESENT\n            | NO_MARKERS_PRESENT\n            action : MOVE\n                | TURN_RIGHT\n                | TURN_LEFT\n                | PICK_MARKER\n                | PUT_MARKER\n                | STAT\n                cste : INT\n        '
    
_lr_action_items = {'DEF':([0,],[2,]),'$end':([1,23,],[0,-1,]),'RUN':([2,],[3,]),'M_LBRACE':([3,],[4,]),'WHILE':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[12,12,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,12,12,12,12,-12,12,12,12,12,12,-11,-9,12,12,-10,]),'REPEAT':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[13,13,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,13,13,13,13,-12,13,13,13,13,13,-11,-9,13,13,-10,]),'MOVE':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[14,14,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,14,14,14,14,-12,14,14,14,14,14,-11,-9,14,14,-10,]),'TURN_RIGHT':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[15,15,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,15,15,15,15,-12,15,15,15,15,15,-11,-9,15,15,-10,]),'TURN_LEFT':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[16,16,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,16,16,16,16,-12,16,16,16,16,16,-11,-9,16,16,-10,]),'PICK_MARKER':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[17,17,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,17,17,17,17,-12,17,17,17,17,17,-11,-9,17,17,-10,]),'PUT_MARKER':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[18,18,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,18,18,18,18,-12,18,18,18,18,18,-11,-9,18,18,-10,]),'STAT':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[19,19,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,19,19,19,19,-12,19,19,19,19,19,-11,-9,19,19,-10,]),'IF':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[20,20,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,20,20,20,20,-12,20,20,20,20,20,-11,-9,20,20,-10,]),'IFELSE':([4,5,6,7,8,9,10,11,14,15,16,17,18,19,22,37,42,45,47,48,49,50,52,53,54,55,58,59,60,],[21,21,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,21,21,21,21,-12,21,21,21,21,21,-11,-9,21,21,-10,]),'M_RBRACE':([5,6,7,8,9,10,11,14,15,16,17,18,19,22,47,54,55,60,],[23,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,-8,-12,-11,-9,-10,]),'R_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,19,22,42,47,54,55,60,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,-8,47,-12,-11,-9,-10,]),'W_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,19,22,47,50,54,55,60,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,-8,-12,54,-11,-9,-10,]),'I_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,19,22,47,52,53,54,55,60,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,-8,-12,55,56,-11,-9,-10,]),'E_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,19,22,47,54,55,59,60,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-25,-8,-12,-11,-9,60,-10,]),'C_LBRACE':([12,20,21,31,],[24,27,28,41,]),'INT':([13,],[26,]),'NOT':([24,27,28,],[31,31,31,]),'FRONT_IS_CLEAR':([24,27,28,41,],[32,32,32,32,]),'LEFT_IS_CLEAR':([24,27,28,41,],[33,33,33,33,]),'RIGHT_IS_CLEAR':([24,27,28,41,],[34,34,34,34,]),'MARKERS_PRESENT':([24,27,28,41,],[35,35,35,35,]),'NO_MARKERS_PRESENT':([24,27,28,41,],[36,36,36,36,]),'R_LBRACE':([25,26,],[37,-26,]),'C_RBRACE':([29,30,32,33,34,35,36,38,39,46,51,],[40,-13,-15,-16,-17,-18,-19,43,44,51,-14,]),'W_LBRACE':([40,],[45,]),'I_LBRACE':([43,44,],[48,49,]),'ELSE':([56,],[57,]),'E_LBRACE':([57,],[58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'stmt':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[5,22,22,42,22,50,52,53,22,22,22,59,22,]),'while':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'repeat':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'stmt_stmt':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'action':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'if':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ifelse':([4,5,22,37,42,45,48,49,50,52,53,58,59,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'cste':([13,],[25,]),'cond':([24,27,28,],[29,38,39,]),'cond_without_not':([24,27,28,41,],[30,30,30,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> DEF RUN M_LBRACE stmt M_RBRACE','prog',5,'p_prog','dsl_prob_hprl.py',49),
  ('stmt -> while','stmt',1,'p_stmt','dsl_prob_hprl.py',61),
  ('stmt -> repeat','stmt',1,'p_stmt','dsl_prob_hprl.py',62),
  ('stmt -> stmt_stmt','stmt',1,'p_stmt','dsl_prob_hprl.py',63),
  ('stmt -> action','stmt',1,'p_stmt','dsl_prob_hprl.py',64),
  ('stmt -> if','stmt',1,'p_stmt','dsl_prob_hprl.py',65),
  ('stmt -> ifelse','stmt',1,'p_stmt','dsl_prob_hprl.py',66),
  ('stmt_stmt -> stmt stmt','stmt_stmt',2,'p_stmt_stmt','dsl_prob_hprl.py',78),
  ('if -> IF C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE','if',7,'p_if','dsl_prob_hprl.py',91),
  ('ifelse -> IFELSE C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE ELSE E_LBRACE stmt E_RBRACE','ifelse',11,'p_ifelse','dsl_prob_hprl.py',106),
  ('while -> WHILE C_LBRACE cond C_RBRACE W_LBRACE stmt W_RBRACE','while',7,'p_while','dsl_prob_hprl.py',125),
  ('repeat -> REPEAT cste R_LBRACE stmt R_RBRACE','repeat',5,'p_repeat','dsl_prob_hprl.py',141),
  ('cond -> cond_without_not','cond',1,'p_cond','dsl_prob_hprl.py',155),
  ('cond -> NOT C_LBRACE cond_without_not C_RBRACE','cond',4,'p_cond','dsl_prob_hprl.py',156),
  ('cond_without_not -> FRONT_IS_CLEAR','cond_without_not',1,'p_cond_without_not','dsl_prob_hprl.py',174),
  ('cond_without_not -> LEFT_IS_CLEAR','cond_without_not',1,'p_cond_without_not','dsl_prob_hprl.py',175),
  ('cond_without_not -> RIGHT_IS_CLEAR','cond_without_not',1,'p_cond_without_not','dsl_prob_hprl.py',176),
  ('cond_without_not -> MARKERS_PRESENT','cond_without_not',1,'p_cond_without_not','dsl_prob_hprl.py',177),
  ('cond_without_not -> NO_MARKERS_PRESENT','cond_without_not',1,'p_cond_without_not','dsl_prob_hprl.py',178),
  ('action -> MOVE','action',1,'p_action','dsl_prob_hprl.py',190),
  ('action -> TURN_RIGHT','action',1,'p_action','dsl_prob_hprl.py',191),
  ('action -> TURN_LEFT','action',1,'p_action','dsl_prob_hprl.py',192),
  ('action -> PICK_MARKER','action',1,'p_action','dsl_prob_hprl.py',193),
  ('action -> PUT_MARKER','action',1,'p_action','dsl_prob_hprl.py',194),
  ('action -> STAT','action',1,'p_action','dsl_prob_hprl.py',195),
  ('cste -> INT','cste',1,'p_cste','dsl_prob_hprl.py',202),
]
