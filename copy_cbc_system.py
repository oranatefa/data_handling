import numpy as np
from pathlib import Path
from tqdm import tqdm
import shutil
import os

# def mount_QNAP():
# 	os.system(
# 		'echo RevDx2016|sudo -S mount -t cifs //192.168.90.108/home33 /mnt -o vers=3.0,username=admin123,password=Admin123')
# 	print('Mounted successfully')
#
#
# def un_mount_QNAP():
# 	os.system('echo RevDx2016|sudo -S umount //192.168.90.108/home33')
# 	print('UNMounted successfully')

def cbc_df_files(source):
	files = []
	dist = []
	try:
		files0 = list(source.glob('cbc_df.csv'))
		files0 = [x for x in files0 if not 'Calibration' in str(x)]
		dist += (list(0 * np.ones(len(files0), dtype=int)))
		files += (files0)
	except:
		pass
	try:
		files1 = list(source.glob('*/cbc_df.csv'))
		files1 = [x for x in files1 if not 'Calibration' in str(x)]
		dist += (list(1 * np.ones(len(files1), dtype=int)))
		files += (files1)
	except:
		pass
	try:
		files2 = list(source.glob('*/*/cbc_df.csv'))
		files2 = [x for x in files2 if not 'Calibration' in str(x)]
		dist += (list(2 * np.ones(len(files2), dtype=int)))
		files += (files2)
	except:
		pass

	data = {}
	data['cbc_dfs'] = {}
	data['cbc_dfs']['files'], data['cbc_dfs']['dist'] =files, dist
	return data



def copy_data(data, source, target_source):
	i = 1
	n = len(data)
	for group in data:
		files = data[group]['files']
		dists = data[group]['dist']

		for f, d in tqdm(zip(files, dists)):
			try:
				relative_files = f.relative_to(source.parent)
				target = Path(target_source, relative_files)
				target.parent.mkdir(exist_ok=True, parents=True)
				shutil.copy(src=f, dst=target)
			except:
				print('hi')

		print(f'\n{i}/{n}: {group} - Done')

		i += 1


def main():
	source = Path(r"/home/oran/Pictures")
	target = Path('/home/oran/Desktop/result_handler')
	with open('/home/oran/Pictures/DO_NOT_DELETE/SN.txt') as f:
		SN = f.read()

	# '/home/oran/Pictures/DO_NOT_DELETE'
	target = Path(target, 'sys_' + SN[:-1])
	os.makedirs(str(target),exist_ok = True)
	data = cbc_df_files(source)
	copy_data(data, source, target)


if __name__ == '__main__':
	main()

#
# CIFS Mount on Ubuntu 14.04
# 1. Install packages
# $ sudo apt-get install cifs-utils
# 2. Create a Mount point Directory
# $ sudo mkdir /mnt/CIFSMOUNT
# $ sudo chown -R <user>:<user> /mnt/CIFSMOUNT
# 3. CIFS Credentials
# $ sudo su
# # cd /root
# # vim .smbcredentials
# Supply the username and password for CIFS storage as follows:
#
# user=<cifsusername>
# password=<password>
# 4. Fstab Entry
# $ sudo vim /etc/fstab
# Add the following content at the bottom of the file:
#
# #
# # CBS NAS CIFS Mount Point
# #
# //<CISFSTORAGEIP>/<cifspath>  /mnt/CIFSMOUNT        cifs    credentials=/root/.smbcredentials,rw,nounix,iocharset=utf8,file_mode=0777,dir_mode=0777 0 0
# Please replace <CISFSTORAGEIP> with actual IP and <cifspath> with actual path
# 5. Mount the CIFS storage
# $ sudo mount -a
# $ df -h
