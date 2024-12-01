#This simple code is mine, and it has already been pushed to github repo as my archive:https://github.com/Blackonlearn/Parenting-is-Useless

def parentingISuSeless():
    ParentLessBone = {'bone25': 'ORG-DEF-Tongue.001', 'bone26': 'ORG-DEF-Tongue.002', 'bone27': 'ORG-DEF-Tongue.003', 'bone28': 'ORG-DEF-Tongue.004', 'bone29': 'ORG-DEF-Tongue.005', 'bone30': 'ORG-DEF-Tongue.006', 'bone31': 'ORG-DEF-Tongue.007', 'bone32': 'Mouth-Base', 'bone0': 'LipsTop.L', 'bone1': 'LipsTop.001.L', 'bone2': 'LipsTop.002.L', 'bone3': 'LipsTop.003.L', 'bone4': 'LipsTop.004.L', 'bone5': 'LipsTop.005.L', 'bone6': 'LipsTop.006.L', 'bone7': 'LipsTop.006.R', 'bone8': 'LipsTop.005.R', 'bone9': 'LipsTop.004.R', 'bone10': 'LipsTop.003.R', 'bone11': 'LipsTop.002.R', 'bone12': 'LipsTop.001.R', 'bone13': 'LipsTop.R', 'bone14': 'LipsBtm.010.R', 'bone15': 'LipsBtm.009.R', 'bone16': 'LipsBtm.008.R', 'bone17': 'LipsBtm.007.R', 'bone18': 'LipsBtm.006.R', 'bone19': 'LipsBtm.005', 'bone20': 'LipsBtm.006.L', 'bone21': 'LipsBtm.007.L', 'bone22': 'LipsBtm.008.L', 'bone23': 'LipsBtm.009.L', 'bone24': 'LipsBtm.010.L'}
    bpy.ops.object.mode_set(mode='EDIT')
    for index, i in enumerate(ParentLessBone):
        bpy.data.objects['RIG-NOE'].data.edit_bones[ParentLessBone[i]].parent = None
    bpy.ops.object.mode_set(mode='POSE')

parentingISuSeless()
