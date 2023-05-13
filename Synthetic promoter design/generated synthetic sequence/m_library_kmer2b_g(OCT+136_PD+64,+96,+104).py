import simdna
import simdna.synthetic as synthetic
import simdna.simdnautil.util as util
import simdna.simdnautil.pwm as pwm
import numpy as np

# create a PWM object to represent the motif (must PPM matrix!!!!)
# create a matrix of motif
matrix_mouse_OCT = np.array([
	[0.801020, 0.158163, 0.000000, 0.040816],
	[0.000000, 0.000000, 0.000000, 1.000000],
	[0.000000, 0.000000, 0.025510, 0.974490],
	[0.000000, 0.000000, 0.000000, 1.000000],
	[0.030612, 0.015306, 0.933673, 0.020408],
	[0.010204, 0.984694, 0.005102, 0.000000],
	[0.979592, 0.015306, 0.005102, 0.000000],
	[0.000000, 0.005102, 0.000000, 0.994898]
    ])
matrix_mouse_Ebox = np.array([
	[0.762701, 0.111408, 0.075089, 0.050802],
	[0.535599, 0.135450, 0.015381, 0.313570],
	[0, 1, 0, 0],
	[0.999416, 0.000584, 0, 0],
	[0.000568, 0.02412, 0.971339, 0.003973],
	[0.006002, 0.97828, 0.014004, 0.001715],
	[0.000292, 0.000292, 0, 0.999416],
	[0, 0.000292, 0.999708, 0],
	[0.467700, 0.029457, 0.086047, 0.416796],
	[0.061815, 0.140996, 0.089518, 0.707670]
	])
matrix_mouse_Arid3a = np.array([
	[1, 0, 0, 0],
	[0, 0, 0, 1],
	[0.037037, 0.333333, 0, 0.62963],
	[1, 0, 0, 0],
	[1, 0, 0, 0],
	[0.740741, 0, 0.037037, 0.222222]
	])
matrix_mouse_PU1 = np.array([
	[0.391697, 0.164326, 0.275555, 0.168422],
	[0.424876, 0.123597, 0.345617, 0.105909],
	[0.611567, 0.051966, 0.216370, 0.120097],
	[0.663125, 0.048701, 0.188841, 0.099333],
	[0.607110, 0.008381, 0.180224, 0.204285],
	[0.197395, 0.127443, 0.675163, 0],
	[0.711857, 0.050365, 0.230448, 0.00733],
	[0.075351, 0, 0.924649, 0],
	[0, 0, 1, 0],
	[0.999215, 0, 0.000785, 0],
	[1, 0, 0, 0],
	[0.053928, 0.159225, 0.786848, 0],
	[0.129483, 0.050585, 0.053127, 0.766805],
	[0.0611, 0.188935, 0.714133, 0.035831],
	[0.343891, 0.188778, 0.329640, 0.137691]
	])
matrix_mouse_RUNX1 = np.array([
	[0.143500, 0.248000, 0.348000, 0.260500],
	[0.117000, 0.242500, 0.233500, 0.407000],
	[0.061500, 0.536000, 0.074500, 0.328000],
	[0.0285, 0, 0.0035, 0.968],
	[0, 0.0375, 0.936, 0.0265],
	[0.0435, 0.0635, 0.035, 0.858],
	[0, 0, 0.9935, 0.0065],
	[0.0085, 0.021, 0.924, 0.0465],
	[0.005, 0.2, 0.1255, 0.6695],
	[0.0655, 0.2315, 0.0405, 0.6625],
	[0.250000, 0.079000, 0.144500, 0.526500]
	])
matrix_mouse_CCCT = np.array([
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 0, 0 ,1]
	])
matrix_mouse_CArGbox = np.array([
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0.5, 0, 0, 0.5],
	[0.5, 0, 0, 0.5],
	[0.5, 0, 0, 0.5],
	[0.5, 0, 0, 0.5],
	[0.5, 0, 0, 0.5],
	[0.5, 0, 0, 0.5],
	[0, 0, 1, 0],
	[0, 0, 1, 0]
	])
matrix_of_motifM02 = np.array([
	[0.000000, 0.801527, 0.106870, 0.091603],
	[0.000000, 0.000000, 0.000000, 1.000000],
	[0.000000, 0.931298, 0.068702, 0.000000],
	[0.152672, 0.022901, 0.000000, 0.824427],
	[0.000000, 0.641221, 0.045802, 0.312977],
	[0.068702, 0.664122, 0.000000, 0.267176],
	[0.603053, 0.000000, 0.000000, 0.396947],
	[0.022901, 0.832061, 0.145038, 0.000000],
	[1.000000, 0.000000, 0.000000, 0.000000],
	[0.061069, 0.114504, 0.725191, 0.099237]
	])
matrix_of_motifM03 = np.array([
	[0.906977, 0.000000, 0.000000, 0.093023],
	[0.000000, 0.000000, 1.000000, 0.000000],
	[0.046512, 0.000000, 0.953488, 0.000000],
	[0.000000, 0.000000, 0.000000, 1.000000],
	[0.906977, 0.000000, 0.093023, 0.000000],
	[1.000000, 0.000000, 0.000000, 0.000000],
	[0.000000, 0.000000, 1.000000, 0.000000],
	[0.069767, 0.000000, 0.906977, 0.023256],
	[0.023256, 0.000000, 0.976744, 0.000000],
	[0.023256, 0.000000, 0.976744, 0.000000]
	])
matrix_of_motifM04 = np.array([
	[0.000000, 0.000000, 0.000000, 1.000000],
	[0.026667, 0.160000, 0.533333, 0.280000],
	[0.000000, 0.000000, 0.013333, 0.986667],
	[0.000000, 0.920000, 0.000000, 0.080000],
	[0.986667, 0.000000, 0.013333, 0.000000],
	[0.000000, 0.066667, 0.933333, 0.000000],
	[0.026667, 0.000000, 0.253333, 0.720000],
	[0.933333, 0.000000, 0.040000, 0.026667],
	[1.000000, 0.000000, 0.000000, 0.000000],
	[0.000000, 0.920000, 0.040000, 0.040000]
	])
#create pd &pd_Ebox
seq_pd_igkv1_99 = 'CTCTTCTATTTATAC'
seq_pd_igkv1_subgroup_01 = 'CTCTTCCTTCTATAC'
seq_pd_igkv1_117_2 = 'CTCTTCCTTCTATAT'
seq_pd_igkv1_122 = 'CTCTTGCTTCTATAC'
seq_pd_igkv1_133 = 'CACTTCTTTGTATAC'
seq_pd_igkv1_135 = 'CCCTTCTTTGTATAC'
seq_pd_igkv2_subgroup_01 = 'TGCTAATTTTCATAC'
seq_pd_igkv2_95_2 = 'TGCTAATTCTCATAC'
seq_pd_igkv2_107 = 'TGACTCTTTTTCTAA'
seq_pd_igkv2_109 = 'AGGTACTTTTTACAC'
seq_pd_igkv2_113 = 'TGGTACTTTTCACAC'
seq_pd_igkv2_137 = 'GGCTACTTTTCACAC'
seq_pd_igkv6_subgroup_01 = 'TGACTGTTTATTTAA'
seq_pd_igkv6_32 = 'TGGATATTTATTTAA'
seq_pd_igkv7_33 = 'TGTTGATTGACACCA'
seq_pd_igkv8_24 = 'TGCCTGTTGATTGAC'
seq_pd_igkv8_27 = 'TGCTTGTTGATTGAC'
seq_pd_igkv8_30 = 'TTTTTGTTGATTGAC'
seq_pd_igkv13_64 = 'AATAGAAGTTCTTAG'
seq_pd_igkv13_subgroup_01 = 'AGTTACTGAGATAAC'
seq_pd_igkv15_101 = 'TGTAGGTGGCTCCAG'
seq_pd_igkv15_101_1 = 'TGTAGCAGTTCTTAT'
seq_pd_igkv15_102 = 'TGTACGGTGCTCCAG'
seq_pd_igkv15_103 = 'TGCAGGTGGCTCTAG'
seq_pd_igkv16_104 = 'TGTAGCTATACATAT'
seq_pd_Ebox_igkv3_subgroup_01 = 'GAGCAGGTGCCCTTG'
seq_pd_Ebox_igkv3_5 = 'GGGCAGGTGCACATG'
seq_pd_Ebox_igkv3_10 = 'GGGCAGGTGCACTTG'
seq_pd_Ebox_igkv3_11 = 'AGCAGGTACCCTTTG'
seq_pd_Ebox_igkv5_37 = 'TTCGGGTAACCAGAA'
seq_pd_Ebox_igkv5_subgroup_01 = 'TTCAGGTAATCAGCA'
seq_pd_Ebox_igkv9_119 = 'TGCACTGGTATCCAG'
seq_pd_Ebox_igkv9_subgroup_01 = 'TGCAGCTGTGACCAA'
seq_pd_Ebox_igkv10_subgroup_01 = 'TGCAGCTGTGCTCAG'
seq_pd_Ebox_igkv11_subgroup_01 = 'TGCAGCTTGGCCCAG'
seq_pd_Ebox_igkv12_38 = 'TACAACTGTGCTTAC'
seq_pd_Ebox_igkv12_40 = 'TGCAGCCTTGCCTAC'
seq_pd_Ebox_igkv12_subgroup_01 = 'TGCAGCTGTGCCTAC'
seq_pd_Ebox_igkv12_subgroup_02 = 'TGCAGCTATGCCTAC'
seq_pd_Ebox_igkv13_87 = 'TACATCTGTCCCTAG'
seq_pd_Ebox_igkv14_subgroup_01 = 'TGCACCTGTTCCCAA'
seq_pd_Ebox_igkv14_subgroup_02 = 'TGCACCTGTTCCCAG'
seq_pd_Ebox_igkv17_subgroup_01 = 'TATCAGCTGTGAAGA'

#create core promoter
seq_promoter_IGHV2_2 = 'ATAAAAGCTCACACTAAGCTGAGAAGCTCCATCCTCTTCTCATAGAGCCTCCATCAGAGCATGG'
seq_promoter_IGHV2_3 = 'ATAAAAGCCCACACAAAGATGAGAAGCCCCATCCTCTTCTCATAGAGCCTCCATCAGACCATGG'
seq_promoter_IGKV1_135 = 'ATAAAACCTCAAGTGTCCTCTTGCCTCCACTGATCACTCTCCTATGTTCATTTCCTCAAAATGA'
seq_promoter_IGKV14_111 = 'ATATACCCGTCACACATGTACGGTACCATTGTCATTGCAGCCAGGACTCAGCATGG'
seq_promoter_IGKV19_93 = 'TTTAATAATCTGATCATACACACTCCAACAGTCATTCTTGGTCAGGAGACGTTGTAGAAATGA'
seq_promoter_IGKV6_15 = 'ATTTATAAACCAGGTCTTTGCAGTGAGATCTGAAATACATCAGATCAGCATGGGCATCAAGATGG'
seq_promoter_IGKV9_120 = 'ATATAACAGTCAAACATATCCTGTGCCATTGTCATTGCAGTCAGGACTCAGCATGG'
seq_promoter_IGKV5_43 = 'TTATAAGACGATCTCTATCAGGACAGTGTCATGAGCCACACAAACTCAGGGAAAGCTCGAAGATGG'
seq_promoter_IGKV6_17 = 'ATTTATAAACCAGGTCTTTGCAGTGAGATATGAAATGCATCACACCAGCATGGGCATCAAAATGG'
seq_promoter_IGKV6_23 = 'ATTTATAAACCAGGTCTTTGCAGTGAGATCTGAAATACATCAGACCAGCATGGGCATCAAGATGG'
#create class pwm
ppm_mouse_OCT = simdna.pwm.PWM(name = 'mouse_OCT',probMatrix = matrix_mouse_OCT, pseudocountProb = 0.001)
ppm_mouse_Ebox = simdna.pwm.PWM(name = 'mouse_Ebox',probMatrix = matrix_mouse_Ebox, pseudocountProb = 0.001)
ppm_mouse_PU1 = simdna.pwm.PWM(name = 'mouse_PU1',probMatrix = matrix_mouse_PU1, pseudocountProb = 0.001)
ppm_mouse_Arid3a = simdna.pwm.PWM(name = 'mouse_Arid3a',probMatrix = matrix_mouse_Arid3a, pseudocountProb = 0.001)
ppm_mouse_RUNX1 = simdna.pwm.PWM(name = 'mouse_RUNX1',probMatrix = matrix_mouse_RUNX1, pseudocountProb = 0.001)
ppm_mouse_CCCT = simdna.pwm.PWM(name = 'mouse_CCCT',probMatrix = matrix_mouse_CCCT, pseudocountProb = 0.001)
ppm_mouse_CArGbox = simdna.pwm.PWM(name = 'mouse_CArGbox',probMatrix = matrix_mouse_CArGbox, pseudocountProb = 0.001)
ppm_motifM02 = simdna.pwm.PWM(name = 'motifM02',probMatrix = matrix_of_motifM02,pseudocountProb = 0.001)
ppm_motifM03 = simdna.pwm.PWM(name = 'motifM03',probMatrix = matrix_of_motifM03,pseudocountProb = 0.001)
ppm_motifM04 = simdna.pwm.PWM(name = 'motifM04',probMatrix = matrix_of_motifM04,pseudocountProb = 0.001)
#create Pwmsampler
#exp, bg = {'A': 0.xxx, 'C': 0.xxx, 'G': 0.xxx, 'T': 0.xxx}
mouse_seqbg = {'A': 0.289, 'C': 0.211, 'G': 0.211, 'T': 0.289}
C = 8
sampler_mouse_OCT = synthetic.PwmSampler(ppm_mouse_OCT, bg = mouse_seqbg, minScore = C)
sampler_mouse_Ebox = synthetic.PwmSampler(ppm_mouse_Ebox, bg = mouse_seqbg, minScore = C)
sampler_mouse_PU1 = synthetic.PwmSampler(ppm_mouse_PU1, bg = mouse_seqbg, minScore = C)
sampler_mouse_Arid3a = synthetic.PwmSampler(ppm_mouse_Arid3a, bg = mouse_seqbg, minScore = 5)
sampler_mouse_RUNX1 = synthetic.PwmSampler(ppm_mouse_RUNX1, bg = mouse_seqbg, minScore = C)
sampler_mouse_CCCT = synthetic.BestHitPwm(ppm_mouse_CCCT)
sampler_mouse_CArGbox = synthetic.PwmSampler(ppm_mouse_CArGbox, bg = mouse_seqbg, minScore = C)
sampler_motifM02 = synthetic.PwmSampler(ppm_motifM02, bg = mouse_seqbg, minScore = C)
sampler_motifM03 = synthetic.PwmSampler(ppm_motifM03, bg = mouse_seqbg, minScore = C)
sampler_motifM04 = synthetic.PwmSampler(ppm_motifM04, bg = mouse_seqbg, minScore = C)
#create pd &pd_Ebox substringgenerator
pd_igkv1_99 = synthetic.FixedSubstringGenerator(seq_pd_igkv1_99)
pd_igkv1_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_igkv1_subgroup_01)
pd_igkv1_117_2 = synthetic.FixedSubstringGenerator(seq_pd_igkv1_117_2)
pd_igkv1_122 = synthetic.FixedSubstringGenerator(seq_pd_igkv1_122)
pd_igkv1_133 = synthetic.FixedSubstringGenerator(seq_pd_igkv1_133)
pd_igkv1_135 = synthetic.FixedSubstringGenerator(seq_pd_igkv1_135)
pd_igkv2_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_igkv2_subgroup_01)
pd_igkv2_95_2 = synthetic.FixedSubstringGenerator(seq_pd_igkv2_95_2)
pd_igkv2_107 = synthetic.FixedSubstringGenerator(seq_pd_igkv2_107)
pd_igkv2_109 = synthetic.FixedSubstringGenerator(seq_pd_igkv2_109)
pd_igkv2_113 = synthetic.FixedSubstringGenerator(seq_pd_igkv2_113)
pd_igkv2_137 = synthetic.FixedSubstringGenerator(seq_pd_igkv2_137)
pd_igkv6_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_igkv6_subgroup_01)
pd_igkv6_32 = synthetic.FixedSubstringGenerator(seq_pd_igkv6_32)
pd_igkv7_33 = synthetic.FixedSubstringGenerator(seq_pd_igkv7_33)
pd_igkv8_24 = synthetic.FixedSubstringGenerator(seq_pd_igkv8_24)
pd_igkv8_27 = synthetic.FixedSubstringGenerator(seq_pd_igkv8_27)
pd_igkv8_30 = synthetic.FixedSubstringGenerator(seq_pd_igkv8_30)
pd_igkv13_64 = synthetic.FixedSubstringGenerator(seq_pd_igkv13_64)
pd_igkv13_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_igkv13_subgroup_01)
pd_igkv15_101 = synthetic.FixedSubstringGenerator(seq_pd_igkv15_101)
pd_igkv15_101_1 = synthetic.FixedSubstringGenerator(seq_pd_igkv15_101_1)
pd_igkv15_102 = synthetic.FixedSubstringGenerator(seq_pd_igkv15_102)
pd_igkv15_103 = synthetic.FixedSubstringGenerator(seq_pd_igkv15_103)
pd_igkv16_104 = synthetic.FixedSubstringGenerator(seq_pd_igkv16_104)
pd_Ebox_igkv3_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv3_subgroup_01)
pd_Ebox_igkv3_5 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv3_5)
pd_Ebox_igkv3_10 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv3_10)
pd_Ebox_igkv3_11 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv3_11)
pd_Ebox_igkv5_37 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv5_37)
pd_Ebox_igkv5_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv5_subgroup_01)
pd_Ebox_igkv9_119 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv9_119)
pd_Ebox_igkv9_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv9_subgroup_01)
pd_Ebox_igkv10_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv10_subgroup_01)
pd_Ebox_igkv11_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv11_subgroup_01)
pd_Ebox_igkv12_38 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv12_38)
pd_Ebox_igkv12_40 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv12_40)
pd_Ebox_igkv12_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv12_subgroup_01)
pd_Ebox_igkv12_subgroup_02 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv12_subgroup_02)
pd_Ebox_igkv13_87 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv13_87)
pd_Ebox_igkv14_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv14_subgroup_01)
pd_Ebox_igkv14_subgroup_02 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv14_subgroup_02)
pd_Ebox_igkv17_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_igkv17_subgroup_01)
#create core promoter substringgenerator
promoter_IGHV2_2 = synthetic.FixedSubstringGenerator(seq_promoter_IGHV2_2)
promoter_IGHV2_3 = synthetic.FixedSubstringGenerator(seq_promoter_IGHV2_3)
promoter_IGKV1_135 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV1_135)
promoter_IGKV14_111 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV14_111)
promoter_IGKV19_93 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV19_93)
promoter_IGKV6_15 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV6_15)
promoter_IGKV9_120 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV9_120)
promoter_IGKV5_43 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV5_43)
promoter_IGKV6_17 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV6_17)
promoter_IGKV6_23 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV6_23)
#create position generator
#Sample position uniformly at random
URgenerator = synthetic.UniformPositionGenerator()
#Sample constant position for oct&pd
FP64generator = synthetic.FixedPositionGenerator(pos = 64)
FP96generator = synthetic.FixedPositionGenerator(pos = 96)
FP104generator = synthetic.FixedPositionGenerator(pos = 104)
FP136generator = synthetic.FixedPositionGenerator(pos = 136)
#Sample constant position for CCCT
FP147generator = synthetic.FixedPositionGenerator(pos = 147)
FP154generator = synthetic.FixedPositionGenerator(pos = 154)
FP162generator = synthetic.FixedPositionGenerator(pos = 162)
#Sample constant position for promoter
FP171generator = synthetic.FixedPositionGenerator(pos = 171)
FP172generator = synthetic.FixedPositionGenerator(pos = 172)
FP173generator = synthetic.FixedPositionGenerator(pos = 173)
FP174generator = synthetic.FixedPositionGenerator(pos = 174)
FP181generator = synthetic.FixedPositionGenerator(pos = 181)
#create Embedder
#basic embed substrings 
#core motifs
#pd &pd_Ebox Embedder
#pd &pd_Ebox Embedder pos64
Embedder_mouse_pd_pos64_01 = synthetic.SubstringEmbedder(pd_igkv1_99, FP64generator)
Embedder_mouse_pd_pos64_02 = synthetic.SubstringEmbedder(pd_igkv1_subgroup_01, FP64generator)
Embedder_mouse_pd_pos64_03 = synthetic.SubstringEmbedder(pd_igkv1_117_2, FP64generator)
Embedder_mouse_pd_pos64_04 = synthetic.SubstringEmbedder(pd_igkv1_122, FP64generator)
Embedder_mouse_pd_pos64_05 = synthetic.SubstringEmbedder(pd_igkv1_133, FP64generator)
Embedder_mouse_pd_pos64_06 = synthetic.SubstringEmbedder(pd_igkv1_135, FP64generator)
Embedder_mouse_pd_pos64_07 = synthetic.SubstringEmbedder(pd_igkv2_subgroup_01, FP64generator)
Embedder_mouse_pd_pos64_08 = synthetic.SubstringEmbedder(pd_igkv2_95_2, FP64generator)
Embedder_mouse_pd_pos64_09 = synthetic.SubstringEmbedder(pd_igkv2_107, FP64generator)
Embedder_mouse_pd_pos64_10 = synthetic.SubstringEmbedder(pd_igkv2_109, FP64generator)
Embedder_mouse_pd_pos64_11 = synthetic.SubstringEmbedder(pd_igkv2_113, FP64generator)
Embedder_mouse_pd_pos64_12 = synthetic.SubstringEmbedder(pd_igkv2_137, FP64generator)
Embedder_mouse_pd_pos64_13 = synthetic.SubstringEmbedder(pd_igkv6_subgroup_01, FP64generator)
Embedder_mouse_pd_pos64_14 = synthetic.SubstringEmbedder(pd_igkv6_32, FP64generator)
Embedder_mouse_pd_pos64_15 = synthetic.SubstringEmbedder(pd_igkv7_33, FP64generator)
Embedder_mouse_pd_pos64_16 = synthetic.SubstringEmbedder(pd_igkv8_24, FP64generator)
Embedder_mouse_pd_pos64_17 = synthetic.SubstringEmbedder(pd_igkv8_27, FP64generator)
Embedder_mouse_pd_pos64_18 = synthetic.SubstringEmbedder(pd_igkv8_30, FP64generator)
Embedder_mouse_pd_pos64_19 = synthetic.SubstringEmbedder(pd_igkv13_64, FP64generator)
Embedder_mouse_pd_pos64_20 = synthetic.SubstringEmbedder(pd_igkv13_subgroup_01, FP64generator)
Embedder_mouse_pd_pos64_21 = synthetic.SubstringEmbedder(pd_igkv15_101, FP64generator)
Embedder_mouse_pd_pos64_22 = synthetic.SubstringEmbedder(pd_igkv15_101_1, FP64generator)
Embedder_mouse_pd_pos64_23 = synthetic.SubstringEmbedder(pd_igkv15_102, FP64generator)
Embedder_mouse_pd_pos64_24 = synthetic.SubstringEmbedder(pd_igkv15_103, FP64generator)
Embedder_mouse_pd_pos64_25 = synthetic.SubstringEmbedder(pd_igkv16_104, FP64generator)
Embedder_mouse_pd_Ebox_pos64_01 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_subgroup_01, FP64generator)
Embedder_mouse_pd_Ebox_pos64_02 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_5, FP64generator)
Embedder_mouse_pd_Ebox_pos64_03 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_10, FP64generator)
Embedder_mouse_pd_Ebox_pos64_04 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_11, FP64generator)
Embedder_mouse_pd_Ebox_pos64_05 = synthetic.SubstringEmbedder(pd_Ebox_igkv5_37, FP64generator)
Embedder_mouse_pd_Ebox_pos64_06 = synthetic.SubstringEmbedder(pd_Ebox_igkv5_subgroup_01, FP64generator)
Embedder_mouse_pd_Ebox_pos64_07 = synthetic.SubstringEmbedder(pd_Ebox_igkv9_119, FP64generator)
Embedder_mouse_pd_Ebox_pos64_08 = synthetic.SubstringEmbedder(pd_Ebox_igkv9_subgroup_01, FP64generator)
Embedder_mouse_pd_Ebox_pos64_09 = synthetic.SubstringEmbedder(pd_Ebox_igkv10_subgroup_01, FP64generator)
Embedder_mouse_pd_Ebox_pos64_10 = synthetic.SubstringEmbedder(pd_Ebox_igkv11_subgroup_01, FP64generator)
Embedder_mouse_pd_Ebox_pos64_11 = synthetic.SubstringEmbedder(pd_Ebox_igkv13_87, FP64generator)
Embedder_mouse_pd_Ebox_pos64_12 = synthetic.SubstringEmbedder(pd_Ebox_igkv14_subgroup_01, FP64generator)
Embedder_mouse_pd_Ebox_pos64_13 = synthetic.SubstringEmbedder(pd_Ebox_igkv14_subgroup_02, FP64generator)
Embedder_mouse_pd_Ebox_pos64_14 = synthetic.SubstringEmbedder(pd_Ebox_igkv17_subgroup_01, FP64generator)
RS_Embedder_pos64_listpd = [Embedder_mouse_pd_pos64_01,Embedder_mouse_pd_pos64_02,Embedder_mouse_pd_pos64_03,Embedder_mouse_pd_pos64_04,
                            Embedder_mouse_pd_pos64_05,Embedder_mouse_pd_pos64_06,Embedder_mouse_pd_pos64_07,Embedder_mouse_pd_pos64_08,
                            Embedder_mouse_pd_pos64_09,Embedder_mouse_pd_pos64_10,Embedder_mouse_pd_pos64_11,Embedder_mouse_pd_pos64_12,
                            Embedder_mouse_pd_pos64_13,Embedder_mouse_pd_pos64_14,Embedder_mouse_pd_pos64_15,Embedder_mouse_pd_pos64_16,
                            Embedder_mouse_pd_pos64_17,Embedder_mouse_pd_pos64_18,Embedder_mouse_pd_pos64_19,Embedder_mouse_pd_pos64_20,
                            Embedder_mouse_pd_pos64_21,Embedder_mouse_pd_pos64_22,Embedder_mouse_pd_pos64_23,Embedder_mouse_pd_pos64_24,
                            Embedder_mouse_pd_pos64_25]
RS_Embedder_pos64_listpd_Ebox = [Embedder_mouse_pd_Ebox_pos64_01,Embedder_mouse_pd_Ebox_pos64_02,Embedder_mouse_pd_Ebox_pos64_03,
                                Embedder_mouse_pd_Ebox_pos64_04,Embedder_mouse_pd_Ebox_pos64_05,Embedder_mouse_pd_Ebox_pos64_06,
                                Embedder_mouse_pd_Ebox_pos64_07,Embedder_mouse_pd_Ebox_pos64_08,Embedder_mouse_pd_Ebox_pos64_09,
                                Embedder_mouse_pd_Ebox_pos64_10,Embedder_mouse_pd_Ebox_pos64_11,Embedder_mouse_pd_Ebox_pos64_12,
                                Embedder_mouse_pd_Ebox_pos64_13,Embedder_mouse_pd_Ebox_pos64_14]
RS_Embedder_mouse_pd_pos64 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos64_listpd)
RS_Embedder_mouse_pd_Ebox_pos64 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos64_listpd_Ebox)
#pd &pd_Ebox Embedder pos96
Embedder_mouse_pd_pos96_01 = synthetic.SubstringEmbedder(pd_igkv1_99, FP96generator)
Embedder_mouse_pd_pos96_02 = synthetic.SubstringEmbedder(pd_igkv1_subgroup_01, FP96generator)
Embedder_mouse_pd_pos96_03 = synthetic.SubstringEmbedder(pd_igkv1_117_2, FP96generator)
Embedder_mouse_pd_pos96_04 = synthetic.SubstringEmbedder(pd_igkv1_122, FP96generator)
Embedder_mouse_pd_pos96_05 = synthetic.SubstringEmbedder(pd_igkv1_133, FP96generator)
Embedder_mouse_pd_pos96_06 = synthetic.SubstringEmbedder(pd_igkv1_135, FP96generator)
Embedder_mouse_pd_pos96_07 = synthetic.SubstringEmbedder(pd_igkv2_subgroup_01, FP96generator)
Embedder_mouse_pd_pos96_08 = synthetic.SubstringEmbedder(pd_igkv2_95_2, FP96generator)
Embedder_mouse_pd_pos96_09 = synthetic.SubstringEmbedder(pd_igkv2_107, FP96generator)
Embedder_mouse_pd_pos96_10 = synthetic.SubstringEmbedder(pd_igkv2_109, FP96generator)
Embedder_mouse_pd_pos96_11 = synthetic.SubstringEmbedder(pd_igkv2_113, FP96generator)
Embedder_mouse_pd_pos96_12 = synthetic.SubstringEmbedder(pd_igkv2_137, FP96generator)
Embedder_mouse_pd_pos96_13 = synthetic.SubstringEmbedder(pd_igkv6_subgroup_01, FP96generator)
Embedder_mouse_pd_pos96_14 = synthetic.SubstringEmbedder(pd_igkv6_32, FP96generator)
Embedder_mouse_pd_pos96_15 = synthetic.SubstringEmbedder(pd_igkv7_33, FP96generator)
Embedder_mouse_pd_pos96_16 = synthetic.SubstringEmbedder(pd_igkv8_24, FP96generator)
Embedder_mouse_pd_pos96_17 = synthetic.SubstringEmbedder(pd_igkv8_27, FP96generator)
Embedder_mouse_pd_pos96_18 = synthetic.SubstringEmbedder(pd_igkv8_30, FP96generator)
Embedder_mouse_pd_pos96_19 = synthetic.SubstringEmbedder(pd_igkv13_64, FP96generator)
Embedder_mouse_pd_pos96_20 = synthetic.SubstringEmbedder(pd_igkv13_subgroup_01, FP96generator)
Embedder_mouse_pd_pos96_21 = synthetic.SubstringEmbedder(pd_igkv15_101, FP96generator)
Embedder_mouse_pd_pos96_22 = synthetic.SubstringEmbedder(pd_igkv15_101_1, FP96generator)
Embedder_mouse_pd_pos96_23 = synthetic.SubstringEmbedder(pd_igkv15_102, FP96generator)
Embedder_mouse_pd_pos96_24 = synthetic.SubstringEmbedder(pd_igkv15_103, FP96generator)
Embedder_mouse_pd_pos96_25 = synthetic.SubstringEmbedder(pd_igkv16_104, FP96generator)
Embedder_mouse_pd_Ebox_pos96_01 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_subgroup_01, FP96generator)
Embedder_mouse_pd_Ebox_pos96_02 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_5, FP96generator)
Embedder_mouse_pd_Ebox_pos96_03 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_10, FP96generator)
Embedder_mouse_pd_Ebox_pos96_04 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_11, FP96generator)
Embedder_mouse_pd_Ebox_pos96_05 = synthetic.SubstringEmbedder(pd_Ebox_igkv5_37, FP96generator)
Embedder_mouse_pd_Ebox_pos96_06 = synthetic.SubstringEmbedder(pd_Ebox_igkv5_subgroup_01, FP96generator)
Embedder_mouse_pd_Ebox_pos96_07 = synthetic.SubstringEmbedder(pd_Ebox_igkv9_119, FP96generator)
Embedder_mouse_pd_Ebox_pos96_08 = synthetic.SubstringEmbedder(pd_Ebox_igkv9_subgroup_01, FP96generator)
Embedder_mouse_pd_Ebox_pos96_09 = synthetic.SubstringEmbedder(pd_Ebox_igkv10_subgroup_01, FP96generator)
Embedder_mouse_pd_Ebox_pos96_10 = synthetic.SubstringEmbedder(pd_Ebox_igkv11_subgroup_01, FP96generator)
Embedder_mouse_pd_Ebox_pos96_11 = synthetic.SubstringEmbedder(pd_Ebox_igkv13_87, FP96generator)
Embedder_mouse_pd_Ebox_pos96_12 = synthetic.SubstringEmbedder(pd_Ebox_igkv14_subgroup_01, FP96generator)
Embedder_mouse_pd_Ebox_pos96_13 = synthetic.SubstringEmbedder(pd_Ebox_igkv14_subgroup_02, FP96generator)
Embedder_mouse_pd_Ebox_pos96_14 = synthetic.SubstringEmbedder(pd_Ebox_igkv17_subgroup_01, FP96generator)
RS_Embedder_pos96_listpd = [Embedder_mouse_pd_pos96_01,Embedder_mouse_pd_pos96_02,Embedder_mouse_pd_pos96_03,Embedder_mouse_pd_pos96_04,
                            Embedder_mouse_pd_pos96_05,Embedder_mouse_pd_pos96_06,Embedder_mouse_pd_pos96_07,Embedder_mouse_pd_pos96_08,
                            Embedder_mouse_pd_pos96_09,Embedder_mouse_pd_pos96_10,Embedder_mouse_pd_pos96_11,Embedder_mouse_pd_pos96_12,
                            Embedder_mouse_pd_pos96_13,Embedder_mouse_pd_pos96_14,Embedder_mouse_pd_pos96_15,Embedder_mouse_pd_pos96_16,
                            Embedder_mouse_pd_pos96_17,Embedder_mouse_pd_pos96_18,Embedder_mouse_pd_pos96_19,Embedder_mouse_pd_pos96_20,
                            Embedder_mouse_pd_pos96_21,Embedder_mouse_pd_pos96_22,Embedder_mouse_pd_pos96_23,Embedder_mouse_pd_pos96_24,
                            Embedder_mouse_pd_pos96_25]
RS_Embedder_pos96_listpd_Ebox = [Embedder_mouse_pd_Ebox_pos96_01,Embedder_mouse_pd_Ebox_pos96_02,Embedder_mouse_pd_Ebox_pos96_03,
                                Embedder_mouse_pd_Ebox_pos96_04,Embedder_mouse_pd_Ebox_pos96_05,Embedder_mouse_pd_Ebox_pos96_06,
                                Embedder_mouse_pd_Ebox_pos96_07,Embedder_mouse_pd_Ebox_pos96_08,Embedder_mouse_pd_Ebox_pos96_09,
                                Embedder_mouse_pd_Ebox_pos96_10,Embedder_mouse_pd_Ebox_pos96_11,Embedder_mouse_pd_Ebox_pos96_12,
                                Embedder_mouse_pd_Ebox_pos96_13,Embedder_mouse_pd_Ebox_pos96_14]
RS_Embedder_mouse_pd_pos96 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos96_listpd)
RS_Embedder_mouse_pd_Ebox_pos96 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos96_listpd_Ebox)
#pd &pd_Ebox Embedder pos104
Embedder_mouse_pd_pos104_01 = synthetic.SubstringEmbedder(pd_igkv1_99, FP104generator)
Embedder_mouse_pd_pos104_02 = synthetic.SubstringEmbedder(pd_igkv1_subgroup_01, FP104generator)
Embedder_mouse_pd_pos104_03 = synthetic.SubstringEmbedder(pd_igkv1_117_2, FP104generator)
Embedder_mouse_pd_pos104_04 = synthetic.SubstringEmbedder(pd_igkv1_122, FP104generator)
Embedder_mouse_pd_pos104_05 = synthetic.SubstringEmbedder(pd_igkv1_133, FP104generator)
Embedder_mouse_pd_pos104_06 = synthetic.SubstringEmbedder(pd_igkv1_135, FP104generator)
Embedder_mouse_pd_pos104_07 = synthetic.SubstringEmbedder(pd_igkv2_subgroup_01, FP104generator)
Embedder_mouse_pd_pos104_08 = synthetic.SubstringEmbedder(pd_igkv2_95_2, FP104generator)
Embedder_mouse_pd_pos104_09 = synthetic.SubstringEmbedder(pd_igkv2_107, FP104generator)
Embedder_mouse_pd_pos104_10 = synthetic.SubstringEmbedder(pd_igkv2_109, FP104generator)
Embedder_mouse_pd_pos104_11 = synthetic.SubstringEmbedder(pd_igkv2_113, FP104generator)
Embedder_mouse_pd_pos104_12 = synthetic.SubstringEmbedder(pd_igkv2_137, FP104generator)
Embedder_mouse_pd_pos104_13 = synthetic.SubstringEmbedder(pd_igkv6_subgroup_01, FP104generator)
Embedder_mouse_pd_pos104_14 = synthetic.SubstringEmbedder(pd_igkv6_32, FP104generator)
Embedder_mouse_pd_pos104_15 = synthetic.SubstringEmbedder(pd_igkv7_33, FP104generator)
Embedder_mouse_pd_pos104_16 = synthetic.SubstringEmbedder(pd_igkv8_24, FP104generator)
Embedder_mouse_pd_pos104_17 = synthetic.SubstringEmbedder(pd_igkv8_27, FP104generator)
Embedder_mouse_pd_pos104_18 = synthetic.SubstringEmbedder(pd_igkv8_30, FP104generator)
Embedder_mouse_pd_pos104_19 = synthetic.SubstringEmbedder(pd_igkv13_64, FP104generator)
Embedder_mouse_pd_pos104_20 = synthetic.SubstringEmbedder(pd_igkv13_subgroup_01, FP104generator)
Embedder_mouse_pd_pos104_21 = synthetic.SubstringEmbedder(pd_igkv15_101, FP104generator)
Embedder_mouse_pd_pos104_22 = synthetic.SubstringEmbedder(pd_igkv15_101_1, FP104generator)
Embedder_mouse_pd_pos104_23 = synthetic.SubstringEmbedder(pd_igkv15_102, FP104generator)
Embedder_mouse_pd_pos104_24 = synthetic.SubstringEmbedder(pd_igkv15_103, FP104generator)
Embedder_mouse_pd_pos104_25 = synthetic.SubstringEmbedder(pd_igkv16_104, FP104generator)
Embedder_mouse_pd_Ebox_pos104_01 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_subgroup_01, FP104generator)
Embedder_mouse_pd_Ebox_pos104_02 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_5, FP104generator)
Embedder_mouse_pd_Ebox_pos104_03 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_10, FP104generator)
Embedder_mouse_pd_Ebox_pos104_04 = synthetic.SubstringEmbedder(pd_Ebox_igkv3_11, FP104generator)
Embedder_mouse_pd_Ebox_pos104_05 = synthetic.SubstringEmbedder(pd_Ebox_igkv5_37, FP104generator)
Embedder_mouse_pd_Ebox_pos104_06 = synthetic.SubstringEmbedder(pd_Ebox_igkv5_subgroup_01, FP104generator)
Embedder_mouse_pd_Ebox_pos104_07 = synthetic.SubstringEmbedder(pd_Ebox_igkv9_119, FP104generator)
Embedder_mouse_pd_Ebox_pos104_08 = synthetic.SubstringEmbedder(pd_Ebox_igkv9_subgroup_01, FP104generator)
Embedder_mouse_pd_Ebox_pos104_09 = synthetic.SubstringEmbedder(pd_Ebox_igkv10_subgroup_01, FP104generator)
Embedder_mouse_pd_Ebox_pos104_10 = synthetic.SubstringEmbedder(pd_Ebox_igkv11_subgroup_01, FP104generator)
Embedder_mouse_pd_Ebox_pos104_11 = synthetic.SubstringEmbedder(pd_Ebox_igkv13_87, FP104generator)
Embedder_mouse_pd_Ebox_pos104_12 = synthetic.SubstringEmbedder(pd_Ebox_igkv14_subgroup_01, FP104generator)
Embedder_mouse_pd_Ebox_pos104_13 = synthetic.SubstringEmbedder(pd_Ebox_igkv14_subgroup_02, FP104generator)
Embedder_mouse_pd_Ebox_pos104_14 = synthetic.SubstringEmbedder(pd_Ebox_igkv17_subgroup_01, FP104generator)
RS_Embedder_pos104_listpd = [Embedder_mouse_pd_pos104_01,Embedder_mouse_pd_pos104_02,Embedder_mouse_pd_pos104_03,Embedder_mouse_pd_pos104_04,
                            Embedder_mouse_pd_pos104_05,Embedder_mouse_pd_pos104_06,Embedder_mouse_pd_pos104_07,Embedder_mouse_pd_pos104_08,
                            Embedder_mouse_pd_pos104_09,Embedder_mouse_pd_pos104_10,Embedder_mouse_pd_pos104_11,Embedder_mouse_pd_pos104_12,
                            Embedder_mouse_pd_pos104_13,Embedder_mouse_pd_pos104_14,Embedder_mouse_pd_pos104_15,Embedder_mouse_pd_pos104_16,
                            Embedder_mouse_pd_pos104_17,Embedder_mouse_pd_pos104_18,Embedder_mouse_pd_pos104_19,Embedder_mouse_pd_pos104_20,
                            Embedder_mouse_pd_pos104_21,Embedder_mouse_pd_pos104_22,Embedder_mouse_pd_pos104_23,Embedder_mouse_pd_pos104_24,
                            Embedder_mouse_pd_pos104_25]
RS_Embedder_pos104_listpd_Ebox = [Embedder_mouse_pd_Ebox_pos104_01,Embedder_mouse_pd_Ebox_pos104_02,Embedder_mouse_pd_Ebox_pos104_03,
                                Embedder_mouse_pd_Ebox_pos104_04,Embedder_mouse_pd_Ebox_pos104_05,Embedder_mouse_pd_Ebox_pos104_06,
                                Embedder_mouse_pd_Ebox_pos104_07,Embedder_mouse_pd_Ebox_pos104_08,Embedder_mouse_pd_Ebox_pos104_09,
                                Embedder_mouse_pd_Ebox_pos104_10,Embedder_mouse_pd_Ebox_pos104_11,Embedder_mouse_pd_Ebox_pos104_12,
                                Embedder_mouse_pd_Ebox_pos104_13,Embedder_mouse_pd_Ebox_pos104_14]
RS_Embedder_mouse_pd_pos104 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos104_listpd)
RS_Embedder_mouse_pd_Ebox_pos104 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos104_listpd_Ebox)


XOREmbedder_mouse_pd_pos64 = synthetic.XOREmbedder(RS_Embedder_mouse_pd_Ebox_pos64, RS_Embedder_mouse_pd_pos64, 0.5)
XOREmbedder_mouse_pd_pos96 = synthetic.XOREmbedder(RS_Embedder_mouse_pd_Ebox_pos96, RS_Embedder_mouse_pd_pos96, 0.5)
XOREmbedder_mouse_pd_pos104 = synthetic.XOREmbedder(RS_Embedder_mouse_pd_Ebox_pos104, RS_Embedder_mouse_pd_pos104, 0.5)
RS_Embedder_mouse_pd = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), [XOREmbedder_mouse_pd_pos64, XOREmbedder_mouse_pd_pos96, XOREmbedder_mouse_pd_pos104])
Embedder_mouse_OCT_pos136 = synthetic.SubstringEmbedder(substringGenerator = sampler_mouse_OCT, positionGenerator = FP136generator)
#noncore motifs
Embedder_mouse_Ebox = synthetic.SubstringEmbedder(substringGenerator = sampler_mouse_Ebox, positionGenerator = URgenerator)
Embedder_mouse_PU1 = synthetic.SubstringEmbedder(substringGenerator = sampler_mouse_PU1, positionGenerator = URgenerator)
Embedder_mouse_Arid3a = synthetic.SubstringEmbedder(substringGenerator = sampler_mouse_Arid3a, positionGenerator = URgenerator)
Embedder_mouse_RUNX1 = synthetic.SubstringEmbedder(substringGenerator = sampler_mouse_RUNX1, positionGenerator = URgenerator)
Embedder_mouse_CArGbox = synthetic.SubstringEmbedder(substringGenerator = sampler_mouse_CArGbox, positionGenerator = URgenerator)
Embedder_motifM02 = synthetic.SubstringEmbedder(substringGenerator = sampler_motifM02, positionGenerator = URgenerator)
Embedder_motifM03 = synthetic.SubstringEmbedder(substringGenerator = sampler_motifM03, positionGenerator = URgenerator)
Embedder_motifM04 = synthetic.SubstringEmbedder(substringGenerator = sampler_motifM04, positionGenerator = URgenerator)
#motif_CCCT
Embedder_CCCT_pos147 = synthetic.SubstringEmbedder(sampler_mouse_CCCT, FP147generator)
Embedder_CCCT_pos154 = synthetic.SubstringEmbedder(sampler_mouse_CCCT, FP154generator)
Embedder_CCCT_pos162 = synthetic.SubstringEmbedder(sampler_mouse_CCCT, FP162generator)
#RandomSubsetEmbedders
RS_Embedder_list01 = [Embedder_mouse_Ebox, Embedder_mouse_Arid3a, Embedder_mouse_PU1, Embedder_mouse_RUNX1,Embedder_mouse_CArGbox]
RS_Embedder_list02 = [Embedder_motifM02, Embedder_motifM03, Embedder_motifM04]
RS_Embedder_list03 = [Embedder_CCCT_pos147, Embedder_CCCT_pos154, Embedder_CCCT_pos162]
RS_Embedders_mouse_01 = synthetic.RandomSubsetOfEmbedders(synthetic.ChooseValueFromASet([0,1,2,3,4,5]), RS_Embedder_list01)
RS_Embedders_mouse_02 = synthetic.RandomSubsetOfEmbedders(synthetic.ChooseValueFromASet([0,1,2,3]), RS_Embedder_list02)
RS_Embedder_CCCT_01 = synthetic.RandomSubsetOfEmbedders(synthetic.ChooseValueFromASet([0,1,2]), RS_Embedder_list03)
#core promoter Embedders
Embedder_promoter_IGHV2_2 = synthetic.SubstringEmbedder(promoter_IGHV2_2, FP173generator, synthetic.DefaultNameMixin('promoter_IGHV2_2'))
Embedder_promoter_IGHV2_3 = synthetic.SubstringEmbedder(promoter_IGHV2_3, FP173generator, synthetic.DefaultNameMixin('promoter_IGHV2_3'))
Embedder_promoter_IGKV1_135 = synthetic.SubstringEmbedder(promoter_IGKV1_135, FP173generator, synthetic.DefaultNameMixin('promoter_IGKV1_135'))
Embedder_promoter_IGKV14_111 = synthetic.SubstringEmbedder(promoter_IGKV14_111, FP181generator, synthetic.DefaultNameMixin('promoter_IGKV14_111'))
Embedder_promoter_IGKV19_93 = synthetic.SubstringEmbedder(promoter_IGKV19_93, FP174generator, synthetic.DefaultNameMixin('promoter_IGKV19_93'))
Embedder_promoter_IGKV6_15 = synthetic.SubstringEmbedder(promoter_IGKV6_15, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV6_15'))
Embedder_promoter_IGKV9_120 = synthetic.SubstringEmbedder(promoter_IGKV9_120, FP181generator, synthetic.DefaultNameMixin('promoter_IGKV9_120'))
Embedder_promoter_IGKV5_43 = synthetic.SubstringEmbedder(promoter_IGKV5_43, FP171generator, synthetic.DefaultNameMixin('promoter_IGKV5_43'))
Embedder_promoter_IGKV6_17 = synthetic.SubstringEmbedder(promoter_IGKV6_17, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV6_17'))
Embedder_promoter_IGKV6_23 = synthetic.SubstringEmbedder(promoter_IGKV6_23, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV6_23'))
RS_Embedder_promoter_list = [Embedder_promoter_IGHV2_2, Embedder_promoter_IGHV2_3, Embedder_promoter_IGKV1_135, Embedder_promoter_IGKV14_111,
                             Embedder_promoter_IGKV19_93, Embedder_promoter_IGKV6_15, Embedder_promoter_IGKV9_120, Embedder_promoter_IGKV5_43,
                             Embedder_promoter_IGKV6_17, Embedder_promoter_IGKV6_23]
RS_Embedder_promoter = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_promoter_list)
#bg generator
mouse_kmer2_bg = synthetic.BackgroundFromSimData('./biasaway_seq(197times)/BiasAway_kmer=2,mouse,(197times).simdna')

#combines the bg and substring
total_Embedder_list = [RS_Embedder_mouse_pd, Embedder_mouse_OCT_pos136, RS_Embedder_CCCT_01, RS_Embedder_promoter, RS_Embedders_mouse_01, RS_Embedders_mouse_02]

seq_set = synthetic.EmbedInABackground(backgroundGenerator = mouse_kmer2_bg, embedders = total_Embedder_list)
generated_sequences = synthetic.GenerateSequenceNTimes(seq_set, 1970)
synthetic.printSequences("m_library_kmer2bg(OCT+136|PD+64,+96,+104).simdata", generated_sequences, 
                         includeFasta=True, includeEmbeddings=True, prefix="m_library_kmer2bg(OCT+136|PD+64,+96,+104)")
