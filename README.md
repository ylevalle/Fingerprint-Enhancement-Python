# Fingerprint-Enhancement-Python

Using oriented gabor filters to enhance fingerprint images based on https://github.com/ylevalle/Fingerprint-Enhancement-Python

this version is written in python3

# Usage: python main_enhancement.py

The images of the fingerprint for the enhancement must be in the "images" directory, the program will enhance all the images in that directory and they will be located in the "enhanced" directory with the same names and the suffix "_enhanced"

## Example:
Command:
```
python main_enhancement.py
```
Output:
```
Found 1 images in "images" folder
Processing images ...
Processing 1.jpg: (1/1)
	All enhanced images saved in the "enhanced" folder.
done.
```
Results:
```
enhanced
└── 1_enhanced.jpg

0 directories, 1 file
```


# Requirements:
```r
cycler==0.10.0
kiwisolver==1.3.1
matplotlib==3.4.2
numpy==1.21.1
opencv-python==4.5.3.56
Pillow==8.3.1
pyparsing==2.4.7
python-dateutil==2.8.2
scipy==1.7.1
six==1.16.0
```
Install it:
```sh
pip install -r requirements.txt
```
# Colaborators
* **Willy Samuel Paz Colque**