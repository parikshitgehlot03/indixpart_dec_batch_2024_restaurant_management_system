
import os 
import sys
sys.path.append(os.getcwd())

from SRC.authentication.manage_profile import Manage

Management=Manage()
Management.management()
