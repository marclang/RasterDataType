# RasterDataType

Provides easy acces to raster or array data types of various lib


Allows you to esaly manipulate the array or images data types the following libraries:

- [Gdal](http://gdal.org)
- [OTB](https://www.orfeo-toolbox.org/)
- [Numpy](http://www.numpy.org)

Note that there is no need for OTB to be installed so that the RasterDataType works, only OTB datatype won't be available.

The purpose of this package is that developer no longer have to care about how to specify a data type in each library.

You can either initialize a RasterDataType instance by specifying the data type with low string or upper string mode :

```python
>>> from RasterDataType import RasterDataType
>>> first_dtype = RasterDataType(lstr_dtype='float32')
>>> second_dtype = RasterDataType(ustr_dtype='Float32')
```

And then get the data type of the library of your choice

```python

>>> print(first_dtype.otb_dtype)
5
>>> print(first_dtype.gdal_dtype)
6
>>> print(first_dtype.numpy_dtype)
<class 'numpy.float32'>
```

You can also initialize a RasterDataType instance from library type and then get the data type of the library of your choice :

```python
>>> import numpy as np
>>> dtype = RasterDataType(numpy_dtype=np.float64)
>>> print(dtype.lstr_dtype)
float64
```

And here the list of data types supported :

```python
>>> help(RasterDataType)
Help on class RasterDataType in module RasterDataType.raster_dtype:
class RasterDataType(builtins.object)
 |  The usable class to manage raster data types
 |  
 |  lstr_dtype can be:
 |      - 'uint8'
 |      - 'uint16',
 |      - 'uint32'
 |      - 'int16'
 |      - 'int32'
 |      - 'float32'
 |      - 'float64'
 |  
 |  Methods defined here:
 |  
 |  __init__(self, lstr_dtype=None, ustr_dtype=None, numpy_dtype=None, otb_dtype=None, gdal_dtype=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  gdal_dtype
 |      Represent a data type for gdal (eg. gdal.GDT_Int16, gdal.GDT_Iint32,
 |      gdal.GDT_Float32, etc.)
 |  
 |  lstr_dtype
 |      Represent a data type given in lower string format (eg. 'int16', 'int32',
 |      'float32', etc.)
 |  
 |  numpy_dtype
 |      Represent a data type for Numpy (eg. np.int16, np.int32, np.float32,
 |      etc.)
 |  
 |  otb_dtype
 |      Represent a data type for orfeo-toolbox
 |      (eg. otb.ImagePixelType_int16)
 |  
 |  ustr_dtype
 |      Represent a data type given in upper string format (eg. 'Int16', 'Int32',
 |      'Float32', etc.)

```
