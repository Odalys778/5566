{\rtf1\fbidis\ansi\ansicpg950\deff0\nouicompat\deflang1033\deflangfe1028{\fonttbl{\f0\fnil\fcharset136 Segoe UI;}}
{\colortbl ;\red0\green0\blue0;}
{\*\generator Riched20 10.0.22621}\viewkind4\uc1 
\pard\tx720\cf1\f0\fs21\lang1028 # \'a9\'77\'b8\'71\'ad\'6e\'a5\'b4\'a6\'4c\'aa\'ba\'ac\'50\'ac\'50\'aa\'ba\'a6\'e6\'bc\'c6\par
num_rows = 5\par
\par
# \'b0\'6a\'b0\'e9\'a6\'4c\'a5\'58\'a8\'43\'a4\'40\'a6\'e6\'aa\'ba\'ac\'50\'b8\'b9\par
for i in range(1, num_rows + 1):\par
    if i <= (num_rows + 1) // 2:  # \'ab\'65\'a5\'62\'ac\'71\'a6\'e6\'bc\'c6\'bb\'bc\'bc\'57\par
        num_stars = 2 * i - 1\par
    else:  # \'ab\'e1\'a5\'62\'ac\'71\'a6\'e6\'bc\'c6\'bb\'bc\'b4\'ee\par
        num_stars = 2 * (num_rows - i) + 1\par
    \par
    print(" " * ((2 * num_rows - 1 - num_stars) // 2) + "*" * num_stars)\par
}
 