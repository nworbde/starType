"""
    extract_symbols.py
    Edward Brown, Michigan State University
    
    This is a lightweight script for making a tables displaying the
    functionality of macros. The output is sent to stdout as a standalone
    document that makes use of the fancyvrb and longtable packages.
    
    Macros of the form \newcommand*{\macro}{definition}  % meaning
    will be writtn in 3 columns: \macro (verbatim); the output; and the meaning.
"""

import argparse
import re


parser = argparse.ArgumentParser(description="generates typeset table of macros from latex source.")
parser.add_argument('macro_filename',action='store',default=None,help="latex file containing the macros")

args = parser.parse_args()

# the input files
main_file = args.macro_filename
texbase = main_file.split('.')[0]

# search pattern
p = re.compile(r'\\newcommand\*?\{([^}]+)\}\{.*\}\s*%(.*)')

# arrays to hold symbols, definitions
syms = []
defins = []

with open(main_file,'r') as f:
  for line in f:
    m = p.search(line)
    if m: # have a symbol
      syms.append(m.group(1)); defins.append(m.group(2))

# construct a dictionary of symbols and definitions

symdict = {}
for sym, defin in zip(syms,defins):
  symdict[sym] = (defin)

keylist = symdict.keys()

# prologue
print(r'''
\documentclass{article}
\usepackage{fancyvrb,longtable}
''')
print('\\input{{{0}}}'.format(texbase))
print(r'''
\DefineShortVerb{\|}
\begin{document}
\begin{center}
\begin{longtable}{lll}
\hline
command & produces & meaning\\
\hline\hline
''')

# body of table
for key in sorted(keylist,key=str.lower):
  print('|{0}| & {0} & {1} \\\\'.format(key,symdict[key]))

# epilogue
print(r'''
\hline
\end{longtable}
\end{center}
\end{document}
''')
