from napari_plugin_engine import napari_hook_implementation

@napari_hook_implementation
def napari_experimental_provide_function():
    from ._hydra_image_processing import median_filter, gaussian_blur

    return [median_filter,
            gaussian_blur, opener, closure, laplacian_of_gaussian, high_pass_filter, max_filter, mean_filter, \
            min_filter, non_local_means, std_filter, var_filter, wiener_filter
            ]

