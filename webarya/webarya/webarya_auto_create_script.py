#!/usr/bin/env python
'''
Autogenerated code using webarya.py
Original Object Document Input:
{"totalCount":"1","imdata":[{"fvAp":{"attributes":{"descr":"","dn":"uni/tn-Heroes1/ap-Save_The_Planet","name":"Save_The_Planet","nameAlias":"","ownerKey":"","ownerTag":"","prio":"unspecified"}}}]}
'''
# raise RuntimeError('Please review the auto generated code before ' +
# 'executing the output. Some placeholders will ' +
# 'need to be changed')

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://1.1.1.1', 'admin', 'password')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
# Confirm the dn below is for your top dn
polUni = cobra.model.pol.Uni('')
fvTenant = cobra.model.fv.Tenant(polUni, 'Heroes1')


# build the request using cobra syntax
fvAp = cobra.model.fv.Ap(fvTenant, ownerKey=u'', name=u'Save_The_Planet', descr=u'', nameAlias=u'', ownerTag=u'', prio=u'unspecified')


# commit the generated code to APIC
print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)