# tableocr
This is a Python library, which will take an image or a pdf (image type) as an input and extract the data given in the table format. 

<p>
<hr>
Error: Unable to get page count. Is poppler installed and in PATH?
<br>
Solution:
conda install -c conda-forge poppler
</p>

<br>
<p>
from PIL import Image
from . import _imaging as core
ImportError: DLL load failed: The specified module could not be found.
<br>
conda uninstall pillow
pip install pillow
<br>
Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.
<br>
pip uninstall -y numpy

pip uninstall -y setuptools

pip install setuptools

pip install numpy
</p>
