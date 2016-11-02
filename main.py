
import imp
run = imp.load_source("on_the_fly", "on_the_fly.py")

# input calibration parameters (make sure the correct calibration is entered)
d_in_pixel = 2309.54007395     # distance from sample to detector plane along beam direction in pixel space
Rotation_angle = 4.72973064797  #detector rotation
tilt_angle = 0.531406930485   # detector tilt
lamda = 0.9762  # wavelength
x0 = 1034.81496248     # beam center in pixel-space
y0 = 2309.54007395    # beam center in pixel-space
PP = 0.95   # beam polarization, decided by beamline setup

# user input
folder_path = 'C:\\Research_FangRen\\Data\\July2016\\Sample16_2thin\\'
base_filename = 'Sample16_2thin_24x24_t30_'
index = 1   # starting from this scan#
last_scan = 441  # end with this scan#
num_of_smpls_on_wafer = 25


run.on_the_fly(folder_path, base_filename, index, last_scan, d_in_pixel, Rotation_angle, tilt_angle, lamda, x0, y0, PP, num_of_smpls_on_wafer)
