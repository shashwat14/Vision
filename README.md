# Vision

This is a python camera calibration script based on OpenCV. You will need to a checkerboard. Change the value of WIDTH and HEIGHT with the number of corners (excluding the one on periphery) present in your checkerboard horizontally and vertically respectively. You need to select a total of 10 to 20 images for good calibration. Run the script using any python interpreter and move the checkerboard around in front of the camera such that it is seen in different sizes in different locations as well as in skewed ways. Everytime the corners are detected and your checkboard is in a new location, press 'c' to select the image. When finished selecting 10-20 images, press 'q'. This should end the calibration. Your intrinsic paramters are stored in a variable called mtx and and distortion coeffecients are stored in variable called  'dist'. 

Feel free to get in touch with me, in case of any queries. My email is shashwatverma14@gmail.com
