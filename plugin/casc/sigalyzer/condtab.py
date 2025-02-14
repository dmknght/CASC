# condtab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'A2577335DA97121715C8FF4A002C1B8A'

_lr_action_items = {'AND': ([1, 2, 3, 4, 5, 6, 8, 10, 11, 14, 18, 19, 20, 21, 22, 23, 27, 28, 29, ],
                            [-2, -5, -10, 12, -4, -6, -1, -3, -7, 12, -12, 12, -11, -16, -18, -14, -17, -19, -15, ]),
                    'RPAREN': ([1, 2, 3, 5, 6, 8, 10, 11, 14, 18, 19, 20, 21, 22, 23, 27, 28, 29, ],
                               [-2, -5, -10, -4, -6, -1, -3, -7, 20, -12, -13, -11, -16, -18, -14, -17, -19, -15, ]),
                    'GREATER': ([3, 8, 9, 11, 20, ], [-10, -9, 15, -8, -11, ]),
                    'LESS': ([3, 8, 9, 11, 20, ], [-10, -9, 16, -8, -11, ]),
                    'NUMBER': ([0, 7, 12, 13, 15, 16, 17, 24, 25, 26, ], [3, 3, 3, 3, 21, 22, 23, 27, 28, 29, ]),
                    'EQUAL': ([3, 8, 9, 11, 20, ], [-10, -9, 17, -8, -11, ]), 'COMMA': ([21, 22, 23, ], [24, 25, 26, ]),
                    'LPAREN': ([0, 7, 12, 13, ], [7, 7, 7, 7, ]), 'OR': (
        [1, 2, 3, 4, 5, 6, 8, 10, 11, 14, 18, 19, 20, 21, 22, 23, 27, 28, 29, ],
        [-2, -5, -10, 13, -4, -6, -1, -3, -7, 13, -12, -13, -11, -16, -18, -14, -17, -19, -15, ]), '$end': (
        [1, 2, 3, 4, 5, 6, 8, 10, 11, 18, 19, 20, 21, 22, 23, 27, 28, 29, ],
        [-2, -5, -10, 0, -4, -6, -1, -3, -7, -12, -13, -11, -16, -18, -14, -17, -19, -15, ]), }

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:  _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'and': ([0, 7, 12, 13, ], [1, 1, 1, 1, ]), 'matchmore': ([0, 7, 12, 13, ], [2, 2, 2, 2, ]),
                  'expr': ([0, 7, 12, 13, ], [4, 14, 18, 19, ]), 'matchexact': ([0, 7, 12, 13, ], [5, 5, 5, 5, ]),
                  'matchless': ([0, 7, 12, 13, ], [6, 6, 6, 6, ]), 'paren': ([0, 7, 12, 13, ], [8, 8, 8, 8, ]),
                  'subgroup': ([0, 7, 12, 13, ], [9, 9, 9, 9, ]), 'or': ([0, 7, 12, 13, ], [10, 10, 10, 10, ]),
                  'subsig': ([0, 7, 12, 13, ], [11, 11, 11, 11, ]), }

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto: _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> expr", "S'", 1, None, None, None),
    ('expr -> paren', 'expr', 1, 'p_expr', 'cond_yacc.py', 18),
    ('expr -> and', 'expr', 1, 'p_expr', 'cond_yacc.py', 19),
    ('expr -> or', 'expr', 1, 'p_expr', 'cond_yacc.py', 20),
    ('expr -> matchexact', 'expr', 1, 'p_expr', 'cond_yacc.py', 21),
    ('expr -> matchmore', 'expr', 1, 'p_expr', 'cond_yacc.py', 22),
    ('expr -> matchless', 'expr', 1, 'p_expr', 'cond_yacc.py', 23),
    ('expr -> subsig', 'expr', 1, 'p_expr', 'cond_yacc.py', 24),
    ('subgroup -> subsig', 'subgroup', 1, 'p_subgroup', 'cond_yacc.py', 28),
    ('subgroup -> paren', 'subgroup', 1, 'p_subgroup', 'cond_yacc.py', 29),
    ('subsig -> NUMBER', 'subsig', 1, 'p_subsig', 'cond_yacc.py', 33),
    ('paren -> LPAREN expr RPAREN', 'paren', 3, 'p_paren', 'cond_yacc.py', 37),
    ('and -> expr AND expr', 'and', 3, 'p_and', 'cond_yacc.py', 41),
    ('or -> expr OR expr', 'or', 3, 'p_or', 'cond_yacc.py', 45),
    ('matchexact -> subgroup EQUAL NUMBER', 'matchexact', 3, 'p_matchextact', 'cond_yacc.py', 49),
    ('matchexact -> subgroup EQUAL NUMBER COMMA NUMBER', 'matchexact', 5, 'p_matchextact', 'cond_yacc.py', 50),
    ('matchmore -> subgroup GREATER NUMBER', 'matchmore', 3, 'p_matchmore', 'cond_yacc.py', 58),
    ('matchmore -> subgroup GREATER NUMBER COMMA NUMBER', 'matchmore', 5, 'p_matchmore', 'cond_yacc.py', 59),
    ('matchless -> subgroup LESS NUMBER', 'matchless', 3, 'p_matchless', 'cond_yacc.py', 67),
    ('matchless -> subgroup LESS NUMBER COMMA NUMBER', 'matchless', 5, 'p_matchless', 'cond_yacc.py', 68),
]
