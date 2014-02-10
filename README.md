Pokemon-Type-Calculator
=======================
Note - all modules in this repo were created/tested on Python 2.7, and no compatibility with other versions is guaranteed.


How To Use:

  1)Download both model.py and thetypes.py, and place them in the same directory.
  
  2)In python, import both modules.
  
  3)To analyze individual pokemon weaknesses - (model.)singleWeakness(type1, type2):
  
    i)type1 and type2 are both strings representing valid pokemon types.  Type strings are case insensitive, and should be
      spelled out completely (i.e. fighting, not fight)
      
    ii)type1 is required, but type2 is optional (in the case of monotyped pokemon)
    
    iii)Common errors include not enclosing typestrings in quotes, and misspelling/inputting an incorrect type name.
    
  4)To analyze entire team weaknesses - (model.)teamWeakness():
  
    i)This function will lead to a prompt taking raw user input, so no arguments are required in the method call.
    
    ii)A prompt will come up, asking for either one or two type entries, which are case-insensitive and should NOT be
       enclosed in quotes.
       
    iii)Monotype pokemon - enter only a single valid type and hit <Return>.
    
    iV)Dualtype pokemon - separate each type by a single forwardslash /.
