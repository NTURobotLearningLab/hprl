
# _parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'C_LBRACE C_RBRACE DEF ELSE E_LBRACE E_RBRACE FRONT_IS_CLEAR IF IFELSE INT I_LBRACE I_RBRACE LEFT_IS_CLEAR MARKERS_PRESENT MOVE M_LBRACE M_RBRACE NOT NO_MARKERS_PRESENT PICK_MARKER PUT_MARKER REPEAT RIGHT_IS_CLEAR RUN R_LBRACE R_RBRACE TURN_LEFT TURN_RIGHT WHILE W_LBRACE W_RBRACEprog : DEF RUN M_LBRACE stmt M_RBRACEstmt : while\n                | repeat\n                | stmt_stmt\n                | action\n                | if\n                | ifelse\n        stmt_stmt : stmt stmt\n        if : IF C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE\n        ifelse : IFELSE C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE ELSE E_LBRACE stmt E_RBRACE\n        while : WHILE C_LBRACE cond C_RBRACE W_LBRACE stmt W_RBRACE\n        repeat : REPEAT cste R_LBRACE stmt R_RBRACE\n        cond : cond_without_not\n                | NOT C_LBRACE cond_without_not C_RBRACE\n        cond_without_not : FRONT_IS_CLEAR\n                | LEFT_IS_CLEAR\n                | RIGHT_IS_CLEAR\n                | MARKERS_PRESENT\n                | NO_MARKERS_PRESENT\n                action : MOVE\n                    | TURN_RIGHT\n                    | TURN_LEFT\n                    | PICK_MARKER\n                    | PUT_MARKER\n                    cste : INT\n        '
    
_lr_action_items = {'DEF':([0,],[2,]),'$end':([1,22,],[0,-1,]),'RUN':([2,],[3,]),'M_LBRACE':([3,],[4,]),'WHILE':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[12,12,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,12,12,12,12,-12,12,12,12,12,12,-11,-9,12,12,-10,]),'REPEAT':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[13,13,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,13,13,13,13,-12,13,13,13,13,13,-11,-9,13,13,-10,]),'MOVE':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[14,14,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,14,14,14,14,-12,14,14,14,14,14,-11,-9,14,14,-10,]),'TURN_RIGHT':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[15,15,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,15,15,15,15,-12,15,15,15,15,15,-11,-9,15,15,-10,]),'TURN_LEFT':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[16,16,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,16,16,16,16,-12,16,16,16,16,16,-11,-9,16,16,-10,]),'PICK_MARKER':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[17,17,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,17,17,17,17,-12,17,17,17,17,17,-11,-9,17,17,-10,]),'PUT_MARKER':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[18,18,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,18,18,18,18,-12,18,18,18,18,18,-11,-9,18,18,-10,]),'IF':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[19,19,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,19,19,19,19,-12,19,19,19,19,19,-11,-9,19,19,-10,]),'IFELSE':([4,5,6,7,8,9,10,11,14,15,16,17,18,21,36,41,44,46,47,48,49,51,52,53,54,57,58,59,],[20,20,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,20,20,20,20,-12,20,20,20,20,20,-11,-9,20,20,-10,]),'M_RBRACE':([5,6,7,8,9,10,11,14,15,16,17,18,21,46,53,54,59,],[22,-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-8,-12,-11,-9,-10,]),'R_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,21,41,46,53,54,59,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-8,46,-12,-11,-9,-10,]),'W_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,21,46,49,53,54,59,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-8,-12,53,-11,-9,-10,]),'I_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,21,46,51,52,53,54,59,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-8,-12,54,55,-11,-9,-10,]),'E_RBRACE':([6,7,8,9,10,11,14,15,16,17,18,21,46,53,54,58,59,],[-2,-3,-4,-5,-6,-7,-20,-21,-22,-23,-24,-8,-12,-11,-9,59,-10,]),'C_LBRACE':([12,19,20,30,],[23,26,27,40,]),'INT':([13,],[25,]),'NOT':([23,26,27,],[30,30,30,]),'FRONT_IS_CLEAR':([23,26,27,40,],[31,31,31,31,]),'LEFT_IS_CLEAR':([23,26,27,40,],[32,32,32,32,]),'RIGHT_IS_CLEAR':([23,26,27,40,],[33,33,33,33,]),'MARKERS_PRESENT':([23,26,27,40,],[34,34,34,34,]),'NO_MARKERS_PRESENT':([23,26,27,40,],[35,35,35,35,]),'R_LBRACE':([24,25,],[36,-25,]),'C_RBRACE':([28,29,31,32,33,34,35,37,38,45,50,],[39,-13,-15,-16,-17,-18,-19,42,43,50,-14,]),'W_LBRACE':([39,],[44,]),'I_LBRACE':([42,43,],[47,48,]),'ELSE':([55,],[56,]),'E_LBRACE':([56,],[57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'stmt':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[5,21,21,41,21,49,51,52,21,21,21,58,21,]),'while':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'repeat':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'stmt_stmt':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'action':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'if':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ifelse':([4,5,21,36,41,44,47,48,49,51,52,57,58,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'cste':([13,],[24,]),'cond':([23,26,27,],[28,37,38,]),'cond_without_not':([23,26,27,40,],[29,29,29,45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> DEF RUN M_LBRACE stmt M_RBRACE','prog',5,'p_prog','dsl_prob_option.py',78),
  ('stmt -> while','stmt',1,'p_stmt','dsl_prob_option.py',90),
  ('stmt -> repeat','stmt',1,'p_stmt','dsl_prob_option.py',91),
  ('stmt -> stmt_stmt','stmt',1,'p_stmt','dsl_prob_option.py',92),
  ('stmt -> action','stmt',1,'p_stmt','dsl_prob_option.py',93),
  ('stmt -> if','stmt',1,'p_stmt','dsl_prob_option.py',94),
  ('stmt -> ifelse','stmt',1,'p_stmt','dsl_prob_option.py',95),
  ('stmt_stmt -> stmt stmt','stmt_stmt',2,'p_stmt_stmt','dsl_prob_option.py',107),
  ('if -> IF C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE','if',7,'p_if','dsl_prob_option.py',120),
  ('ifelse -> IFELSE C_LBRACE cond C_RBRACE I_LBRACE stmt I_RBRACE ELSE E_LBRACE stmt E_RBRACE','ifelse',11,'p_ifelse','dsl_prob_option.py',135),
  ('while -> WHILE C_LBRACE cond C_RBRACE W_LBRACE stmt W_RBRACE','while',7,'p_while','dsl_prob_option.py',154),
  ('repeat -> REPEAT cste R_LBRACE stmt R_RBRACE','repeat',5,'p_repeat','dsl_prob_option.py',170),
  ('cond -> cond_without_not','cond',1,'p_cond','dsl_prob_option.py',184),
  ('cond -> NOT C_LBRACE cond_without_not C_RBRACE','cond',4,'p_cond','dsl_prob_option.py',185),
  ('cond_without_not -> FRONT_IS_CLEAR','cond_without_not',1,'p_cond_without_not','dsl_prob_option.py',203),
  ('cond_without_not -> LEFT_IS_CLEAR','cond_without_not',1,'p_cond_without_not','dsl_prob_option.py',204),
  ('cond_without_not -> RIGHT_IS_CLEAR','cond_without_not',1,'p_cond_without_not','dsl_prob_option.py',205),
  ('cond_without_not -> MARKERS_PRESENT','cond_without_not',1,'p_cond_without_not','dsl_prob_option.py',206),
  ('cond_without_not -> NO_MARKERS_PRESENT','cond_without_not',1,'p_cond_without_not','dsl_prob_option.py',207),
  ('action -> MOVE','action',1,'p_action','dsl_prob_option.py',218),
  ('action -> TURN_RIGHT','action',1,'p_action','dsl_prob_option.py',219),
  ('action -> TURN_LEFT','action',1,'p_action','dsl_prob_option.py',220),
  ('action -> PICK_MARKER','action',1,'p_action','dsl_prob_option.py',221),
  ('action -> PUT_MARKER','action',1,'p_action','dsl_prob_option.py',222),
  ('cste -> INT','cste',1,'p_cste','dsl_prob_option.py',230),
]
