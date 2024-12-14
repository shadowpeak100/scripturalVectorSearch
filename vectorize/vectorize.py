import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
import json
from shared.bomVectorizedLine import BomVectorizedLine


def main():
    load_dotenv()
    BomJsonPath = os.getenv("BOM_JSON_PATH")
    BomOutputVectorFilePath = os.getenv("BOM_OUTPUT_VECTOR_FILEPATH")

    iterateFile(BomJsonPath, BomOutputVectorFilePath)

def iterateFile(inputFilePath, outputFilePath):
    with open(inputFilePath) as inputFile, open(outputFilePath, 'w') as outputFile:
        for line in inputFile:
            data = json.loads(line)
            vectorEntry = BomVectorizedLine()
            vectorEntry.from_dict(data)
            embeddings = None
            if "verse" in data:
                embeddings = get_embeddings(data["verse"])
                #embeddings = [-0.013431912, -0.016207842, -0.00020827459, -0.046129026, -0.020953784, 0.029550208, -0.005897249, 0.0095750345, -0.011538653, -0.01764058, 0.0060635493, 0.021184046, 0.0057949107, 0.00558064, 0.0020435695, 0.013674966, 0.04075626, -0.011621802, 0.005967607, 0.0023074108, 0.0025952375, -0.00051449024, 0.0059100417, -0.017858047, -0.013099313, 0.010873453, 0.011852064, -0.026633564, 0.0083405785, -0.03535791, 0.004921837, -0.01436575, -0.013150482, -0.028577993, -0.026659148, -0.024957772, -0.0045476616, -0.0073235906, 0.012293398, 0.014506466, 0.003917641, -0.002705571, -0.0062074624, 0.0036266164, -0.012325379, -0.0089482125, -0.00040895378, -0.0307271, -0.022974966, 0.0048738653, 0.036330126, -0.014161074, -0.024228612, -0.006309801, 0.011973591, -0.0041862796, 0.01765337, 0.014161074, -0.015286796, -0.016860249, 0.0009946012, 0.028066302, 0.009984388, 0.017551033, -0.023102889, -0.0024753097, -0.012510867, 0.0018612794, -0.0027343535, 0.004349381, -0.0012792298, -0.003054161, 0.0013311985, -0.012120702, 0.0124852825, -0.011033357, -0.027094087, 0.009293605, -0.007912036, 0.0009066541, -0.012274209, -0.019521046, -0.0008378955, 0.0026464066, 0.0044549177, -0.0043174005, 0.008398144, 0.031494636, -0.0077521326, -0.03963054, 0.020531638, 0.02399835, 0.017474279, 0.02388322, -0.019776892, 0.0015198849, -0.017602202, 0.0199304, 0.00029162443, -0.024701927, -0.025507841, 0.004643604, -0.0027567402, 0.0018580812, -0.029626962, -0.028270978, -0.007892848, -0.016540442, 0.026019534, -0.03175048, 0.0032492436, 0.0021714924, -4.9919945e-05, -0.018433701, 0.020199038, -0.0022690338, 0.012945806, -0.0025472662, -0.01177531, 0.0015670565, 0.0016214238, 0.009792504, 0.012210248, -0.022629574, 0.0009362363, 0.020736314, -0.03223659, -0.022757499, 0.013713343, 0.008065544, 0.0194315, 0.008545255, 0.008781913, 0.008679574, -0.00060963293, 0.009843674, -0.017883632, 0.0034731089, -0.0035498627, -0.011474691, 0.009869258, -0.00015740523, -0.017858047, -0.010540853, 0.013278405, 0.016412519, 0.010598418, 0.0018676755, 0.0073107984, -0.022309767, 0.02071073, 0.0019588205, 0.027375517, 0.01091183, 0.007918432, -0.003310007, 0.0042566373, 0.03597194, -0.015849657, -0.012901032, 0.0026831843, 0.0056893746, 0.010540853, -0.014519258, -0.031699315, 0.023614582, 0.0055486592, -0.039272353, -0.0069462177, -0.010067538, 0.009664581, 0.021925999, -0.022156259, 0.013150482, -0.003738549, 0.0060731433, 0.014352958, -0.0061690854, -0.024177443, 0.0018740717, -0.0091337, 0.01659161, 0.037788447, 0.01177531, -0.0066839755, -0.016412519, 0.019239616, -0.0040103854, -0.025175242, -0.0066775796, 0.0023234012, 0.016463688, -0.019009354, -0.0023761692, -0.6660182, -0.004896252, -0.010598418, -0.0064633084, 0.011417125, 0.007643398, -0.0016837862, 0.014020358, -0.007982394, 0.021081707, 0.007515475, 0.021184046, 0.008385351, -0.02021183, -0.0026703922, -0.024561211, -0.012248625, -0.020480469, -0.008398144, -0.019968776, 0.0052160593, -0.0076689827, 0.0031676928, -0.005801307, -0.011832875, 0.024139065, 0.008059148, -0.015120496, -0.004592435, 0.017013757, -0.01135956, 0.023077305, 0.026812656, 0.022412106, 0.04587318, -0.007387552, -0.007828887, 0.035537004, 0.016386934, 0.022962175, -0.042956535, -0.0117241405, 0.000986606, 0.022847043, -0.009261624, 0.009408735, 0.017678956, 0.031776067, 0.03451362, 0.0007015776, 0.016169464, -0.016156672, -3.805209e-05, -0.0047971117, -0.009562243, -0.0031660937, 0.026403302, -0.007995186, 0.024970565, -0.01552985, 0.004003989, 0.011666575, -0.005299209, 0.009530262, -0.0026863825, 0.008257428, -0.011768914, 0.011736933, -0.0009634199, -0.0052640303, 0.017551033, 0.010169877, -0.0014671166, -0.008219051, 0.008487689, -0.0007851273, 0.038018707, -0.013457498, -0.0023841646, -0.01709051, -0.014352958, -0.014378543, -0.03333673, -0.016898625, 0.014288996, -0.00679271, -0.040321324, 0.0055870363, -0.009319189, -0.008052751, -0.008813893, 0.0076753786, -0.002313807, -0.01514608, -0.0039752065, -0.012913825, -0.037583772, -0.018420909, 0.011896837, 0.0024737106, 0.023576206, -0.005724553, 0.009901239, -0.006153095, 0.034001928, -0.0038376893, 0.005142504, 0.026185833, 0.011468295, -0.013572628, -0.005922834, -0.0055134804, -0.003828095, 0.0050913347, -0.006754333, -0.027042918, -0.004339787, 0.009658185, 0.00235858, 0.008283013, 0.011308392, 0.021324761, -0.009319189, -0.0017317573, 0.0077137556, 0.028296562, -0.020186245, 0.00704216, -0.008270221, -0.010118707, 0.0027439478, -0.0040359697, 0.019162862, 0.0045220773, 0.024471665, -0.042879783, 0.015299588, -0.021682944, 0.016834663, -0.0065272697, 0.005711761, 0.01514608, 0.014058735, -0.0042822217, -0.006437724, -0.022360936, 0.022974966, -0.011142091, -0.03456479, 0.0033132052, -0.0008722748, 0.0053151995, -0.03251802, -0.0010785506, 0.011071734, 0.0054015475, 0.00091145124, -0.003132514, 0.020032737, -0.019009354, -0.0056126206, 0.022987759, -0.0395282, -0.0023937586, 0.017000964, -0.025136866, -0.017435903, 0.026083495, 0.0044165407, -0.014941404, -0.018740715, 0.005705365, -0.012056741, 0.00027343538, -0.0027359526, 0.00050049863, -0.0049602133, -0.005238446, 0.014186658, 0.00823824, -0.016821872, -0.0022674347, -0.02271912, -0.009587827, 0.020019947, -0.0077073593, -0.012235832, -0.008481293, 0.025239203, 0.019124486, 0.0055966303, 0.008468501, 0.005155296, 0.0043589757, 0.0041479026, 0.009760523, 0.015337965, -0.0043781637, 0.009856465, 0.025047319, -0.025354335, 0.008430124, 0.023077305, -0.0044005504, 0.006888652, -0.032773867, 0.0058588726, -0.0013831672, 0.0039624143, -0.00063841563, -0.011238034, -0.015619395, -0.0040135835, -0.024241405, 0.0111356955, 0.0042278543, 0.016348556, 0.007880055, 0.001355184, -0.011845668, 0.016898625, -0.00308934, 0.020621184, -0.009331982, -0.030522423, 0.03812105, 0.007918432, 0.019341955, 0.0062042642, -0.016770702, 0.0072340444, -0.0031660937, 0.0023601789, 0.023448281, -0.005666988, 0.019265201, 0.009581431, -0.045463827, 0.010137896, -0.0017509458, -0.008577236, 0.0033771666, 0.009984388, -0.011922422, 0.008455709, -0.003735351, 0.015005365, -0.009069739, -0.013150482, 0.025354335, -0.0036170222, 0.0096517885, -0.026070703, -0.010227442, 0.0028942574, -0.046461627, -0.01569615, 0.03262036, 0.0195978, 0.034385696, 0.006101926, 0.014544843, -0.0076753786, -0.006741541, 0.034462452, -0.008244636, 0.016271804, -0.021030538, -0.043058876, -0.012466094, -0.0034986935, 0.013674966, 0.011429918, 0.0007463506, 0.009268019, -0.0021347147, 0.00036478037, -0.0049282326, 0.009191266, 0.0071956674, -0.012996974, -0.005033769, 0.01709051, 0.016796287, 0.015465888, -0.023090098, -0.016540442, -0.002539271, -0.030880608, -0.015517057, 0.001308812, 0.004199072, -0.0052224556, -0.01038095, 0.005500688, 0.0022130676, 0.04643604, -0.016386934, 0.009376754, -0.0034986935, -0.011730537, 0.0037673316, -0.010585627, 0.006191472, 0.012005571, -0.0008978594, -0.009702958, -0.0065560527, 0.0010697559, -0.018190647, -0.010112312, -0.009037758, -0.00567978, -0.008129505, 0.012625998, -0.025098488, -0.027733702, 0.017435903, -0.013150482, -0.019546632, -0.0037097663, -0.01514608, -0.03617662, 0.025367126, 0.10632958, -0.0014759114, -0.0070997253, 0.014378543, 0.010272215, 0.020864237, 0.011212449, -0.030445669, 0.037072077, 8.939618e-05, 0.0058236937, -0.023678543, 0.011167676, -0.012414925, -0.0052960115, -0.0075858324, 0.006440922, -0.012498075, -0.02265516, -0.007182875, -0.0043301927, 0.017269602, 0.03295296, -0.0032380503, 0.002742349, -0.016668364, 0.037507016, 0.01619505, -0.00938315, 0.0019220427, -0.016220633, 0.006434526, 0.017806878, 0.01272194, -0.006233047, 0.03144347, 0.007956809, 0.023090098, 0.016297387, -0.008052751, 0.023102889, -0.001441532, 0.008781913, -0.021567814, 0.0003086142, -0.00835337, -0.007266025, 0.01486465, -0.0026959768, -0.00971575, 0.011986383, -0.036483634, -0.01169216, -0.018996563, 0.01135956, -0.009236039, 0.035767265, 0.005407944, -0.008775516, 0.02265516, -0.026966164, -0.035178818, 0.01292022, 0.016169464, -0.016079918, -0.013406328, -0.01881747, 0.029882807, -0.037072077, 0.004640406, -0.03128996, 0.00030601575, -0.040218983, -0.018894223, 0.03361816, 0.012338171, 0.01564498, -0.0013367952, 0.0025616577, -0.013009767, 0.009197662, -0.015018158, 0.005411142, -0.01702655, 0.015990373, 0.024548419, -0.0013663773, -0.0001247249, -0.008775516, 0.0039272355, -0.0022914202, -0.021836452, 0.0028254988, 0.0044357292, -0.0013280004, 0.009325585, 0.02343549, 0.00024425294, -0.02398556, -0.01898377, 0.021056121, -0.01647648, -0.0074515133, -0.0031596976, 0.022412106, 0.022744706, -0.009638997, 0.015120496, -0.024292573, -0.020570016, 0.030855022, -0.030803854, 0.044466026, -0.017973179, -0.014493673, 0.05863989, 0.005654196, 0.008468501, 0.018663963, -0.029243194, -0.018024348, -0.028936177, 0.02688941, -0.0009546252, -0.027631363, -0.009415131, 0.0044069467, -0.0035690512, 0.0032364514, 0.02120963, -0.003310007, 0.02845007, -0.0076178135, -0.0070165754, -0.023294775, -0.021196837, -0.013790097, 0.010617607, -0.009159286, -0.0032492436, -0.005327992, -0.02717084, -0.00757304, -0.023947181, 0.02660798, -0.03412985, -0.0118008945, -0.01503095, -0.0038504817, 0.024881018, -0.0024097492, -0.003908047, -0.018958185, 0.011468295, -0.0012152683, -0.010221045, -0.00046132223, 0.008532463, 0.012530056, 0.0054751034, 0.022911005, -0.0043653715, -0.02065956, 0.023627374, -0.0069334256, 0.007777717, -0.010572834, -0.009402338, -0.03200633, 0.01469835, 0.015465888, 0.011148487, 0.026198626, -0.013956397, 0.0045316713, 0.02177249, 0.0029470257, -0.018344155, -0.007790509, -0.04042366, -0.013764513, 0.0034283358, 0.01199278, 0.027784871, -0.006181878, -0.013994774, 0.032441266, -0.0038952546, -0.018305779, -0.009082532, 0.03428336, -0.028296562, 0.038939755, 0.010739134, 0.019393124, -0.024817057, 0.023563413, 0.0067095603, 0.007841678, 0.01531238, 0.0058620702, 0.028066302, -0.0028958565, -0.0037257567, -0.018459287, 0.00025364727, -0.002961417, -0.020953784, 0.0011409131, 0.0052672285, -0.010508873, -0.004861073, 0.008129505, -0.016386934, 0.026787072, -0.015222834, -0.012862655, 0.017512655, -0.017295187, -0.003946424, -0.016770702, 0.0025584595, 0.023729712, -0.0051297112, 0.015210042, 0.03479505, -0.015542642, -0.016873041, 0.008135902, 0.02399835, 0.007182875, 0.03144347, 0.020122284, -0.008500482, -0.0034539204, -0.0022210628, 0.0026288172, -0.008647594, -0.021503853, 0.021350345, 0.002064357, -0.01659161, 0.0043557775, -0.0015622594, -0.006837483, 0.024305366, -0.0074898903, 0.0015670565, -0.025495049, -0.0139308125, -0.01453205, -0.0015270805, -0.019917607, 0.030087484, 0.0057821185, -0.017883632, -0.0049602133, -0.004323797, -0.0043142023, 0.01764058, -0.028603578, -0.005711761, 0.016233426, 0.0018836658, 0.0017493467, 0.012101513, -0.0026224211, 0.0010249829, -0.038530402, 0.02032696, -0.021004952, -0.012050345, 0.009741335, 0.0025088894, -7.520472e-05, -0.0006755932, -0.016322972, 5.096931e-06, 0.014071528, 0.0028622765, -0.004509285, -0.00270717, 0.0015390733, -0.014762311, -0.013124897, -0.011180468, -0.0005228852, 0.002998195, -0.0027407499, -0.007880055, -0.022898212, -0.015222834, 0.01692421, 0.016054334, -0.008506878, 0.002662397, 0.0011856861, 0.017474279, -0.007182875, 0.015747318, -0.004761933, -0.0010185867, -0.012088722, -0.006105124, 0.002536073, 0.011340372, 0.016527649, -0.012926617, -0.024023935, 0.002878267, 0.0014159475, 0.012753921, 0.01235736, -0.02220743, -0.013291198, -0.006354574, 0.018062724, -0.0146727655, 0.0042566373, 0.012824278, 0.020122284, 0.0058620702, 0.021414306, -0.014493673, -0.005251238, -0.0059644086, -0.010515269, 0.01569615, -0.0493271, -0.005727751, -0.0015862449, 7.0607486e-05, -0.0050913347, -0.0050049867, 0.0064313277, 0.0024017538, 0.0012560438, 0.010969396, -0.02282146, -0.0058908532, 0.00584608, 0.010809491, 0.0041574966, 0.0025888414, -0.0012120702, 0.01004835, -0.0015094911, -0.028270978, -0.032543607, -0.015504265, -0.0077073593, 0.035639342, 0.028680332, 0.016438102, -0.013508666, 0.00092104543, -0.051783223, -0.013393536, 0.012344567, 0.016860249, 0.006044361, 0.010093123, 0.010041954, 0.009511073, -0.016489271, -0.008634801, -0.025495049, -0.0072724214, -0.0021219223, -0.023729712, 0.0044133426, -0.0012896236, -0.0040519605, -0.015619395, 0.013854058, -0.023422698, 0.013611005, -0.006373762, -0.0003367972, 4.6247154e-05, 0.0034283358, 0.021785283, 0.01358542, -0.0030269774, 0.009504677, -0.012881844, 0.009939616, -0.013738927, 0.0118776485, -0.021670152, -0.020685146, 0.01160901, 0.009830881, -0.010534457, -0.0030397698, -0.008487689, -0.00044053476, 0.017448694, 0.009255228, -0.006863068, -0.018011555, 0.028936177, -0.019968776, -0.025431087, -0.008692366, 0.029473454, 0.01587524, -0.018113894, -0.0081103165, -0.008737139, 0.011954403, 0.006351376, 0.0023809664, -0.004419739, -0.010668776, 0.001632617, 0.0002426539, -0.009172077, -0.012350963, 0.026531225, -0.009274416, -0.006607222, 0.0017781294, -0.011730537, -0.0071253097, -0.0197641, 0.0045828405, -0.0074898903, -0.0040359697, 0.024970565, 0.011551444, -0.0070613483, -0.021670152, 0.008526066, 0.00076074194, 0.004761933, 0.21982284, -0.001529479, -0.025367126, 0.019892024, 0.004678783, 0.00793762, 0.01642531, -0.0053471806, -0.004851479, 0.008673178, -0.02137593, -0.007681775, -0.0040167817, 0.0050401655, 0.003828095, -0.048406053, -0.019840853, 0.0012736331, -0.008219051, -0.05623494, 0.017794086, -0.01469835, 0.014659973, -0.018625585, 0.02466355, 0.032748282, -0.027042918, 0.00086987624, 0.030445669, 0.006009182, 0.00074595085, -0.006741541, 0.0005916438, -0.015734525, -0.004985798, -0.010304196, 0.032313343, -0.0008075138, 0.0026224211, -0.036432464, 0.010822284, 0.007432325, 0.02605791, -0.020250207, -0.00488346, 0.037327927, -0.005017779, -0.021465475, -0.047305916, -0.020071115, -0.024548419, -0.0022050724, 0.012274209, 0.0010185867, -0.010067538, -0.012830675, 0.0044964924, 0.016860249, -0.02182366, -0.025674142, 0.015568227, 0.011756121, -0.023704128, 0.014736727, 0.0096709775, 0.028347732, -0.019290784, -0.00976692, 0.020493262, -0.028475655, 0.008123109, -0.03870949, 0.0023090097, 0.030778268, -0.012568433, -0.0075858324, 0.011122903, 0.0030669533, 0.0021251205, -0.0068694637, 0.012325379, -0.041063275, -0.009479092, -0.0076625864, -0.021977168, -0.05495571, 0.004042366, 0.004288618, -0.025367126, 0.019687347, 0.013080125, 0.007483494, -0.015401927, 0.00037737278, 0.0011281208, -0.0052544363, 0.0014591215, 0.026096288, -0.00868597, 0.01536355, -0.013457498, 0.00782249, 0.012785901, 0.0032284562, -0.006533666, 0.012498075, 0.016463688, 0.02433095, 0.0025584595, -0.015670564, 0.01255564, -0.020864237, 0.004154299, -0.010950207, 0.011935214, 0.023128474, -0.00954945, -0.036867402, 0.0290641, -0.0038121047, 0.008231844, -0.006914237, -0.0047587347, 0.017244017, 0.00076034217, -0.015670564, -0.022591198, 0.016028749, -0.0071381023, -0.031366713, 0.02967813, -0.009645392, -0.0064665065, 0.011743329, 0.0063193953, 0.008845874, -0.007080537, 0.014647181, -0.038069878, 0.009370358, -0.0146343885, -0.0041798833, 0.030599177, -0.0047459425, 0.0007979196, -0.0033323935, 0.00832139, 0.005152098, 0.0004753138, -0.011589821, -0.010073935, 0.006620014, -0.0021762897, 0.018318571, 0.026352134, 0.010886245, -0.032313343, -0.023576206, -0.0021954782, -0.007176479, -0.039963137, 0.0054910937, 0.004602029, -0.0050625517, -0.0053151995, 0.0005900447, -0.16087593, 0.009555846, 0.02071073, -0.021913206, 0.021734115, -0.018318571, 0.033541404, -0.01881747, -0.0065080817, -0.00065280695, 0.0016949795, -0.021900414, -0.008647594, 0.0011009371, -0.021900414, 0.00524804, -0.01199278, 0.012536452, 0.027708117, 0.011666575, 0.01798597, 0.00773934, 0.006533666, -0.01647648, 0.035383496, 0.017896425, -0.0051808804, 0.00010393742, 0.021107292, -0.01815227, -0.0025840441, 0.023294775, 0.013201651, -0.0041574966, 0.017922008, 0.011628198, -0.009095323, 0.010035558, -0.0009746132, 0.017269602, 0.01964897, 0.013598213, 0.018536039, 0.003981603, -0.004295014, 0.028347732, 0.014263412, -0.00910172, 0.00773934, -0.010905433, 0.020135077, -0.036560386, -0.001722163, 0.0049506193, 0.010975791, -0.014020358, -0.0067095603, 0.0022930193, -0.0194315, -0.009159286, -0.0023074108, 0.0071061216, -0.0044868984, 0.005468707, 0.027324349, -0.016015956, -0.019725723, 0.012760317, -0.036330126, 0.008270221, -0.009178474, -0.03702091, 0.01609271, 0.001978009, 0.00031401095, 0.0097989, -0.012517263, 0.016463688, 0.001674192, 0.007342779, -0.02127359, 0.019162862, -0.007182875, -0.008641197, -0.013380744, 0.0012120702, -0.016962586, -0.013086521, -0.0026224211, -0.013674966, -0.010585627, -0.013521459, -0.00010403736, 0.00061243126, 0.024023935, 0.00832139, 0.016450895, 0.011001376, -0.0023473867, -0.01581128, 0.0012560438, -0.004429333, -0.025405504, 0.007982394, 0.024177443, -0.018548831, 0.016693948, 0.016131088, 0.041165613, -0.022552822, 0.00851967, -0.0007691369, -0.0081870705, 0.015836865, -0.010732737, 0.02099216, -0.020672353, -0.008845874, 0.0050977306, 0.023166852, 0.05674663, -0.004691575, 0.0023809664, -0.0010505675, -0.009933219, -0.008039959, -0.11482366, -0.024151858, 0.006271424, 0.026531225, 0.025085695, 0.0186, -0.0147495195, 0.011122903, -0.025802065, 0.014723935, -0.0032060696, -0.018420909, -0.022373728, 0.006402545, 0.021068914, -0.011935214, -0.0096901655, -0.02071073, -0.022028336, 0.03597194, -0.015082119, 0.0073555713, 0.006645599, -0.0028095085, 0.016118295, -0.017845256, -0.023345944, 0.021120084, 0.020838654, 0.0019684148, 0.011218845, -0.0190989, 0.008065544, 0.009626204, -0.014442504, 0.014097112, -0.031878404, 0.024970565, 0.006265028, -0.01742311, -0.00071357033, 0.007931225, -0.0010353766, -0.023691336, 0.0055262726, 0.00456685, -0.021862037, 0.039221186, 0.026582396, -0.020979369, -0.018433701, -0.011468295, -0.037097663, 0.026173042, 0.00058125, -0.020288585, 0.0012624399, 0.0145960115, -0.007432325, -0.0035530608, -0.014787897, 0.0123701515, -0.010739134, 0.00729161, -0.008660385, -0.015951995, 0.010982187, -0.02277029, 0.012261418, -0.026134664, 0.0044005504, 0.004630812, -0.014890235, 0.027759286, -0.025878819, 0.032415684, -0.039502617, -0.03602311, 0.017154472, -0.03868391, -0.0051393057, -0.009389547, 0.015261211, -0.011832875, 0.035946358, 0.0042758253, 0.009843674, 0.012498075, 0.004461314, -0.0037641337, -0.003265234, -0.008807497, -0.005801307, -0.032083083, -0.015043742, -0.0005076943, 0.0030141852, -0.004557256, 0.005142504, -0.004336589, -0.0075410595, -0.011282806, -0.04170289, 0.013764513, -0.013905228, -0.0001841891, 0.012881844, -0.02427978, 0.015184457, -0.046845395, -0.03346465, -0.0011537054, -0.01931637, 0.016105503, -0.0050881365, -0.01531238, -0.002528078, -0.008897043, 0.009331982, 0.020749107, 0.0062202546, 0.035920773, -0.009645392, 0.0022914202, -0.0026735903, 0.016847456, -0.021631775, 0.01803714, 0.020122284, -0.001802115, 0.00043573763, -0.03295296, 0.0027567402, -0.02282146, 0.0479967, 0.042623937, 0.000126224, -0.008020771, 0.016860249, 0.013572628, 0.036048695, 0.065547734, -0.022847043, -0.024919396, 0.005676582, -0.014288996, 0.009997181, 0.004288618, -0.013176067, 0.05249959, 0.025456673, -0.020915408, 0.009952407, 0.012261418, -0.016502064, -0.010969396, -0.017410317, 0.00935117, 0.0036905778, -0.0038920566, 0.01135956, -0.052755438, 0.03001073, -0.03144347, 0.01519725, -0.015721735, 0.017678956, -0.020813068, -0.0021251205, 0.040065475, -0.0052640303, -0.010777511, 0.0021794878, -0.01441692, 0.01815227, 0.023832051, 0.008378955, 0.0037097663, 0.02099216, 0.0018852649, -0.015657773, 0.016220633, 0.037993126, 0.0072852136, -0.0013871648, 0.01647648, 0.013016163, 0.0021698936, -0.008532463, 0.0018884629, 0.0063193953, 0.009280812, -0.0089290235, 0.022028336, -0.0033739686, -0.008270221, -0.0067735217, 0.008660385, 0.013316782, -0.0016334165, 0.007477098, 0.014045943, -0.037046496, 0.0040935352, 0.01709051, -0.00244173, -0.0026767883, 0.035153233, -0.02459959, -0.014966988, 0.005024175, 0.016156672, -0.0054015475, 0.028143056, -0.0061978684, 0.016860249, -0.00976692, 0.015222834, 0.023486659, 0.009223247, -0.02343549, 0.041651722, 0.012696356, 0.011250826, 0.028501239, -0.02878267, 0.021056121, 0.0124469055, 0.012958597, 0.0041447044, -0.0075922287, 0.0072980057, 0.008494086, -0.01948267, -0.020940991, 0.008941816, 0.022271391, -0.0083405785, -0.02220743, 0.020685146, -0.044082258, 0.017845256, 0.0055230744, -0.023409905, 0.013854058, 0.020288585, 0.01881747, -0.004208666, -0.0017045736, 0.024407703, -0.020122284, 0.0027759287, -0.005759732, 0.039758462, -0.0065560527, -0.031571392, 0.0028446873, -0.008308598, 0.023729712, -0.004410145, 0.0009274416, 0.014455296, 0.008653989, 0.022360936, -0.00019118488, -0.012766713, -0.0019284389, 0.041958738, -0.008219051, -0.0056350073, -0.021721322, -0.0062906123, 0.01702655, -0.03622779, -0.0153763415, 0.02521362, -0.015222834, 0.0023729713, 0.00014711142, -0.009088928, 0.0027247595, -0.009229643, -0.0018165063, -0.020186245, 0.002278628, 0.05449519, -0.01213989, -0.01054725, 0.009677373, -0.04564292]
            vectorEntry.vector = embeddings

            if not vectorEntry.completeObject():
                print("Not complete object")
                continue

            json_data = json.dumps(vectorEntry.to_dict())
            outputFile.write(json_data + "\n")


def get_embeddings(text):
    # if we access this from elsewhere, make sure to load the env
    load_dotenv()
    openAIKey = os.getenv("OPEN_AI_KEY")
    client = OpenAI(api_key=openAIKey)
    response = client.embeddings.create(input=text,
    model="text-embedding-ada-002")
    return response.data[0].embedding


if __name__ == '__main__':
    main()