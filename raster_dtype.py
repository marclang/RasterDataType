# -*- coding: utf-8 -*-

try:
    import otbApplication as otb

    OTB_IS_LOAD = True
except ImportError as e:
    OTB_IS_LOAD = False
    ERROR_OTB = ImportError(str(e)
                            + "\n\nThis functionnality is not available without Orfeo Toolbox. " +
                            "Please install Orfeo Toolbox if it isn't installed yet and set the "
                            "proper environment variable\n\n")

try:
    from osgeo import gdal
except ImportError as e:
    raise ImportError(
        str(e) + "\n\nPlease install GDAL.")
try:
    import numpy as np
except ImportError as e:
    raise ImportError(
        str(e) + "\n\nPlease install NumPy.")


class IdDefaultDict(dict):
    """A dictionary where trying to reach a missing key does create the key with
    value equal to itself"""

    def __missing__(self, key):
        self[key] = key
        return self[key]


class DataType(object):
    """Abstract class for a data type (int16, int32, float32, etc.)"""

    data_type_match = IdDefaultDict()

    def __set__(self, instance, value):
        instance.gdal_dtype = self.data_type_match[value]

    def __get__(self, instance, owner):
        revert_match = {v: k for k, v in self.data_type_match.items()}
        return revert_match[instance.gdal_dtype]


class LStrDataType(DataType):
    """Represent a data type given in lower string format (eg. 'int16', 'int32',
    'float32', etc.)"""

    data_type_match = {'uint8': gdal.GDT_Byte,
                       'uint16': gdal.GDT_UInt16,
                       'uint32': gdal.GDT_UInt32,
                       'int16': gdal.GDT_Int16,
                       'int32': gdal.GDT_Int32,
                       'float32': gdal.GDT_Float32,
                       'float64': gdal.GDT_Float64}


class UStrDataType(DataType):
    """Represent a data type given in upper string format (eg. 'Int16', 'Int32',
    'Float32', etc.)"""

    data_type_match = {'UInt8': gdal.GDT_Byte,
                       'UInt16': gdal.GDT_UInt16,
                       'UInt32': gdal.GDT_UInt32,
                       'Int16': gdal.GDT_Int16,
                       'Int32': gdal.GDT_Int32,
                       'Float32': gdal.GDT_Float32,
                       'Float64': gdal.GDT_Float64}


class NumpyDataType(DataType):
    """Represent a data type for Numpy (eg. np.int16, np.int32, np.float32,
    etc.)"""

    data_type_match = {np.uint8: gdal.GDT_Byte,
                       np.uint16: gdal.GDT_UInt16,
                       np.uint32: gdal.GDT_UInt32,
                       np.int16: gdal.GDT_Int16,
                       np.int32: gdal.GDT_Int32,
                       np.float32: gdal.GDT_Float32,
                       np.float64: gdal.GDT_Float64}


class GdalDataType(DataType):
    """Represent a data type for gdal (eg. gdal.GDT_Int16, gdal.GDT_Iint32,
    gdal.GDT_Float32, etc.)"""

    def __set__(self, instance, value):
        instance._gdal_type = value

    def __get__(self, instance, owner):
        return instance._gdal_type


class OtbDataType(DataType):
    """Represent a data type for orfeo-toolbox
    (eg. otb.ImagePixelType_int16)"""

    if OTB_IS_LOAD:
        data_type_match = {otb.ImagePixelType_uint8: gdal.GDT_Byte,
                           otb.ImagePixelType_uint16: gdal.GDT_UInt16,
                           otb.ImagePixelType_uint32: gdal.GDT_UInt32,
                           otb.ImagePixelType_int16: gdal.GDT_Int16,
                           otb.ImagePixelType_int32: gdal.GDT_Int32,
                           otb.ImagePixelType_float: gdal.GDT_Float32,
                           otb.ImagePixelType_double: gdal.GDT_Float64}
    else:
        def __get__(self, instance, owner):
            raise ERROR_OTB


class RasterDataType(object):
    """The usable class to manage raster data types

    lstr_dtype can be:
        - 'uint8'
        - 'uint16',
        - 'uint32'
        - 'int16'
        - 'int32'
        - 'float32'
        - 'float64'
    """

    lstr_dtype = LStrDataType()
    ustr_dtype = UStrDataType()
    numpy_dtype = NumpyDataType()
    gdal_dtype = GdalDataType()
    otb_dtype = OtbDataType()

    def __init__(self,
                 lstr_dtype=None,
                 ustr_dtype=None,
                 numpy_dtype=None,
                 otb_dtype=None,
                 gdal_dtype=None):

        if lstr_dtype:
            self.lstr_dtype = lstr_dtype
        elif ustr_dtype:
            self.ustr_dtype = ustr_dtype
        elif numpy_dtype:
            self.numpy_dtype = numpy_dtype
        elif gdal_dtype:
            self.gdal_dtype = gdal_dtype
        elif otb_dtype:
            self.otb_dtype = otb_dtype
