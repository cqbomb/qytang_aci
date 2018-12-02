#!/usr/bin/env python
'''
Autogenerated code using webarya.py
Original Object Document Input:
{"totalCount":"1","imdata":[{"fvAp":{"attributes":{"descr":"","dn":"uni/tn-Heroes/ap-Save_The_Planet","name":"Save_The_Planet","nameAlias":"","ownerKey":"","ownerTag":"","prio":"unspecified"},"children":[{"fvAEPg":{"attributes":{"descr":"","fwdCtrl":"","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"db","nameAlias":"","pcEnfPref":"unenforced","prefGrMemb":"exclude","prio":"unspecified"},"children":[{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"sql"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-202","instrImedcy":"lazy","mode":"regular","primaryEncap":"unknown","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-202","instrImedcy":"lazy","mode":"regular","primaryEncap":"unknown","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]"}}},{"fvRsDomAtt":{"attributes":{"classPref":"encap","delimiter":"","encap":"unknown","encapMode":"auto","epgCos":"Cos0","epgCosPref":"disabled","instrImedcy":"lazy","netflowDir":"both","netflowPref":"disabled","primaryEncap":"unknown","resImedcy":"lazy","tDn":"uni/phys-Heroes_phys"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"Hero_Land"}}}]}},{"fvAEPg":{"attributes":{"descr":"","fwdCtrl":"","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"web","nameAlias":"","pcEnfPref":"unenforced","prefGrMemb":"exclude","prio":"unspecified"},"children":[{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"web"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-200","instrImedcy":"lazy","mode":"regular","primaryEncap":"unknown","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-200","instrImedcy":"lazy","mode":"regular","primaryEncap":"unknown","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]"}}},{"fvRsDomAtt":{"attributes":{"classPref":"encap","delimiter":"","encap":"unknown","encapMode":"auto","epgCos":"Cos0","epgCosPref":"disabled","instrImedcy":"lazy","netflowDir":"both","netflowPref":"disabled","primaryEncap":"unknown","resImedcy":"lazy","tDn":"uni/phys-Heroes_phys"}}},{"fvRsCons":{"attributes":{"prio":"unspecified","tnVzBrCPName":"sql"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"Hero_Land"}}}]}},{"fvAEPg":{"attributes":{"descr":"","fwdCtrl":"","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"app","nameAlias":"","pcEnfPref":"unenforced","prefGrMemb":"exclude","prio":"unspecified"},"children":[{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"power_up"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-201","instrImedcy":"lazy","mode":"regular","primaryEncap":"unknown","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]"}}},{"fvRsPathAtt":{"attributes":{"descr":"","encap":"vlan-201","instrImedcy":"lazy","mode":"regular","primaryEncap":"unknown","tDn":"topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]"}}},{"fvRsDomAtt":{"attributes":{"classPref":"encap","delimiter":"","encap":"unknown","encapMode":"auto","epgCos":"Cos0","epgCosPref":"disabled","instrImedcy":"lazy","netflowDir":"both","netflowPref":"disabled","primaryEncap":"unknown","resImedcy":"lazy","tDn":"uni/phys-Heroes_phys"}}},{"fvRsCons":{"attributes":{"prio":"unspecified","tnVzBrCPName":"sql"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"Hero_Land"}}}]}}]}}]}
'''
# raise RuntimeError('Please review the auto generated code before ' +
# 'executing the output. Some placeholders will ' +
# 'need to be changed')

# list of packages that should be imported for this code to work
from credentials import *
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
from cobra.internal.codec.xmlcodec import toXMLStr

# configuration variables
tenant = 'Heroes'
bridge_domain = 'Hero_Land'
application = 'Save_The_Network'
vlan1 = 'vlan-211'
vlan2 = 'vlan-212'
vlan3 = 'vlan-210'

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
# Confirm the dn below is for your top dn
topDn = cobra.mit.naming.Dn.fromString('uni/tn-Heroes/ap-Save_The_Planet')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# build the request using cobra syntax
fvAp = cobra.model.fv.Ap(topMo, ownerKey=u'', name=u'Save_The_Planet', descr=u'', nameAlias=u'', ownerTag=u'', prio=u'unspecified')
fvAEPg = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'db', descr=u'', fwdCtrl=u'', prefGrMemb=u'exclude', nameAlias=u'', prio=u'unspecified', pcEnfPref=u'unenforced')
fvRsProv = cobra.model.fv.RsProv(fvAEPg, tnVzBrCPName=u'sql', matchT=u'AtleastOne', prio=u'unspecified')
fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-202')
fvRsPathAtt2 = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-202')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, tDn=u'uni/phys-Heroes_phys', netflowDir=u'both', epgCos=u'Cos0', classPref=u'encap', primaryEncap=u'unknown', delimiter=u'', instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', encapMode=u'auto', netflowPref=u'disabled', epgCosPref=u'disabled')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName=u'')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=u'Hero_Land')
fvAEPg2 = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'web', descr=u'', fwdCtrl=u'', prefGrMemb=u'exclude', nameAlias=u'', prio=u'unspecified', pcEnfPref=u'unenforced')
fvRsProv2 = cobra.model.fv.RsProv(fvAEPg2, tnVzBrCPName=u'web', matchT=u'AtleastOne', prio=u'unspecified')
fvRsPathAtt3 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-200')
fvRsPathAtt4 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-200')
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, tDn=u'uni/phys-Heroes_phys', netflowDir=u'both', epgCos=u'Cos0', classPref=u'encap', primaryEncap=u'unknown', delimiter=u'', instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', encapMode=u'auto', netflowPref=u'disabled', epgCosPref=u'disabled')
fvRsCons = cobra.model.fv.RsCons(fvAEPg2, tnVzBrCPName=u'sql', prio=u'unspecified')
fvRsCustQosPol2 = cobra.model.fv.RsCustQosPol(fvAEPg2, tnQosCustomPolName=u'')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName=u'Hero_Land')
fvAEPg3 = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=u'app', descr=u'', fwdCtrl=u'', prefGrMemb=u'exclude', nameAlias=u'', prio=u'unspecified', pcEnfPref=u'unenforced')
fvRsProv3 = cobra.model.fv.RsProv(fvAEPg3, tnVzBrCPName=u'power_up', matchT=u'AtleastOne', prio=u'unspecified')
fvRsPathAtt5 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-201')
fvRsPathAtt6 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-201')
fvRsDomAtt3 = cobra.model.fv.RsDomAtt(fvAEPg3, tDn=u'uni/phys-Heroes_phys', netflowDir=u'both', epgCos=u'Cos0', classPref=u'encap', primaryEncap=u'unknown', delimiter=u'', instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', encapMode=u'auto', netflowPref=u'disabled', epgCosPref=u'disabled')
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg3, tnVzBrCPName=u'sql', prio=u'unspecified')
fvRsCustQosPol3 = cobra.model.fv.RsCustQosPol(fvAEPg3, tnQosCustomPolName=u'')
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, tnFvBDName=u'Hero_Land')


# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)