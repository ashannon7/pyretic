
################################################################################
# The Pyretic Project                                                          #
# frenetic-lang.org/pyretic                                                    #
# author: Joshua Reich (jreich@cs.princeton.edu)                               #
# author: Christopher Monsanto (chris@monsan.to)                               #
################################################################################
# Licensed to the Pyretic Project by one or more contributors. See the         #
# NOTICES file distributed with this work for additional information           #
# regarding copyright and ownership. The Pyretic Project licenses this         #
# file to you under the following license.                                     #
#                                                                              #
# Redistribution and use in source and binary forms, with or without           #
# modification, are permitted provided the following conditions are met:       #
# - Redistributions of source code must retain the above copyright             #
#   notice, this list of conditions and the following disclaimer.              #
# - Redistributions in binary form must reproduce the above copyright          #
#   notice, this list of conditions and the following disclaimer in            #
#   the documentation or other materials provided with the distribution.       #
# - The names of the copyright holds and contributors may not be used to       #
#   endorse or promote products derived from this work without specific        #
#   prior written permission.                                                  #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT    #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the     #
# LICENSE file distributed with this work for specific language governing      #
# permissions and limitations under the License.                               #
################################################################################

##############################################################################################################################
# TO TEST EXAMPLE                                                                                                            #
# -------------------------------------------------------------------                                                        #
# run controller: pox.py --no-cli PATH_TO_THIS_EXAMPLE                                                                       #
# start mininet:  pyretic/mininet.sh --topo=clique,5,5                                                                       #
# test:           pingall                                                                                                    #
##############################################################################################################################

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.virt import *

from pyretic.modules.mac_learner import mac_learner
from pyretic.modules.arp import arp, translate, ARP
from pyretic.vdef.bfs_vdef import BFS_vdef


def main():
    bfs1  = [1,2,3]
    bfs2  = [1,4]
    pol = if_(ARP,arp(),mac_learner())
#    pol = mac_learner()
    return virtualize(
        virtualize(pol,
                   BFS_vdef(from_switches=[1,4])),
        BFS_vdef(from_switches=[1,2,3]))

