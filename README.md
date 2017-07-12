# PrimeTones
Generates synth tones using the first billion prime numbers  
  
Creates audio by plotting the difference between the approximate linear slope of y = P(n) || y = the nth prime number and the actual value at that location (currently does not output audio)
It then multiplies the difference by a sine wave to produce a synth like tone.

# TODO
Using the wav library, make it output audio instead of a graph  
Allow the user to input their own linear approximations for different tones  
Some sort of MIDI intigration to hear the tones in context
