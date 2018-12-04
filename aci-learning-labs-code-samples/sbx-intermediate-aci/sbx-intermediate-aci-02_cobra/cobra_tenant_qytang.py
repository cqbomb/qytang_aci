#!/usr/bin/env python

import requests
import cobra.mit.access
import cobra.mit.session
import cobra.mit.request
import cobra.model.pol
import cobra.model.fv
from credentials import *


def create_epg(tenant_name, app_profile, epg_name):
    """
    This function creates the new Tenant with a VRF, Bridge Domain and Subnet.
    """
    # create a session and define the root
    requests.packages.urllib3.disable_warnings()
    auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
    session = cobra.mit.access.MoDirectory(auth)
    session.login()

    root = cobra.model.pol.Uni('')

    # model new tenant configuration
    tenant = cobra.model.fv.Tenant(root, tenant_name)
    app_profile = cobra.model.fv.Ap(tenant, app_profile)
    epg = cobra.model.fv.AEPg(app_profile, epg_name)
    # contract = cobra.model.fv.RsCons(epg_name, contract_name)

    #
    config_request = cobra.mit.request.ConfigRequest()
    config_request.addMo(tenant)
    session.commit(config_request)
    config_request.addMo(app_profile)
    session.commit(config_request)
    config_request.addMo(epg)
    session.commit(config_request)
    # config_request.addMo(contract)
    # session.commit(config_request)


if __name__ == '__main__':
    create_epg('a_qytang_cobra_tenant6', 'qytang_cobra_app_profile', 'qytang_cobra_epg')


