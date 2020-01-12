import tkinter, time, requests, zipfile, pandas, numpy, os, nibabel, tempfile, shutil
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
from skimage import data
from skimage import io
from tkinter import *

## https://www.datacamp.com/community/tutorials/matplotlib-3d-volumetric-data - Helpful resource!

class BrainViewer:

	def multi_slice_viewer(self, volume):
		self.remove_keymap_conflicts({'j', 'k'})
		fig, ax = plt.subplots()
		ax.volume = volume
		ax.index = volume.shape[0] // 2
		ax.imshow(volume[ax.index])
		fig.canvas.mpl_connect('key_press_event', self.process_key)
		plt.show()

	def process_key(self, event):
		fig = event.canvas.figure
		ax = fig.axes[0]
		if event.key == 'j':
			self.previous_slice(ax)
		elif event.key == 'k':
			self.next_slice(ax)
		fig.canvas.draw()

	def previous_slice(self, ax):
		volume = ax.volume
		ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
		ax.images[0].set_array(volume[ax.index])

	def next_slice(self, ax):
		volume = ax.volume
		ax.index = (ax.index + 1) % volume.shape[0]
		ax.images[0].set_array(volume[ax.index])

	def remove_keymap_conflicts(self, new_keys_set):
		for prop in plt.rcParams:
			if prop.startswith('keymap.'):
				keys = plt.rcParams[prop]
				remove_list = set(keys) & new_keys_set
				for key in remove_list:
					keys.remove(key)

	def data_wrangle(self, d):
		### Download Available Data ###

		# Define path
		os.path.basename('http://google.com/attention.zip') 

		# Define URL
		url = 'http://www.fil.ion.ucl.ac.uk/spm/download/data/attention/attention.zip'

		# Retrieve the data
		fn, info = urlretrieve(url, os.path.join(d, 'attention.zip'))

		# Extract the contents into the temporary directory we created earlier
		zipfile.ZipFile(fn).extractall(path=d)

		# List first 5 files
		print([f.filename for f in zipfile.ZipFile(fn).filelist[:5]])

		# Read the image 
		struct = nibabel.load(os.path.join(d, 'attention/structural/nsM00587_0002.hdr'))

		# Get a plain NumPy array, without all the metadata
		struct_arr = struct.get_data()

		struct_arr = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")

		self.struct_arr2 = struct_arr.T

	def __init__(self):

		d = tempfile.mkdtemp() # Make a temporary directory

		self.data_wrangle(d)

		self.multi_slice_viewer(self.struct_arr2)

		shutil.rmtree(d)


brainview = BrainViewer()

