.average(@x, @y) {
  @average: ((@x + @y) / 2);
}
============TEST
T_WORD,1:1,1:8,".average"
T_OPENBRACKET,1,9,"("
T_ATWORD,1:1,10:11,"@x"
T_COMMA,1,12,","
T_WHITESPACE,1,13," "
T_ATWORD,1:1,14:15,"@y"
T_CLOSEBRACKET,1,16,")"
T_WHITESPACE,1,17," "
T_OPENCURLY,1,18,"{"
T_WHITESPACE,1:2,19:2,"\n  "
T_ATWORD,2:2,3:10,"@average"
T_COLON,2,11,":"
T_WHITESPACE,2,12," "
T_OPENBRACKET,2,13,"("
T_OPENBRACKET,2,14,"("
T_ATWORD,2:2,15:16,"@x"
T_WHITESPACE,2,17," "
T_WORD,2:2,18:18,"+"
T_WHITESPACE,2,19," "
T_ATWORD,2:2,20:21,"@y"
T_CLOSEBRACKET,2,22,")"
T_WHITESPACE,2,23," "
T_WORD,2:2,24:24,"\/"
T_WHITESPACE,2,25," "
T_WORD,2:2,26:26,"2"
T_CLOSEBRACKET,2,27,")"
T_SEMICOLON,2,28,";"
T_WHITESPACE,2:3,29:0,"\n"
T_CLOSECURLY,3,1,"}"
