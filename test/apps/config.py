##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including          #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################
import os

def get_test_filenames():
    return ("tall.h5", 
            "shuffle_compress.h5", 
            "d_objref.h5",
            "a_objref.h5",
            "d_link_hard.h5",
            "d_link_soft.h5",
            "scale_offset.h5",
            "fletcher32.h5",
            "undecodable_attr.h5",
            "diamond.h5"
    )

cfg = {
    'use_h5py': False,
    'test_file_http_path': "https://s3.amazonaws.com/hdfgroup/data/hdf5test/"
}

def get(x):
    # see if there is a command-line override
    config_value = None

    # see if there are an environment variable override
    if x.upper() in os.environ:
        config_value = os.environ[x.upper()]
    # no command line override, just return the cfg value
    if config_value is None:
        config_value = cfg[x]

    # convert string to boolean if true or false
    if type(config_value) is str:
        if config_value.upper() in ('T', 'TRUE'):
            config_value = True
        elif config_value.upper() in ('F', 'FALSE'):
            config_value = False
    return config_value



