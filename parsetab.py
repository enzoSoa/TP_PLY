
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocLESSTHANBIGGERTHANEQUALISEQUALNOTEQUALleftPLUSMINUSleftTIMESDIVIDEAND BIGGERTHAN DIVIDE EQUAL FALSE FOR IF ISEQUAL LBRACKET LESSTHAN LPAREN MINUS NAME NOTEQUAL NUMBER OR PLUS PRINT RBRACKET RPAREN SEMICOLON TIMES TRUE WHILEstart : blocbloc : statement SEMICOLON\n                | bloc statement SEMICOLONstatement : NAME LPAREN statement RPAREN LBRACKET bloc RBRACKET\n                | NAME LPAREN RPAREN LBRACKET bloc RBRACKETstatement : NAME LPAREN RPAREN statement : PRINT LPAREN expression RPARENstatement : IF LPAREN expression RPAREN LBRACKET bloc RBRACKETstatement : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LBRACKET bloc RBRACKETstatement : WHILE LPAREN expression RPAREN LBRACKET bloc RBRACKETstatement : NAME PLUS PLUS\n                | NAME MINUS MINUSexpression : NAMEexpression : expression AND expression\n                | expression OR expression\n                | expression LESSTHAN expression\n                | expression BIGGERTHAN expression\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression TIMES expression\n\t\t\t\t| expression DIVIDE expression\n\t\t\t\t| expression ISEQUAL expression\n\t\t\t\t| expression NOTEQUAL expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : TRUE\n                | FALSEstatement : NAME EQUAL expression'
    
_lr_action_items = {'NAME':([0,2,10,11,14,15,16,17,18,19,26,35,36,37,38,39,40,41,42,43,44,45,49,51,52,64,66,67,69,70,71,77,78,],[4,4,-2,4,24,24,24,4,24,-3,24,4,24,24,24,24,24,24,24,24,24,24,24,4,4,4,4,4,4,4,4,4,4,]),'PRINT':([0,2,10,11,17,19,35,51,52,64,66,67,69,70,71,77,78,],[5,5,-2,5,5,-3,5,5,5,5,5,5,5,5,5,5,5,]),'IF':([0,2,10,11,17,19,35,51,52,64,66,67,69,70,71,77,78,],[6,6,-2,6,6,-3,6,6,6,6,6,6,6,6,6,6,6,]),'FOR':([0,2,10,11,17,19,35,51,52,64,66,67,69,70,71,77,78,],[7,7,-2,7,7,-3,7,7,7,7,7,7,7,7,7,7,7,]),'WHILE':([0,2,10,11,17,19,35,51,52,64,66,67,69,70,71,77,78,],[8,8,-2,8,8,-3,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,2,10,19,],[0,-1,-2,-3,]),'SEMICOLON':([3,9,21,22,23,24,25,27,28,29,32,47,53,54,55,56,57,58,59,60,61,62,63,65,68,72,73,75,79,],[10,19,-6,-11,-12,-13,-28,-25,-26,-27,49,-7,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,70,-5,-4,-8,-10,-9,]),'LPAREN':([4,5,6,7,8,14,15,16,18,26,36,37,38,39,40,41,42,43,44,45,49,],[11,15,16,17,18,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'PLUS':([4,12,24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[12,22,-13,40,-25,-26,-27,40,40,40,40,40,40,40,40,-18,-19,-20,-21,40,40,-24,40,]),'MINUS':([4,13,24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[13,23,-13,41,-25,-26,-27,41,41,41,41,41,41,41,41,-18,-19,-20,-21,41,41,-24,41,]),'EQUAL':([4,],[14,]),'RBRACKET':([10,19,52,67,69,71,78,],[-2,-3,68,72,73,75,79,]),'RPAREN':([11,20,21,22,23,24,25,27,28,29,30,31,33,46,47,53,54,55,56,57,58,59,60,61,62,63,68,72,73,74,75,79,],[21,34,-6,-11,-12,-13,-28,-25,-26,-27,47,48,50,63,-7,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-5,-4,-8,76,-10,-9,]),'NUMBER':([14,15,16,18,26,36,37,38,39,40,41,42,43,44,45,49,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'TRUE':([14,15,16,18,26,36,37,38,39,40,41,42,43,44,45,49,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FALSE':([14,15,16,18,26,36,37,38,39,40,41,42,43,44,45,49,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'LBRACKET':([21,34,48,50,76,],[35,51,64,66,77,]),'AND':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,36,-25,-26,-27,36,36,36,36,-14,36,-16,-17,-18,-19,-20,-21,-22,-23,-24,36,]),'OR':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,37,-25,-26,-27,37,37,37,37,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,37,]),'LESSTHAN':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,38,-25,-26,-27,38,38,38,38,38,38,None,None,-18,-19,-20,-21,None,None,-24,38,]),'BIGGERTHAN':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,39,-25,-26,-27,39,39,39,39,39,39,None,None,-18,-19,-20,-21,None,None,-24,39,]),'TIMES':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,42,-25,-26,-27,42,42,42,42,42,42,42,42,42,42,-20,-21,42,42,-24,42,]),'DIVIDE':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,43,-25,-26,-27,43,43,43,43,43,43,43,43,43,43,-20,-21,43,43,-24,43,]),'ISEQUAL':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,44,-25,-26,-27,44,44,44,44,44,44,None,None,-18,-19,-20,-21,None,None,-24,44,]),'NOTEQUAL':([24,25,27,28,29,30,31,33,46,53,54,55,56,57,58,59,60,61,62,63,65,],[-13,45,-25,-26,-27,45,45,45,45,45,45,None,None,-18,-19,-20,-21,None,None,-24,45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'bloc':([0,35,51,64,66,77,],[2,52,67,69,71,78,]),'statement':([0,2,11,17,35,51,52,64,66,67,69,70,71,77,78,],[3,9,20,32,3,3,9,3,3,9,9,74,9,3,9,]),'expression':([14,15,16,18,26,36,37,38,39,40,41,42,43,44,45,49,],[25,30,31,33,46,53,54,55,56,57,58,59,60,61,62,65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> bloc','start',1,'p_start','calcBase.py',88),
  ('bloc -> statement SEMICOLON','bloc',2,'p_bloc','calcBase.py',95),
  ('bloc -> bloc statement SEMICOLON','bloc',3,'p_bloc','calcBase.py',96),
  ('statement -> NAME LPAREN statement RPAREN LBRACKET bloc RBRACKET','statement',7,'p_statement_function','calcBase.py',103),
  ('statement -> NAME LPAREN RPAREN LBRACKET bloc RBRACKET','statement',6,'p_statement_function','calcBase.py',104),
  ('statement -> NAME LPAREN RPAREN','statement',3,'p_statement_function_call','calcBase.py',111),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_expr','calcBase.py',115),
  ('statement -> IF LPAREN expression RPAREN LBRACKET bloc RBRACKET','statement',7,'p_statement_condition','calcBase.py',119),
  ('statement -> FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LBRACKET bloc RBRACKET','statement',11,'p_statement_for','calcBase.py',123),
  ('statement -> WHILE LPAREN expression RPAREN LBRACKET bloc RBRACKET','statement',7,'p_statement_while','calcBase.py',127),
  ('statement -> NAME PLUS PLUS','statement',3,'p_expression_incrementation','calcBase.py',131),
  ('statement -> NAME MINUS MINUS','statement',3,'p_expression_incrementation','calcBase.py',132),
  ('expression -> NAME','expression',1,'p_expression_var','calcBase.py',136),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','calcBase.py',140),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','calcBase.py',141),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_binop','calcBase.py',142),
  ('expression -> expression BIGGERTHAN expression','expression',3,'p_expression_binop','calcBase.py',143),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calcBase.py',144),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calcBase.py',145),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calcBase.py',146),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calcBase.py',147),
  ('expression -> expression ISEQUAL expression','expression',3,'p_expression_binop','calcBase.py',148),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_binop','calcBase.py',149),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calcBase.py',153),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcBase.py',157),
  ('expression -> TRUE','expression',1,'p_expression_bool','calcBase.py',161),
  ('expression -> FALSE','expression',1,'p_expression_bool','calcBase.py',162),
  ('statement -> NAME EQUAL expression','statement',3,'p_assignement','calcBase.py',166),
]
