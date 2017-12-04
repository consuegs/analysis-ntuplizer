import FWCore.ParameterSet.Config as cms

MssmHbbNtuplizerL1Seeds = cms.PSet(
   L1Seeds    = cms.vstring  (
                                     'L1_Mu3_JetC16_dEta_Max0p4_dPhi_Max0p4', 
                                     'L1_Mu3_JetC60_dEta_Max0p4_dPhi_Max0p4',
                                     'L1_Mu3_JetC120_dEta_Max0p4_dPhi_Max0p4',
                                     'L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6',
                                     'L1_DoubleJet40er3p0',
                                     'L1_DoubleJet100er3p0',
                                     'L1_DoubleJet112er3p0',
                                     'L1_DoubleJet120er3p0',
                                     'L1_DoubleJet100er2p3_dEta_Max1p6',
                                     'L1_DoubleJet112er2p3_dEta_Max1p6',
                                     'L1_ZeroBias',
                                     'L1_SingleJet35',
                                     'L1_SingleJet60',
                                     'L1_SingleJet90',
                                     'L1_SingleJet120',
                                     'L1_SingleJet170',
                                     'L1_SingleJet180',
                                     'L1_SingleJet200',
                                     'L1_SingleMu3',
                                     'L1_SingleMu5',
                                     'L1_SingleMu7',
                                     'L1_Mu3_Jet30er2p5',
   ),
)
