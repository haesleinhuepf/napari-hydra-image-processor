import numpy as np
from typing import Callable
from functools import wraps
from toolz import curry
import inspect
from napari_tools_menu import register_function
from napari_time_slicer import time_slicer
import warnings

@curry
def plugin_function(
        function: Callable
) -> Callable:
    @wraps(function)
    def worker_function(*args, **kwargs):
        sig = inspect.signature(function)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # convert input images to numpy-types
        for key, value in bound.arguments.items():
            np_value = None
            if isinstance(value, np.ndarray):
                np_value = value
            elif 'pyclesperanto_prototype._tier0._pycl.OCLArray' in str(type(value)) or \
                    'dask.array.core.Array' in str(type(value)):
                # compatibility with pyclesperanto and dask
                np_value = np.asarray(value)

            print(type(np_value))

            if np_value is not None:
                if np_value.dtype == bool:
                    np_value = np_value * 1

                np_value = np.ascontiguousarray(np_value)
                bound.arguments[key] = np_value

        # call the decorated function
        result = function(*bound.args, **bound.kwargs)

        return result

    worker_function.__module__ = "napari_hydra_image_processor"

    from stackview import jupyter_displayable_output
    return jupyter_displayable_output(worker_function,"n-HIP", "https://www.napari-hub.org/plugins/napari-hydra-image-processor")


@register_function(menu="Filtering / noise removal > Median-Filter (n-HIP)")
@time_slicer
@plugin_function
def median_filter(image:"napari.types.ImageData", radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.MedianFilter(image, kernel)


@register_function(menu="Filtering / noise removal > Gaussian (n-HIP)")
@time_slicer
@plugin_function
def gaussian(image:"napari.types.ImageData", sigma_x: float = 1, sigma_y: float = 1, sigma_z: float = 0) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    return HIP.Gaussian(image, [sigma_z, sigma_y, sigma_x])

@register_function(menu="Filtering > Opener (n-HIP)")
@time_slicer
@plugin_function
def opener(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.Opener(image,kernel)

@register_function(menu="Filtering > Closure (n-HIP)")
@time_slicer
@plugin_function
def closure(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.Closure(image,kernel)


# @register_function(menu="Filtering > Entropy-Filter (n-HIP)")
# @time_slicer
# @plugin_function
# def entropy_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
#             radius_z: int = 1) -> "napari.types.ImageData":
#    from napari_hydra_image_processor import HIP
#    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
#    return HIP.EntropyFilter(image,kernel)
# # Commented out because it crashes with 2D images

@register_function(menu="Filtering / edge enhancement > Laplacian of Gaussian (n-HIP)")
@time_slicer
@plugin_function
def laplacian_of_gaussian(image:"napari.types.ImageData", sigma_x: float = 1, sigma_y: float = 1, sigma_z: float = 0) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    return HIP.LoG(image, [sigma_z, sigma_y, sigma_x])


@register_function(menu="Filtering / background removal > High Pass Filter (n-HIP)")
@time_slicer
@plugin_function
def high_pass_filter(image:"napari.types.ImageData", sigma_x: float = 1, sigma_y: float = 1, sigma_z: float = 0) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    return HIP.HighPassFilter(image, [sigma_z, sigma_y, sigma_x])


@register_function(menu="Filtering > Max Filter (n-HIP)")
@time_slicer
@plugin_function
def max_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.MaxFilter(image,kernel)


@register_function(menu="Filtering / noise removal > Mean Filter (n-HIP)")
@time_slicer
@plugin_function
def mean_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.MeanFilter(image,kernel)


@register_function(menu="Filtering > Min Filter (n-HIP)")
@time_slicer
@plugin_function
def min_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.MinFilter(image,kernel)


@register_function(menu="Filtering > Standard deviation Filter (n-HIP)")
@time_slicer
@plugin_function
def std_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.StdFilter(image,kernel)


@register_function(menu="Filtering > Variance Filter (n-HIP)")
@time_slicer
@plugin_function
def var_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.VarFilter(image,kernel)


@register_function(menu="Filtering / noise removal > Non-local means (n-HIP)")
@time_slicer
@plugin_function
def non_local_means(image: "napari.types.ImageData", h: float = 1, searchWindowRadius: float = 1,
             nhoodRadius: float = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    return HIP.NLMeans(image, h, searchWindowRadius, nhoodRadius)


@register_function(menu="Filtering / noise removal > Wiener Filter (n-HIP)")
@time_slicer
@plugin_function
def wiener_filter(image: "napari.types.ImageData", radius_x: int = 1, radius_y: int = 1,
             radius_z: int = 1, noise_variance: float = 1) -> "napari.types.ImageData":
    from napari_hydra_image_processor import HIP
    kernel = _make_kernel(radius_x, radius_y, radius_z, image.shape)
    return HIP.WienerFilter(image, kernel, noise_variance)



# ElementWiseDifference
# GetMinMax
# IdentityFilter
# MakeBallMask
# MakeEllipsoidMask
# MultiplySum
# Sum
#




def _make_kernel(radius_x, radius_y, radius_z, image_shape):
    dims = (int(radius_z*2+1), int(radius_y*2+1), int(radius_x*2+1))
    kernel = np.ones(dims)
    return kernel

