from functools import partial
from _Framework.Util import group

from Ubermap import UbermapDevices
ubermap = UbermapDevices.UbermapDevices()

""" 
Ubermap alpha v0.1: modified devices.py 
---------------------------------------
This file has been modified from the version edited by Stray on 10/26/13 to allow 
easy mapping of plugins, using custom configuration files. It also contains the
Live Community Mapping, which enhances the original mappings for Ableton's devices
(https://forum.ableton.com/viewtopic.php?f=55&t=198946&p=1562395#p1562395).

All modified variables and functions are prefixed with ubermap.

For more information, see http://github.com/tomduncalf/ubermap

Much credit due to Stray, TomViolenz and any others who figured out how to modify
mappings using this file in the first place.
---------------------------------------

Enjoy :)
Tom
"""

RCK_BANK1 = ('Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7', 'Macro 8')
RCK_BANKS = (RCK_BANK1,)
RCK_BOBS = (RCK_BANK1,)
RCK_BNK_NAMES = ('Macros',)
ALG_BANK1 = ('OSC1 Level', 'OSC1 Octave', 'OSC1 Semi', 'OSC1 Detune', 'OSC1 Shape', 'OSC1 Balance', 'PEG1 Amount', 'PEG1 Time')
ALG_BANK2 = ('F1 Type', 'F1 Freq', 'F1 Resonance', 'F1 To F2', 'FEG1 Attack', 'FEG1 Decay', 'FEG1 Sustain', 'FEG1 Rel')
ALG_BANK3 = ('AMP1 Level', 'AMP1 Pan', 'AEG1 S Time', 'AEG1 Loop', 'AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel')
ALG_BANK4 = ('LFO1 Shape', 'LFO1 Sync', 'LFO1 SncRate', 'LFO1 Speed', 'LFO1 PW', 'LFO1 Phase', 'LFO1 Delay', 'LFO1 Fade In')
ALG_BANK5 = ('OSC2 Level', 'OSC2 Octave', 'OSC2 Semi', 'OSC2 Detune', 'OSC2 Shape', 'OSC2 Balance', 'PEG2 Amount', 'PEG2 Time')
ALG_BANK6 = ('F2 Type', 'F2 Freq', 'F2 Resonance', 'F2 Slave', 'FEG2 Attack', 'FEG2 Decay', 'FEG2 Sustain', 'FEG2 Rel')
ALG_BANK7 = ('AMP2 Level', 'AMP2 Pan', 'AEG2 S Time', 'AEG2 Loop', 'AEG2 Attack', 'AEG2 Decay', 'AEG2 Sustain', 'AEG2 Rel')
ALG_BANK8 = ('LFO2 Shape', 'LFO2 Sync', 'LFO2 SncRate', 'LFO2 Speed', 'LFO2 PW', 'LFO2 Phase', 'LFO2 Delay', 'LFO2 Fade In')
ALG_BANK9 = ('OSC1 < LFO', 'OSC1 PW', 'O1 PW < LFO', 'LFO1 On/Off', 'F1 Freq < LFO', 'F1 Res < LFO', 'A1 Pan < LFO', 'AMP1 < LFO')
ALG_BANK10 = ('OSC2 < LFO', 'OSC2 PW', 'O2 PW < LFO', 'LFO2 On/Off', 'F2 Freq < LFO', 'F2 Res < LFO', 'A2 Pan < LFO', 'AMP2 < LFO')
ALG_BANK11 = ('Noise On/Off', 'Noise Level', 'Noise Balance', 'Noise Color', 'O1 Sub/Sync', 'O2 Sub/Sync', 'F1 Drive', 'F2 Drive')
ALG_BANK12 = ('Vib On/Off', 'Vib Amount', 'Vib Speed', 'Vib Delay', 'Vib Error', 'Vib Fade-In', 'Vib < ModWh', 'Volume')
ALG_BANK13 = ('Unison On/Off', 'Unison Detune', 'Unison Delay', 'Unison Voices', 'Glide On/Off', 'Glide Time', 'Glide Legato', 'Glide Mode')
ALG_BANK14 = ('Noise On/Off', 'OSC2 On/Off', 'F1 On/Off', 'F2 On/Off', 'AMP1 On/Off', 'AMP2 On/Off', 'LFO1 On/Off', 'LFO2 On/Off')
ALG_BANK15 = ('FEG1 Attack', 'FEG1 Decay', 'FEG1 Sustain', 'FEG1 Rel', 'FEG2 Attack', 'FEG2 Decay', 'FEG2 Sustain', 'FEG2 Rel')
ALG_BANK16 = ('AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel', 'AEG2 Attack', 'AEG2 Decay', 'AEG2 Sustain', 'AEG2 Rel')
ALG_BANK17 = ('LFO1 SncRate', 'LFO1 Speed', 'LFO1 Fade In', 'LFO1 Phase', 'LFO2 SncRate', 'LFO2 Speed', 'LFO2 Fade In', 'LFO2 Phase')
ALG_BANK18 = ('PEG1 Amount', 'PEG1 Time', 'OSC1 Semi', 'OSC1 Level', 'PEG2 Amount', 'PEG2 Time', 'OSC2 Semi', 'OSC2 Level')
ALG_BOB = ('OSC1 Level', 'OSC1 Semi', 'OSC1 Balance', 'F1 Freq', 'OSC2 Level', 'OSC2 Semi', 'OSC2 Balance', 'F2 Freq')
ALG_BANKS = (ALG_BANK1,
ALG_BANK2,
ALG_BANK3,
ALG_BANK4,
ALG_BANK5,
ALG_BANK6,
ALG_BANK7,
ALG_BANK8,
ALG_BANK9,
ALG_BANK10,
ALG_BANK11,
ALG_BANK12,
ALG_BANK13,
ALG_BANK14,
ALG_BANK15,
ALG_BANK16,
ALG_BANK17,
ALG_BANK18)
ALG_BOBS = (ALG_BOB,)
ALG_BNK_NAMES = ('Osc1', 'Filter1', 'Amp1', 'LFO1', 'Osc2', 'Filter2', 'Amp2', 'LFO2', 'LFO1Rout', 'LFO2Rout', 'NsSubDrv', 'Vibrato', 'UniGlide', 'ON', '2FiltEnv.', '2AmpEnv.', '2LFOs', '2Osc')
COL_BANK1 = ('Mallet Volume', 'Mallet Volume < Key', 'Mallet Volume < Vel', 'Mallet Noise Amount', 'Mallet Noise Amount < Key', 'Mallet Noise Amount < Vel', 'Mallet Stiffness', 'Mallet Noise Color')
COL_BANK2 = ('Noise Volume', 'Noise Filter Type', 'Noise Filter Freq', 'Noise Filter Q', 'Noise Attack', 'Noise Decay', 'Noise Sustain', 'Noise Release')
COL_BANK3 = ('Res 1 On/Off', 'Res 1 Tune', 'Res 1 Fine Tune', 'Res 1 Pitch Env.', 'Res 1 Pitch Env. Time', 'Res 1 Bleed', 'Panorama', 'Res 1 Volume')
COL_BANK4 = ('Res 2 On/Off', 'Res 2 Tune', 'Res 2 Fine Tune', 'Res 2 Pitch Env.', 'Res 2 Pitch Env. Time', 'Res 2 Bleed', 'Panorama', 'Res 2 Volume')
COL_BANK5 = ('Res 1 Type', 'Res 1 Ratio', 'Res 1 Brightness', 'Res 1 Opening', 'Res 1 Inharmonics', 'Res 1 Listening L', 'Res 1 Listening R', 'Res 1 Hit')
COL_BANK6 = ('Res 2 Type', 'Res 2 Ratio', 'Res 2 Brightness', 'Res 2 Opening', 'Res 2 Inharmonics', 'Res 2 Listening L', 'Res 2 Listening R', 'Res 2 Hit')
COL_BANK7 = ('Res 1 Decay', 'Res 1 Radius', 'Res 1 Material', 'Res 1 Quality', 'Res 2 Decay', 'Res 2 Material', 'Res 2 Radius', 'Res 2 Quality')
COL_BANK8 = ('LFO 1 Shape', 'LFO 1 Sync', 'LFO 1 Sync Rate', 'LFO 1 Rate', 'LFO 1 Destination A', 'LFO 1 Destination A Amount', 'LFO 1 Destination B', 'LFO 1 Destination B Amount')
COL_BANK9 = ('LFO 2 Shape', 'LFO 2 Sync', 'LFO 2 Sync Rate', 'LFO 2 Rate', 'LFO 2 Destination A', 'LFO 2 Destination A Amount', 'LFO 2 Destination B', 'LFO 2 Destination B Amount')
COL_BANK10 = ('Mallet Volume', 'Mallet Noise Amount', 'Noise Volume', 'Res 1 Volume', 'Res 2 Volume', 'Structure', 'Voices', 'Volume')
COL_BANK11 = ('PB Destination A', 'PB Destination A Amount', 'MW Destination A', 'MW Destination A Amount', 'AT Destination A', 'AT Destination A Amount', 'AT Destination B', 'AT Destination B Amount')
COL_BANK12 = ('Mallet Volume < Vel', 'Mallet Stiffness < Vel', 'Mallet Noise Amount < Vel', 'Noise Volume < Vel', 'Noise Freq < Vel', '', '', '')
COL_BANK13 = ('Res 1 Pitch Env. < Vel', 'Res 1 Decay < Vel', 'Res 1 Material < Vel', 'Res 1 Radius < Vel', 'Res 1 Inharmonics < Vel', 'Res 1 Opening < Vel', '', '')
COL_BANK14 = ('Res 2 Pitch Env. < Vel', 'Res 2 Decay < Vel', 'Res 2 Material < Vel', 'Res 2 Radius < Vel', 'Res 2 Inharmonics < Vel', 'Res 2 Opening < Vel', '', '')
COL_BOB = ('Res 1 Brightness', 'Res 1 Type', 'Mallet Stiffness', 'Mallet Noise Amount', 'Res 1 Inharmonics', 'Res 1 Decay', 'Res 1 Tune', 'Volume')
COL_BANKS = (COL_BANK1,
COL_BANK2,
COL_BANK3,
COL_BANK4,
COL_BANK5,
COL_BANK6,
COL_BANK7,
COL_BANK8,
COL_BANK9,
COL_BANK10,
COL_BANK11,
COL_BANK12,
COL_BANK13,
COL_BANK14)
COL_BOBS = (COL_BOB,)
COL_BNK_NAMES = ('Mallet', 'Noise', 'Res1 Pitch/Mix', 'Res2 Pitch/Mix', 'Res1 Material', 'Res2 Material', 'Res1+2 Decay/Quality', 'LFO 1', 'LFO 2', 'All Vol/Global', 'PB/MW/AT', 'Ml/Ns Vel', 'Res1 Vel', 'Res2 Vel')
ELC_BANK1 = ('M Stiffness', 'M Stiff < Vel', 'M Force', 'M Force < Vel', 'Noise Pitch', 'Noise Decay', 'Noise Amount', 'Noise < Key')
ELC_BANK2 = ('F Tine Color', 'F Tine Decay', 'F Tine Vol', 'F Tine < Key', 'F Tone Decay', 'F Release', 'F Tone Vol', 'Volume')
ELC_BANK3 = ('Damp Tone', 'Damp Balance', 'Damp Amount', 'P Symmetry', 'P Amp In', 'P Distance', 'P Amp Out', 'P Amp < Key')
ELC_BANK4 = ('Voices', 'Semitone', 'Detune', 'KB Stretch', 'PB Range', 'M Stiff < Key', 'M Force < Key', 'Volume')
ELC_BANK5 = ('Noise Amount', 'F Tine Vol', 'F Tone Vol', 'Damp Amount', 'P Amp In', 'P Amp Out', '', 'Volume')
ELC_BOB = ('M Stiffness', 'M Force', 'Noise Amount', 'F Tine Vol', 'F Tone Vol', 'F Release', 'P Symmetry', 'Volume')
ELC_BANKS = (ELC_BANK1,
ELC_BANK2,
ELC_BANK3,
ELC_BANK4,
ELC_BANK5)
ELC_BOBS = (ELC_BOB,)
ELC_BNK_NAMES = ('Mallet', 'TineTone', 'DampPick', 'Global', 'AllLevel')
IMP_BANK1 = ('1 Start', '1 Transpose', '1 Stretch Factor', '1 Saturator Drive', '1 Filter Freq', '1 Filter Res', '1 Pan', '1 Volume')
IMP_BANK2 = ('2 Start', '2 Transpose', '2 Stretch Factor', '2 Saturator Drive', '2 Filter Freq', '2 Filter Res', '2 Pan', '2 Volume')
IMP_BANK3 = ('3 Start', '3 Transpose', '3 Stretch Factor', '3 Saturator Drive', '3 Filter Freq', '3 Filter Res', '3 Pan', '3 Volume')
IMP_BANK4 = ('4 Start', '4 Transpose', '4 Stretch Factor', '4 Saturator Drive', '4 Filter Freq', '4 Filter Res', '4 Pan', '4 Volume')
IMP_BANK5 = ('5 Start', '5 Transpose', '5 Stretch Factor', '5 Saturator Drive', '5 Filter Freq', '5 Filter Res', '5 Pan', '5 Volume')
IMP_BANK6 = ('6 Start', '6 Transpose', '6 Stretch Factor', '6 Saturator Drive', '6 Filter Freq', '6 Filter Res', '6 Pan', '6 Volume')
IMP_BANK7 = ('7 Start', '7 Transpose', '7 Stretch Factor', '7 Saturator Drive', '7 Filter Freq', '7 Filter Res', '7 Pan', '7 Volume')
IMP_BANK8 = ('8 Start', '8 Transpose', '8 Stretch Factor', '8 Saturator Drive', '8 Filter Freq', '8 Filter Res', '8 Pan', '8 Volume')
IMP_BANK9 = ('1 Transpose <- Vel', '1 Transpose <- Random', '1 Stretch <- Vel', '1 Filter <- Vel', '1 Filter <- Random', '1 Pan <- Vel', '1 Pan <- Random', '1 Volume <- Vel')
IMP_BANK10 = ('2 Transpose <- Vel', '2 Transpose <- Random', '2 Stretch <- Vel', '2 Filter <- Vel', '2 Filter <- Random', '2 Pan <- Vel', '2 Pan <- Random', '2 Volume <- Vel')
IMP_BANK11 = ('3 Transpose <- Vel', '3 Transpose <- Random', '3 Stretch <- Vel', '3 Filter <- Vel', '3 Filter <- Random', '3 Pan <- Vel', '3 Pan <- Random', '3 Volume <- Vel')
IMP_BANK12 = ('4 Transpose <- Vel', '4 Transpose <- Random', '4 Stretch <- Vel', '4 Filter <- Vel', '4 Filter <- Random', '4 Pan <- Vel', '4 Pan <- Random', '4 Volume <- Vel')
IMP_BANK13 = ('5 Transpose <- Vel', '5 Transpose <- Random', '5 Stretch <- Vel', '5 Filter <- Vel', '5 Filter <- Random', '5 Pan <- Vel', '5 Pan <- Random', '5 Volume <- Vel')
IMP_BANK14 = ('6 Transpose <- Vel', '6 Transpose <- Random', '6 Stretch <- Vel', '6 Filter <- Vel', '6 Filter <- Random', '6 Pan <- Vel', '6 Pan <- Random', '6 Volume <- Vel')
IMP_BANK15 = ('7 Transpose <- Vel', '7 Transpose <- Random', '7 Stretch <- Vel', '7 Filter <- Vel', '7 Filter <- Random', '7 Pan <- Vel', '7 Pan <- Random', '7 Volume <- Vel')
IMP_BANK16 = ('8 Transpose <- Vel', '8 Transpose <- Random', '8 Stretch <- Vel', '8 Filter <- Vel', '8 Filter <- Random', '8 Pan <- Vel', '8 Pan <- Random', '8 Volume <- Vel')
IMP_BOB = ('Global Time', 'Global Transpose', '1 Transpose', '2 Transpose', '3 Transpose', '4 Transpose', '5 Transpose', '6 Transpose')
IMP_BANKS = (IMP_BANK1,
IMP_BANK2,
IMP_BANK3,
IMP_BANK4,
IMP_BANK5,
IMP_BANK6,
IMP_BANK7,
IMP_BANK8,
IMP_BANK9,
IMP_BANK10,
IMP_BANK11,
IMP_BANK12,
IMP_BANK13,
IMP_BANK14,
IMP_BANK15,
IMP_BANK16)
IMP_BOBS = (IMP_BOB,)
IMP_BNK_NAMES = ('Pad 1', 'Pad 2', 'Pad 3', 'Pad 4', 'Pad 5', 'Pad 6', 'Pad 7', 'Pad 8', 'Pad1Rand', 'Pad2Rand', 'Pad3Rand', 'Pad4Rand', 'Pad5Rand', 'Pad6Rand', 'Pad7Rand', 'Pad8Rand')
OPR_BANK1 = ('A Fix Freq', 'A Fix Freq Mul', 'A Coarse', 'A Fine', 'A Fix On ', 'Osc-A On', 'Osc-A Wave', 'Osc-A Level')
OPR_BANK2 = ('Ae Mode', 'Osc-A Phase', 'Ae Init', 'Ae Peak', 'Ae Attack', 'Ae Decay', 'Ae Sustain', 'Ae Release')
OPR_BANK3 = ('B Fix Freq', 'B Fix Freq Mul', 'B Coarse', 'B Fine', 'B Fix On ', 'Osc-B On', 'Osc-B Wave', 'Osc-B Level')
OPR_BANK4 = ('Be Mode', 'Osc-B Phase', 'Be Init', 'Be Peak', 'Be Attack', 'Be Decay', 'Be Sustain', 'Be Release')
OPR_BANK5 = ('C Fix Freq', 'C Fix Freq Mul', 'C Coarse', 'C Fine', 'C Fix On ', 'Osc-C On', 'Osc-C Wave', 'Osc-C Level')
OPR_BANK6 = ('Ce Mode', 'Osc-C Phase', 'Ce Init', 'Ce Peak', 'Ce Attack', 'Ce Decay', 'Ce Sustain', 'Ce Release')
OPR_BANK7 = ('D Fix Freq', 'D Fix Freq Mul', 'D Coarse', 'D Fine', 'D Fix On ', 'Osc-D On', 'Osc-D Wave', 'Osc-D Level')
OPR_BANK8 = ('De Mode', 'Osc-D Phase', 'De Init', 'De Peak', 'De Attack', 'De Decay', 'De Sustain', 'De Release')
OPR_BANK9 = ('Filter On', 'Filter Type', 'Filter Freq', 'Filter Res', 'Shaper Type', 'Shaper Amt', 'Fe Amount', 'Filt < LFO')
OPR_BANK10 = ('Fe Mode', 'Fe End', 'Fe Init', 'Fe Peak', 'Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release')
OPR_BANK11 = ('Pe Amount', 'Pe End', 'Pe Init', 'Pe Peak', 'Pe Attack', 'Pe Decay', 'Pe Sustain', 'Pe Release')
OPR_BANK12 = ('Osc-A < Pe', 'Osc-B < Pe', 'Osc-C < Pe', 'Osc-D < Pe', 'LFO < Pe', 'Pe Amt A', 'Pe Dst B', 'Pe Amt B')
OPR_BANK13 = ('LFO On', 'LFO Type', 'LFO Range', 'LFO Sync', 'LFO Rate', 'LFO Amt', 'LFO Retrigger', 'LFO < Vel')
OPR_BANK14 = ('Le Mode', 'Le End', 'Le Init', 'Le Peak', 'Le Attack', 'Le Decay', 'Le Sustain', 'Le Release')
OPR_BANK15 = ('Osc-A < LFO', 'Osc-B < LFO', 'Osc-C < LFO', 'Osc-D < LFO', 'Filt < LFO', 'LFO Amt A', 'LFO Dst B', 'LFO Amt B')
OPR_BANK16 = ('Ae Loop', 'Ae Retrig', 'Fe Loop', 'Fe Retrig', 'Pe Loop', 'Pe Retrig', 'Le Loop', 'Le Retrig')
OPR_BANK17 = ('Glide On', 'Glide Time', 'Spread', 'Transpose', 'Algorithm', 'Time', 'Tone', 'Volume')
OPR_BANK18 = ('Ae Decay', 'Be Decay', 'Ce Decay', 'De Decay', 'Fe Decay', 'Pe Decay', 'Le Decay', '')
OPR_BANK19 = ('Ae Attack', 'Be Attack', 'Ce Attack', 'De Attack', 'Fe Attack', 'Pe Attack', 'Le Attack', '')
OPR_BANK20 = ('Ae Sustain', 'Be Sustain', 'Ce Sustain', 'De Sustain', 'Fe Sustain', 'Pe Sustain', 'Le Sustain', '')
OPR_BANK21 = ('Ae Release', 'Be Release', 'Ce Release', 'De Release', 'Fe Release', 'Pe Release', 'Le Release', '')
OPR_BANK22 = ('A Coarse', 'A Fine', 'B Coarse', 'B Fine', 'C Coarse', 'C Fine', 'D Coarse', 'D Fine')
OPR_BANK23 = ('A Fix Freq', 'A Fix Freq Mul', 'B Fix Freq', 'B Fix Freq Mul', 'C Fix Freq', 'C Fix Freq Mul', 'D Fix Freq', 'D Fix Freq Mul')
OPR_BANK24 = ('Osc-A Level', 'Osc-A Wave', 'Osc-B Level', 'Osc-B Wave', 'Osc-C Level', 'Osc-C Wave', 'Osc-D Level', 'Osc-D Wave')
OPR_BANK25 = ('Osc-A Feedb', 'Osc-A Phase', 'Osc-B Feedb', 'Osc-B Phase', 'Osc-C Feedb', 'Osc-C Phase', 'Osc-D Feedb', 'Osc-D Phase')
OPR_BOB = ('LFO Amt', 'Filter Freq', 'Fe Amount', 'Pe Amount', 'Algorithm', 'Transpose', 'Time', 'Volume')
OPR_BANKS = (OPR_BANK1,
OPR_BANK2,
OPR_BANK3,
OPR_BANK4,
OPR_BANK5,
OPR_BANK6,
OPR_BANK7,
OPR_BANK8,
OPR_BANK9,
OPR_BANK10,
OPR_BANK11,
OPR_BANK12,
OPR_BANK13,
OPR_BANK14,
OPR_BANK15,
OPR_BANK16,
OPR_BANK17,
OPR_BANK19,
OPR_BANK18,
OPR_BANK20,
OPR_BANK21,
OPR_BANK22,
OPR_BANK23,
OPR_BANK24,
OPR_BANK25)
OPR_BOBS = (OPR_BOB,)
OPR_BNK_NAMES = ('OscA', 'OscA Env', 'OscB', 'OscB Env', 'OscC', 'OscC Env', 'OscD', 'OscD Env', 'Filter', 'FiltEnv', 'PitchEnv', 'PtchDest', 'LFO', 'LFO Env', 'LFO Dest', 'EnvLoop', 'Misc', 'All Att', 'All Dec', 'All Sust', 'All Rel', 'CrseFine', 'FreqMult', 'LevPhase', 'FB/Phase')
SAM_BANK1 = ('Spread', 'Transpose', 'Detune', 'Glide Time', 'Pe < Env', 'Pe Mode', 'Pe Loop', 'Pe Retrig')
SAM_BANK2 = ('Pe Retrig', 'Pe End', 'Pe Init', 'Pe Peak', 'Pe Attack', 'Pe Decay', 'Pe Sustain', 'Pe Release')
SAM_BANK3 = ('O Type', 'O Volume', 'O Mode', 'O Fix On', 'O Coarse', 'O Fine', 'O Fix Freq', 'O Fix Freq Mul')
SAM_BANK4 = ('Oe Mode', 'Oe End', 'Oe Init', 'Oe Peak', 'Oe Attack', 'Oe Decay', 'Oe Sustain', 'Oe Release')
SAM_BANK5 = ('Filter Type', 'Filter Freq', 'Filter Res', 'Filter Morph', 'Shaper On', 'Shaper Pre-Filter', 'Shaper Type', 'Shaper Amt')
SAM_BANK6 = ('Fe < Env', 'Fe End', 'Fe Init', 'Fe Peak', 'Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release')
SAM_BANK7 = ('Ve Retrig', 'Ve Loop', 'Ve Init', 'Ve Peak', 'Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release')
SAM_BANK8 = ('Ae On', 'Ae End', 'Ae Init', 'Ae Peak', 'Ae Attack', 'Ae Decay', 'Ae Sustain', 'Ae Release')
SAM_BANK9 = ('L 1 On', 'L 1 Sync', 'L 1 Sync Rate', 'L 1 Rate', 'L 1 Attack', 'L 1 Retrig', 'L 1 Offset', 'L 1 Wave')
SAM_BANK10 = ('L 1 Wave', 'L 1 Sync', 'L 1 Sync Rate', 'L 1 Rate', 'Vol < LFO', 'Pan < LFO', 'Filt < LFO', 'Pitch < LFO')
SAM_BANK11 = ('L 2 On', 'L 2 Sync', 'L 2 Sync Rate', 'L 2 Rate', 'L 2 Attack', 'L 2 Retrig', 'L 2 Offset', 'L 2 Wave')
SAM_BANK12 = ('L 3 On', 'L 3 Sync', 'L 3 Sync Rate', 'L 3 Rate', 'L 3 Attack', 'L 3 Retrig', 'L 3 Offset', 'L 3 Wave')
SAM_BANK13 = ('L 2 St Mode', 'L 2 Phase', 'L 2 Spin', 'L 2 Width', 'L 3 St Mode', 'L 3 Phase', 'L 3 Spin', 'L 3 Width')
SAM_BANK14 = ('Oe Mode', 'Oe Retrig', 'Oe Loop', 'Ae Mode', 'Ae Retrig', 'Pe Mode', 'Pe Retrig', 'Pe Loop')
SAM_BANK15 = ('Fe Mode', 'Fe Retrig', 'Fe Loop', 'Ae Mode', 'Ae Loop', 'Ve Mode', 'Ve Retrig', 'Ve Loop')
SAM_BANK16 = ('Osc On', 'Pe On', 'F On', 'Fe On', 'Ae On', 'L 1 On', 'L 2 On', 'L 3 On')
SAM_BANK17 = ('Oe Attack', 'Oe Decay', 'Pe Attack', 'Pe Decay', 'Fe Attack', 'Fe Decay', 'Ve Attack', 'Ve Decay')
SAM_BANK18 = ('Oe Sustain', 'Oe Release', 'Pe Sustain', 'Pe Release', 'Fe Sustain', 'Fe Release', 'Ve Sustain', 'Ve Release')
SAM_BANK19 = ('L 1 Sync Rate', 'L 1 Rate', 'L 2 Sync Rate', 'L 2 Rate', 'L 3 Sync Rate', 'L 3 Rate', 'L 2 Phase', 'L 3 Phase')
SAM_BANK20 = ('L 1 Attack', 'L 1 Offset', 'L 2 Attack', 'L 2 Offset', 'L 3 Attack', 'L 3 Offset', 'L 2 Spin', 'L 3 Spin')
SAM_BOB = ('Volume', 'Sample Selector', 'Ve Init', 'Ve Peak', 'Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release')
SAM_BANKS = (SAM_BANK1,
SAM_BANK2,
SAM_BANK3,
SAM_BANK4,
SAM_BANK5,
SAM_BANK6,
SAM_BANK7,
SAM_BANK8,
SAM_BANK9,
SAM_BANK10,
SAM_BANK11,
SAM_BANK12,
SAM_BANK13,
SAM_BANK14,
SAM_BANK15,
SAM_BANK16,
SAM_BANK17,
SAM_BANK18,
SAM_BANK19,
SAM_BANK20)
SAM_BOBS = (SAM_BOB,)
SAM_BNK_NAMES = ('Pitch', 'PitchEnv', 'Osc', 'Osc Env', 'Filter', 'FiltEnv', 'VolEnv.', 'Aux Env.', 'LFO 1', 'LFO1Rout', 'LFO 2', 'LFO 3', 'LFO2/3St', 'LpOeAePe', 'LpFeAeVe', 'ON', 'AttDec', 'SustRel', 'LFORates', 'LFOAttOf')
SIM_BANK1 = ('S Start', 'S Loop Length', 'S Length', 'S Loop Fade', 'S Loop On', 'Snap', 'Pan', 'Volume')
SIM_BANK2 = ('Volume', 'Pan', 'Pan < Rnd', 'Vol < Vel', 'Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release')
SIM_BANK3 = ('Filter Type', 'Filter Freq', 'Filter Res', 'Fe < Env', 'Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release')
SIM_BANK4 = ('Transpose', 'Detune', 'Spread', 'Pe < Env', 'Pe Attack', 'Pe Decay', 'Pe Sustain', 'Pe Release')
SIM_BANK5 = ('L On', 'L Sync', 'L Sync Rate', 'L Rate', 'L Attack', 'L R < Key', 'L Offset', 'L Wave')
SIM_BANK6 = ('Glide Mode', 'Glide Time', 'Vol < Vel', 'Filt < Vel', 'Vol < LFO', 'Pan < LFO', 'Filt < LFO', 'Pitch < LFO')
SIM_BOB = ('Filter Freq', 'Filter Res', 'S Start', 'S Length', 'Ve Attack', 'Ve Release', 'Transpose', 'Volume')
SIM_BANKS = (SIM_BANK1,
SIM_BANK2,
SIM_BANK3,
SIM_BANK4,
SIM_BANK5,
SIM_BANK6)
SIM_BOBS = (SIM_BOB,)
SIM_BNK_NAMES = ('Loop', 'Volume', 'Filter', 'Pitch', 'LFO', 'LFORout')
TNS_BANK1 = ('Exc On/Off', 'Excitator Type', 'Exc Force', 'Exc Friction', 'Exc Velocity', 'E Pos', 'Exc Damping', 'E Pos Abs')
TNS_BANK2 = ('Damper On', 'Damper Gated', 'Damper Mass', 'D Stiffness', 'D Velocity', 'Damp Pos', 'D Damping', 'D Pos Abs')
TNS_BANK3 = ('Term On/Off', 'T Mass < Vel', 'T Mass < Key', 'Term Mass', 'Term Fng Stiff', 'Term Fret Stiff', '', 'Volume')
TNS_BANK4 = ('Body On/Off', 'Body Type', 'Body Size', 'Body Decay', 'Body Low-Cut', 'Body High-Cut', 'Body Mix', 'Volume')
TNS_BANK5 = ('String Decay', 'S Decay < Key', 'S Decay Ratio', 'Str Inharmon', 'Str Damping', 'S Damp < Key', 'Pickup On/Off', 'Pickup Pos')
TNS_BANK6 = ('Vibrato On/Off', 'Vib Delay', 'Vib Fade-In', 'Vib Speed', 'Vib Amount', 'Vib < ModWh', 'Vib Error', 'Volume')
TNS_BANK7 = ('Filter On/Off', 'Filter Type', 'Filter Freq', 'Filter Reso', 'Freq < Env', 'Reso < Env', 'Freq < LFO', 'Reso < LFO')
TNS_BANK8 = ('FEG On/Off', '', 'FEG Att < Vel', 'FEG < Vel', 'FEG Attack', 'FEG Decay', 'FEG Sustain', 'FEG Release')
TNS_BANK9 = ('LFO On/Off', 'LFO Sync On', 'LFO SyncRate', 'LFO Speed', 'LFO Delay', 'LFO Fade In', '', 'LFO Shape')
TNS_BANK10 = ('Octave', 'Semitone', 'Fine Tune', 'Voices', 'PB Depth', 'Stretch', 'Error', 'Key Priority')
TNS_BANK11 = ('Unison Voices', 'Uni Detune', 'Uni Delay', 'Porta On/Off', 'Porta Time', 'Porta Legato', 'Porta Prop', 'Volume')
TNS_BANK12 = ('Exc Force < Vel', 'Exc Force < Key', 'Exc Fric < Vel', 'Exc Fric < Key', 'Exc Vel < Vel', 'Exc Vel < Key', 'E Pos < Vel', 'E Pos < Key')
TNS_BANK13 = ('D Mass < Key', 'D Stiff < Key', 'D Velo < Key', 'D Pos < Key', 'T Mass < Vel', 'T Mass < Key', 'Freq < Key', 'Reso < Key')
TNS_BOB = ('Filter Freq', 'Filter Reso', 'Filter Type', 'Excitator Type', 'E Pos', 'String Decay', 'Str Damping', 'Volume')
TNS_BANKS = (TNS_BANK1,
TNS_BANK2,
TNS_BANK3,
TNS_BANK4,
TNS_BANK5,
TNS_BANK6,
TNS_BANK7,
TNS_BANK8,
TNS_BANK9,
TNS_BANK10,
TNS_BANK11,
TNS_BANK12,
TNS_BANK13)
TNS_BOBS = (TNS_BOB,)
TNS_BNK_NAMES = ('Excite', 'Damper', 'TermPick', 'Body', 'String', 'Vibrato', 'Filter', 'FiltEnv', 'LFO', 'Keyboard', 'UniPort', 'ExVelKey', 'RestKey')
ARP_BANK1 = ('Style', 'Groove', 'Offset', 'Hold On', '', '', '', 'Device On')
ARP_BANK2 = ('Sync On', 'Free Rate', 'Synced Rate', 'Gate', 'Retrigger Mode', 'Ret. Interval', 'Repeats', 'Device On')
ARP_BANK3 = ('Tranpose Mode', 'Tranpose Key', 'Transp. Steps', 'Transp. Dist.', 'Velocity Decay', 'Velocity Target', 'Velocity On', 'Vel. Retrigger')
ARP_BOB = ('Sync On', 'Free Rate', 'Synced Rate', 'Gate', 'Groove', 'Transp. Steps', 'Transp. Dist.', 'Velocity Decay')
ARP_BANKS = (ARP_BANK1, ARP_BANK2, ARP_BANK3)
ARP_BOBS = (ARP_BOB,)
ARP_BNK_NAMES = ('Style', 'Rate/Retrigger', 'Transp./Vel.')
CRD_BANK1 = ('Shift1', 'Shift2', 'Shift3', 'Shift4', 'Shift5', 'Shift6', '', 'Device On')
CRD_BANK2 = ('Velocity1', 'Velocity2', 'Velocity3', 'Velocity4', 'Velocity5', 'Velocity6', '', 'Device On')
CRD_BANK3 = ('Shift1', 'Velocity1', 'Shift2', 'Velocity2', 'Shift3', 'Velocity3', 'Shift4', 'Velocity4')
CRD_BOB = ('Shift1', 'Shift2', 'Shift3', 'Shift4', 'Velocity1', 'Velocity2', 'Velocity3', 'Velocity4')
CRD_BANKS = (CRD_BANK1, CRD_BANK2, CRD_BANK3)
CRD_BOBS = (CRD_BOB,)
CRD_BNK_NAMES = ('PtchShft', 'Velocity', 'StVel1-4')
NTL_BANK1 = ('Trigger Mode', 'Sync On', 'Synced Length', 'Time Length', 'Gate', 'On/Off-Balance', 'Decay Time', 'Decay Key Scale')
NTL_BANKS = (NTL_BANK1,)
NTL_BOBS = (NTL_BANK1,)
PIT_BANK1 = ('Pitch', 'Range', 'Lowest', '', '', '', '', 'Device On')
PIT_BANKS = (PIT_BANK1,)
PIT_BOBS = (PIT_BANK1,)
RND_BANK1 = ('Chance', 'Choices', 'Mode', 'Scale', 'Sign', '', '', 'Device On')
RND_BANKS = (RND_BANK1,)
RND_BOBS = (RND_BANK1,)
SCL_BANK1 = ('Base', 'Transpose', 'Range', 'Lowest', 'Fold', 'Map 0', 'Map 1', 'Device On')
SCL_BANK2 = ('Map 0', 'Map 1', 'Map 2', 'Map 3', 'Map 4', 'Map 5', 'Map 6', 'Map 7')
SCL_BANKS = (SCL_BANK1, SCL_BANK2)
SCL_BOBS = (SCL_BANK1,)
SCL_BNK_NAMES = ('Scale', 'Maps')
VEL_BANK1 = ('Mode', 'Drive', 'Compand', 'Random', 'Out Hi', 'Out Low', 'Range', 'Lowest')
VEL_BANKS = (VEL_BANK1,)
VEL_BOBS = (VEL_BANK1,)
AMP_BANK1 = ('Amp Type', 'Gain', 'Bass', 'Middle', 'Treble', 'Presence', 'Volume', 'Dry/Wet')
AMP_BANK2 = ('Dual Mono', '', '', '', '', '', '', '')
AMP_BANKS = (AMP_BANK1, AMP_BANK2)
AMP_BOBS = (AMP_BANK1,)
AMP_BNK_NAMES = ('Global', 'DualMono')
AFL_BANK1 = ('Env. Modulation', 'Env. Attack', 'Env. Release', 'Filter Type', 'Frequency', 'Resonance', 'LFO Quantize On', 'LFO Quantize Rate')
AFL_BANK2 = ('LFO Amount', 'LFO Sync', 'LFO Sync Rate', 'LFO Frequency', 'LFO Waveform', 'LFO Stereo Mode', 'LFO Phase', 'LFO Spin')
AFL_BANK3 = ('', '', '', '', 'LFO Offset', 'Ext. In On', 'Ext. In Gain', 'Ext. In Mix')
AFL_BOB = ('Frequency', 'Resonance', 'Filter Type', 'Env. Modulation', 'LFO Amount', 'LFO Waveform', 'LFO Frequency', 'LFO Phase')
AFL_BANKS = (AFL_BANK1, AFL_BANK2, AFL_BANK3)
AFL_BOBS = (AFL_BOB,)
AFL_BNK_NAMES = ('Env/Filt', 'LFO', 'SideChain')
APN_BANK1 = ('LFO Type', 'Frequency', 'Stereo Mode', 'Spin', 'Amount', 'Sync Rate', 'Phase', 'Offset')
APN_BANK2 = ('Waveform', 'Shape', 'Width (Random)', 'Invert', '', '', '', 'Device On')
APN_BOB = ('LFO Type', 'Frequency', 'Stereo Mode', 'Spin', 'Amount', 'Sync Rate', 'Phase', 'Offset')
APN_BANKS = (APN_BANK1, APN_BANK2)
APN_BOBS = (APN_BOB,)
APN_BNK_NAMES = ('LFORates', 'LFO Wave')
BRP_BANK1 = ('Interval', 'Offset', 'Chance', 'Gate', 'Repeat', '', '', 'Device On')
BRP_BANK2 = ('Grid', 'Variation', 'Variation Type', 'Block Triplets', 'Pitch', 'Pitch Decay', '', '')
BRP_BANK3 = ('Filter Freq', 'Filter Width', '', 'Filter On', 'Volume', 'Decay', '', 'Mix Type')
BRP_BOB = ('Grid', 'Interval', 'Offset', 'Gate', 'Pitch', 'Pitch Decay', 'Filter Freq', 'Decay')
BRP_BANKS = (BRP_BANK1, BRP_BANK2, BRP_BANK3)
BRP_BOBS = (BRP_BOB,)
BRP_BNK_NAMES = ('RepeatRt', 'GridPitch', 'Filt/Mix')
CAB_BANK1 = ('Cabinet Type', 'Microphone Position', 'Microphone Type', 'Dual Mono', '', '', 'Device On', 'Dry/Wet')
CAB_BANKS = (CAB_BANK1,)
CAB_BOBS = (CAB_BANK1,)
CHR_BANK1 = ('Delay 1 HiPass', 'Delay 1 Time', 'Delay 2 Time', 'Link On', 'Delay 2 Mode', 'LFO Amount', 'LFO Extend On', 'LFO Rate')
CHR_BANK2 = ('Feedback', '', '', 'Dry/Wet', 'Polarity', '', '', 'Device On')
CHR_BOB = ('Delay 1 HiPass', 'Delay 1 Time', 'Delay 2 Time', 'Feedback', 'Dry/Wet', 'LFO Amount', 'LFO Extend On', 'LFO Rate')
CHR_BANKS = (CHR_BANK1, CHR_BANK2)
CHR_BOBS = (CHR_BOB,)
CHR_BNK_NAMES = ('DelayMod', 'Mixer')
CP3_BANK1 = ('Ext. In On', 'Side Listen', 'Ext. In Gain', 'Ext. In Mix', 'EQ Mode', 'EQ Freq', 'EQ Q', 'EQ Gain')
CP3_BANK2 = ('Ratio', 'Expansion Ratio', 'Attack', 'Release', 'Threshold', 'Output Gain', 'Knee', 'LookAhead')
CP3_BANK3 = ('EQ On', 'Auto Release On/Off', 'Env Mode', 'Makeup', 'Model', '', '', 'Dry/Wet')
CP3_BOB = ('Ratio', 'Expansion Ratio', 'Attack', 'Release', 'Threshold', 'Output Gain', 'Knee', 'Dry/Wet')
CP3_BANKS = (CP3_BANK1, CP3_BANK2, CP3_BANK3)
CP3_BOBS = (CP3_BOB,)
CP3_BNK_NAMES = ('SideChain', 'Compress', 'Output')
CRP_BANK1 = ('Tune', 'Fine', 'Spread', 'Dry Wet', 'Mid Freq', 'Width', 'Bleed', 'Width')
CRP_BANK2 = ('LFO Sync', 'LFO Sync Rate', 'LFO Rate', 'LFO Amount', 'LFO Stereo Mode', 'Phase', 'Spin', 'LFO Shape')
CRP_BANK3 = ('Resonance Type', 'Listening L', 'Listening R', 'Hit', 'Inharmonics', 'Decay', 'Material', 'Brightness')
CRP_BANK4 = ('Transpose', 'Opening', 'Radius', 'Ratio', 'MIDI Frequency', 'PB Range', 'Note Off', 'Off Decay')
CRP_BOB = ('Brightness', 'Resonance Type', 'Material', 'Inharmonics', 'Decay', 'Ratio', 'Tune', 'Dry Wet')
CRP_BANKS = (CRP_BANK1, CRP_BANK2, CRP_BANK3, CRP_BANK4)
CRP_BOBS = (CRP_BOB,)
CRP_BNK_NAMES = ('TuneFilt', 'LFO', 'Body', 'SideChain')
DTB_BANK1 = ('Drive', 'Tube Type', 'Tone', 'Bias', 'Envelope', 'Attack', 'Release', 'Dry/Wet')
DTB_BANK2 = ('Output', '', '', '', '', '', '', 'Dry/Wet')
DTB_BOB = ('Drive', 'Tube Type', 'Tone', 'Bias', 'Envelope', 'Attack', 'Release', 'Dry/Wet')
DTB_BANKS = (DTB_BANK1, DTB_BANK2)
DTB_BOBS = (DTB_BOB,)
DTB_BNK_NAMES = ('Dynamics', 'Output')
EQ8_BANK1 = ('1 Filter On A', '2 Filter On A', '3 Filter On A', '4 Filter On A', '5 Filter On A', '6 Filter On A', '7 Filter On A', '8 Filter On A')
EQ8_BANK2 = ('1 Frequency A', '1 Resonance A', '1 Gain A', '1 Filter Type A', '8 Frequency A', '8 Resonance A', '8 Gain A', '8 Filter Type A')
EQ8_BANK3 = ('2 Frequency A', '2 Resonance A', '2 Gain A', '2 Filter Type A', '7 Frequency A', '7 Resonance A', '7 Gain A', '7 Filter Type A')
EQ8_BANK4 = ('3 Frequency A', '3 Resonance A', '3 Gain A', '3 Filter Type A', '6 Frequency A', '6 Resonance A', '6 Gain A', '6 Filter Type A')
EQ8_BANK5 = ('4 Frequency A', '4 Resonance A', '4 Gain A', '4 Filter Type A', '5 Frequency A', '5 Resonance A', '5 Gain A', '5 Filter Type A')
EQ8_BANK6 = ('1 Frequency A', '1 Gain A', '2 Frequency A', '2 Resonance A', '7 Frequency A', '7 Resonance A', '8 Frequency A', '8 Gain A')
EQ8_BANK7 = ('3 Frequency A', '3 Resonance A', '4 Frequency A', '4 Resonance A', '5 Frequency A', '5 Resonance A', '6 Frequency A', '6 Resonance A')
EQ8_BANK8 = ('', '', '', '', '', 'Adaptive Q', 'Scale', 'Output Gain')
EQ8_BANK9 = ('1 Filter On B', '2 Filter On B', '3 Filter On B', '4 Filter On B', '5 Filter On B', '6 Filter On B', '7 Filter On B', '8 Filter On B')
EQ8_BANK10 = ('1 Frequency A', '1 Resonance A', '1 Gain A', '1 Filter Type A', '1 Frequency B', '1 Resonance B', '1 Gain B', '1 Filter Type B')
EQ8_BANK11 = ('2 Frequency A', '2 Resonance A', '2 Gain A', '2 Filter Type A', '2 Frequency B', '2 Resonance B', '2 Gain B', '2 Filter Type B')
EQ8_BANK12 = ('3 Frequency A', '3 Resonance A', '3 Gain A', '3 Filter Type A', '3 Frequency B', '3 Resonance B', '3 Gain B', '3 Filter Type B')
EQ8_BANK13 = ('4 Frequency A', '4 Resonance A', '4 Gain A', '4 Filter Type A', '4 Frequency B', '4 Resonance B', '4 Gain B', '4 Filter Type B')
EQ8_BANK14 = ('5 Frequency A', '5 Resonance A', '5 Gain A', '5 Filter Type A', '5 Frequency B', '5 Resonance B', '5 Gain B', '5 Filter Type B')
EQ8_BANK15 = ('6 Frequency A', '6 Resonance A', '6 Gain A', '6 Filter Type A', '6 Frequency B', '6 Resonance B', '6 Gain B', '6 Filter Type B')
EQ8_BANK16 = ('7 Frequency A', '7 Resonance A', '7 Gain A', '7 Filter Type A', '7 Frequency B', '7 Resonance B', '7 Gain B', '7 Filter Type B')
EQ8_BANK17 = ('8 Frequency A', '8 Resonance A', '8 Gain A', '8 Filter Type A', '8 Frequency B', '8 Resonance B', '8 Gain B', '8 Filter Type B')
EQ8_BANK18 = ('1 Frequency A', '1 Resonance A', '1 Frequency B', '1 Resonance B', '8 Frequency A', '8 Resonance A', '8 Frequency B', '8 Resonance B')
EQ8_BANK19 = ('2 Frequency A', '2 Gain A', '2 Frequency B', '2 Gain B', '7 Frequency A', '7 Gain A', '7 Frequency B', '7 Gain B')
EQ8_BANK20 = ('3 Frequency A', '3 Gain A', '3 Frequency B', '3 Gain B', '6 Frequency A', '6 Gain A', '6 Frequency B', '6 Gain B')
EQ8_BANK21 = ('4 Frequency A', '4 Gain A', '4 Frequency B', '4 Gain B', '5 Frequency A', '5 Gain A', '5 Frequency B', '5 Gain B')
EQ8_BOB = ('1 Frequency A', '1 Gain A', '2 Frequency A', '2 Resonance A', '7 Frequency A', '7 Resonance A', '8 Frequency A', '8 Gain A')
EQ8_BANKS = (EQ8_BANK1,
EQ8_BANK2,
EQ8_BANK3,
EQ8_BANK4,
EQ8_BANK5,
EQ8_BANK6,
EQ8_BANK7,
EQ8_BANK8,
EQ8_BANK9,
EQ8_BANK10,
EQ8_BANK11,
EQ8_BANK12,
EQ8_BANK13,
EQ8_BANK14,
EQ8_BANK15,
EQ8_BANK16,
EQ8_BANK17,
EQ8_BANK18,
EQ8_BANK19,
EQ8_BANK20,
EQ8_BANK21)
EQ8_BOBS = (EQ8_BOB,)
EQ8_BNK_NAMES = ('SterAOn', 'SFilt1+8', 'SFilt2+7', 'SFilt3+6', 'SFilt4+5', 'S1/2+7/8', 'S3/4+5/6', 'OutputGn', 'M/S:B ON', 'MFlt1A+B', 'MFlt2A+B', 'MFlt3A+B', 'MFlt4A+B', 'MFlt5A+B', 'MFlt6A+B', 'MFlt7A+B', 'MFlt8A+B', 'MF1/8A+B', 'MF 2/7A+B', 'MF3/6A+B', 'MF4/5A+B')
EQ3_BANK1 = ('GainLo', 'GainMid', 'GainHi', 'LowOn', 'MidOn', 'HighOn', 'FreqLo', 'FreqHi')
EQ3_BANKS = (EQ3_BANK1,)
EQ3_BOBS = (EQ3_BANK1,)
ERO_BANK1 = ('Mode', 'Frequency', 'Width', 'Amount', '', '', '', '')
ERO_BANKS = (ERO_BANK1,)
ERO_BOBS = (ERO_BANK1,)
FLD_BANK1 = ('1 Input On', '1 Filter Freq', '1 Filter Width', '1 Delay Mode', '1 Beat Delay', '1 Feedback', '1 Pan', '1 Volume')
FLD_BANK2 = ('2 Input On', '2 Filter Freq', '2 Filter Width', '2 Delay Mode', '2 Beat Delay', '2 Feedback', '2 Pan', '2 Volume')
FLD_BANK3 = ('3 Input On', '3 Filter Freq', '3 Filter Width', '3 Delay Mode', '3 Beat Delay', '3 Feedback', '3 Pan', '3 Volume')
FLD_BANK4 = ('1 Filter Freq', '3 Filter Freq', '1 Beat Delay', '2 Beat Delay', '3 Beat Delay', '1 Feedback', '2 Feedback', '3 Feedback')
FLD_BANK5 = ('1 Pan', '3 Pan', '1 Volume', '2 Volume', '3 Volume', '1 Beat Swing', '2 Beat Swing', '3 Beat Swing')
FLD_BANK6 = ('1 Feedback', '3 Feedback', '1 Time Delay', '2 Time Delay', '3 Time Delay', '1 Pan', '3 Pan', 'Dry')
FLD_BOB = ('2 Filter Freq', '1 Beat Swing', '2 Beat Swing', '3 Beat Swing', '1 Feedback', '2 Feedback', '3 Feedback', 'Dry')
FLD_BANKS = (FLD_BANK1, FLD_BANK2, FLD_BANK3, FLD_BANK4, FLD_BANK5, FLD_BANK6)
FLD_BOBS = (FLD_BOB,)
FLD_BNK_NAMES = ('L Filter', 'L+R Filter', 'R Filter', 'FrqDlyFB', 'PanVolSw', 'FB/Dly/Pan')
FLG_BANK1 = ('Delay Time', 'Polarity', 'Feedback', 'Env. Modulation', 'Env. Attack', 'Env. Release', 'Hi Pass', 'Dry/Wet')
FLG_BANK2 = ('Sync', 'Frequency', 'Sync Rate', 'LFO Offset', 'LFO Stereo Mode', 'LFO Spin', 'LFO Amount', 'LFO Waveform')
FLG_BOB = ('Hi Pass', 'Delay Time', 'Frequency', 'Sync Rate', 'LFO Amount', 'Env. Modulation', 'Feedback', 'Dry/Wet')
FLG_BANKS = (FLG_BANK1, FLG_BANK2)
FLG_BOBS = (FLG_BOB,)
FLG_BNK_NAMES = ('DlyEnvMx', 'LFO/S&H')
FRS_BANK1 = ('Mode', 'Coarse', 'Ring Mod Frequency', 'Fine', 'Drive On/Off', 'Drive', 'Wide', 'Dry/Wet')
FRS_BANK2 = ('Sync', 'LFO Frequency', 'Sync Rate', 'LFO Offset', 'LFO Stereo Mode', 'LFO Spin', 'LFO Amount', 'LFO Waveform')
FRS_BANKS = (FRS_BANK1, FRS_BANK2)
FRS_BOBS = (FRS_BANK1,)
FRS_BNK_NAMES = ('FreqDrive', 'LFO/S&H')
GTE_BANK1 = ('Ext. In On', 'Side Listen', 'Ext. In Gain', 'Ext. In Mix', 'EQ Mode', 'EQ Freq', 'EQ Q', 'EQ Gain')
GTE_BANK2 = ('Threshold', 'Return', 'FlipMode', 'LookAhead', 'Attack', 'Hold', 'Release', 'Floor')
GTE_BOB = ('Ext. In Gain', 'Ext. In Mix', 'EQ On', 'EQ Freq', 'Threshold', 'Attack', 'Release', 'Floor')
GTE_BANKS = (GTE_BANK1, GTE_BANK2)
GTE_BOBS = (GTE_BOB,)
GTE_BNK_NAMES = ('SideChain', 'Gate')
GLU_BANK1 = ('Ext. In On', 'EQ On', 'Ext. In Gain', 'Ext. In Mix', 'EQ Mode', 'EQ Freq', 'EQ Q', 'EQ Gain')
GLU_BANK2 = ('Ratio', 'Peak Clip In', 'Attack', 'Release', 'Threshold', 'Makeup', 'Range', 'Dry/Wet')
GLU_BOB = ('Ratio', 'EQ Freq', 'Attack', 'Release', 'Threshold', 'Makeup', 'Range', 'Dry/Wet')
GLU_BANKS = (GLU_BANK1, GLU_BANK2)
GLU_BOBS = (GLU_BOB,)
GLU_BNK_NAMES = ('SideChain', 'Compress')
GRD_BANK1 = ('Frequency', 'Pitch', 'Time Delay', 'Beat Swing', 'Random', 'Spray', 'Feedback', 'DryWet')
GRD_BANK2 = ('Delay Mode', 'Beat Delay', '', '', '', '', '', 'Device On')
GRD_BANKS = (GRD_BANK1, GRD_BANK2)
GRD_BOBS = (GRD_BANK1,)
LPR_BANK1 = ('State', 'Quantization', 'Song Control', 'Tempo Control', 'Feedback', 'Monitor', 'Speed', 'Reverse')
LPR_BANKS = (LPR_BANK1,)
LPR_BOBS = (LPR_BANK1,)
MBD_BANK1 = ('Band Activator (High)', 'Mid-High Crossover', 'Input Gain (High)', 'Output Gain (High)', 'Master Output', 'Time Scaling', 'Amount', 'Soft Knee On/Off')
MBD_BANK2 = ('Attack Time (High)', 'Release Time (High)', 'Below Threshold (High)', 'Below Ratio (High)', 'Above Threshold (High)', 'Above Ratio (High)', 'Input Gain (High)', 'Output Gain (High)')
MBD_BANK3 = ('Band Activator (Mid)', '', 'Input Gain (Mid)', 'Output Gain (Mid)', 'Master Output', 'Time Scaling', 'Amount', 'Peak/RMS Mode')
MBD_BANK4 = ('Attack Time (Mid)', 'Release Time (Mid)', 'Below Threshold (Mid)', 'Below Ratio (Mid)', 'Above Threshold (Mid)', 'Above Ratio (Mid)', 'Input Gain (Mid)', 'Output Gain (Mid)')
MBD_BANK5 = ('Band Activator (Low)', 'Low-Mid Crossover', 'Input Gain (Low)', 'Output Gain (Low)', 'Master Output', 'Time Scaling', 'Amount', 'Soft Knee On/Off')
MBD_BANK6 = ('Attack Time (Low)', 'Release Time (Low)', 'Below Threshold (Low)', 'Below Ratio (Low)', 'Above Threshold (Low)', 'Above Ratio (Low)', 'Input Gain (Low)', 'Output Gain (Low)')
MBD_BANK7 = ('Attack Time (High)', 'Release Time (High)', 'Attack Time (Mid)', 'Release Time (Mid)', 'Attack Time (Low)', 'Release Time (Low)', 'Mid-High Crossover', 'Low-Mid Crossover')
MBD_BANK8 = ('Below Threshold (High)', 'Below Ratio (High)', 'Below Threshold (Mid)', 'Below Ratio (Mid)', 'Below Threshold (Low)', 'Below Ratio (Low)', 'Mid-High Crossover', 'Low-Mid Crossover')
MBD_BANK9 = ('Above Threshold (High)', 'Above Ratio (High)', 'Above Threshold (Mid)', 'Above Ratio (Mid)', 'Above Threshold (Low)', 'Above Ratio (Low)', 'Mid-High Crossover', 'Low-Mid Crossover')
MBD_BANK10 = ('Input Gain (High)', 'Output Gain (High)', 'Input Gain (Mid)', 'Output Gain (Mid)', 'Input Gain (Low)', 'Output Gain (Low)', 'Mid-High Crossover', 'Low-Mid Crossover')
MBD_BANK11 = ('Ext. In On', 'Ext. In Gain', 'Ext. In Mix', 'Soft Knee On/Off', 'Peak/RMS Mode', 'Master Output', 'Time Scaling', 'Amount')
MBD_BOB = ('Below Threshold (High)', 'Above Threshold (High)', 'Below Threshold (Mid)', 'Above Threshold (Mid)', 'Below Threshold (Low)', 'Above Threshold (Low)', 'Master Output', 'Amount')
MBD_BANKS = (MBD_BANK1,
MBD_BANK2,
MBD_BANK3,
MBD_BANK4,
MBD_BANK5,
MBD_BANK6,
MBD_BANK7,
MBD_BANK8,
MBD_BANK9,
MBD_BANK10,
MBD_BANK11)
MBD_BOBS = (MBD_BOB,)
MBD_BNK_NAMES = ('H:Filt+IO', 'H:T/B/A', 'M:Filt+IO', 'M: T/B/A', 'L:Filt+IO', 'L: T/B/A', 'All:Time', 'All:Below', 'All:Above', 'All:InOut', 'SdChnMix')
OVR_BANK1 = ('Filter Freq', 'Filter Width', 'Drive', 'Tone', 'Preserve Dynamics', '', '', 'Dry/Wet')
OVR_BANKS = (OVR_BANK1,)
OVR_BOBS = (OVR_BANK1,)
PHS_BANK1 = ('Poles', 'Color', 'Frequency', 'Feedback', 'Env. Modulation', 'Env. Attack', 'Env. Release', 'Dry/Wet')
PHS_BANK2 = ('LFO Sync', 'LFO Frequency', 'LFO Sync Rate', 'LFO Phase', 'LFO Stereo Mode', 'LFO Spin', 'LFO Amount', 'LFO Waveform')
PHS_BOB = ('Frequency', 'Feedback', 'Poles', 'Env. Modulation', 'Color', 'LFO Amount', 'LFO Frequency', 'Dry/Wet')
PHS_BANKS = (PHS_BANK1, PHS_BANK2)
PHS_BOBS = (PHS_BOB,)
PHS_BNK_NAMES = ('PFreqEnv', 'LFO/S&H')
PPG_BANK1 = ('Delay Mode', 'Beat Delay', 'Beat Swing', 'Time Delay', 'Filter Freq', 'Filter Width', 'Feedback', 'Dry/Wet')
PPG_BANKS = (PPG_BANK1,)
PPG_BOBS = (PPG_BANK1,)
RDX_BANK1 = ('Bit On', 'Bit Depth', 'Sample Mode', 'Sample Hard', 'Sample Soft', '', '', '')
RDX_BANKS = (RDX_BANK1,)
RDX_BOBS = (RDX_BANK1,)
RSN_BANK1 = ('Mode', 'I On', 'II On', 'III On', 'IV On', 'V On', 'Filter On', 'Dry/Wet')
RSN_BANK2 = ('Decay', 'I Note', 'II Pitch', 'III Pitch', 'IV Pitch', 'V Pitch', 'Frequency', 'Filter Type')
RSN_BANK3 = ('Const', 'I Tune', 'II Tune', 'III Tune', 'IV Tune', 'V Tune', 'Width', 'Dry/Wet')
RSN_BANK4 = ('Color', 'I Gain', 'II Gain', 'III Gain', 'IV Gain', 'V Gain', 'Global Gain', 'Dry/Wet')
RSN_BANK5 = ('Mode', 'Decay', 'Const', 'Color', 'I On', 'I Note', 'I Tune', 'I Gain')
RSN_BANK6 = ('II On', 'II Pitch', 'II Tune', 'II Gain', 'III On', 'III Pitch', 'III Tune', 'III Gain')
RSN_BANK7 = ('IV On', 'IV Pitch', 'IV Tune', 'IV Gain', 'V On', 'V Pitch', 'V Tune', 'V Gain')
RSN_BANK8 = ('Filter On', 'Frequency', 'Filter Type', 'Decay', 'Color', 'Width', 'Global Gain', 'Dry/Wet')
RSN_BOB = ('Frequency', 'Decay', 'Color', 'I Gain', 'II Gain', 'III Gain', 'Width', 'Dry/Wet')
RSN_BANKS = (RSN_BANK1,
RSN_BANK2,
RSN_BANK3,
RSN_BANK4,
RSN_BANK5,
RSN_BANK6,
RSN_BANK7,
RSN_BANK8)
RSN_BOBS = (RSN_BOB,)
RSN_BNK_NAMES = ('ON', 'Pitch', 'Tune', 'Gain', 'Mode I', 'Md:II+III', 'Md:IV+V', 'Filt/Mix')
RVB_BANK1 = ('In LowCut On', 'In HighCut On', 'ER Spin On', 'ER Shape', 'In Filter Freq', 'In Filter Width', 'ER Spin Rate', 'ER Spin Amount')
RVB_BANK2 = ('PreDelay', 'Room Size', 'Stereo Image', 'Chorus On', 'Chorus Rate', 'Chorus Amount', 'Density', 'Scale')
RVB_BANK3 = ('HiShelf On', 'HiShelf Freq', 'HiShelf Gain', 'LowShelf On', 'LowShelf Freq', 'LowShelf Gain', 'DecayTime', 'Freeze On')
RVB_BOB = ('PreDelay', 'ER Shape', 'Room Size', 'Stereo Image', 'Freeze On', 'ER Level', 'Diffuse Level', 'Dry/Wet')
RVB_BANKS = (RVB_BANK1, RVB_BANK2, RVB_BANK3)
RVB_BOBS = (RVB_BOB,)
RVB_BNK_NAMES = ('In/Reflc', 'GlobChrs', 'Diffusion')
SAT_BANK1 = ('Drive', 'Type', 'WS Drive', 'Color', 'Base', 'Frequency', 'Width', 'Depth')
SAT_BANK2 = ('Drive', 'Type', 'WS Drive', 'WS Curve', 'WS Depth', 'WS Lin', 'WS Damp', 'WS Period')
SAT_BOB = ('Drive', 'Type', 'Base', 'Frequency', 'Width', 'Depth', 'Output', 'Dry/Wet')
SAT_BANKS = (SAT_BANK1, SAT_BANK2)
SAT_BOBS = (SAT_BOB,)
SAT_BNK_NAMES = ('General', 'Waveshape')
SMD_BANK1 = ('L Delay Mode', 'L Beat Delay', 'L Beat Swing', 'L Time Delay', 'R Delay Mode', 'R Beat Delay', 'R Beat Swing', 'R Time Delay')
SMD_BOB = ('L Delay Mode', 'L Beat Delay', 'L Beat Swing', 'R Time Delay', 'R Beat Swing', 'Link On', 'Feedback', 'Dry/Wet')
SMD_BANKS = (SMD_BANK1,)
SMD_BOBS = (SMD_BOB,)
UTL_BANK1 = ('Gain', 'Mute', 'BlockDc', 'Signal Source', 'PhaseInvertL', 'PhaseInvertR', 'StereoSeparation', 'Panorama')
UTL_BANKS = (UTL_BANK1,)
UTL_BOBS = (UTL_BANK1,)
VDS_BANK1 = ('Tracing On', 'Tracing Drive', 'Tracing Freq.', 'Tracing Width', 'Pinch Soft On.', 'Pinch Mono On', 'Crackle Density', 'Crackle Volume')
VDS_BOB = ('Pinch Soft On.', 'Pinch Mono On', 'Pinch On', 'Crackle Density', 'Pinch Drive', 'Pinch Freq.', 'Pinch Width', 'Global Drive')
VDS_BANKS = (VDS_BANK1,)
VDS_BOBS = (VDS_BOB,)
VOC_BANK1 = ('Unvoiced Level', 'Ext. In Gain', 'Noise Rate', 'Noise Crackle', 'Upper Pitch Detection', 'Lower Pitch Detection', 'Oscillator Waveform', 'Oscillator Pitch')
VOC_BANK2 = ('Enhance', 'Unvoiced Sensitivity', 'Mono/Stereo', 'Envelope Depth', 'Attack Time', 'Release Time', 'Formant Shift', 'Dry/Wet')
VOC_BANK3 = ('Upper Filter Band', 'Lower Filter Band', 'Filter Bandwidth', 'Precise/Retro', 'Gate Threshold', 'Output Level', 'Envelope Depth', 'Dry/Wet')
VOC_BOB = ('Unvoiced Level', 'Filter Bandwidth', 'Gate Threshold', 'Formant Shift', 'Attack Time', 'Release Time', 'Envelope Depth', 'Dry/Wet')
VOC_BANKS = (VOC_BANK1, VOC_BANK2, VOC_BANK3)
VOC_BOBS = (VOC_BOB,)
VOC_BNK_NAMES = ('Carrier', 'Env/Mix', 'Filter')
DEVICE_DICT = {'AudioEffectGroupDevice': RCK_BANKS,
 'MidiEffectGroupDevice': RCK_BANKS,
 'InstrumentGroupDevice': RCK_BANKS,
 'DrumGroupDevice': RCK_BANKS,
 'InstrumentImpulse': IMP_BANKS,
 'Operator': OPR_BANKS,
 'UltraAnalog': ALG_BANKS,
 'OriginalSimpler': SIM_BANKS,
 'MultiSampler': SAM_BANKS,
 'MidiArpeggiator': ARP_BANKS,
 'LoungeLizard': ELC_BANKS,
 'StringStudio': TNS_BANKS,
 'Collision': COL_BANKS,
 'MidiChord': CRD_BANKS,
 'MidiNoteLength': NTL_BANKS,
 'MidiPitcher': PIT_BANKS,
 'MidiRandom': RND_BANKS,
 'MidiScale': SCL_BANKS,
 'MidiVelocity': VEL_BANKS,
 'AutoFilter': AFL_BANKS,
 'AutoPan': APN_BANKS,
 'BeatRepeat': BRP_BANKS,
 'Chorus': CHR_BANKS,
 'Compressor2': CP3_BANKS,
 'Corpus': CRP_BANKS,
 'Eq8': EQ8_BANKS,
 'FilterEQ3': EQ3_BANKS,
 'Erosion': ERO_BANKS,
 'FilterDelay': FLD_BANKS,
 'Flanger': FLG_BANKS,
 'FrequencyShifter': FRS_BANKS,
 'GrainDelay': GRD_BANKS,
 'Looper': LPR_BANKS,
 'MultibandDynamics': MBD_BANKS,
 'Overdrive': OVR_BANKS,
 'Phaser': PHS_BANKS,
 'Redux': RDX_BANKS,
 'Saturator': SAT_BANKS,
 'Resonator': RSN_BANKS,
 'CrossDelay': SMD_BANKS,
 'StereoGain': UTL_BANKS,
 'Tube': DTB_BANKS,
 'Reverb': RVB_BANKS,
 'Vinyl': VDS_BANKS,
 'Gate': GTE_BANKS,
 'PingPongDelay': PPG_BANKS,
 'Vocoder': VOC_BANKS,
 'Amp': AMP_BANKS,
 'Cabinet': CAB_BANKS,
 'GlueCompressor': GLU_BANKS}
DEVICE_BOB_DICT = {'AudioEffectGroupDevice': RCK_BOBS,
 'MidiEffectGroupDevice': RCK_BOBS,
 'InstrumentGroupDevice': RCK_BOBS,
 'DrumGroupDevice': RCK_BOBS,
 'InstrumentImpulse': IMP_BOBS,
 'Operator': OPR_BOBS,
 'UltraAnalog': ALG_BOBS,
 'OriginalSimpler': SIM_BOBS,
 'MultiSampler': SAM_BOBS,
 'MidiArpeggiator': ARP_BOBS,
 'LoungeLizard': ELC_BOBS,
 'StringStudio': TNS_BOBS,
 'Collision': COL_BOBS,
 'MidiChord': CRD_BOBS,
 'MidiNoteLength': NTL_BOBS,
 'MidiPitcher': PIT_BOBS,
 'MidiRandom': RND_BOBS,
 'MidiScale': SCL_BOBS,
 'MidiVelocity': VEL_BOBS,
 'AutoFilter': AFL_BOBS,
 'AutoPan': APN_BOBS,
 'BeatRepeat': BRP_BOBS,
 'Chorus': CHR_BOBS,
 'Compressor2': CP3_BOBS,
 'Corpus': CRP_BOBS,
 'Eq8': EQ8_BOBS,
 'FilterEQ3': EQ3_BOBS,
 'Erosion': ERO_BOBS,
 'FilterDelay': FLD_BOBS,
 'Flanger': FLG_BOBS,
 'FrequencyShifter': FRS_BOBS,
 'GrainDelay': GRD_BOBS,
 'Looper': LPR_BOBS,
 'MultibandDynamics': MBD_BOBS,
 'Overdrive': OVR_BOBS,
 'Phaser': PHS_BOBS,
 'Redux': RDX_BOBS,
 'Saturator': SAT_BOBS,
 'Resonator': RSN_BOBS,
 'CrossDelay': SMD_BOBS,
 'StereoGain': UTL_BOBS,
 'Tube': DTB_BOBS,
 'Reverb': RVB_BOBS,
 'Vinyl': VDS_BOBS,
 'Gate': GTE_BOBS,
 'PingPongDelay': PPG_BOBS,
 'Vocoder': VOC_BOBS,
 'Amp': AMP_BOBS,
 'Cabinet': CAB_BOBS,
 'GlueCompressor': GLU_BOBS}
BANK_NAME_DICT = {'AudioEffectGroupDevice': RCK_BNK_NAMES,
 'MidiEffectGroupDevice': RCK_BNK_NAMES,
 'InstrumentGroupDevice': RCK_BNK_NAMES,
 'DrumGroupDevice': RCK_BNK_NAMES,
 'InstrumentImpulse': IMP_BNK_NAMES,
 'Operator': OPR_BNK_NAMES,
 'UltraAnalog': ALG_BNK_NAMES,
 'OriginalSimpler': SIM_BNK_NAMES,
 'MultiSampler': SAM_BNK_NAMES,
 'MidiArpeggiator': ARP_BNK_NAMES,
 'LoungeLizard': ELC_BNK_NAMES,
 'StringStudio': TNS_BNK_NAMES,
 'Collision': COL_BNK_NAMES,
 'MidiChord': CRD_BNK_NAMES,
 'BeatRepeat': BRP_BNK_NAMES,
 'Compressor2': CP3_BNK_NAMES,
 'Corpus': CRP_BNK_NAMES,
 'Eq8': EQ8_BNK_NAMES,
 'FilterDelay': FLD_BNK_NAMES,
 'Flanger': FLG_BNK_NAMES,
 'Gate': GTE_BNK_NAMES,
 'MultibandDynamics': MBD_BNK_NAMES,
 'Phaser': PHS_BNK_NAMES,
 'Saturator': SAT_BNK_NAMES,
 'Resonator': RSN_BNK_NAMES,
 'Reverb': RVB_BNK_NAMES,
 'Vocoder': VOC_BNK_NAMES,
 'Amp': AMP_BNK_NAMES,
 'GlueCompressor': GLU_BNK_NAMES,
 'AutoFilter': AFL_BNK_NAMES}
MAX_DEVICES = ('MxDeviceInstrument', 'MxDeviceAudioEffect', 'MxDeviceMidiEffect')

def device_parameters_to_map(device):
    return tuple(device.parameters[1:])


def parameter_bank_names(device, bank_name_dict = BANK_NAME_DICT, ubermap_skip = False):
    """ Determine the bank names to use for a device """
    if device != None:
        if not ubermap_skip:
            ubermap_banks = ubermap.get_custom_device_banks(device)
            if ubermap_banks:
                return ubermap_banks
            ubermap.dump_device(device)

        if device.class_name in bank_name_dict.keys():
            return bank_name_dict[device.class_name]
        else:
            banks = number_of_parameter_banks(device)

            def _default_bank_name(bank_index):
                return 'Bank ' + str(bank_index + 1)

            if device.class_name in MAX_DEVICES and banks != 0:

                def _is_ascii(c):
                    return ord(c) < 128

                def _bank_name(bank_index):
                    try:
                        name = device.get_bank_name(bank_index)
                    except:
                        name = None

                    if name:
                        return str(filter(_is_ascii, name))
                    else:
                        return _default_bank_name(bank_index)

                return map(_bank_name, range(0, banks))
            else:
                return map(_default_bank_name, range(0, banks))
    return []


def parameter_banks(device, device_dict = DEVICE_DICT, ubermap_skip = False):
    """ Determine the parameters to use for a device """
    if device != None:
        if not ubermap_skip:
            ubermap_params = ubermap.get_custom_device_params(device)
            if ubermap_params:
                return ubermap_params

        if device.class_name in device_dict.keys():

            def names_to_params(bank):
                return map(partial(get_parameter_by_name, device), bank)

            return map(names_to_params, device_dict[device.class_name])
        else:
            if device.class_name in MAX_DEVICES:
                try:
                    banks = device.get_bank_count()
                except:
                    banks = 0

                if banks != 0:

                    def _bank_parameters(bank_index):
                        try:
                            parameter_indices = device.get_bank_parameters(bank_index)
                        except:
                            parameter_indices = []

                        if len(parameter_indices) != 8:
                            return [ None for i in range(0, 8) ]
                        else:
                            return [ (device.parameters[i] if i != -1 else None) for i in parameter_indices ]

                    return map(_bank_parameters, range(0, banks))
            return group(device_parameters_to_map(device), 8)
    return []


""" Original function, not working with M4L devices and plugins. Probably due to weird decompilation issues. """
#def best_of_parameter_bank(device, device_bob_dict = DEVICE_BOB_DICT):
    #bobs = device and device.class_name in device_bob_dict and device_bob_dict[device.class_name]
    #if not len(bobs) == 1:
        #raise AssertionError
        #return map(partial(get_parameter_by_name, device), bobs[0])
    #if device.class_name in MAX_DEVICES:
        #try:
            #parameter_indices = device.get_bank_parameters(-1)
            #return [ (device.parameters[i] if i != -1 else None) for i in parameter_indices ]
        #except:
            #return []

    #return []
    
    
def best_of_parameter_bank(device, device_bob_dict = DEVICE_BOB_DICT, ubermap_skip = False):
    """ Revised function by Stray that should work fine with any type of device. """
    if not ubermap_skip:
        ubermap_bank = ubermap.get_custom_device_params(device, ubermap.SECTION_BEST_OF)
        if ubermap_bank:
            return ubermap_bank[0]

    if device.class_name in MAX_DEVICES:
        try:
            parameter_indices = device.get_bank_parameters(-1)
            return [ (device.parameters[i] if i != -1 else None) for i in parameter_indices ]
        except:
            return []
    elif device and device.class_name in device_bob_dict and device_bob_dict[device.class_name]:
        return map(partial(get_parameter_by_name, device), device_bob_dict[device.class_name][0])

    return []


def number_of_parameter_banks(device, device_dict = DEVICE_DICT):
    """ Determine the amount of parameter banks the given device has """
    if device != None:
        if device.class_name in device_dict.keys():
            device_bank = device_dict[device.class_name]
            return len(device_bank)
        else:
            if device.class_name in MAX_DEVICES:
                try:
                    banks = device.get_bank_count()
                except:
                    banks = 0

                if banks != 0:
                    return banks
            param_count = len(device.parameters[1:])
            return param_count / 8 + (1 if param_count % 8 else 0)
    return 0


def get_parameter_by_name(device, name):
    """ Find the given device's parameter that belongs to the given name """
    for i in device.parameters:
        if i.original_name == name:
            return i

