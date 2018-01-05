# -*- coding: utf-8 -*-
# Roman Numeral Converter
vinculum = "̅" # unicode "combining overline"
places = [
    ["I", "V", "X"],
    ["X", "L", "C"],
    ["C", "D", "M"],
    ["M", "V"+vinculum, "X"+vinculum],
    ["X"+vinculum, "L"+vinculum, "C"+vinculum],
    ["C"+vinculum, "D"+vinculum, "M"+vinculum],
    ["M"+vinculum]
]
digits = [
    "",
    "{0[0]}",
    "{0[0]}{0[0]}",
    "{0[0]}{0[0]}{0[0]}",
    "{0[0]}{0[1]}",
    "{0[1]}",
    "{0[1]}{0[0]}",
    "{0[1]}{0[0]}{0[0]}",
    "{0[1]}{0[0]}{0[0]}{0[0]}",
    "{0[0]}{0[2]}"
]
def decToRom(n):
    if n >= 4000000: return "unreasonably large" # I mean, probably
    dec, rom = list(str(n)), ""
    for i in range(len(dec)):
        rom += digits[int(dec[i])].format(places[len(dec)-i-1]) # stick the letters in the places list in place of the placeholders in the digits list
    return rom
values = {
    "": 0,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "I_": 1000,
    "V_": 5000,
    "X_": 10000,
    "L_": 50000,
    "C_": 100000,
    "D_": 500000,
    "M_": 1000000
}
from numpy import copysign
from re import compile
isRoman = compile("[ivxlcdmIVXLCDM_]+") # This matches some things that aren't quite valid roman numerals, but the conversions should still make some sense
def romToDec(n): # n is a string here, which is weird, but that's how the Romans did it
    rom = list(n.upper())
    withVinc = [rom[i]+"_" if (rom+[""])[i+1]=="_" else rom[i] for i in range(len(rom)) if rom[i] != "_"] # put the underscores and preceding letters together: ["I", "_"] becomes ["I_"]
    dec = int(sum([values[x]*copysign(1, values[x]-values[(withVinc+[""])[i+1]]) for i, x in enumerate(withVinc) if x in values.keys()])) # add together the list of letters by substituting their values, and making them negative if they're smaller than the ones after them. (And make it an integer, because the type changed to a numpy float or something like that when you used copysign().) 
    return dec
def converter():
    toConvert = raw_input("Input number: ")
    if unicode(toConvert, "utf-8").isnumeric():
        print "In the Roman numeral system, this number is {}.".format(decToRom(int(toConvert)))
    elif  isRoman.match(toConvert):
        print "In the Arabic numeral system, this number is {}.".format(romToDec(toConvert))
    else:
        print "...What kind of numeral system is that?"
    if "Y" in raw_input("Convert another number? ").upper(): converter()
print """Roman and Arabic Numerals Convertor
Input a number (with either numeral system) to see the equivalent number in the other system. You can use an underscore (_) to indicate a vinculum for the Roman system. """
converter()