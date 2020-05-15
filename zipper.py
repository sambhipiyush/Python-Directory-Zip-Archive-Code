#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:49:47 2020

@author: Piyush Sambhi
 (                          (                              
 )\ )                   )   )\ )                 )    )    
(()/((  (      (     ( /(  (()/(    )    )    ( /( ( /((   
 /(_))\ )\ )  ))\ (  )\())  /(_))( /(   (     )\()))\())\  
(_))((_|()/( /((_))\((_)\  (_))  )(_))  )\  '((_)\((_)((_) 
| _ \(_))(_)|_))(((_) |(_) / __|((_)_ _((_)) | |(_) |(_|_) 
|  _/| | || | || (_-< ' \  \__ \/ _` | '  \()| '_ \ ' \| | 
|_|  |_|\_, |\_,_/__/_||_| |___/\__,_|_|_|_| |_.__/_||_|_| 
        |__/                                               

@team: R&D Team
@Contact-Details:
    Email: piyush.sambhi@denave.com
    Phone: +91-9821179339
"""
## Code for Creating folder zip using python and python lib
## If you think code can be improved, please suggest the changes. :-)


import os
import sys
import shutil
from zipfile import ZipFile, ZIP_DEFLATED

script_path = os.path.dirname(os.path.abspath(__file__)) + os.sep

def zip_me_up(root_path, source_dir, target_dir, folder_to_zip):
	try:
		shutil.make_archive(os.path.join(root_path, tgt_dir_path, source_folder), 'zip', os.path.join(root_path, source_dir_path, source_folder))
		return True, 'Success'
	except Exception as e:
		exception_str = 'ERROR :: zip_me_up :: Message :: {}'.format(str(e))
		return False, exception_str
		#raise RuntimeError(exception_str)
	
	
def zip_me_up_2(root_path, source_dir, target_dir, folder_to_zip):
	target_path = os.path.join(root_path, tgt_dir_path, source_folder) + '_2nd_method.zip'
	source_path = os.path.join(root_path, source_dir_path, source_folder)
	try:
		fantasy_zip = ZipFile(target_path, 'w', compression = ZIP_DEFLATED)
		for folder, subfolders, files in os.walk(source_path): 
			for file in files:
				fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), source_path), compress_type = ZIP_DEFLATED)
		 
		fantasy_zip.close()
		return True, 'Success'
	except Exception as e:
		exception_str = 'ERROR :: zip_me_up_2 :: Message :: {}'.format(str(e))
		return False, exception_str
		#raise RuntimeError(exception_str)


source_dir_path = 'source_dir'
tgt_dir_path = 'target_dir'
source_folder = 'zip_move_me'


try:
	status_flag, status_message = zip_me_up(script_path, source_dir_path, tgt_dir_path, source_folder)
	if status_flag == False:
		print('Process Failed with error message - 1st Method :: {}'.format(status_message))
	elif status_flag == True:
		print('Zip process Successful - 1st Method')
except Exception as e:
	print(str(e))
	sys.exit(str(e))


try:
	status_flag, status_message = zip_me_up_2(script_path, source_dir_path, tgt_dir_path, source_folder)
	if status_flag == False:
		print('Process Failed with error message - 2nd Method :: {}'.format(status_message))
	elif status_flag == True:
		print('Zip process Successful - 2nd Method')
except Exception as e:
	print(str(e))
	sys.exit(str(e))
