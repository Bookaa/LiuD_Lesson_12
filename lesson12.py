# LiuD Lesson Twelve

from LiuD_Main_Gen import Gen_All


LiuD_syntax = '''option.prefix = LiuD
states.skip = crlf
    values_or = NAME ^+ '|'
    string_or = STRING ^+ '|'

states.skip = space
main = (stmt1 NEWLINE)*
stmt1 := options | stmt | inline | ends
ends = NAME '->' stmt_value
inline = NAME ':=' stmt_value
options := option1 | state1 | state2 | basic1
    option1 = 'option.prefix' '=' NAME
    state1 = 'states.skip' '=' NAME
    state2 = 'states.linecomments' '=' STRING
    basic1 = 'basic.' NAME '=' strcat
        strcat = STRING ^* '+'
stmt = NAME '=' stmt_value
stmt_value := multiop | endswith | values_or | string_or | jiap | jiad | headseries | series
    headseries = NAME ',' value*
    series = value*
    jiap = NAME '^+' STRING
    jiad = NAME '^*' STRING
    endswith = NAME '(,' NAME* ')'
    multiop = NAME '(,' opstr* ')' NAME
        opstr := litstring | enclosedstrs
        enclosedstrs = '(' STRING* ')'

litname = NAME
litstring = STRING
value1 := litname | litstring | enclosed
    enclosed = '(' stmt_value ')'
value := itemd | itemq | value1
    itemd = value1 '*'
    itemq = value1 '?'
'''

syntax_Py = r'''option.prefix = PY
    states.linecomments = '#'
    basic.STR2 = '"""(?:.|\n)*?"""'
    basic.STR3 = "''" + "'(?:.|\n)*?'" + "''"
    basic.STR4 = 'r"""(?:.|\n)*?"""'
    basic.STR5 = "r''" + "'(?:.|\n)*?'" + "''"
    basic.STR6 = "r'[^'\\]*(?:\\.[^'\\]*)*'"
    basic.STR7 = 'r"[^"\\]*(?:\\.[^"\\]*)*"'

    states.skip = crlf
        dict = '{' dict_items? ','? '}'
            dict_items = dict_item ^* ','
    states.skip = no
    stmts = (IDENT stmt)*
    deepstmts = IDENTIN stmts IDENTOUT

    states.skip = space

    main = stmts

    stmt_1line := oneword_stmt | assert_stmt | assign | augassign | value
    stmt_multi = stmt_1line ^+ ';'
    stmt := if_stmt | while_stmt | for_stmt | return_stmt | print_stmt | funcdef | import | classdef
        | stmt_multi | stmt_1line


        if_stmt = 'if' value ':' deepstmts elif_part* else_part?
            elif_part = IDENT 'elif' value ':' deepstmts
            else_part = IDENT 'else' ':' deepstmts
        while_stmt = 'while' value ':' deepstmts else_part?
        for_stmt = 'for' commas 'in' value ':' deepstmts else_part?
        return_stmt = 'return' valuecomma?
            valuecomma = value ^* ','
        funcdef = 'def' NAME '(' params? ')' ':' deepstmts
            params = param ^* ','
            param = NAME ('=' value)?
        augassign = dest ('+=' | '-=' | '/=' | '*=') value
        assign = dest '=' (valuecommap | value)
            valuecommap = value ^+ ','
        dest1 = litname (, ext_array_index ext_call ext_dot)
        dest := commap | dest_tuple | dest1
            dest_tuple = '(' commas ','? ')'
        print_stmt = 'print' args? ','?
            args = value ^* ','
        import := import1 | import2
        import1 = 'from' dots 'import' (star | importcommas)
            star = '*'
        import2 = 'import' importcommas
        importcommas = importitem ^* ','
        importitem = dots ('as' NAME)?

        classdef = 'class' NAME ('(' dotscomma ')')? ':' deepstmts
        assert_stmt = 'assert' value
        oneword_stmt = 'pass' | 'break' | 'continue'

    dots = NAME ^* '.'
    commas = NAME ^* ','
    commap = NAME ^+ ','
    dotscomma = dots ^* ','

    value_bool = 'True' | 'False'
    value0 = NUMBER | STR2 | STR3 | STR4 | STR5 | STR6 | STR7 | STRING | NAME
    value1 := list | list_comprehen | dict | tuple | enclosed | funccall | value_bool | value0
        list = '[' args? ','? ']'
                dict_item = value ':' value
        list_comprehen = '[' value 'for' commas 'in' value ']'
        tuple := tuple1 | tuple2
        tuple1 = '(' value ',' ')'
        tuple2 = '(' tupleitem ','? ')'
            tupleitem = value ^+ ','
        enclosed = '(' value ')'
        funccall = NAME '(' funcargs? ')'
            funcargs = funcarg ^* ','
            funcarg = (NAME '=')? value

    value3 = value1 (, ext_array_index ext_call ext_dot)
        ext_array_index -> '[' idx ']'
        ext_call -> '(' funcargs? ')'
        ext_dot -> '.' NAME

    idx := idx1 | idx2 | value
    idx1 = value? ':' value? ':' value?
    idx2 = value? ':' value?

    value2 := signed | value3
        signed = ('-' | '+' | 'not') value3
    value_7 = value2 (, ('*' '/') ('+' '-')) value3
    binvalue = value_7 (, '%' ('>=' '>' '<=' '<' '==' '!=') ('in' 'is') ) value_7
    value5 = binvalue, 'if' binvalue 'else' binvalue
    value6 = value5 (, ('and' 'or')) value5
    value := value6


    litname = NAME
    '''
sample_Python = '''
from LiuD_Main_Gen import Gen_All

# this is comments
class cls1:
    v3 = a1.a2[3].a3(a4,a5)
class cls2(cls1, object):
    # and here
    v = 3+2 if True else -66

s = """test
test
    multiline
        string"""
def main():
    c = 2800
    f = [10000 / 5] * 2801
    f[c] = 0
    e = 0
    while c != 0:
        d = 0
        b = c
        while True:
            d += f[b] * 10000
            f[b] = d % (b * 2 - 1)
            d /= (b * 2 - 1)
            b -= 1
            if b == 0:
                break
            d *= b

        c -= 14
        print '%04d' % (e + d / 10000),
        e = d % 10000

    print

main()
'''


import unittest
class Test(unittest.TestCase):
    def test1(self):
        s = Gen_All(LiuD_syntax)

        #open('Ast_LiuD2.py', 'w').write(s)
        s2 = open('Ast_LiuD.py').read()
        self.assertEqual(s, s2)

    def test3(self):
        import Ast_LiuD
        the = Ast_LiuD.LiuD_Parser(LiuD_syntax)
        mod = the.handle_main()

        outp = Ast_LiuD.OutP()
        the2 = Ast_LiuD.LiuD_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        print '<%s>' % txt
        txt2 = '''option.prefix = LiuD
states.skip = crlf
values_or = NAME ^+ '|'
string_or = STRING ^+ '|'
states.skip = space
main = ( stmt1 NEWLINE ) *
stmt1 := options | stmt | inline | ends
ends = NAME '->' stmt_value
inline = NAME ':=' stmt_value
options := option1 | state1 | state2 | basic1
option1 = 'option.prefix' '=' NAME
state1 = 'states.skip' '=' NAME
state2 = 'states.linecomments' '=' STRING
basic1 = 'basic.' NAME '=' strcat
strcat = STRING ^* '+'
stmt = NAME '=' stmt_value
stmt_value := multiop | endswith | values_or | string_or | jiap | jiad | headseries | series
headseries = NAME ',' value *
series = value *
jiap = NAME '^+' STRING
jiad = NAME '^*' STRING
endswith = NAME '(,' NAME * ')'
multiop = NAME '(,' opstr * ')' NAME
opstr := litstring | enclosedstrs
enclosedstrs = '(' STRING * ')'
litname = NAME
litstring = STRING
value1 := litname | litstring | enclosed
enclosed = '(' stmt_value ')'
value := itemd | itemq | value1
itemd = value1 '*'
itemq = value1 '?'
'''
        #print '<%s>' % txt2
        #print txt == txt2
        self.assertEqual(txt, txt2)
    def test4(self):
        sample_Python = open('lesson12.py').read()
        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        mod = the.handle_main()
        print mod

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        lines = txt.splitlines()
        self.assertEqual(lines[-1].strip(), "print 'good'")
        #print '<%s>' % lines[-1]
    def test5(self):
        s = Gen_All(syntax_Py, True)
        #open('Ast_Py2.py', 'w').write(s)
        s2 = open('Ast_Py.py').read()
        #self.assertEqual(s, s2)
        #return

        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        the.deep()
        mod = the.handle_main()
        last = the.SerialOut()

        stand = [[[[['LiuD_Main_Gen'], [[[['Gen_All'], []]], 1]], 0], 6], [['cls1', [], [[[[[['v3', 0], 2], [[[[[[[[[[[[[[[[['a1', 8], 7], 0], 'a2'], 3], [[[[[[[[['3', 0], 7], 0], 1]]]]], 2]], 1], 'a3'], 3], [[[], [[[[[[[['a4', 8], 7], 0], 1]]]]]], [[], [[[[[[[['a5', 8], 7], 0], 1]]]]]]]], 2], 1]]]]], 1]], 2], 9]]], 7], [['cls2', [[['cls1'], ['object']]], [[[[[['v', 0], 2], [[[[[[[[[[['3', 0], 7], 0], 1]], '+', [[[['2', 0], 7], 0]]]]], [[[[[0, 6], 0], 1]]], [[[[0, [[['66', 0], 7], 0]], 0]]]]], 1]], 2], 9]]], 7], [[[[['s', 0], 2], [[[[[[[[['"""test\ntest\n    multiline\n        string"""', 1], 7], 0], 1]]]]], 1]], 2], 9], [['main', [], [[[[[['c', 0], 2], [[[[[[[[['2800', 0], 7], 0], 1]]]]], 1]], 2], 9], [[[[['f', 0], 2], [[[[[[[[[[[[[[[[[[[['10000', 0], 7], 0], 1]], '/', [[[['5', 0], 7], 0]]]]]]], 0], 0], 0], 1]], '*', [[[['2801', 0], 7], 0]]]]]], 1]], 2], 9], [[[[[[['f', 0], [[[[[[[[['c', 8], 7], 0], 1]]]]], 2]], 1], 2], [[[[[[[[['0', 0], 7], 0], 1]]]]], 1]], 2], 9], [[[[['e', 0], 2], [[[[[[[[['0', 0], 7], 0], 1]]]]], 1]], 2], 9], [[[[[[[[[[['c', 8], 7], 0], 1]]], '!=', [[[[[['0', 0], 7], 0], 1]]]]]], [[[[[['d', 0], 2], [[[[[[[[['0', 0], 7], 0], 1]]]]], 1]], 2], 9], [[[[['b', 0], 2], [[[[[[[[['c', 8], 7], 0], 1]]]]], 1]], 2], 9], [[[[[[[[[0, 6], 0], 1]]]]], [[[[[['d', 0], 2], 0, [[[[[[[[[[['f', 8], 7], 0], [[[[[[[[['b', 8], 7], 0], 1]]]]], 2]], 1], 1]], '*', [[[['10000', 0], 7], 0]]]]]]], 3], 9], [[[[[[['f', 0], [[[[[[[[['b', 8], 7], 0], 1]]]]], 2]], 1], 2], [[[[[[[[[['d', 8], 7], 0], 1]]], '%', [[[[[[[[[[[[[[['b', 8], 7], 0], 1]], '*', [[[['2', 0], 7], 0]]], '-', [[[['1', 0], 7], 0]]]]]], 4], 0], 1]]]]]], 1]], 2], 9], [[[[['d', 0], 2], 2, [[[[[[[[[[[[[[[[['b', 8], 7], 0], 1]], '*', [[[['2', 0], 7], 0]]], '-', [[[['1', 0], 7], 0]]]]]], 4], 0], 1]]]]]], 3], 9], [[[[['b', 0], 2], 1, [[[[[[[['1', 0], 7], 0], 1]]]]]], 3], 9], [[[[[[[[[[['b', 8], 7], 0], 1]]], '==', [[[[[['0', 0], 7], 0], 1]]]]]], [[[1, 0], 9]], [], []], 0], [[[[['d', 0], 2], 3, [[[[[[[['b', 8], 7], 0], 1]]]]]], 3], 9]], []], 1], [[[[['c', 0], 2], 1, [[[[[[[['14', 0], 7], 0], 1]]]]]], 3], 9], [[[[[[[[[[[["'%04d'", 7], 7], 0], 1]]], '%', [[[[[[[[[[[[[['e', 8], 7], 0], 1]], '+', [[[[['d', 8], 7], 0]], '/', [[[['10000', 0], 7], 0]]]]]]], 4], 0], 1]]]]]]], 1], 4], [[[[['e', 0], 2], [[[[[[[[[['d', 8], 7], 0], 1]]], '%', [[[[[['10000', 0], 7], 0], 1]]]]]], 1]], 2], 9]], []], 1], [[[], 0], 4]]], 5], [[[[[[[[[['main', []], 5], 0], 1]]]]], 4], 9]]
        if last != stand:
            print last
        self.assertEqual(last, stand)

        the2 = Ast_Py.PY_SerialIn()
        mod2 = the2.handle_main(stand)

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        print '<%s>' % txt
        txt2 = '''
from LiuD_Main_Gen import Gen_All
class cls1 :
     v3 = a1 . a2 [ 3 ] . a3 ( a4 , a5 )
class cls2 ( cls1 , object ) :
     v = 3 + 2 if True else - 66
s = """test
test
    multiline
        string"""
def main ( ) :
     c = 2800
     f = [ 10000 / 5 ] * 2801
     f [ c ] = 0
     e = 0
     while c != 0 :
         d = 0
         b = c
         while True :
             d += f [ b ] * 10000
             f [ b ] = d % ( b * 2 - 1 )
             d /= ( b * 2 - 1 )
             b -= 1
             if b == 0 :
                 break
             d *= b
         c -= 14
         print '%04d' % ( e + d / 10000 ) ,
         e = d % 10000
     print
main ( )'''
        self.assertEqual(txt, txt2)

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod2.walkabout(the2)
        txt = outp.txt
        self.assertEqual(txt, txt2)
    def test6(self):
        sample_Python = open('LiuD_Main_Gen.py').read()
        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        mod = the.handle_main()
        print mod

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        self.assertEqual(txt.splitlines()[-1].strip(), 'return s')
    def test7(self):
        sample_Python = open('GDL_common.py').read()
        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        mod = the.handle_main()

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        self.assertEqual(txt.splitlines()[-1].strip(), "print '  ' * len ( self . lst ) + s + '<-'")

    def test7(self):
        sample_Python = open('Ast_LiuD.py').read()
        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        mod = the.handle_main()

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        self.assertEqual(txt.splitlines()[-1].strip(), "self . outp . puts ( '?' )")

    def test8(self):
        sample_Python = open('Ast_Py.py').read()
        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        mod = the.handle_main()

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        self.assertEqual(txt.splitlines()[-1].strip(), "return PY_litname ( s )")

if __name__ == '__main__':
    print 'good'
