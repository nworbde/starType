#starType
Useful LaTeX macros for commonly used symbols in stellar astrophysics. Many of these macros were compiled during the preparation of the second MESA instrument paper(Paxton et al. 2013, ApJS 208: 4).

## installation and usage
After cloning the project directory, cd into it and run the install script
    
    $./install /path/to/texmf

Here the argument to the command is somewhere on the `TEXPATH`. For example, on my Mac, I do

    $./install ~/Library/texmf

The install script creates in this texmf directory a subdirectory, 
`tex/latex/starType`,
that contains `starType.sty`.  It then builds the documentation in a 
subdirectory of `texmf` called `doc/latex/starType`.

To use, load the package in the preamble of the tex document,

    \usepackage[<opts>]{starType}
    
where `<opts>` is a subset of `code`, `derivatives`, `nuclides`, `symbols`,    `units`, `vectors`, or `all`.  Each of these options loads the particular set of macros.  Calling `starType` with no options is equivalent to
    
    \usepackage[all]{starType}
    
### usage with mathspec

If you use XeLaTeX and mathspec, you must declare the math fonts before loading starType's vector macros, which use the `bm` package.  For example, in my notes for stellar astrophysics, my preamble looks like

    \usepackage{mathspec}
    \setmainfont[Scale=MatchLowercase,Mapping=tex-text]{Minion Pro}
    \setallmonofonts[Scale=MatchLowercase,Mapping=tex-text]{Menlo}
    \setallsansfonts[Scale=MatchLowercase,Mapping=tex-text]{Myriad Pro}
    \setmathsfont(Digits,Latin)[Scale=MatchLowercase,Mapping=tex-text]{Minion Pro}
    \setmathsfont(Greek)[Scale=MatchLowercase,Mapping=tex-text]{STIXGeneral}
    \setmathrm{Minion Pro}

    \usepackage{starType}


## macros
*   `st_code.tex`: uses tt font for code, macros for some common codes
*   `st_derivatives.tex`: macros for typesetting common used expressions for deriviatives
*   `st_nuclides.tex`:  macros to typset all named nuclides
*   `st_symbols.tex`: lots of symbols for commonly used quantities in astrophysics and stellar physics
*   `st_units.tex`: macros for typesetting units
*   `st_vectors.tex`: macros for typesetting vector expressions

## scripts
*   `extract_symbols.py`: a lightweight python script that constructs a latex table of the macros in a given file. The output is sent to `stdout` as a standalone document that makes use of the `fancyvrb` and `longtable` packages.
