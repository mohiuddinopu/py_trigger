#!/usr/bin/python
# -*- coding: utf-8 -*-

import ast
from cm_api.api_client import ApiResource
from optparse import OptionParser
from cm_api.endpoints.cms import ClouderaManager
import socket, os, sys, ConfigParser,logging,re


parser = OptionParser()
CONFIG = ConfigParser.ConfigParser()
CONFIG.read("config.ini")


parser.add_option("-c", "--cluster_nm", dest="cluster_nm", action="store",
                  help="Name of CDH cluster to be Updated",metavar="CLUSTER_NM")
parser.add_option("-i", "--host", dest="cm_host", action="store",
                  help="Cloudera Manager Host Name", metavar="CM_HOST")
parser.add_option("-l", "--id", dest="admin_id", action="store",
                  help="Cloudera Manager admin id", metavar="CM_HOST")
parser.add_option("-p", "--pass", dest="admin_pass", action="store",
                  help="Cloudera Manager admin password", metavar="CM_HOST")


(options, args) = parser.parse_args()



cluster_nm = options.cluster_nm
cm_host = options.cm_host
admin_id = options.admin_id
admin_pass = options.admin_pass


f = open( '/tmp/file.py', 'w' )
f.write ("%s, %s, %s, %s\n " % (cluster_nm, cm_host, admin_id, admin_pass)  )
f.close()
