# napari-hydra-image-processor (n-HIP)

[![License](https://img.shields.io/pypi/l/napari-hydra-image-processor.svg?color=green)](https://github.com/haesleinhuepf/napari-hydra-image-processor/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-hydra-image-processor.svg?color=green)](https://pypi.org/project/napari-hydra-image-processor)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-hydra-image-processor.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-hydra-image-processor/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-hydra-image-processor/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-hydra-image-processor/branch/main/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-hydra-image-processor)
[![Development Status](https://img.shields.io/pypi/status/napari-hydra-image-processor.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-hydra-image-processor)](https://napari-hub.org/plugins/napari-hydra-image-processor)
[![DOI](https://zenodo.org/badge/432729955.svg)](https://zenodo.org/badge/latestdoi/432729955)

Process images using the [Hydra Image Processor](https://hydraimageprocessor.com/) and [CUDA-compatible graphics cards](https://developer.nvidia.com/cuda-toolkit) in [napari]

## Usage

Filters, segmentation algorithms and measurements provided by this napari plugin can be found in the `Tools` menu. 
You can recognize them with their suffix `(n-HIP)`.
Furthermore, it can be used from the [napari-assistant](https://www.napari-hub.org/plugins/napari-assistant) graphical user interface. 
Therefore, just click the menu `Tools > Utilities > Assistant (na)` or run `naparia` from the command line.

![img.png](https://github.com/haesleinhuepf/napari-hydra-image-processor/raw/main/docs/screenshot_with_assistant.png)

All filters implemented in this napari plugin are also demonstrated in [this notebook](https://github.com/haesleinhuepf/napari-hydra-image-processor/blob/main/docs/demo.ipynb).

## Installation

You can install `napari-hydra-image-processor` via using `mamba`/`conda` and `pip`.
If you have never used `conda` before, please go through [this tutorial](https://biapol.github.io/blog/johannes_mueller/anaconda_getting_started/) first.

    mamba create --name napari_hip_env python=3.9 cudatoolkit=11.2 napari -c conda-forge
    conda activate napari_hip_env

    pip install napari-hydra-image-processor

## See also

There are other napari plugins with similar functionality for processing images and extracting features:
* [napari-skimage-regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops)
* [napari-cupy-image-processing](https://www.napari-hub.org/plugins/napari-cupy-image-processing)
* [napari-simpleitk-image-processing](https://www.napari-hub.org/plugins/napari-simpleitk-image-processing)
* [napari-pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)
* [napari-allencell-segmenter](https://napari-hub.org/plugins/napari-allencell-segmenter)
* [RedLionfish](https://www.napari-hub.org/plugins/RedLionfish)
* [bbii-decon](https://www.napari-hub.org/plugins/bbii-decon)  
* [napari-segment-blobs-and-things-with-membranes](https://www.napari-hub.org/plugins/napari-segment-blobs-and-things-with-membranes)

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [BSD-3] license,
"napari-hydra-image-processor" is free and open source software

## Citation

This napari plugin uses the HIP infrastructure published in this paper:

Wait, E., Winter, M. & Cohen, A. R.
Hydra image processor: 5-D GPU image analysis library with MATLAB and python wrappers. Bioinformatics (2019).
[doi:10.1093/bioinformatics/btz523](https://doi.org/10.1093/bioinformatics/btz523)

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/haesleinhuepf/napari-hydra-image-processor/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
