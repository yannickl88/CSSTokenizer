@base: #f04615;
@width: 0.5;

.class {
  width: percentage(@width);
  color: saturate(@base, 5%);
  background-color: spin(lighten(@base, 25%), 8);
}
============TEST
T_ATWORD,1:1,1:5,"@base"
T_COLON,1,6,":"
T_WHITESPACE,1,7," "
T_WORD,1:1,8:14,"#f04615"
T_SEMICOLON,1,15,";"
T_WHITESPACE,2,0,"\n"
T_ATWORD,2:2,1:6,"@width"
T_COLON,2,7,":"
T_WHITESPACE,2,8," "
T_WORD,2:2,9:11,"0.5"
T_SEMICOLON,2,12,";"
T_WHITESPACE,4,0,"\n\n"
T_WORD,4:4,2:7,".class"
T_WHITESPACE,4,8," "
T_OPENCURLY,4,9,"{"
T_WHITESPACE,5,0,"\n  "
T_WORD,5:5,3:7,"width"
T_COLON,5,8,":"
T_WHITESPACE,5,9," "
T_WORD,5:5,10:19,"percentage"
T_OPENBRACKET,5,20,"("
T_ATWORD,5:5,21:26,"@width"
T_CLOSEBRACKET,5,27,")"
T_SEMICOLON,5,28,";"
T_WHITESPACE,6,0,"\n  "
T_WORD,6:6,3:7,"color"
T_COLON,6,8,":"
T_WHITESPACE,6,9," "
T_WORD,6:6,10:17,"saturate"
T_OPENBRACKET,6,18,"("
T_ATWORD,6:6,19:23,"@base"
T_COMMA,6,24,","
T_WHITESPACE,6,25," "
T_WORD,6:6,26:27,"5%"
T_CLOSEBRACKET,6,28,")"
T_SEMICOLON,6,29,";"
T_WHITESPACE,7,0,"\n  "
T_WORD,7:7,3:18,"background-color"
T_COLON,7,19,":"
T_WHITESPACE,7,20," "
T_WORD,7:7,21:24,"spin"
T_OPENBRACKET,7,25,"("
T_WORD,7:7,26:32,"lighten"
T_OPENBRACKET,7,33,"("
T_ATWORD,7:7,34:38,"@base"
T_COMMA,7,39,","
T_WHITESPACE,7,40," "
T_WORD,7:7,41:43,"25%"
T_CLOSEBRACKET,7,44,")"
T_COMMA,7,45,","
T_WHITESPACE,7,46," "
T_WORD,7:7,47:47,"8"
T_CLOSEBRACKET,7,48,")"
T_SEMICOLON,7,49,";"
T_WHITESPACE,8,0,"\n"
T_CLOSECURLY,8,1,"}"
