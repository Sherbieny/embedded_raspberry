from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["things/*"]

setup(name = "humiditySense",
    version = "1.00",
    description = "accessing the HTS221 Humidity/temprature sensor on sense-hat",
    author = "Eslam El-Sherbieny",
    author_email = "sherbieny@outlook.com",
    url = "https://github.com/Sherbieny/embedded_raspberry",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['package'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #'runner' is in the root.
    scripts = ["runner"],
    long_description = """This package is a learning attempt to create a python distutil
                        that contain a program that access and manipulates the RaspberryPI 
                        sense hat HTS221 sensor through I2C addresses and doing some actions 
                        on it hopefully...""" 
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
