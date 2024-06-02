{\rtf1\fbidis\ansi\ansicpg950\deff0\nouicompat\deflang1033\deflangfe1028{\fonttbl{\f0\fnil\fcharset136 Segoe UI;}{\f1\fnil Segoe UI;}}
{\colortbl ;\red0\green0\blue0;}
{\*\generator Riched20 10.0.22621}\viewkind4\uc1 
\pard\tx720\cf1\f0\fs21\lang1028 # \'aa\'ec\'a9\'6c\'a4\'c6\'ad\'70\'bc\'c6\'be\'b9\'a9\'4d\'c1\'60\'a6\'a8\'c1\'5a\f1\par
total_students = 0\par
pass_students = 0\par
fail_students = 0\par
total_score = 0\par
\par
\f0 # \'bf\'e9\'a4\'4a\'be\'c7\'a5\'cd\'a6\'a8\'c1\'5a\'a1\'41\'aa\'bd\'a8\'ec\'bf\'e9\'a4\'4a -1 \'b5\'b2\'a7\'f4\f1\par
while True:\par
    score = input("\f0\'bd\'d0\'bf\'e9\'a4\'4a\'be\'c7\'a5\'cd\'a6\'a8\'c1\'5a\'a1\'5d\'bf\'e9\'a4\'4a-1\'b5\'b2\'a7\'f4\'a1\'5e\'a1\'47")\f1\par
    \par
\f0     # \'c0\'cb\'ac\'64\'ac\'4f\'a7\'5f\'bf\'e9\'a4\'4a\'b5\'b2\'a7\'f4\f1\par
    if score == "-1":\par
        break\par
    \par
\f0     # \'b1\'4e\'bf\'e9\'a4\'4a\'aa\'ba\'a6\'a8\'c1\'5a\'c2\'e0\'b4\'ab\'ac\'b0\'be\'e3\'bc\'c6\f1\par
    score = int(score)\par
    \par
\f0     # \'a7\'f3\'b7\'73\'ad\'70\'bc\'c6\'be\'b9\'a9\'4d\'c1\'60\'a6\'a8\'c1\'5a\f1\par
    total_students += 1\par
    total_score += score\par
    \par
\f0     # \'a7\'50\'c2\'5f\'a4\'ce\'ae\'e6\'bb\'50\'a7\'5f\f1\par
    if score >= 60:\par
        pass_students += 1\par
    else:\par
        fail_students += 1\par
\par
\f0 # \'ad\'70\'ba\'e2\'a5\'ad\'a7\'a1\'a6\'a8\'c1\'5a\f1\par
average_score = total_score / total_students if total_students != 0 else 0\par
\par
\f0 # \'c5\'e3\'a5\'dc\'b5\'b2\'aa\'47\f1\par
print("\f0\'a5\'fe\'af\'5a\'a4\'48\'bc\'c6\'a1\'47",\f1  total_students)\par
print("\f0\'a4\'ce\'ae\'e6\'a4\'48\'bc\'c6\'a1\'47", \f1 pass_students)\par
print("\f0\'a4\'a3\'a4\'ce\'ae\'e6\'a4\'48\'bc\'c6\'a1\'47", \f1 fail_students)\par
print("\f0\'a5\'fe\'af\'5a\'a5\'ad\'a7\'a1\'ad\'c8\'a1\'47", \f1 average_score)\par
}
