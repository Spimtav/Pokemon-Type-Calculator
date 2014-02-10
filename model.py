# model.py
# Maximillian Tinati
# December 15, 2013
"""This module contains the model for the Pokemon type calculation app."""
from thetypes import *


#Useful constant: list containing all pokemon types as separate strings in lowercase.
TYPE_LIST = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting',
             'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost',
             'dragon', 'dark', 'steel', 'fairy']

TYPE_ATTACKS = ['normalAtk', 'fireAtk', 'waterAtk', 'electricAtk', 'grassAtk',
                'iceAtk', 'fightingAtk', 'poisonAtk', 'groundAtk', 'flyingAtk',
                'psychicAtk', 'bugAtk', 'rockAtk', 'ghostAtk', 'dragonAtk',
                'darkAtk', 'steelAtk', 'fairyAtk']

def valid_type(thetype):
    """Returns: True if <thetype> is a string representing a valid Pokemon type;
    False otherwise."""
    assert isinstance(thetype, str)
    
    thetype = thetype.lower()   #default string to a standard case for easy checking
    assert thetype in TYPE_LIST


def typeChecker(thetype):
        """Returns: a <Type> object corresponding to the specified Pokemon type
        <thetype>.
        
        Precondition:  <thetype> is a str and a valid Pokemon type."""
        assert isinstance(thetype, str)
        
        thetype = thetype.lower()
        
        if thetype == 'normal':
            return Normal()
        elif thetype == 'fire':
            return Fire()
        elif thetype == 'water':
            return Water()
        elif thetype == 'electric':
            return Electric()
        elif thetype == 'grass':
            return Grass()
        elif thetype == 'ice':
            return Ice()
        elif thetype == 'fighting':
            return Fighting()
        elif thetype == 'poison':
            return Poison()
        elif thetype == 'ground':
            return Ground()
        elif thetype == 'flying':
            return Flying()
        elif thetype == 'psychic':
            return Psychic()
        elif thetype == 'bug':
            return Bug()
        elif thetype == 'rock':
            return Rock()
        elif thetype == 'ghost':
            return Ghost()
        elif thetype == 'dragon':
            return Dragon()
        elif thetype == 'dark':
            return Dark()
        elif thetype == 'steel':
            return Steel()
        elif thetype == 'fairy':
            return Fairy()


def singleWeakness(type1, type2 = None):
    """Prints: a string corresponding to the weaknesses of the given type
    combination.  Values are PRINTED, not returned.
    
    Each line is a different type, and all type attacks are listed.
    
    Precondition: type1 and type2 are str representing valid Pokemon types."""
    #Asserting type1 and type2 are valid Pokemon types
    valid_type(type1)
    if type2 != None:
        valid_type(type2)
    
    pokemon = SingleModel(type1, type2)  #construct the summed type model for the 1-2 types
    
    #poketype is str of the format "Type1 / Type2" for easy displaying of data
    poketype = type1.upper()
    if type2 != None:
        poketype = poketype + " / " + type2.upper()
    
    print poketype
    print "Normal    " + str(pokemon.sumType.normalAtk)
    print "Fire:     " + str(pokemon.sumType.fireAtk)
    print "Water:    " + str(pokemon.sumType.waterAtk)
    print "Electric: " + str(pokemon.sumType.electricAtk)
    print "Grass:    " + str(pokemon.sumType.grassAtk)
    print "Ice:      " + str(pokemon.sumType.iceAtk)
    print "Fighting: " + str(pokemon.sumType.fightingAtk)
    print "Poison:   " + str(pokemon.sumType.poisonAtk)
    print "Ground:   " + str(pokemon.sumType.groundAtk)
    print "Flying:   " + str(pokemon.sumType.flyingAtk)
    print "Psychic:  " + str(pokemon.sumType.psychicAtk)
    print "Bug:      " + str(pokemon.sumType.bugAtk)
    print "Rock:     " + str(pokemon.sumType.rockAtk)
    print "Ghost:    " + str(pokemon.sumType.ghostAtk)
    print "Dragon:   " + str(pokemon.sumType.dragonAtk)
    print "Dark:     " + str(pokemon.sumType.darkAtk)
    print "Steel:    " + str(pokemon.sumType.steelAtk)
    print "Fairy:    " + str(pokemon.sumType.fairyAtk)


def teamWeakness():
    """Prints: a string corresponding to the weakness of an entire pokemon team
    given the typings of all 6 pokemon on the team.  Values are PRINTED, not
    returned.
    
    Each line is a different type, and all type attacks are listed."""
    
    team = TeamModel()  #construct type model for the entire pokemon team
    
    print "This team's overall weakness to incoming attacks is:"
    print "Normal    " + str(team.sumType.normalAtk)
    print "Fire:     " + str(team.sumType.fireAtk)
    print "Water:    " + str(team.sumType.waterAtk)
    print "Electric: " + str(team.sumType.electricAtk)
    print "Grass:    " + str(team.sumType.grassAtk)
    print "Ice:      " + str(team.sumType.iceAtk)
    print "Fighting: " + str(team.sumType.fightingAtk)
    print "Poison:   " + str(team.sumType.poisonAtk)
    print "Ground:   " + str(team.sumType.groundAtk)
    print "Flying:   " + str(team.sumType.flyingAtk)
    print "Psychic:  " + str(team.sumType.psychicAtk)
    print "Bug:      " + str(team.sumType.bugAtk)
    print "Rock:     " + str(team.sumType.rockAtk)
    print "Ghost:    " + str(team.sumType.ghostAtk)
    print "Dragon:   " + str(team.sumType.dragonAtk)
    print "Dark:     " + str(team.sumType.darkAtk)
    print "Steel:    " + str(team.sumType.steelAtk)
    print "Fairy:    " + str(team.sumType.fairyAtk)


class SingleModel(object):
    """An instance of this class models incoming attack effectiveness against
    A SINGLE defending pokemon, whose type(s) are chosen upon class construction.
    This model calls the appropriate single type classes from thetypes.py, and
    determines the overall effectiveness if the defending pokemon is dual-typed.
    
    Instance attributes:
        types:      a list containing the types of the pokemon to be analyzed
                    [list of 1-2 <Type> objects if any are selected, None otherwise]
        sumType:    a fictional pokemon type containing the effectiveness of
                    incoming attacks to both of the Pokemon's types
                    [a single <Type> object if types specified, None otherwise]"""
    
    def __init__(self, type1 = None, type2 = None):
        """Initializer: constructs an object of type <SingleModel> with all initial
        variable states corresponding to  the inputted Pokemon types.
        
        Precondition: type1 and type2 are strings and valid Pokemon types."""
        #assert valid_type(type1)
        #assert valid_type(type2)
        
        #Create appropriate Type classes if any and append to <types>
        self.types = []
        if type1 is not None:
            typeObj1 = typeChecker(type1)
            self.types.append(typeObj1)
        if type2 is not None:
            typeObj2 = typeChecker(type2)
            self.types.append(typeObj2)
        
        #Initialize sumType att using helper method b/c really long
        self.constructSumType()
    
    def constructSumType(self):
        """Method to handle initialization of the <sumType> attribute.
        Initially, <sumType> is None.  If <types> contains only a single type,
        then <sumType> will contain that particular Type obj.  If <types>
        contains 2 Type objs, then a dual-type Type obj is constructed and stored
        in <sumType>."""
        #Default to None
        self.sumType = None
        
        #If 1 type specified, set the sumType to this type
        if len(self.types) == 1:
            self.sumType = self.types[0]
        
        #If 2 types specified, construct artificial Type w/multiplied effectivenesses
        elif len(self.types) == 2:
            type1 = self.types[0]
            type2 = self.types[1]
            self.sumType = Type()
            
            self.sumType.normalAtk = type1.normalAtk * type2.normalAtk
            self.sumType.fireAtk = type1.fireAtk * type2.fireAtk
            self.sumType.waterAtk = type1.waterAtk * type2.waterAtk
            self.sumType.electricAtk = type1.electricAtk * type2.electricAtk
            self.sumType.grassAtk = type1.grassAtk * type2.grassAtk
            self.sumType.iceAtk = type1.iceAtk * type2.iceAtk
            self.sumType.fightingAtk = type1.fightingAtk * type2.fightingAtk
            self.sumType.poisonAtk = type1.poisonAtk * type2.poisonAtk
            self.sumType.groundAtk = type1.groundAtk * type2.groundAtk
            self.sumType.flyingAtk = type1.flyingAtk * type2.flyingAtk
            self.sumType.psychicAtk = type1.psychicAtk * type2.psychicAtk
            self.sumType.bugAtk = type1.bugAtk * type2.bugAtk
            self.sumType.rockAtk = type1.rockAtk * type2.rockAtk
            self.sumType.ghostAtk = type1.ghostAtk * type2.ghostAtk
            self.sumType.dragonAtk = type1.dragonAtk * type2.dragonAtk
            self.sumType.darkAtk = type1.darkAtk * type2.darkAtk
            self.sumType.steelAtk = type1.steelAtk * type2.steelAtk
            self.sumType.fairyAtk = type1.fairyAtk * type2.fairyAtk



class TeamModel(object):
    """An instance of this class models incoming attack effectiveness against
    an ENTIRE TEAM of 6 pokemon, whose 1-2 types are chosen by raw user input.
    This model first calls class <SingleModel> to get incoming attack effectiveness
    for each individual pokemon.  Then, the team attack effectiveness is calculated
    and displayed in the same way as <SingleModel>.
    
    Instance Attributes:
        types:          a 2d list containing team type info.  Each 2nd level list
                        contains an individual pokemon's typing.
                        [A 2-dimensional list of valid type strings if any selected;
                        blank list otherwise]
        singleModels:   A list of <SingleModel> objects whose individual 1-2
                        types correspond to the instance attribute <types>.
                        [A list of <SingleModel> objects; blank list otherwise]
        sumType:        A fictional pokemon type containing the effectiveness of
                        incoming attacks against the entire team's types.
                        [a single <Type> object]"""
    
    def __init__(self):
        """Initializer: constructs an object of type <TeamModel> with all initial
        variable states corresponding to raw inputted Pokemon types."""
        self.types = []
        self.singleModels = []
        self.sumType = Type()
        
        self.pokemon_input()  #handles construction of <types>
        self.construct_single_models() #handles construction of <singleModels>
        self.construct_sum_type() #handles construction of <sumType>
    
    def pokemon_input(self):
        """A function that uses raw user input to determine how many pokemon are
        going to be analyzed, and the types of these pokemon.  Function handles
        recognizing and appending input types to the typelist, but not the
        parsing of dual types and checking of type validity."""
        #Initialize loop variables, each one is a pokemon's typing
        #pokemonList needed to be able to iterate over all 6 in 1 loop
        poke1 = None
        poke2 = None
        poke3 = None
        poke4 = None
        poke5 = None
        poke6 = None
        pokemonList = [poke1, poke2, poke3, poke4, poke5, poke6]
        
        #Get input, parse types, check for correctness, and append to <types> att.
        for i in range(6):
            pokemonList[i] = raw_input("Pokemon " + str(i+1) + " (Type " +
                                       "or Type1/Type2): ")
            pokemonList[i] = self.type_parser(pokemonList[i])
            self.type_checker(pokemonList[i])
            self.types.append(pokemonList[i])
    
    def construct_single_models(self):
        """Constructs instances of class <SingleModel> for each pokemon/types
        in the instance attribute <types>. The type of each SingleModel is the
        1-2 types of an individual pokemon in <types>.  After each SingleModel
        object is created, it is appended to the instance attribute
        <singleModels>"""
        for i in self.types:
            if len(i) == 1:   #If monotype pokemon
                self.singleModels.append(SingleModel(i[0]))
            elif len(i) == 2: #If dualtype pokemon
                self.singleModels.append(SingleModel(i[0], i[1]))
    
    def construct_sum_type(self):
        """Method to handle construction of the instance attribute <sumType>,
        the artificial type containing the effectiveness of incoming attacks
        against the entire team of pokemon.  This is done by multiplying the
        type weakness attributes of all 6 SingleModel instances."""
        for pokemon in self.singleModels:
            self.sumType.normalAtk = self.sumType.normalAtk * pokemon.sumType.normalAtk
            self.sumType.fireAtk = self.sumType.fireAtk * pokemon.sumType.fireAtk
            self.sumType.waterAtk = self.sumType.waterAtk * pokemon.sumType.waterAtk
            self.sumType.electricAtk = self.sumType.electricAtk * pokemon.sumType.electricAtk
            self.sumType.grassAtk = self.sumType.grassAtk * pokemon.sumType.grassAtk
            self.sumType.iceAtk = self.sumType.iceAtk * pokemon.sumType.iceAtk
            self.sumType.fightingAtk = self.sumType.fightingAtk * pokemon.sumType.fightingAtk
            self.sumType.poisonAtk = self.sumType.poisonAtk * pokemon.sumType.poisonAtk
            self.sumType.groundAtk = self.sumType.groundAtk * pokemon.sumType.groundAtk
            self.sumType.flyingAtk = self.sumType.flyingAtk * pokemon.sumType.flyingAtk
            self.sumType.psychicAtk = self.sumType.psychicAtk * pokemon.sumType.psychicAtk
            self.sumType.bugAtk = self.sumType.bugAtk * pokemon.sumType.bugAtk
            self.sumType.rockAtk = self.sumType.rockAtk * pokemon.sumType.rockAtk
            self.sumType.ghostAtk = self.sumType.ghostAtk * pokemon.sumType.ghostAtk
            self.sumType.dragonAtk = self.sumType.dragonAtk * pokemon.sumType.dragonAtk
            self.sumType.darkAtk = self.sumType.darkAtk * pokemon.sumType.darkAtk
            self.sumType.steelAtk = self.sumType.steelAtk * pokemon.sumType.steelAtk
            self.sumType.fairyAtk = self.sumType.fairyAtk * pokemon.sumType.fairyAtk
    
    def type_parser(self, typeString):
        """A function that parses user-inputted pokemon types.  If a single type
        is inputted, then it is returned as a list of a single string (the type).
        A dual-type string of the format "Type1/Type2" is split into its two
        individual pokemon types.  Then, the function returns the two types
        as strings in a list of length 2.
        
        Precondition:  typeString is a string.  If it corresponds to a dual-type
        pokemon, it should be of the format "Type1/Type2"."""
        assert isinstance(typeString, str)
        
        #If dual-typed, returns each type as a string in a list of length 2
        if "/" in typeString:
            divider = typeString.index("/")
            leftSide = typeString[:divider].strip()
            rightSide = typeString[divider + 1:].strip()
            return [leftSide, rightSide]
        
        #If singly typed, returns type as a string in a list of of length 1
        else:
            #print "in type_parser else"
            return [typeString]
    
    def type_checker(self, pokemon):
        """Function that determines whether or not the types in <pokemon> are
        valid types.  This function calls <valid_type> to determine type
        validity.  This function also serves to check that raw input and parsing
        were done correctly, by verifying that <pokemon> is a list of 1-2 strings.
        
        Precondition: pokemon is a list of 2 strings."""
        assert isinstance(pokemon, list)
        for i in pokemon:
            assert isinstance(i, str)
        assert len(pokemon) == 1 or len(pokemon) == 2
        
        for i in pokemon:
            valid_type(i)
