#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# blocktree - Tries to figure out hierachy from device mapper and udev
# Copyright (C) 2013 Tomas Edwardsson
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.



# need python-pyblock and python-pyudev packages on Fedora/RHEL based systems


import pyudev
import block
from block import dm

def main():
	global dm_maps, context

	# Udev context for querying
	context = pyudev.Context()

	# Cache the device mapper maps
	dm_maps = dm.maps()

	# Loop through the device mapper maps
	for map in dm.maps():
		print map.name.strip()
		get_deps(map.deps, 1)

def get_deps(deps, depth):
	for dep in deps:
		dmmap = lookup_map(dep.major, dep.minor)
		local_deps = block.getDmDeps(major=dep.major, minor=dep.minor)
		# DM Device
		if local_deps:
			print "%s%s" % (" "*depth*8, dmmap.name.strip())
			get_deps(local_deps, depth + 1)
		# NON DM device
		else:
			print "%s%s" % (" "*depth*8, find_name_by_devnum(dep.dev))
	
def find_name_by_devnum(devnum):
	for i in context.list_devices(subsystem='block'):
		if i.device_number == devnum:
			return i.device_node.strip()
def lookup_map(major, minor):
	global dm_maps

	for m in dm_maps:
		if m.dev.major == major and m.dev.minor == minor:
			return m
	
	return None


if __name__ == "__main__":
	main()
