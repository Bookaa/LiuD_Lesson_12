# auto generated

# LiuD syntax :

# option.prefix = PY
#     states.linecomments = '#'
#     basic.STR2 = '"""(?:.|\n)*?"""'
#     basic.STR3 = "''" + "'(?:.|\n)*?'" + "''"
#     basic.STR4 = 'r"""(?:.|\n)*?"""'
#     basic.STR5 = "r''" + "'(?:.|\n)*?'" + "''"
#     basic.STR6 = "r'[^'\\]*(?:\\.[^'\\]*)*'"
#     basic.STR7 = 'r"[^"\\]*(?:\\.[^"\\]*)*"'
# 
#     states.skip = crlf
#         dict = '{' dict_items? ','? '}'
#             dict_items = dict_item ^* ','
#     states.skip = no
#     stmts = (IDENT stmt)*
#     deepstmts = IDENTIN stmts IDENTOUT
# 
#     states.skip = space
# 
#     main = stmts
# 
#     stmt_1line := oneword_stmt | assert_stmt | assign | augassign | value
#     stmt_multi = stmt_1line ^+ ';'
#     stmt := if_stmt | while_stmt | for_stmt | return_stmt | print_stmt | funcdef | import | classdef
#         | stmt_multi | stmt_1line
# 
# 
#         if_stmt = 'if' value ':' deepstmts elif_part* else_part?
#             elif_part = IDENT 'elif' value ':' deepstmts
#             else_part = IDENT 'else' ':' deepstmts
#         while_stmt = 'while' value ':' deepstmts else_part?
#         for_stmt = 'for' commas 'in' value ':' deepstmts else_part?
#         return_stmt = 'return' valuecomma?
#             valuecomma = value ^* ','
#         funcdef = 'def' NAME '(' params? ')' ':' deepstmts
#             params = param ^* ','
#             param = NAME ('=' value)?
#         augassign = dest ('+=' | '-=' | '/=' | '*=') value
#         assign = dest '=' (valuecommap | value)
#             valuecommap = value ^+ ','
#         dest1 = litname (, ext_array_index ext_call ext_dot)
#         dest := dotscommap | dest_tuple | dest1
#             dest_tuple = '(' commas ','? ')'
#         print_stmt = 'print' args? ','?
#             args = value ^* ','
#         import := import1 | import2
#         import1 = 'from' dots 'import' (star | importcommas)
#             star = '*'
#         import2 = 'import' importcommas
#         importcommas = importitem ^* ','
#         importitem = dots ('as' NAME)?
# 
#         classdef = 'class' NAME ('(' dotscomma ')')? ':' deepstmts
#         assert_stmt = 'assert' value
#         oneword_stmt = 'pass' | 'break' | 'continue'
# 
#     dots = NAME ^* '.'
#     commas = NAME ^* ','
#     commap = NAME ^+ ','
#     dotscomma = dots ^* ','
#     dotscommap = dots ^+ ','
# 
#     value_bool = 'True' | 'False'
#     value_str = STR2 | STR3 | STR4 | STR5 | STR6 | STR7 | STRING
#     value_n = NUMBER | NAME
#     value0 := value_str | value_n
#     value1 := list | list_comprehen | dict | tuple | enclosed | funccall | value_bool | value0
#         list = '[' args? ','? ']'
#                 dict_item = value ':' value
#         list_comprehen = '[' value 'for' commas 'in' value ']'
#         tuple := tuple1 | tuple2
#         tuple1 = '(' value ',' ')'
#         tuple2 = '(' tupleitem ','? ')'
#             tupleitem = value ^+ ','
#         enclosed = '(' value ')'
#         funccall = NAME '(' funcargs? ')'
#             funcargs = funcarg ^* ','
#             funcarg = (NAME '=')? value
# 
#     value3 = value1 (, ext_array_index ext_call ext_dot)
#         ext_array_index -> '[' idx ']'
#         ext_call -> '(' funcargs? ')'
#         ext_dot -> '.' NAME
# 
#     idx := idx1 | idx2 | value
#     idx1 = value? ':' value? ':' value?
#     idx2 = value? ':' value?
# 
#     value2 := signed | value3
#         signed = ('-' | '+' | 'not') value3
#     value_7 = value2 (, ('*' '/') ('+' '-')) value3
#     binvalue = value_7 (, '%' ('>=' '>' '<=' '<' '==' '!=') ('in' 'is') ) value_7
#     value5 = binvalue, 'if' binvalue 'else' binvalue
#     value6 = value5 (, ('and' 'or')) value5
#     value := value6
# 
# 
#     litname = NAME
#     

from GDL_common import *

class PY_dict:
    def __init__(self, vq, nq):
        self.vq = vq
        self.nq = nq
    def walkabout(self, visitor):
        return visitor.visit_dict(self)

class PY_dict_items:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_dict_items(self)

class PY_stmts:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_stmts(self)

class PY_deepstmts:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_deepstmts(self)

class PY_main:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_main(self)

class PY_stmt_multi:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_stmt_multi(self)

class PY_if_stmt:
    def __init__(self, v1, v2, vlst, vq):
        self.v1 = v1
        self.v2 = v2
        self.vlst = vlst
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_if_stmt(self)

class PY_elif_part:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_elif_part(self)

class PY_else_part:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_else_part(self)

class PY_while_stmt:
    def __init__(self, v1, v2, vq):
        self.v1 = v1
        self.v2 = v2
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_while_stmt(self)

class PY_for_stmt:
    def __init__(self, v1, v2, v3, vq):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_for_stmt(self)

class PY_return_stmt:
    def __init__(self, vq):
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_return_stmt(self)

class PY_valuecomma:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_valuecomma(self)

class PY_funcdef:
    def __init__(self, n, vq, v):
        self.n = n
        self.vq = vq
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_funcdef(self)

class PY_params:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_params(self)

class PY_param:
    def __init__(self, n, vq):
        self.n = n
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_param(self)

class PY_augassign:
    def __init__(self, v1, n, v2):
        self.v1 = v1
        self.n = n
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_augassign(self)

class PY_assign:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_assign(self)

class PY_valuecommap:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_valuecommap(self)

class PY_dest1:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_dest1(self)

class PY_dest_tuple:
    def __init__(self, v, nq):
        self.v = v
        self.nq = nq
    def walkabout(self, visitor):
        return visitor.visit_dest_tuple(self)

class PY_print_stmt:
    def __init__(self, vq, nq):
        self.vq = vq
        self.nq = nq
    def walkabout(self, visitor):
        return visitor.visit_print_stmt(self)

class PY_args:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_args(self)

class PY_import1:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_import1(self)

class PY_star:
    def walkabout(self, visitor):
        return visitor.visit_star(self)

class PY_import2:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_import2(self)

class PY_importcommas:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_importcommas(self)

class PY_importitem:
    def __init__(self, v, nq):
        self.v = v
        self.nq = nq
    def walkabout(self, visitor):
        return visitor.visit_importitem(self)

class PY_classdef:
    def __init__(self, n, vq, v):
        self.n = n
        self.vq = vq
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_classdef(self)

class PY_assert_stmt:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_assert_stmt(self)

class PY_oneword_stmt:
    def __init__(self, n):
        self.n = n
    def walkabout(self, visitor):
        return visitor.visit_oneword_stmt(self)

class PY_dots:
    def __init__(self, nlst):
        self.nlst = nlst
    def walkabout(self, visitor):
        return visitor.visit_dots(self)

class PY_commas:
    def __init__(self, nlst):
        self.nlst = nlst
    def walkabout(self, visitor):
        return visitor.visit_commas(self)

class PY_commap:
    def __init__(self, nlst):
        self.nlst = nlst
    def walkabout(self, visitor):
        return visitor.visit_commap(self)

class PY_dotscomma:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_dotscomma(self)

class PY_dotscommap:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_dotscommap(self)

class PY_value_bool:
    def __init__(self, n):
        self.n = n
    def walkabout(self, visitor):
        return visitor.visit_value_bool(self)

class PY_value_str:
    def __init__(self, s):
        self.s = s[1]; self.s_raw = s[0]
    def walkabout(self, visitor):
        return visitor.visit_value_str(self)

class PY_value_n:
    def __init__(self, n):
        self.n = n
    def walkabout(self, visitor):
        return visitor.visit_value_n(self)

class PY_list:
    def __init__(self, vq, nq):
        self.vq = vq
        self.nq = nq
    def walkabout(self, visitor):
        return visitor.visit_list(self)

class PY_dict_item:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_dict_item(self)

class PY_list_comprehen:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def walkabout(self, visitor):
        return visitor.visit_list_comprehen(self)

class PY_tuple1:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_tuple1(self)

class PY_tuple2:
    def __init__(self, v, nq):
        self.v = v
        self.nq = nq
    def walkabout(self, visitor):
        return visitor.visit_tuple2(self)

class PY_tupleitem:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_tupleitem(self)

class PY_enclosed:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_enclosed(self)

class PY_funccall:
    def __init__(self, n, vq):
        self.n = n
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_funccall(self)

class PY_funcargs:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_funcargs(self)

class PY_funcarg:
    def __init__(self, nq, v):
        self.nq = nq
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_funcarg(self)

class PY_value3:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_value3(self)

class PY_ext_array_index:
    def __init__(self, v0, v):
        self.v0 = v0
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_ext_array_index(self)

class PY_ext_call:
    def __init__(self, v0, vq):
        self.v0 = v0
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_ext_call(self)

class PY_ext_dot:
    def __init__(self, v0, n):
        self.v0 = v0
        self.n = n
    def walkabout(self, visitor):
        return visitor.visit_ext_dot(self)

class PY_idx1:
    def __init__(self, vq1, vq2, vq3):
        self.vq1 = vq1
        self.vq2 = vq2
        self.vq3 = vq3
    def walkabout(self, visitor):
        return visitor.visit_idx1(self)

class PY_idx2:
    def __init__(self, vq1, vq2):
        self.vq1 = vq1
        self.vq2 = vq2
    def walkabout(self, visitor):
        return visitor.visit_idx2(self)

class PY_signed:
    def __init__(self, n, v):
        self.n = n
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_signed(self)

class PY_value_7:
    def __init__(self, v1, n, v2):
        self.v1 = v1
        self.n = n
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_value_7(self)

class PY_binvalue:
    def __init__(self, v1, n, v2):
        self.v1 = v1
        self.n = n
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_binvalue(self)

class PY_value5:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def walkabout(self, visitor):
        return visitor.visit_value5(self)

class PY_value6:
    def __init__(self, v1, n, v2):
        self.v1 = v1
        self.n = n
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_value6(self)

class PY_litname:
    def __init__(self, n):
        self.n = n
    def walkabout(self, visitor):
        return visitor.visit_litname(self)

class PY_Parser(Parser00, Serial00):
    def __init__(self, txt):
        Parser00.__init__(self, txt)
        Serial00.__init__(self)
    def handle_NUMBER(self):
        s = Parser00.handle_NUMBER(self)
        if s:
            self.last.append(s)
        return s
    def handle_FLOAT(self):
        s = Parser00.handle_FLOAT(self)
        if s:
            self.last.append(s)
        return s
    def handle_NAME(self):
        s = Parser00.handle_NAME(self)
        if s:
            self.last.append(s)
        return s
    def handle_STRING(self):
        s = Parser00.handle_STRING(self)
        if s:
            self.last.append(s[0])
        return s
    def get_linecomments(self):
            return '#'
    def handle_STR2(self):
        pattn = r'"""(?:.|\n)*?"""'
        s = self.handle_basic(pattn)
        if s:
            self.last.append(s[0])
        return s
    def handle_STR3(self):
        pattn = r"''" + r"'(?:.|\n)*?'" + r"''"
        s = self.handle_basic(pattn)
        if s:
            self.last.append(s[0])
        return s
    def handle_STR4(self):
        pattn = r'r"""(?:.|\n)*?"""'
        s = self.handle_basic(pattn)
        if s:
            self.last.append(s[0])
        return s
    def handle_STR5(self):
        pattn = r"r''" + r"'(?:.|\n)*?'" + r"''"
        s = self.handle_basic(pattn)
        if s:
            self.last.append(s[0])
        return s
    def handle_STR6(self):
        pattn = r"r'[^'\\]*(?:\\.[^'\\]*)*'"
        s = self.handle_basic(pattn)
        if s:
            self.last.append(s[0])
        return s
    def handle_STR7(self):
        pattn = r'r"[^"\\]*(?:\\.[^"\\]*)*"'
        s = self.handle_basic(pattn)
        if s:
            self.last.append(s[0])
        return s
        
    def handle_dict(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('{'):
            self.upfail()
            return None
        self.skipspacecrlf()
        vq = self.handle_dict_items()
        if not vq:
            self.last.append([])
        self.skipspacecrlf()
        nq = self.handle_str(',')
        self.last.append(1 if nq else 0)
        self.skipspacecrlf()
        if not self.handle_str('}'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_dict(vq, nq)
        
    def handle_dict_items(self):
        self.deep()
        self.deep()
        s = self.handle_dict_item()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspacecrlf()
            if not self.handle_str(','):
                break
            self.skipspacecrlf()
            s = self.handle_dict_item()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_dict_items(vlst)
        
    def handle_stmts(self):
        self.deep()
        vlst = []
        savpos = self.pos
        self.deep()
        while True:
            if not self.handle_IDENT():
                break
            v = self.hdl_stmt()
            if not v:
                break
            vlst.append(v)
            savpos = self.pos
        self.restorepos(savpos)
        if not vlst:
            self.upfail()
            self.upfail()
            return None
        self.up()
        self.upone()
        return PY_stmts(vlst)
        
    def handle_deepstmts(self):
        self.deep()
        savpos = self.pos
        if not self.handle_IDENTIN():
            self.upfail()
            return None
        v = self.handle_stmts()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        if not self.handle_IDENTOUT():
            self.upfail()
            return self.restorepos(savpos)
        self.upone()
        return PY_deepstmts(v)
        
    def handle_main(self):
        self.deep()
        v = self.handle_stmts()
        if not v:
            self.upfail()
            return None
        self.upone()
        return PY_main(v)
        
    def hdl_stmt_1line(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_oneword_stmt()
        if not v:
            no_ += 1
            v = self.handle_assert_stmt()
        if not v:
            no_ += 1
            v = self.handle_assign()
        if not v:
            no_ += 1
            v = self.handle_augassign()
        if not v:
            no_ += 1
            v = self.hdl_value()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_stmt_multi(self):
        self.deep()
        self.deep()
        savpos = self.pos
        s = self.hdl_stmt_1line()
        if not s:
            self.upfail()
            self.upfail()
            return None
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(';'):
                break
            self.skipspace()
            s = self.hdl_stmt_1line()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(vlst) < 2:
            self.upfail()
            self.upfail()
            return None
        self.up()
        self.upone()
        return PY_stmt_multi(vlst)
        
    def hdl_stmt(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_if_stmt()
        if not v:
            no_ += 1
            v = self.handle_while_stmt()
        if not v:
            no_ += 1
            v = self.handle_for_stmt()
        if not v:
            no_ += 1
            v = self.handle_return_stmt()
        if not v:
            no_ += 1
            v = self.handle_print_stmt()
        if not v:
            no_ += 1
            v = self.handle_funcdef()
        if not v:
            no_ += 1
            v = self.hdl_import()
        if not v:
            no_ += 1
            v = self.handle_classdef()
        if not v:
            no_ += 1
            v = self.handle_stmt_multi()
        if not v:
            no_ += 1
            v = self.hdl_stmt_1line()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_if_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('if'):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vlst = []
        savpos2 = self.pos
        self.deep()
        while True:
            v_ = self.handle_elif_part()
            if not v_:
                break
            vlst.append(v_)
            savpos2 = self.pos
            self.skipspace()
        self.up()
        self.restorepos(savpos2)
        self.skipspace()
        vq = self.handle_else_part()
        if not vq:
            self.last.append([])
        self.upn(4)
        return PY_if_stmt(v1, v2, vlst, vq)
        
    def handle_elif_part(self):
        self.deep()
        savpos = self.pos
        if not self.handle_IDENT():
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('elif'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_elif_part(v1, v2)
        
    def handle_else_part(self):
        self.deep()
        savpos = self.pos
        if not self.handle_IDENT():
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('else'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upone()
        return PY_else_part(v)
        
    def handle_while_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('while'):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_else_part()
        if not vq:
            self.last.append([])
        self.upn(3)
        return PY_while_stmt(v1, v2, vq)
        
    def handle_for_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('for'):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.handle_commas()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('in'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v3 = self.handle_deepstmts()
        if not v3:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_else_part()
        if not vq:
            self.last.append([])
        self.upn(4)
        return PY_for_stmt(v1, v2, v3, vq)
        
    def handle_return_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('return'):
            self.upfail()
            return None
        self.skipspace()
        vq = self.handle_valuecomma()
        if not vq:
            self.last.append([])
        self.upone()
        return PY_return_stmt(vq)
        
    def handle_valuecomma(self):
        self.deep()
        self.deep()
        s = self.hdl_value()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_valuecomma(vlst)
        
    def handle_funcdef(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('def'):
            self.upfail()
            return None
        self.skipspace()
        n = self.handle_NAME()
        if not n:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('('):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_params()
        if not vq:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(3)
        return PY_funcdef(n, vq, v)
        
    def handle_params(self):
        self.deep()
        self.deep()
        s = self.handle_param()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_param()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_params(vlst)
        
    def handle_param(self):
        self.deep()
        savpos = self.pos
        n = self.handle_NAME()
        if not n:
            self.upfail()
            return None
        self.skipspace()
        def enclosed():
            self.deep()
            savpos = self.pos
            if not self.handle_str('='):
                self.upfail()
                return None
            self.skipspace()
            vq = self.hdl_value()
            if not vq:
                self.upfail()
                return self.restorepos(savpos)
            self.upn(1)
            return vq
        vq = enclosed()
        if not vq:
            self.last.append([])
        self.upn(2)
        return PY_param(n, vq)
        
    def handle_augassign(self):
        self.deep()
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            self.upfail()
            return None
        self.skipspace()
        no_ = 0
        n = self.handle_str('+=')
        if not n:
            no_ += 1
            n = self.handle_str('-=')
        if not n:
            no_ += 1
            n = self.handle_str('/=')
        if not n:
            no_ += 1
            n = self.handle_str('*=')
        if not n:
            self.upfail()
            return self.restorepos(savpos)
        self.last.append(no_)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(3)
        return PY_augassign(v1, n, v2)
        
    def handle_assign(self):
        self.deep()
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('='):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        self.deep()
        no_ = 0
        v2 = self.handle_valuecommap()
        if not v2:
            no_ += 1
            v2 = self.hdl_value()
        if not v2:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upn(2)
        return PY_assign(v1, v2)
        
    def handle_valuecommap(self):
        self.deep()
        self.deep()
        savpos = self.pos
        s = self.hdl_value()
        if not s:
            self.upfail()
            self.upfail()
            return None
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(vlst) < 2:
            self.upfail()
            self.upfail()
            return None
        self.up()
        self.upone()
        return PY_valuecommap(vlst)
        
    def handle_dest1(self):
        self.deep()
        v0 = self.handle_litname()
        if not v0:
            self.upfail()
            return None
        self.last.append(0)
        self.upn(2)
        savpos = self.pos
        while True:
            self.skipspace()
            self.deep1()
            v1 = self.hdlext_ext_array_index(v0)
            if v1:
                v0 = v1
                savpos = self.pos
                self.last.append(1)
                self.upn(2)
                continue
            v1 = self.hdlext_ext_call(v0)
            if v1:
                v0 = v1
                savpos = self.pos
                self.last.append(2)
                self.upn(2)
                continue
            v1 = self.hdlext_ext_dot(v0)
            if v1:
                v0 = v1
                savpos = self.pos
                self.last.append(3)
                self.upn(2)
                continue
            self.upfail()
            break
        self.restorepos(savpos)
        return v0
        
    def hdl_dest(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_dotscommap()
        if not v:
            no_ += 1
            v = self.handle_dest_tuple()
        if not v:
            no_ += 1
            v = self.handle_dest1()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_dest_tuple(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('('):
            self.upfail()
            return None
        self.skipspace()
        v = self.handle_commas()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        nq = self.handle_str(',')
        self.last.append(1 if nq else 0)
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_dest_tuple(v, nq)
        
    def handle_print_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('print'):
            self.upfail()
            return None
        self.skipspace()
        vq = self.handle_args()
        if not vq:
            self.last.append([])
        self.skipspace()
        nq = self.handle_str(',')
        self.last.append(1 if nq else 0)
        self.upn(2)
        return PY_print_stmt(vq, nq)
        
    def handle_args(self):
        self.deep()
        self.deep()
        s = self.hdl_value()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_args(vlst)
        
    def hdl_import(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_import1()
        if not v:
            no_ += 1
            v = self.handle_import2()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_import1(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('from'):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.handle_dots()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('import'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        self.deep()
        no_ = 0
        v2 = self.handle_star()
        if not v2:
            no_ += 1
            v2 = self.handle_importcommas()
        if not v2:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upn(2)
        return PY_import1(v1, v2)
        
    def handle_star(self):
        if not self.handle_str('*'):
            return None
        self.last.append([])
        return PY_star()
        
    def handle_import2(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('import'):
            self.upfail()
            return None
        self.skipspace()
        v = self.handle_importcommas()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upone()
        return PY_import2(v)
        
    def handle_importcommas(self):
        self.deep()
        self.deep()
        s = self.handle_importitem()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_importitem()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_importcommas(vlst)
        
    def handle_importitem(self):
        self.deep()
        savpos = self.pos
        v = self.handle_dots()
        if not v:
            self.upfail()
            return None
        self.skipspace()
        def enclosed():
            self.deep()
            savpos = self.pos
            if not self.handle_str('as'):
                self.upfail()
                return None
            self.skipspace()
            nq = self.handle_NAME()
            if not nq:
                self.upfail()
                return self.restorepos(savpos)
            self.upn(1)
            return nq
        nq = enclosed()
        if not nq:
            self.last.append([])
        self.upn(2)
        return PY_importitem(v, nq)
        
    def handle_classdef(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('class'):
            self.upfail()
            return None
        self.skipspace()
        n = self.handle_NAME()
        if not n:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        def enclosed():
            self.deep()
            savpos = self.pos
            if not self.handle_str('('):
                self.upfail()
                return None
            self.skipspace()
            vq = self.handle_dotscomma()
            if not vq:
                self.upfail()
                return self.restorepos(savpos)
            self.skipspace()
            if not self.handle_str(')'):
                self.upfail()
                return self.restorepos(savpos)
            self.upn(1)
            return vq
        vq = enclosed()
        if not vq:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(3)
        return PY_classdef(n, vq, v)
        
    def handle_assert_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('assert'):
            self.upfail()
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upone()
        return PY_assert_stmt(v)
        
    def handle_oneword_stmt(self):
        self.deep()
        no_ = 0
        n = self.handle_str('pass')
        if not n:
            no_ += 1
            n = self.handle_str('break')
        if not n:
            no_ += 1
            n = self.handle_str('continue')
        if not n:
            self.upfail()
            return None
        self.last.append(no_)
        self.upone()
        return PY_oneword_stmt(n)
        
    def handle_dots(self):
        self.deep()
        self.deep()
        s = self.handle_NAME()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        nlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str('.'):
                break
            self.skipspace()
            s = self.handle_NAME()
            if not s:
                break
            nlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_dots(nlst)
        
    def handle_commas(self):
        self.deep()
        self.deep()
        s = self.handle_NAME()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        nlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_NAME()
            if not s:
                break
            nlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_commas(nlst)
        
    def handle_commap(self):
        self.deep()
        self.deep()
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            self.upfail()
            self.upfail()
            return None
        nlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_NAME()
            if not s:
                break
            nlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(nlst) < 2:
            self.upfail()
            self.upfail()
            return None
        self.up()
        self.upone()
        return PY_commap(nlst)
        
    def handle_dotscomma(self):
        self.deep()
        self.deep()
        s = self.handle_dots()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_dots()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_dotscomma(vlst)
        
    def handle_dotscommap(self):
        self.deep()
        self.deep()
        savpos = self.pos
        s = self.handle_dots()
        if not s:
            self.upfail()
            self.upfail()
            return None
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_dots()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(vlst) < 2:
            self.upfail()
            self.upfail()
            return None
        self.up()
        self.upone()
        return PY_dotscommap(vlst)
        
    def handle_value_bool(self):
        self.deep()
        no_ = 0
        n = self.handle_str('True')
        if not n:
            no_ += 1
            n = self.handle_str('False')
        if not n:
            self.upfail()
            return None
        self.last.append(no_)
        self.upone()
        return PY_value_bool(n)
        
    def handle_value_str(self):
        self.deep()
        self.deep()
        no_ = 0
        s = self.handle_STR2()
        if not s:
            no_ += 1
            s = self.handle_STR3()
        if not s:
            no_ += 1
            s = self.handle_STR4()
        if not s:
            no_ += 1
            s = self.handle_STR5()
        if not s:
            no_ += 1
            s = self.handle_STR6()
        if not s:
            no_ += 1
            s = self.handle_STR7()
        if not s:
            no_ += 1
            s = self.handle_STRING()
        if not s:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return PY_value_str(s)
        
    def handle_value_n(self):
        self.deep()
        self.deep()
        no_ = 0
        n = self.handle_NUMBER()
        if not n:
            no_ += 1
            n = self.handle_NAME()
        if not n:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return PY_value_n(n)
        
    def hdl_value0(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_value_str()
        if not v:
            no_ += 1
            v = self.handle_value_n()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def hdl_value1(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_list()
        if not v:
            no_ += 1
            v = self.handle_list_comprehen()
        if not v:
            no_ += 1
            v = self.handle_dict()
        if not v:
            no_ += 1
            v = self.hdl_tuple()
        if not v:
            no_ += 1
            v = self.handle_enclosed()
        if not v:
            no_ += 1
            v = self.handle_funccall()
        if not v:
            no_ += 1
            v = self.handle_value_bool()
        if not v:
            no_ += 1
            v = self.hdl_value0()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_list(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('['):
            self.upfail()
            return None
        self.skipspace()
        vq = self.handle_args()
        if not vq:
            self.last.append([])
        self.skipspace()
        nq = self.handle_str(',')
        self.last.append(1 if nq else 0)
        self.skipspace()
        if not self.handle_str(']'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_list(vq, nq)
        
    def handle_dict_item(self):
        self.deep()
        savpos = self.pos
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_dict_item(v1, v2)
        
    def handle_list_comprehen(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('['):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('for'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_commas()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('in'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v3 = self.hdl_value()
        if not v3:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(']'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(3)
        return PY_list_comprehen(v1, v2, v3)
        
    def hdl_tuple(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_tuple1()
        if not v:
            no_ += 1
            v = self.handle_tuple2()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_tuple1(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('('):
            self.upfail()
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(','):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upone()
        return PY_tuple1(v)
        
    def handle_tuple2(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('('):
            self.upfail()
            return None
        self.skipspace()
        v = self.handle_tupleitem()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        nq = self.handle_str(',')
        self.last.append(1 if nq else 0)
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_tuple2(v, nq)
        
    def handle_tupleitem(self):
        self.deep()
        self.deep()
        savpos = self.pos
        s = self.hdl_value()
        if not s:
            self.upfail()
            self.upfail()
            return None
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(vlst) < 2:
            self.upfail()
            self.upfail()
            return None
        self.up()
        self.upone()
        return PY_tupleitem(vlst)
        
    def handle_enclosed(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('('):
            self.upfail()
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upone()
        return PY_enclosed(v)
        
    def handle_funccall(self):
        self.deep()
        savpos = self.pos
        n = self.handle_NAME()
        if not n:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('('):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_funcargs()
        if not vq:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_funccall(n, vq)
        
    def handle_funcargs(self):
        self.deep()
        self.deep()
        s = self.handle_funcarg()
        if not s:
            self.upfail()
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_funcarg()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        self.upone()
        return PY_funcargs(vlst)
        
    def handle_funcarg(self):
        self.deep()
        savpos = self.pos
        def enclosed():
            self.deep()
            savpos = self.pos
            nq = self.handle_NAME()
            if not nq:
                self.upfail()
                return None
            self.skipspace()
            if not self.handle_str('='):
                self.upfail()
                return self.restorepos(savpos)
            self.upn(1)
            return nq
        nq = enclosed()
        if not nq:
            self.last.append([])
        self.skipspace()
        v = self.hdl_value()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_funcarg(nq, v)
        
    def handle_value3(self):
        self.deep()
        v0 = self.hdl_value1()
        if not v0:
            self.upfail()
            return None
        self.last.append(0)
        self.upn(2)
        savpos = self.pos
        while True:
            self.skipspace()
            self.deep1()
            v1 = self.hdlext_ext_array_index(v0)
            if v1:
                v0 = v1
                savpos = self.pos
                self.last.append(1)
                self.upn(2)
                continue
            v1 = self.hdlext_ext_call(v0)
            if v1:
                v0 = v1
                savpos = self.pos
                self.last.append(2)
                self.upn(2)
                continue
            v1 = self.hdlext_ext_dot(v0)
            if v1:
                v0 = v1
                savpos = self.pos
                self.last.append(3)
                self.upn(2)
                continue
            self.upfail()
            break
        self.restorepos(savpos)
        return v0
        
    def hdlext_ext_array_index(self, v0):
        self.deep1()
        savpos = self.pos
        if not self.handle_str('['):
            self.upfail()
            return None
        self.skipspace()
        v = self.hdl_idx()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(']'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_ext_array_index(v0, v)
        
    def hdlext_ext_call(self, v0):
        self.deep1()
        savpos = self.pos
        if not self.handle_str('('):
            self.upfail()
            return None
        self.skipspace()
        vq = self.handle_funcargs()
        if not vq:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_ext_call(v0, vq)
        
    def hdlext_ext_dot(self, v0):
        self.deep1()
        savpos = self.pos
        if not self.handle_str('.'):
            self.upfail()
            return None
        self.skipspace()
        n = self.handle_NAME()
        if not n:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_ext_dot(v0, n)
        
    def hdl_idx(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_idx1()
        if not v:
            no_ += 1
            v = self.handle_idx2()
        if not v:
            no_ += 1
            v = self.hdl_value()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_idx1(self):
        self.deep()
        savpos = self.pos
        vq1 = self.hdl_value()
        if not vq1:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq2 = self.hdl_value()
        if not vq2:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq3 = self.hdl_value()
        if not vq3:
            self.last.append([])
        self.upn(3)
        return PY_idx1(vq1, vq2, vq3)
        
    def handle_idx2(self):
        self.deep()
        savpos = self.pos
        vq1 = self.hdl_value()
        if not vq1:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq2 = self.hdl_value()
        if not vq2:
            self.last.append([])
        self.upn(2)
        return PY_idx2(vq1, vq2)
        
    def hdl_value2(self):
        self.deep()
        self.deep()
        no_ = 0
        v = self.handle_signed()
        if not v:
            no_ += 1
            v = self.handle_value3()
        if not v:
            self.upfail()
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        self.upone()
        return v
        
    def handle_signed(self):
        self.deep()
        savpos = self.pos
        no_ = 0
        n = self.handle_str('-')
        if not n:
            no_ += 1
            n = self.handle_str('+')
        if not n:
            no_ += 1
            n = self.handle_str('not')
        if not n:
            self.upfail()
            return None
        self.last.append(no_)
        self.skipspace()
        v = self.handle_value3()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_signed(n, v)
        
    def handle_value_7(self):
        self.deep()
        v1 = self.hdl_value2()
        if not v1:
            self.upfail()
            return None
        self.upn(1)
        def multiop1(v1):
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for n in ['*', '/']:
                    if self.handle_str(n):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(n)
                self.skipspace()
                self.deep()
                v2 = self.handle_value3()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                self.upn(3)
                v1 = PY_value_7(v1, n, v2)
        def multiop2(v1):
            v1 = multiop1(v1)
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for n in ['+', '-']:
                    if self.handle_str(n):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(n)
                self.skipspace()
                self.deep()
                v2 = self.handle_value3()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                v2 = multiop1(v2)
                self.upn(3)
                v1 = PY_value_7(v1, n, v2)
        return multiop2(v1)
        
    def handle_binvalue(self):
        self.deep()
        v1 = self.handle_value_7()
        if not v1:
            self.upfail()
            return None
        self.upn(1)
        def multiop1(v1):
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for n in ['%']:
                    if self.handle_str(n):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(n)
                self.skipspace()
                self.deep()
                v2 = self.handle_value_7()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                self.upn(3)
                v1 = PY_binvalue(v1, n, v2)
        def multiop2(v1):
            v1 = multiop1(v1)
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for n in ['>=', '>', '<=', '<', '==', '!=']:
                    if self.handle_str(n):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(n)
                self.skipspace()
                self.deep()
                v2 = self.handle_value_7()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                v2 = multiop1(v2)
                self.upn(3)
                v1 = PY_binvalue(v1, n, v2)
        def multiop3(v1):
            v1 = multiop2(v1)
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for n in ['in', 'is']:
                    if self.handle_str(n):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(n)
                self.skipspace()
                self.deep()
                v2 = self.handle_value_7()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                v2 = multiop2(v2)
                self.upn(3)
                v1 = PY_binvalue(v1, n, v2)
        return multiop3(v1)
        
    def handle_value5(self):
        self.deep()
        v1 = self.handle_binvalue()
        if not v1:
            self.upfail()
            return None
        self.upn(1)
        savpos3 = self.pos
        self.skipspace()
        def afterhd():
            self.deep1()
            savpos = self.pos
            if not self.handle_str('if'):
                self.upfail()
                return None
            self.skipspace()
            v2 = self.handle_binvalue()
            if not v2:
                self.upfail()
                return self.restorepos(savpos)
            self.skipspace()
            if not self.handle_str('else'):
                self.upfail()
                return self.restorepos(savpos)
            self.skipspace()
            v3 = self.handle_binvalue()
            if not v3:
                self.upfail()
                return self.restorepos(savpos)
            self.upn(3)
            return PY_value5(v1, v2, v3)
        vafter = afterhd()
        if not vafter:
            self.restorepos(savpos3)
            return v1
        return vafter
        
    def handle_value6(self):
        self.deep()
        v1 = self.handle_value5()
        if not v1:
            self.upfail()
            return None
        self.upn(1)
        def multiop1(v1):
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for n in ['and', 'or']:
                    if self.handle_str(n):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(n)
                self.skipspace()
                self.deep()
                v2 = self.handle_value5()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                self.upn(3)
                v1 = PY_value6(v1, n, v2)
        return multiop1(v1)
        
    def hdl_value(self):
        self.deep()
        v = self.handle_value6()
        if not v:
            self.upfail()
            return None
        self.upone()
        return v
        
    def handle_litname(self):
        self.deep()
        n = self.handle_NAME()
        if not n:
            self.upfail()
            return None
        self.upone()
        return PY_litname(n)

class PY_output:
    def __init__(self, outp):
        self.outp = outp
    def visit_dict(self, node):
        self.outp.puts('{')
        if node.vq:
            node.vq.walkabout(self)
        if node.nq:
            self.outp.puts(',')
        self.outp.puts('}')
    def visit_dict_items(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_stmts(self, node):
        for v in node.vlst:
            self.outp.ident()
            v.walkabout(self)
    def visit_deepstmts(self, node):
        self.outp.identin()
        node.v.walkabout(self)
        self.outp.identout()
    def visit_main(self, node):
        node.v.walkabout(self)
    def visit_stmt_1line(self, node):
        node.v.walkabout(self)
    def visit_stmt_multi(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(';')
            v.walkabout(self)
    def visit_stmt(self, node):
        node.v.walkabout(self)
    def visit_if_stmt(self, node):
        self.outp.puts('if')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
        for v in node.vlst:
            v.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_elif_part(self, node):
        self.outp.ident()
        self.outp.puts('elif')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
    def visit_else_part(self, node):
        self.outp.ident()
        self.outp.puts('else')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_while_stmt(self, node):
        self.outp.puts('while')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_for_stmt(self, node):
        self.outp.puts('for')
        node.v1.walkabout(self)
        self.outp.puts('in')
        node.v2.walkabout(self)
        self.outp.puts(':')
        node.v3.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_return_stmt(self, node):
        self.outp.puts('return')
        if node.vq:
            node.vq.walkabout(self)
    def visit_valuecomma(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_funcdef(self, node):
        self.outp.puts('def')
        self.outp.puts(node.n)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_params(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_param(self, node):
        self.outp.puts(node.n)
        if node.vq:
            self.outp.puts('=')
            node.vq.walkabout(self)
    def visit_augassign(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.n)
        node.v2.walkabout(self)
    def visit_assign(self, node):
        node.v1.walkabout(self)
        self.outp.puts('=')
        node.v2.walkabout(self)
    def visit_valuecommap(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_dest(self, node):
        node.v.walkabout(self)
    def visit_dest_tuple(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        if node.nq:
            self.outp.puts(',')
        self.outp.puts(')')
    def visit_print_stmt(self, node):
        self.outp.puts('print')
        if node.vq:
            node.vq.walkabout(self)
        if node.nq:
            self.outp.puts(',')
    def visit_args(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_import(self, node):
        node.v.walkabout(self)
    def visit_import1(self, node):
        self.outp.puts('from')
        node.v1.walkabout(self)
        self.outp.puts('import')
        node.v2.walkabout(self)
    def visit_star(self, node):
        self.outp.puts('*')
    def visit_import2(self, node):
        self.outp.puts('import')
        node.v.walkabout(self)
    def visit_importcommas(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_importitem(self, node):
        node.v.walkabout(self)
        if node.nq:
            self.outp.puts('as')
            self.outp.puts(node.nq)
    def visit_classdef(self, node):
        self.outp.puts('class')
        self.outp.puts(node.n)
        if node.vq:
            self.outp.puts('(')
            node.vq.walkabout(self)
            self.outp.puts(')')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_assert_stmt(self, node):
        self.outp.puts('assert')
        node.v.walkabout(self)
    def visit_oneword_stmt(self, node):
        self.outp.puts(node.n)
    def visit_dots(self, node):
        self.outp.puts(node.nlst[0])
        for s_ in node.nlst[1:]:
            self.outp.puts('.')
            self.outp.puts(s_)
    def visit_commas(self, node):
        self.outp.puts(node.nlst[0])
        for s_ in node.nlst[1:]:
            self.outp.puts(',')
            self.outp.puts(s_)
    def visit_commap(self, node):
        self.outp.puts(node.nlst[0])
        for s_ in node.nlst[1:]:
            self.outp.puts(',')
            self.outp.puts(s_)
    def visit_dotscomma(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_dotscommap(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_value_bool(self, node):
        self.outp.puts(node.n)
    def visit_value_str(self, node):
        self.outp.puts(node.s_raw)
    def visit_value_n(self, node):
        self.outp.puts(node.n)
    def visit_value0(self, node):
        node.v.walkabout(self)
    def visit_value1(self, node):
        node.v.walkabout(self)
    def visit_list(self, node):
        self.outp.puts('[')
        if node.vq:
            node.vq.walkabout(self)
        if node.nq:
            self.outp.puts(',')
        self.outp.puts(']')
    def visit_dict_item(self, node):
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
    def visit_list_comprehen(self, node):
        self.outp.puts('[')
        node.v1.walkabout(self)
        self.outp.puts('for')
        node.v2.walkabout(self)
        self.outp.puts('in')
        node.v3.walkabout(self)
        self.outp.puts(']')
    def visit_tuple(self, node):
        node.v.walkabout(self)
    def visit_tuple1(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        self.outp.puts(',')
        self.outp.puts(')')
    def visit_tuple2(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        if node.nq:
            self.outp.puts(',')
        self.outp.puts(')')
    def visit_tupleitem(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_enclosed(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        self.outp.puts(')')
    def visit_funccall(self, node):
        self.outp.puts(node.n)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
    def visit_funcargs(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_funcarg(self, node):
        if node.nq:
            self.outp.puts(node.nq)
            self.outp.puts('=')
        node.v.walkabout(self)
    def visit_ext_array_index(self, node):
        node.v0.walkabout(self)
        self.outp.puts('[')
        node.v.walkabout(self)
        self.outp.puts(']')
    def visit_ext_call(self, node):
        node.v0.walkabout(self)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
    def visit_ext_dot(self, node):
        node.v0.walkabout(self)
        self.outp.puts('.')
        self.outp.puts(node.n)
    def visit_idx(self, node):
        node.v.walkabout(self)
    def visit_idx1(self, node):
        if node.vq1:
            node.vq1.walkabout(self)
        self.outp.puts(':')
        if node.vq2:
            node.vq2.walkabout(self)
        self.outp.puts(':')
        if node.vq3:
            node.vq3.walkabout(self)
    def visit_idx2(self, node):
        if node.vq1:
            node.vq1.walkabout(self)
        self.outp.puts(':')
        if node.vq2:
            node.vq2.walkabout(self)
    def visit_value2(self, node):
        node.v.walkabout(self)
    def visit_signed(self, node):
        self.outp.puts(node.n)
        node.v.walkabout(self)
    def visit_value_7(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.n)
        node.v2.walkabout(self)
    def visit_binvalue(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.n)
        node.v2.walkabout(self)
    def visit_value5(self, node):
        node.v1.walkabout(self)
        self.outp.puts('if')
        node.v2.walkabout(self)
        self.outp.puts('else')
        node.v3.walkabout(self)
    def visit_value6(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.n)
        node.v2.walkabout(self)
    def visit_value(self, node):
        node.v.walkabout(self)
    def visit_litname(self, node):
        self.outp.puts(node.n)

class PY_SerialIn:
    def handle_dict(self, lst):
        lst_vq, lst_nq = lst
        vq = None
        if lst_vq:
            vq = self.handle_dict_items(lst_vq)
        nq = ""
        if lst_nq != 0:
            nq = ','
        return PY_dict(vq, nq)
    def handle_dict_items(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.handle_dict_item(l2)
            vlst.append(s)
        return PY_dict_items(vlst)
    def handle_stmts(self, lst):
        lst_vlst = lst
        vlst = []
        for l_ in lst_vlst:
            v = self.hdl_stmt(l_)
            vlst.append(v)
        return PY_stmts(vlst)
    def handle_deepstmts(self, lst):
        lst_v = lst
        v = self.handle_stmts(lst_v)
        return PY_deepstmts(v)
    def handle_main(self, lst):
        lst_v = lst
        v = self.handle_stmts(lst_v)
        return PY_main(v)
    def hdl_stmt_1line(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_oneword_stmt(l_)
        elif no_ == 1:
            v = self.handle_assert_stmt(l_)
        elif no_ == 2:
            v = self.handle_assign(l_)
        elif no_ == 3:
            v = self.handle_augassign(l_)
        elif no_ == 4:
            v = self.hdl_value(l_)
        else:
            assert False
        return v
    def handle_stmt_multi(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.hdl_stmt_1line(l2)
            vlst.append(s)
        return PY_stmt_multi(vlst)
    def hdl_stmt(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_if_stmt(l_)
        elif no_ == 1:
            v = self.handle_while_stmt(l_)
        elif no_ == 2:
            v = self.handle_for_stmt(l_)
        elif no_ == 3:
            v = self.handle_return_stmt(l_)
        elif no_ == 4:
            v = self.handle_print_stmt(l_)
        elif no_ == 5:
            v = self.handle_funcdef(l_)
        elif no_ == 6:
            v = self.hdl_import(l_)
        elif no_ == 7:
            v = self.handle_classdef(l_)
        elif no_ == 8:
            v = self.handle_stmt_multi(l_)
        elif no_ == 9:
            v = self.hdl_stmt_1line(l_)
        else:
            assert False
        return v
    def handle_if_stmt(self, lst):
        lst_v1, lst_v2, lst_vlst, lst_vq = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.handle_deepstmts(lst_v2)
        vlst = []
        for l_ in lst_vlst:
            v = self.handle_elif_part()
            if not v:
                break
            vlst.append(v)
            savpos = self.pos
        vq = None
        if lst_vq:
            vq = self.handle_else_part(lst_vq)
        return PY_if_stmt(v1, v2, vlst, vq)
    def handle_elif_part(self, lst):
        lst_v1, lst_v2 = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.handle_deepstmts(lst_v2)
        return PY_elif_part(v1, v2)
    def handle_else_part(self, lst):
        lst_v = lst
        v = self.handle_deepstmts(lst_v)
        return PY_else_part(v)
    def handle_while_stmt(self, lst):
        lst_v1, lst_v2, lst_vq = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.handle_deepstmts(lst_v2)
        vq = None
        if lst_vq:
            vq = self.handle_else_part(lst_vq)
        return PY_while_stmt(v1, v2, vq)
    def handle_for_stmt(self, lst):
        lst_v1, lst_v2, lst_v3, lst_vq = lst
        v1 = self.handle_commas(lst_v1)
        v2 = self.hdl_value(lst_v2)
        v3 = self.handle_deepstmts(lst_v3)
        vq = None
        if lst_vq:
            vq = self.handle_else_part(lst_vq)
        return PY_for_stmt(v1, v2, v3, vq)
    def handle_return_stmt(self, lst):
        lst_vq = lst
        vq = None
        if lst_vq:
            vq = self.handle_valuecomma(lst_vq)
        return PY_return_stmt(vq)
    def handle_valuecomma(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.hdl_value(l2)
            vlst.append(s)
        return PY_valuecomma(vlst)
    def handle_funcdef(self, lst):
        lst_n, lst_vq, lst_v = lst
        n = lst_n
        vq = None
        if lst_vq:
            vq = self.handle_params(lst_vq)
        v = self.handle_deepstmts(lst_v)
        return PY_funcdef(n, vq, v)
    def handle_params(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.handle_param(l2)
            vlst.append(s)
        return PY_params(vlst)
    def handle_param(self, lst):
        lst_n, lst_vq = lst
        n = lst_n
        vq = None
        if lst_vq:
            lst_vq = lst_vq[0]
            vq = self.hdl_value(lst_vq)
        return PY_param(n, vq)
    def handle_augassign(self, lst):
        lst_v1, lst_n, lst_v2 = lst
        v1 = self.hdl_dest(lst_v1)
        no_ = lst_n
        if no_ == 0:
            n = '+='
        elif no_ == 1:
            n = '-='
        elif no_ == 2:
            n = '/='
        elif no_ == 3:
            n = '*='
        else:
            assert False
        v2 = self.hdl_value(lst_v2)
        return PY_augassign(v1, n, v2)
    def handle_assign(self, lst):
        lst_v1, lst_v2 = lst
        v1 = self.hdl_dest(lst_v1)
        (l_,no_) = lst_v2
        if no_ == 0:
            v2 = self.handle_valuecommap(l_)
        elif no_ == 1:
            v2 = self.hdl_value(l_)
        else:
            assert False
        return PY_assign(v1, v2)
    def handle_valuecommap(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.hdl_value(l2)
            vlst.append(s)
        return PY_valuecommap(vlst)
    def handle_dest1(self, lst):
        lst_v, no_ = lst
        if no_ == 0:
            return self.handle_litname(lst_v)
        elif no_ == 1:
            v0 = self.handle_dest1(lst_v[0])
            return self.hdlext_ext_array_index(lst_v, v0)
        elif no_ == 2:
            v0 = self.handle_dest1(lst_v[0])
            return self.hdlext_ext_call(lst_v, v0)
        elif no_ == 3:
            v0 = self.handle_dest1(lst_v[0])
            return self.hdlext_ext_dot(lst_v, v0)
        else:
            assert False
    def hdl_dest(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_dotscommap(l_)
        elif no_ == 1:
            v = self.handle_dest_tuple(l_)
        elif no_ == 2:
            v = self.handle_dest1(l_)
        else:
            assert False
        return v
    def handle_dest_tuple(self, lst):
        lst_v, lst_nq = lst
        v = self.handle_commas(lst_v)
        nq = ""
        if lst_nq != 0:
            nq = ','
        return PY_dest_tuple(v, nq)
    def handle_print_stmt(self, lst):
        lst_vq, lst_nq = lst
        vq = None
        if lst_vq:
            vq = self.handle_args(lst_vq)
        nq = ""
        if lst_nq != 0:
            nq = ','
        return PY_print_stmt(vq, nq)
    def handle_args(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.hdl_value(l2)
            vlst.append(s)
        return PY_args(vlst)
    def hdl_import(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_import1(l_)
        elif no_ == 1:
            v = self.handle_import2(l_)
        else:
            assert False
        return v
    def handle_import1(self, lst):
        lst_v1, lst_v2 = lst
        v1 = self.handle_dots(lst_v1)
        (l_,no_) = lst_v2
        if no_ == 0:
            v2 = self.handle_star(l_)
        elif no_ == 1:
            v2 = self.handle_importcommas(l_)
        else:
            assert False
        return PY_import1(v1, v2)
    def handle_star(self, lst):
        return PY_star()
    def handle_import2(self, lst):
        lst_v = lst
        v = self.handle_importcommas(lst_v)
        return PY_import2(v)
    def handle_importcommas(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.handle_importitem(l2)
            vlst.append(s)
        return PY_importcommas(vlst)
    def handle_importitem(self, lst):
        lst_v, lst_nq = lst
        v = self.handle_dots(lst_v)
        nq = None
        if lst_nq:
            lst_nq = lst_nq[0]
            nq = lst_nq
        return PY_importitem(v, nq)
    def handle_classdef(self, lst):
        lst_n, lst_vq, lst_v = lst
        n = lst_n
        vq = None
        if lst_vq:
            lst_vq = lst_vq[0]
            vq = self.handle_dotscomma(lst_vq)
        v = self.handle_deepstmts(lst_v)
        return PY_classdef(n, vq, v)
    def handle_assert_stmt(self, lst):
        lst_v = lst
        v = self.hdl_value(lst_v)
        return PY_assert_stmt(v)
    def handle_oneword_stmt(self, lst):
        lst_n = lst
        no_ = lst_n
        if no_ == 0:
            n = 'pass'
        elif no_ == 1:
            n = 'break'
        elif no_ == 2:
            n = 'continue'
        else:
            assert False
        return PY_oneword_stmt(n)
    def handle_dots(self, lst):
        lst_nlst = lst
        nlst = []
        for l2 in lst_nlst:
            s = l2
            nlst.append(s)
        return PY_dots(nlst)
    def handle_commas(self, lst):
        lst_nlst = lst
        nlst = []
        for l2 in lst_nlst:
            s = l2
            nlst.append(s)
        return PY_commas(nlst)
    def handle_commap(self, lst):
        lst_nlst = lst
        nlst = []
        for l2 in lst_nlst:
            s = l2
            nlst.append(s)
        return PY_commap(nlst)
    def handle_dotscomma(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.handle_dots(l2)
            vlst.append(s)
        return PY_dotscomma(vlst)
    def handle_dotscommap(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.handle_dots(l2)
            vlst.append(s)
        return PY_dotscommap(vlst)
    def handle_value_bool(self, lst):
        lst_n = lst
        no_ = lst_n
        if no_ == 0:
            n = 'True'
        elif no_ == 1:
            n = 'False'
        else:
            assert False
        return PY_value_bool(n)
    def handle_value_str(self, lst):
        lst_s = lst
        (l_,no_) = lst_s
        if no_ == 0:
            s = l_
        elif no_ == 1:
            s = l_
        elif no_ == 2:
            s = l_
        elif no_ == 3:
            s = l_
        elif no_ == 4:
            s = l_
        elif no_ == 5:
            s = l_
        elif no_ == 6:
            s = l_
        else:
            assert False
        return PY_value_str((s, s))
    def handle_value_n(self, lst):
        lst_n = lst
        (l_,no_) = lst_n
        if no_ == 0:
            n = l_
        elif no_ == 1:
            n = l_
        else:
            assert False
        return PY_value_n(n)
    def hdl_value0(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_value_str(l_)
        elif no_ == 1:
            v = self.handle_value_n(l_)
        else:
            assert False
        return v
    def hdl_value1(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_list(l_)
        elif no_ == 1:
            v = self.handle_list_comprehen(l_)
        elif no_ == 2:
            v = self.handle_dict(l_)
        elif no_ == 3:
            v = self.hdl_tuple(l_)
        elif no_ == 4:
            v = self.handle_enclosed(l_)
        elif no_ == 5:
            v = self.handle_funccall(l_)
        elif no_ == 6:
            v = self.handle_value_bool(l_)
        elif no_ == 7:
            v = self.hdl_value0(l_)
        else:
            assert False
        return v
    def handle_list(self, lst):
        lst_vq, lst_nq = lst
        vq = None
        if lst_vq:
            vq = self.handle_args(lst_vq)
        nq = ""
        if lst_nq != 0:
            nq = ','
        return PY_list(vq, nq)
    def handle_dict_item(self, lst):
        lst_v1, lst_v2 = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.hdl_value(lst_v2)
        return PY_dict_item(v1, v2)
    def handle_list_comprehen(self, lst):
        lst_v1, lst_v2, lst_v3 = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.handle_commas(lst_v2)
        v3 = self.hdl_value(lst_v3)
        return PY_list_comprehen(v1, v2, v3)
    def hdl_tuple(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_tuple1(l_)
        elif no_ == 1:
            v = self.handle_tuple2(l_)
        else:
            assert False
        return v
    def handle_tuple1(self, lst):
        lst_v = lst
        v = self.hdl_value(lst_v)
        return PY_tuple1(v)
    def handle_tuple2(self, lst):
        lst_v, lst_nq = lst
        v = self.handle_tupleitem(lst_v)
        nq = ""
        if lst_nq != 0:
            nq = ','
        return PY_tuple2(v, nq)
    def handle_tupleitem(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.hdl_value(l2)
            vlst.append(s)
        return PY_tupleitem(vlst)
    def handle_enclosed(self, lst):
        lst_v = lst
        v = self.hdl_value(lst_v)
        return PY_enclosed(v)
    def handle_funccall(self, lst):
        lst_n, lst_vq = lst
        n = lst_n
        vq = None
        if lst_vq:
            vq = self.handle_funcargs(lst_vq)
        return PY_funccall(n, vq)
    def handle_funcargs(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.handle_funcarg(l2)
            vlst.append(s)
        return PY_funcargs(vlst)
    def handle_funcarg(self, lst):
        lst_nq, lst_v = lst
        nq = None
        if lst_nq:
            lst_nq = lst_nq[0]
            nq = lst_nq
        v = self.hdl_value(lst_v)
        return PY_funcarg(nq, v)
    def handle_value3(self, lst):
        lst_v, no_ = lst
        if no_ == 0:
            return self.hdl_value1(lst_v)
        elif no_ == 1:
            v0 = self.handle_value3(lst_v[0])
            return self.hdlext_ext_array_index(lst_v, v0)
        elif no_ == 2:
            v0 = self.handle_value3(lst_v[0])
            return self.hdlext_ext_call(lst_v, v0)
        elif no_ == 3:
            v0 = self.handle_value3(lst_v[0])
            return self.hdlext_ext_dot(lst_v, v0)
        else:
            assert False
    def hdlext_ext_array_index(self, lst, v0):
        lst_v0, lst_v = lst
        v = self.hdl_idx(lst_v)
        return PY_ext_array_index(v0, v)
    def hdlext_ext_call(self, lst, v0):
        lst_v0, lst_vq = lst
        vq = None
        if lst_vq:
            vq = self.handle_funcargs(lst_vq)
        return PY_ext_call(v0, vq)
    def hdlext_ext_dot(self, lst, v0):
        lst_v0, lst_n = lst
        n = lst_n
        return PY_ext_dot(v0, n)
    def hdl_idx(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_idx1(l_)
        elif no_ == 1:
            v = self.handle_idx2(l_)
        elif no_ == 2:
            v = self.hdl_value(l_)
        else:
            assert False
        return v
    def handle_idx1(self, lst):
        lst_vq1, lst_vq2, lst_vq3 = lst
        vq1 = None
        if lst_vq1:
            vq1 = self.hdl_value(lst_vq1)
        vq2 = None
        if lst_vq2:
            vq2 = self.hdl_value(lst_vq2)
        vq3 = None
        if lst_vq3:
            vq3 = self.hdl_value(lst_vq3)
        return PY_idx1(vq1, vq2, vq3)
    def handle_idx2(self, lst):
        lst_vq1, lst_vq2 = lst
        vq1 = None
        if lst_vq1:
            vq1 = self.hdl_value(lst_vq1)
        vq2 = None
        if lst_vq2:
            vq2 = self.hdl_value(lst_vq2)
        return PY_idx2(vq1, vq2)
    def hdl_value2(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_signed(l_)
        elif no_ == 1:
            v = self.handle_value3(l_)
        else:
            assert False
        return v
    def handle_signed(self, lst):
        lst_n, lst_v = lst
        no_ = lst_n
        if no_ == 0:
            n = '-'
        elif no_ == 1:
            n = '+'
        elif no_ == 2:
            n = 'not'
        else:
            assert False
        v = self.handle_value3(lst_v)
        return PY_signed(n, v)
    def handle_value_7(self, lst):
        if len(lst) == 1:
            return self.hdl_value2(lst[0])
        def func1(lst2):
            if len(lst2) == 1:
                return self.handle_value3(lst2[0])
            lst_v1, s, lst_v2 = lst2
            v1 = func1(lst_v1)
            v2 = func1(lst_v2)
            return PY_value_7(v1, s, v2)
        lst_v1, s, lst_v2 = lst
        v1 = self.handle_value_7(lst_v1)
        v2 = func1(lst_v2)
        return PY_value_7(v1, s, v2)
    def handle_binvalue(self, lst):
        if len(lst) == 1:
            return self.handle_value_7(lst[0])
        def func1(lst2):
            if len(lst2) == 1:
                return self.handle_value_7(lst2[0])
            lst_v1, s, lst_v2 = lst2
            v1 = func1(lst_v1)
            v2 = func1(lst_v2)
            return PY_binvalue(v1, s, v2)
        lst_v1, s, lst_v2 = lst
        v1 = self.handle_binvalue(lst_v1)
        v2 = func1(lst_v2)
        return PY_binvalue(v1, s, v2)
    def handle_value5(self, lst):
        if len(lst) == 1:
            return self.handle_binvalue(lst[0])
        lst_v1, lst_v2, lst_v3 = lst
        v1 = self.handle_binvalue(lst_v1[0])
        v2 = self.handle_binvalue(lst_v2)
        v3 = self.handle_binvalue(lst_v3)
        return PY_value5(v1, v2, v3)
    def handle_value6(self, lst):
        if len(lst) == 1:
            return self.handle_value5(lst[0])
        def func1(lst2):
            if len(lst2) == 1:
                return self.handle_value5(lst2[0])
            lst_v1, s, lst_v2 = lst2
            v1 = func1(lst_v1)
            v2 = func1(lst_v2)
            return PY_value6(v1, s, v2)
        lst_v1, s, lst_v2 = lst
        v1 = self.handle_value6(lst_v1)
        v2 = func1(lst_v2)
        return PY_value6(v1, s, v2)
    def hdl_value(self, lst):
        lst_v = lst
        v = self.handle_value6(lst_v)
        return v
    def handle_litname(self, lst):
        lst_n = lst
        n = lst_n
        return PY_litname(n)
