import simdna
import simdna.synthetic as synthetic
import simdna.simdnautil.util as util
import simdna.simdnautil.pwm as pwm
import numpy as np

# create a PWM object to represent the motif (must PPM matrix!!!!)
# create matrix of motifs
matrix_human_OCT = np.array([
	[0.930435, 0.069565, 0, 0],
	[0, 0, 0, 1],
	[0, 0, 0, 1],
	[0, 0.008696, 0, 0.991304],
	[0, 0.008696, 0.973913, 0.017391],
	[0, 1, 0, 0],
	[0.973913, 0.008696, 0, 0.017391],
	[0, 0, 0, 1]
	])
matrix_human_Ebox = np.array([
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
matrix_human_EBF = np.array([
	[0.718912, 0.074482, 0.107513, 0.099093],
	[0.166343, 0.178641, 0.216181, 0.438835],
	[0.020408, 0.127965, 0, 0.851627],
	[0, 0.997416, 0.001938, 0.000646],
	[0.001912, 0.984066, 0.002549, 0.011472],
	[0, 0.996129, 0, 0.003871],
	[0.363754, 0.253074, 0.040777, 0.342395],
	[0.503238, 0.04987, 0.134715, 0.312176],
	[0.013367, 0.003819, 0.982813, 0],
	[0.064497, 0.004822, 0.930681, 0],
	[0.003817, 0, 0.982188, 0.013995],
	[0.925105, 0.010186, 0.05033, 0.01438],
	[0.391192, 0.379534, 0.093912, 0.135363],
	[0.161917, 0.235751, 0.052461, 0.549870]
	])
matrix_human_PU1 = np.array([
	[0.785714, 0.071429, 0.142857, 0],
	[0.095238, 0, 0.880952, 0.02381],
	[0.095238, 0, 0.904762, 0],
	[1, 0, 0, 0],
	[0.97619, 0, 0.02381, 0],
	[0.119048, 0.071429, 0.785714, 0.02381],
	[0.071429, 0.119048, 0.047619, 0.761905]
	])
matrix_human_RUNX1 = np.array([
	[0.384615, 0.076923, 0.115385, 0.423077],
	[0.461538, 0.076923, 0.038462, 0.423077],
	[0.153846, 0.269231, 0.038462, 0.538462],
	[0.038462, 0.038462, 0, 0.923077],
	[0.076923, 0, 0.884615, 0.038462],
	[0.076923, 0.307692, 0, 0.615385],
	[0, 0, 1, 0],
	[0, 0, 1, 0],
	[0, 0.038462, 0, 0.961538],
	[0.307692, 0.076923, 0, 0.615385],
	[0.500000, 0.076923, 0.153846, 0.269231]
	])
matrix_human_CCCT = np.array([
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 0, 0 ,1]
	])
matrix_human_CArGbox = np.array([
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
matrix_of_motifH02 = np.array([
	[0.066116, 0.636364, 0.206612, 0.090909],
	[0.181818, 0.809917, 0, 0.008264],
	[0.024793, 0.975207, 0, 0],
	[0.719008, 0, 0, 0.280992],
	[0.016529, 0.371901, 0.570248, 0.041322],
	[0.057851, 0.900826, 0, 0.041322],
	[0.140496, 0.669421, 0, 0.190083],
	[0, 1, 0, 0],
	[0.214876, 0.008264, 0, 0.77686],
	[0, 0.123967, 0.793388, 0.082645]
	])
matrix_of_motifH03 = np.array([
	[0.14876, 0.123967, 0.123967, 0.603306],
	[0.016529, 0.371901, 0.61157, 0],
	[0.545455, 0, 0.008264, 0.446281],
	[0.008264, 0, 0.991736, 0],
	[0.057851, 0.214876, 0.181818, 0.545455],
	[0, 0.801653, 0.181818, 0.016529],
	[0.024793, 0.975207, 0, 0],
	[0, 0, 0, 1],
	[0, 0.008264, 0.991736, 0],
	[0.694215, 0.033058, 0.256198, 0.016529]
	])
matrix_of_motifH04 = np.array([
	[0.016529, 0.942149, 0, 0.041322],
	[0.008264, 0.231405, 0, 0.760331],
	[0, 0.92562, 0.07438, 0],
	[0.049587, 0, 0, 0.950413],
	[0.057851, 0, 0.92562, 0.016529],
	[0.165289, 0.016529, 0.760331, 0.057851],
	[0.082645, 0, 0.917355, 0],
	[0.677686, 0, 0.247934, 0.07438]
	])
#create pd &pd_Ebox
seq_pd_IGKV2_4 = 'TGGATATTTCTTCAC'
seq_pd_IGKV2_subgroup_01 = 'TGGCTCTTTCCACCC'
seq_pd_IGKV2_subgroup_02 = 'TGGCTCTTTCCACAC'
seq_pd_IGKV2_24 = 'ATGTTATTTCTACAC'
seq_pd_IGKV2_26 = 'TGTTGCGCTTAGCAT'
seq_pd_IGKV2_28 = 'TGACTCTTTCCACAC'
seq_pd_IGKV2_40 = 'CAACCTTTTCCACAC'
seq_pd_IGKV4_1 = 'TGGCTCTTGATTTAC'
seq_pd_Ebox_IGKV1_subgroup01 = 'TGCAGCTGTGCCCAG'
seq_pd_Ebox_IGKV1_subgroup02 = 'TGCAGCTGCGCCCAG'
seq_pd_Ebox_IGKV1_27 = 'TGCAGTGTTATTGAG'
seq_pd_Ebox_IGKV1_32 = 'TGCAGGTAAAGTCAT'
seq_pd_Ebox_IGKV1_37 = 'CGCAGCTGTGCCCAG'
seq_pd_Ebox_IGKV1_39 = 'TGCAGCTGTGCTCAG'
seq_pd_Ebox_IGKV1D_32 = 'TGCAGATAAAGTCAT'
seq_pd_Ebox_IGKV1D_42 = 'CGCAGCTGTATCCAG'
seq_pd_Ebox_IGKV1D_43 = 'ATCCCCTGTGCCCAG'
seq_pd_Ebox_IGKV3_subgroup01 = 'TGCAGCTGGAAGCTC'
seq_pd_Ebox_IGKV3_15 = 'TGCAGCTGAAAGCTC'
seq_pd_Ebox_IGKV3_20 = 'TGCAGCTGCAAGCCC'
seq_pd_Ebox_IGKV3_25 = 'TTCTAATGTCACTAA'
seq_pd_Ebox_IGKV3_31 = 'TGCAGTTTCGAAGCC'
seq_pd_Ebox_IGKV3_subgroup02 = 'TGCAGCTGGAAGCCC'
seq_pd_Ebox_IGKV3D_20 = 'TGAAGCTGGAAGCCC'
seq_pd_Ebox_IGKV5_2 = 'TGCACAGCTGTGAAG'
seq_pd_Ebox_IGKV6_subgroup01 = 'TGCAGGTGCCAGCAG'

#create core promoter
seq_promoter_IGHV4_39 = 'TTAAATTCAGGTCCAACTCATAAGGGAAATGCTTTCTGAGAGTCATGGATCTCATGTGCAAGAAAATGA'
seq_promoter_IGHV4_34 = 'TTAAATTCAGGGTCCAGCTCACATGGGAAGTGCTTTCTGAGAGTCATGGACCTCCTGCACAAGAACATGA'
seq_promoter_IGKV1_5 = 'TTATTAATAGGCTGGTCACACTTTGTGCAGGAGTCAGACCCAGTCAGGACACAGCATGG'
seq_promoter_IGKV1_39 = 'TTTTTTATGGGCTGGTCGCACCCTGTGCAGGAGTCAGTCTCAGTCAGGACACAGCATGG' 
seq_promoter_IGKV3_20 = 'ATATCAATGCCTGGGTCAGAGCTCTGGAGAAGAGCTGCTCAGTTAGGACCCAGAGGGAACCATGG'
seq_promoter_IGKV2_28 = 'ATAAAAGCTCAGCTGTAACTGTGCCTTGACTGATCAGGACTCCTCAGTTCACCTTCTCACAATGA'
seq_promoter_IGKV1_6 = 'TTATTAACAGGCTGATCACACCCTGTGCAGGAGTCAGACCCACTCAGGACACAGCATGG' 
seq_promoter_IGKV1_17 = 'TTATTAATAGGCTGGACACACTTCATGCAGGAATCAGTCCCACTCAGGACACAGCATGG'
seq_promoter_IGKV4_1 = 'TTTTATAAACGGGCCGTTTGCATTGTGAACTGAGCTACAACAGGCAGGCAGGGGCAGCAAGATGG' 
seq_promoter_IGKV3_15 = 'ATATCAATGCCTGGGTCAGAGCTCTGGGGAGGAACTGCTCAGTTAGGACCCAGACGGAACCATGG' 
#create class pwm
ppm_human_OCT = simdna.pwm.PWM(name = 'human_OCT',probMatrix = matrix_human_OCT, pseudocountProb = 0.001)
ppm_human_Ebox = simdna.pwm.PWM(name = 'human_Ebox',probMatrix = matrix_human_Ebox, pseudocountProb = 0.001)
ppm_human_EBF = simdna.pwm.PWM(name = 'human_EBF',probMatrix = matrix_human_EBF, pseudocountProb = 0.001)
ppm_human_PU1 = simdna.pwm.PWM(name = 'human_PU1',probMatrix = matrix_human_PU1, pseudocountProb = 0.001)
ppm_human_RUNX1 = simdna.pwm.PWM(name = 'human_RUNX1',probMatrix = matrix_human_RUNX1, pseudocountProb = 0.001)
ppm_human_CCCT = simdna.pwm.PWM(name = 'human_CCCT',probMatrix = matrix_human_CCCT, pseudocountProb = 0.001)
ppm_human_CArGbox = simdna.pwm.PWM(name = 'human_CArGbox',probMatrix = matrix_human_CArGbox, pseudocountProb = 0.001)
ppm_motifH02 = simdna.pwm.PWM(name = 'motifH02',probMatrix = matrix_of_motifH02,pseudocountProb = 0.001)
ppm_motifH03 = simdna.pwm.PWM(name = 'motifH03',probMatrix = matrix_of_motifH03,pseudocountProb = 0.001)
ppm_motifH04 = simdna.pwm.PWM(name = 'motifH04',probMatrix = matrix_of_motifH04,pseudocountProb = 0.001)

#create Pwmsampler
#exp, bg = {'A': 0.xxx, 'C': 0.xxx, 'G': 0.xxx, 'T': 0.xxx}
human_seqbg = {'A': 0.235, 'C': 0.265, 'G': 0.265, 'T': 0.235}
C = 8
sampler_human_OCT = synthetic.PwmSampler(ppm_human_OCT, bg = human_seqbg, minScore = C)
sampler_human_Ebox = synthetic.PwmSampler(ppm_human_Ebox, bg = human_seqbg, minScore = C)
sampler_human_EBF = synthetic.PwmSampler(ppm_human_EBF, bg = human_seqbg, minScore = C)
sampler_human_PU1 = synthetic.PwmSampler(ppm_human_PU1, bg = human_seqbg, minScore = C)
sampler_human_RUNX1 = synthetic.PwmSampler(ppm_human_RUNX1, bg = human_seqbg, minScore = C)
sampler_human_CCCT = synthetic.BestHitPwm(ppm_human_CCCT)
sampler_human_CArGbox = synthetic.PwmSampler(ppm_human_CArGbox, bg = human_seqbg, minScore = C)
sampler_motifH02 = synthetic.PwmSampler(ppm_motifH02, bg = human_seqbg, minScore = C)
sampler_motifH03 = synthetic.PwmSampler(ppm_motifH03, bg = human_seqbg, minScore = C)
sampler_motifH04 = synthetic.PwmSampler(ppm_motifH04, bg = human_seqbg, minScore = C)
#create pd &pd_Ebox substringgenerator
pd_IGKV2_4 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_4)
pd_IGKV2_subgroup_01 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_subgroup_01)
pd_IGKV2_subgroup_02 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_subgroup_02)
pd_IGKV2_24 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_24)
pd_IGKV2_26 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_26)
pd_IGKV2_28 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_28)
pd_IGKV2_40 = synthetic.FixedSubstringGenerator(seq_pd_IGKV2_40)
pd_IGKV4_1 = synthetic.FixedSubstringGenerator(seq_pd_IGKV4_1)
pd_Ebox_IGKV1_subgroup01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1_subgroup01)
pd_Ebox_IGKV1_subgroup02 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1_subgroup02)
pd_Ebox_IGKV1_27 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1_27)
pd_Ebox_IGKV1_32 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1_32)
pd_Ebox_IGKV1_37 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1_37)
pd_Ebox_IGKV1_39 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1_39)
pd_Ebox_IGKV1D_32 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1D_32)
pd_Ebox_IGKV1D_42 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1D_42)
pd_Ebox_IGKV1D_43 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV1D_43)
pd_Ebox_IGKV3_subgroup01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3_subgroup01)
pd_Ebox_IGKV3_15 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3_15)
pd_Ebox_IGKV3_20 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3_20)
pd_Ebox_IGKV3_25 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3_25)
pd_Ebox_IGKV3_31 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3_31)
pd_Ebox_IGKV3_subgroup02 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3_subgroup02)   
pd_Ebox_IGKV3D_20 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV3D_20)   
pd_Ebox_IGKV5_2 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV5_2)   
pd_Ebox_IGKV6_subgroup01 = synthetic.FixedSubstringGenerator(seq_pd_Ebox_IGKV6_subgroup01)             
#create core promoter substringgenerator
promoter_IGHV4_39 = synthetic.FixedSubstringGenerator(seq_promoter_IGHV4_39)
promoter_IGHV4_34 = synthetic.FixedSubstringGenerator(seq_promoter_IGHV4_34)
promoter_IGKV1_5 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV1_5)
promoter_IGKV1_39 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV1_39)
promoter_IGKV3_20 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV3_20)
promoter_IGKV2_28 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV2_28)
promoter_IGKV1_6 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV1_6)
promoter_IGKV1_17 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV1_17)
promoter_IGKV4_1 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV4_1)
promoter_IGKV3_15 = synthetic.FixedSubstringGenerator(seq_promoter_IGKV3_15)
#create position generator
#Sample position uniformly at random
URgenerator = synthetic.UniformPositionGenerator()
#Sample constant position for oct&pd
FP26generator = synthetic.FixedPositionGenerator(pos = 26)
FP56generator = synthetic.FixedPositionGenerator(pos = 56)
FP96generator = synthetic.FixedPositionGenerator(pos = 96)
FP126generator = synthetic.FixedPositionGenerator(pos = 126)
#Sample constant position for CCCT
FP137generator = synthetic.FixedPositionGenerator(pos = 137)
FP144generator = synthetic.FixedPositionGenerator(pos = 144)
FP147generator = synthetic.FixedPositionGenerator(pos = 147)
FP151generator = synthetic.FixedPositionGenerator(pos = 151)
FP156generator = synthetic.FixedPositionGenerator(pos = 156)
FP158generator = synthetic.FixedPositionGenerator(pos = 158)
FP161generator = synthetic.FixedPositionGenerator(pos = 161)
#Sample constant position for promoter
FP167generator = synthetic.FixedPositionGenerator(pos = 167)
FP168generator = synthetic.FixedPositionGenerator(pos = 168)
FP172generator = synthetic.FixedPositionGenerator(pos = 172)
FP178generator = synthetic.FixedPositionGenerator(pos = 178)
#basic embed substrings 
#core motifs
#pd &pd_Ebox Embedder
#pd &pd_Ebox Embedder pos26
Embedder_human_pd_pos26_01 = synthetic.SubstringEmbedder(pd_IGKV2_4, FP26generator)
Embedder_human_pd_pos26_02 = synthetic.SubstringEmbedder(pd_IGKV2_subgroup_01, FP26generator)
Embedder_human_pd_pos26_03 = synthetic.SubstringEmbedder(pd_IGKV2_subgroup_02, FP26generator)
Embedder_human_pd_pos26_04 = synthetic.SubstringEmbedder(pd_IGKV2_24, FP26generator)
Embedder_human_pd_pos26_05 = synthetic.SubstringEmbedder(pd_IGKV2_26, FP26generator)
Embedder_human_pd_pos26_06 = synthetic.SubstringEmbedder(pd_IGKV2_28, FP26generator)
Embedder_human_pd_pos26_07 = synthetic.SubstringEmbedder(pd_IGKV2_40, FP26generator)
Embedder_human_pd_pos26_08 = synthetic.SubstringEmbedder(pd_IGKV4_1, FP26generator)
Embedder_human_pd_Ebox_pos26_01 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_subgroup01, FP26generator)
Embedder_human_pd_Ebox_pos26_02 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_subgroup02, FP26generator)
Embedder_human_pd_Ebox_pos26_03 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_27, FP26generator)
Embedder_human_pd_Ebox_pos26_04 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_32, FP26generator)
Embedder_human_pd_Ebox_pos26_05 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_37, FP26generator)
Embedder_human_pd_Ebox_pos26_06 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_39, FP26generator)
Embedder_human_pd_Ebox_pos26_07 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1D_32, FP26generator)
Embedder_human_pd_Ebox_pos26_08 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1D_43, FP26generator)
Embedder_human_pd_Ebox_pos26_09 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_subgroup01, FP26generator)
Embedder_human_pd_Ebox_pos26_10 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_15, FP26generator)
Embedder_human_pd_Ebox_pos26_11 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_20, FP26generator)
Embedder_human_pd_Ebox_pos26_12 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_25, FP26generator)
Embedder_human_pd_Ebox_pos26_13 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_31, FP26generator)
Embedder_human_pd_Ebox_pos26_14 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_subgroup02, FP26generator)
Embedder_human_pd_Ebox_pos26_15 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3D_20, FP26generator)
Embedder_human_pd_Ebox_pos26_16 = synthetic.SubstringEmbedder(pd_Ebox_IGKV5_2, FP26generator)
Embedder_human_pd_Ebox_pos26_17 = synthetic.SubstringEmbedder(pd_Ebox_IGKV6_subgroup01, FP26generator)
RS_Embedder_pos26_listpd = [Embedder_human_pd_pos26_01,Embedder_human_pd_pos26_02,Embedder_human_pd_pos26_03,Embedder_human_pd_pos26_04,
                            Embedder_human_pd_pos26_05,Embedder_human_pd_pos26_06,Embedder_human_pd_pos26_07,Embedder_human_pd_pos26_08]
RS_Embedder_pos26_listpd_Ebox = [Embedder_human_pd_Ebox_pos26_01,Embedder_human_pd_Ebox_pos26_02,Embedder_human_pd_Ebox_pos26_03,
                                Embedder_human_pd_Ebox_pos26_04,Embedder_human_pd_Ebox_pos26_05,Embedder_human_pd_Ebox_pos26_06,
                                Embedder_human_pd_Ebox_pos26_07,Embedder_human_pd_Ebox_pos26_08,Embedder_human_pd_Ebox_pos26_09,
                                Embedder_human_pd_Ebox_pos26_10,Embedder_human_pd_Ebox_pos26_11,Embedder_human_pd_Ebox_pos26_12,
                                Embedder_human_pd_Ebox_pos26_13,Embedder_human_pd_Ebox_pos26_14,Embedder_human_pd_Ebox_pos26_15,
                                Embedder_human_pd_Ebox_pos26_16,Embedder_human_pd_Ebox_pos26_17]
RS_Embedder_human_pd_pos26 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos26_listpd)
RS_Embedder_human_pd_Ebox_pos26 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1),RS_Embedder_pos26_listpd_Ebox)
#pd &pd_Ebox Embedder pos56
Embedder_human_pd_pos56_01 = synthetic.SubstringEmbedder(pd_IGKV2_4, FP56generator)
Embedder_human_pd_pos56_02 = synthetic.SubstringEmbedder(pd_IGKV2_subgroup_01, FP56generator)
Embedder_human_pd_pos56_03 = synthetic.SubstringEmbedder(pd_IGKV2_subgroup_02, FP56generator)
Embedder_human_pd_pos56_04 = synthetic.SubstringEmbedder(pd_IGKV2_24, FP56generator)
Embedder_human_pd_pos56_05 = synthetic.SubstringEmbedder(pd_IGKV2_26, FP56generator)
Embedder_human_pd_pos56_06 = synthetic.SubstringEmbedder(pd_IGKV2_28, FP56generator)
Embedder_human_pd_pos56_07 = synthetic.SubstringEmbedder(pd_IGKV2_40, FP56generator)
Embedder_human_pd_pos56_08 = synthetic.SubstringEmbedder(pd_IGKV4_1, FP56generator)
Embedder_human_pd_Ebox_pos56_01 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_subgroup01, FP56generator)
Embedder_human_pd_Ebox_pos56_02 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_subgroup02, FP56generator)
Embedder_human_pd_Ebox_pos56_03 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_27, FP56generator)
Embedder_human_pd_Ebox_pos56_04 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_32, FP56generator)
Embedder_human_pd_Ebox_pos56_05 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_37, FP56generator)
Embedder_human_pd_Ebox_pos56_06 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_39, FP56generator)
Embedder_human_pd_Ebox_pos56_07 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1D_32, FP56generator)
Embedder_human_pd_Ebox_pos56_08 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1D_43, FP56generator)
Embedder_human_pd_Ebox_pos56_09 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_subgroup01, FP56generator)
Embedder_human_pd_Ebox_pos56_10 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_15, FP56generator)
Embedder_human_pd_Ebox_pos56_11 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_20, FP56generator)
Embedder_human_pd_Ebox_pos56_12 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_25, FP56generator)
Embedder_human_pd_Ebox_pos56_13 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_31, FP56generator)
Embedder_human_pd_Ebox_pos56_14 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_subgroup02, FP56generator)
Embedder_human_pd_Ebox_pos56_15 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3D_20, FP56generator)
Embedder_human_pd_Ebox_pos56_16 = synthetic.SubstringEmbedder(pd_Ebox_IGKV5_2, FP56generator)
Embedder_human_pd_Ebox_pos56_17 = synthetic.SubstringEmbedder(pd_Ebox_IGKV6_subgroup01, FP56generator)
RS_Embedder_pos56_listpd = [Embedder_human_pd_pos56_01,Embedder_human_pd_pos56_02,Embedder_human_pd_pos56_03,Embedder_human_pd_pos56_04,
                            Embedder_human_pd_pos56_05,Embedder_human_pd_pos56_06,Embedder_human_pd_pos56_07,Embedder_human_pd_pos56_08]
RS_Embedder_pos56_listpd_Ebox = [Embedder_human_pd_Ebox_pos56_01,Embedder_human_pd_Ebox_pos56_02,Embedder_human_pd_Ebox_pos56_03,
                                Embedder_human_pd_Ebox_pos56_04,Embedder_human_pd_Ebox_pos56_05,Embedder_human_pd_Ebox_pos56_06,
                                Embedder_human_pd_Ebox_pos56_07,Embedder_human_pd_Ebox_pos56_08,Embedder_human_pd_Ebox_pos56_09,
                                Embedder_human_pd_Ebox_pos56_10,Embedder_human_pd_Ebox_pos56_11,Embedder_human_pd_Ebox_pos56_12,
                                Embedder_human_pd_Ebox_pos56_13,Embedder_human_pd_Ebox_pos56_14,Embedder_human_pd_Ebox_pos56_15,
                                Embedder_human_pd_Ebox_pos56_16,Embedder_human_pd_Ebox_pos56_17]
RS_Embedder_human_pd_pos56 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_pos56_listpd)
RS_Embedder_human_pd_Ebox_pos56 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_pos56_listpd_Ebox)
#pd &pd_Ebox Embedder pos96
Embedder_human_pd_pos96_01 = synthetic.SubstringEmbedder(pd_IGKV2_4, FP96generator)
Embedder_human_pd_pos96_02 = synthetic.SubstringEmbedder(pd_IGKV2_subgroup_01, FP96generator)
Embedder_human_pd_pos96_03 = synthetic.SubstringEmbedder(pd_IGKV2_subgroup_02, FP96generator)
Embedder_human_pd_pos96_04 = synthetic.SubstringEmbedder(pd_IGKV2_24, FP96generator)
Embedder_human_pd_pos96_05 = synthetic.SubstringEmbedder(pd_IGKV2_26, FP96generator)
Embedder_human_pd_pos96_06 = synthetic.SubstringEmbedder(pd_IGKV2_28, FP96generator)
Embedder_human_pd_pos96_07 = synthetic.SubstringEmbedder(pd_IGKV2_40, FP96generator)
Embedder_human_pd_pos96_08 = synthetic.SubstringEmbedder(pd_IGKV4_1, FP96generator)
Embedder_human_pd_Ebox_pos96_01 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_subgroup01, FP96generator)
Embedder_human_pd_Ebox_pos96_02 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_subgroup02, FP96generator)
Embedder_human_pd_Ebox_pos96_03 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_27, FP96generator)
Embedder_human_pd_Ebox_pos96_04 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_32, FP96generator)
Embedder_human_pd_Ebox_pos96_05 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_37, FP96generator)
Embedder_human_pd_Ebox_pos96_06 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1_39, FP96generator)
Embedder_human_pd_Ebox_pos96_07 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1D_32, FP96generator)
Embedder_human_pd_Ebox_pos96_08 = synthetic.SubstringEmbedder(pd_Ebox_IGKV1D_43, FP96generator)
Embedder_human_pd_Ebox_pos96_09 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_subgroup01, FP96generator)
Embedder_human_pd_Ebox_pos96_10 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_15, FP96generator)
Embedder_human_pd_Ebox_pos96_11 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_20, FP96generator)
Embedder_human_pd_Ebox_pos96_12 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_25, FP96generator)
Embedder_human_pd_Ebox_pos96_13 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_31, FP96generator)
Embedder_human_pd_Ebox_pos96_14 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3_subgroup02, FP96generator)
Embedder_human_pd_Ebox_pos96_15 = synthetic.SubstringEmbedder(pd_Ebox_IGKV3D_20, FP96generator)
Embedder_human_pd_Ebox_pos96_16 = synthetic.SubstringEmbedder(pd_Ebox_IGKV5_2, FP96generator)
Embedder_human_pd_Ebox_pos96_17 = synthetic.SubstringEmbedder(pd_Ebox_IGKV6_subgroup01, FP96generator)
RS_Embedder_pos96_listpd = [Embedder_human_pd_pos96_01,Embedder_human_pd_pos96_02,Embedder_human_pd_pos96_03,Embedder_human_pd_pos96_04,
                            Embedder_human_pd_pos96_05,Embedder_human_pd_pos96_06,Embedder_human_pd_pos96_07,Embedder_human_pd_pos96_08]
RS_Embedder_pos96_listpd_Ebox = [Embedder_human_pd_Ebox_pos96_01,Embedder_human_pd_Ebox_pos96_02,Embedder_human_pd_Ebox_pos96_03,
                                Embedder_human_pd_Ebox_pos96_04,Embedder_human_pd_Ebox_pos96_05,Embedder_human_pd_Ebox_pos96_06,
                                Embedder_human_pd_Ebox_pos96_07,Embedder_human_pd_Ebox_pos96_08,Embedder_human_pd_Ebox_pos96_09,
                                Embedder_human_pd_Ebox_pos96_10,Embedder_human_pd_Ebox_pos96_11,Embedder_human_pd_Ebox_pos96_12,
                                Embedder_human_pd_Ebox_pos96_13,Embedder_human_pd_Ebox_pos96_14,Embedder_human_pd_Ebox_pos96_15,
                                Embedder_human_pd_Ebox_pos96_16,Embedder_human_pd_Ebox_pos96_17]
RS_Embedder_human_pd_pos96 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_pos96_listpd)
RS_Embedder_human_pd_Ebox_pos96 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_pos96_listpd_Ebox)

XOREmbedder_human_pd_pos26 = synthetic.XOREmbedder(RS_Embedder_human_pd_Ebox_pos26, RS_Embedder_human_pd_pos26, 0.715)
XOREmbedder_human_pd_pos56 = synthetic.XOREmbedder(RS_Embedder_human_pd_Ebox_pos56, RS_Embedder_human_pd_pos56, 0.715)
XOREmbedder_human_pd_pos96 = synthetic.XOREmbedder(RS_Embedder_human_pd_Ebox_pos96, RS_Embedder_human_pd_pos96, 0.715)
RS_Embedder_human_pd = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), [XOREmbedder_human_pd_pos26, XOREmbedder_human_pd_pos56, XOREmbedder_human_pd_pos96])
Embedder_human_OCT_pos126 = synthetic.SubstringEmbedder(substringGenerator = sampler_human_OCT, positionGenerator = FP126generator)
#noncore motifs
Embedder_human_Ebox = synthetic.SubstringEmbedder(substringGenerator = sampler_human_Ebox, positionGenerator = URgenerator)
Embedder_human_EBF = synthetic.SubstringEmbedder(substringGenerator = sampler_human_EBF, positionGenerator = URgenerator)
Embedder_human_PU1 = synthetic.SubstringEmbedder(substringGenerator = sampler_human_PU1, positionGenerator = URgenerator)
Embedder_human_RUNX1 = synthetic.SubstringEmbedder(substringGenerator = sampler_human_RUNX1, positionGenerator = URgenerator)
Embedder_human_CArGbox = synthetic.SubstringEmbedder(substringGenerator = sampler_human_CArGbox, positionGenerator = URgenerator)
Embedder_motifH02 = synthetic.SubstringEmbedder(substringGenerator = sampler_motifH02, positionGenerator = URgenerator)
Embedder_motifH03 = synthetic.SubstringEmbedder(substringGenerator = sampler_motifH03, positionGenerator = URgenerator)
Embedder_motifH04 = synthetic.SubstringEmbedder(substringGenerator = sampler_motifH04, positionGenerator = URgenerator)
#motif_CCCT
Embedder_CCCT_pos137 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP137generator)
Embedder_CCCT_pos144 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP144generator)
Embedder_CCCT_pos147 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP147generator)
Embedder_CCCT_pos151 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP151generator)
Embedder_CCCT_pos156 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP156generator)
Embedder_CCCT_pos158 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP158generator)
Embedder_CCCT_pos161 = synthetic.SubstringEmbedder(sampler_human_CCCT, FP161generator)
#motif_CCCT_pair
Embedder_CCCT_pair137and144 = synthetic.AllEmbedders([Embedder_CCCT_pos137, Embedder_CCCT_pos144])
Embedder_CCCT_pair137and147 = synthetic.AllEmbedders([Embedder_CCCT_pos137, Embedder_CCCT_pos147])
Embedder_CCCT_pair144and151 = synthetic.AllEmbedders([Embedder_CCCT_pos144, Embedder_CCCT_pos151])
Embedder_CCCT_pair151and158 = synthetic.AllEmbedders([Embedder_CCCT_pos151, Embedder_CCCT_pos158])
Embedder_CCCT_pair151and161 = synthetic.AllEmbedders([Embedder_CCCT_pos151, Embedder_CCCT_pos161])
Embedder_CCCT_pair156and161 = synthetic.AllEmbedders([Embedder_CCCT_pos156, Embedder_CCCT_pos161])
#RandomSubsetEmbedders
RS_Embedder_list01 = [Embedder_human_Ebox, Embedder_human_EBF, Embedder_human_PU1, Embedder_human_RUNX1,Embedder_human_CArGbox]
RS_Embedder_list02 = [Embedder_motifH02, Embedder_motifH03, Embedder_motifH04]
RS_Embedder_list03 = [Embedder_CCCT_pos137, Embedder_CCCT_pos144, Embedder_CCCT_pos151, Embedder_CCCT_pos156, Embedder_CCCT_pos161]
RS_Embedder_list04 = [Embedder_CCCT_pair137and144, Embedder_CCCT_pair137and147, Embedder_CCCT_pair144and151,
                      Embedder_CCCT_pair151and158, Embedder_CCCT_pair151and161, Embedder_CCCT_pair156and161]
RS_Embedders_human_01 = synthetic.RandomSubsetOfEmbedders(synthetic.ChooseValueFromASet([0,1,2,3,4,5]), RS_Embedder_list01)
RS_Embedders_human_02 = synthetic.RandomSubsetOfEmbedders(synthetic.ChooseValueFromASet([0,1,2,3]), RS_Embedder_list02)
RS_Embedder_CCCT_01 = synthetic.RandomSubsetOfEmbedders(synthetic.ChooseValueFromASet([0,1]), RS_Embedder_list03)
RS_Embedder_CCCT_02 = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_list04)
XOREmbedder_CCCT = synthetic.XOREmbedder(RS_Embedder_CCCT_01, RS_Embedder_CCCT_02, 0.6)
#core promoter Embedders
Embedder_promoter_IGHV4_39 = synthetic.SubstringEmbedder(promoter_IGHV4_39, FP168generator, synthetic.DefaultNameMixin('promoter_IGHV4_39'))
Embedder_promoter_IGHV4_34 = synthetic.SubstringEmbedder(promoter_IGHV4_34, FP167generator, synthetic.DefaultNameMixin('promoter_IGHV4_34'))
Embedder_promoter_IGKV1_5 = synthetic.SubstringEmbedder(promoter_IGKV1_5, FP178generator, synthetic.DefaultNameMixin('promoter_IGKV1_5'))
Embedder_promoter_IGKV1_39 = synthetic.SubstringEmbedder(promoter_IGKV1_39, FP178generator, synthetic.DefaultNameMixin('promoter_IGKV1_39'))
Embedder_promoter_IGKV3_20 = synthetic.SubstringEmbedder(promoter_IGKV3_20, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV3_20'))
Embedder_promoter_IGKV2_28 = synthetic.SubstringEmbedder(promoter_IGKV2_28, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV2_28'))
Embedder_promoter_IGKV1_6 = synthetic.SubstringEmbedder(promoter_IGKV1_6, FP178generator, synthetic.DefaultNameMixin('promoter_IGKV1_6'))
Embedder_promoter_IGKV1_17 = synthetic.SubstringEmbedder(promoter_IGKV1_17, FP178generator, synthetic.DefaultNameMixin('promoter_IGKV1_17'))
Embedder_promoter_IGKV4_1 = synthetic.SubstringEmbedder(promoter_IGKV4_1, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV4_1'))
Embedder_promoter_IGKV3_15 = synthetic.SubstringEmbedder(promoter_IGKV3_15, FP172generator, synthetic.DefaultNameMixin('promoter_IGKV3_15'))
RS_Embedder_promoter_list = [Embedder_promoter_IGHV4_39, Embedder_promoter_IGHV4_34, Embedder_promoter_IGKV1_5, Embedder_promoter_IGKV1_39,
                             Embedder_promoter_IGKV3_20, Embedder_promoter_IGKV2_28, Embedder_promoter_IGKV1_6, Embedder_promoter_IGKV1_17,
                             Embedder_promoter_IGKV4_1, Embedder_promoter_IGKV3_15]
RS_Embedder_promoter = synthetic.RandomSubsetOfEmbedders(synthetic.FixedQuantityGenerator(1), RS_Embedder_promoter_list)
#bg generator
zero_order_bg = synthetic.ZeroOrderBackgroundGenerator(seqLength=238, discreteDistribution = human_seqbg)

#combines the bg and substring
total_Embedder_list = [RS_Embedder_human_pd, Embedder_human_OCT_pos126, XOREmbedder_CCCT, RS_Embedder_promoter, RS_Embedders_human_01, RS_Embedders_human_02]

seq_set = synthetic.EmbedInABackground(backgroundGenerator = zero_order_bg, embedders = total_Embedder_list)
generated_sequences = synthetic.GenerateSequenceNTimes(seq_set, 1970)
synthetic.printSequences("h_library_zerobg(OCT+126|PD+26,+56,+96).simdata", generated_sequences, 
                         includeFasta=True, includeEmbeddings=True, prefix="h_library_zerobg(OCT+126|PD+26,+56,+96)")