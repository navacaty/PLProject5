
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '8BE3FF979E430D2CF67CF536293E0941'
    
_lr_action_items = {'STRING':([0,11,13,15,18,23,],[2,15,17,-10,21,-9,]),'-':([2,3,16,17,],[11,12,20,11,]),'HEADER1':([0,],[5,]),'DATE':([0,],[1,]),'INTEGER':([0,6,12,19,20,24,],[3,14,16,23,24,-8,]),':':([14,],[19,]),'$end':([0,1,2,4,5,6,7,8,9,10,15,21,22,24,],[-13,-5,-11,0,-1,-4,-6,-3,-7,-2,-10,-11,-12,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[4,]),'time':([6,],[13,]),'date':([0,],[6,]),'offense':([0,13,],[7,18,]),'data':([0,],[8,]),'day':([0,18,],[9,22,]),'empty':([0,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> HEADER1','start',1,'p_start','PlyMpstat.py',57),
  ('start -> empty','start',1,'p_start','PlyMpstat.py',58),
  ('start -> data','start',1,'p_start','PlyMpstat.py',59),
  ('start -> date','start',1,'p_start','PlyMpstat.py',60),
  ('start -> DATE','start',1,'p_start','PlyMpstat.py',61),
  ('start -> offense','start',1,'p_start','PlyMpstat.py',62),
  ('start -> day','start',1,'p_start','PlyMpstat.py',63),
  ('date -> INTEGER - INTEGER - INTEGER','date',5,'p_date','PlyMpstat.py',68),
  ('time -> INTEGER : INTEGER','time',3,'p_time','PlyMpstat.py',72),
  ('offense -> STRING - STRING','offense',3,'p_offense','PlyMpstat.py',77),
  ('day -> STRING','day',1,'p_day','PlyMpstat.py',81),
  ('data -> date time offense day','data',4,'p_data','PlyMpstat.py',86),
  ('empty -> <empty>','empty',0,'p_empty','PlyMpstat.py',91),
]
