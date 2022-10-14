import numpy as np

def test_something():
    from napari_hydra_image_processor import median_filter, gaussian, opener, closure, laplacian_of_gaussian, \
        high_pass_filter, max_filter, mean_filter, \
        min_filter, non_local_means, std_filter, var_filter, wiener_filter

    image = np.asarray([[0, 1, 2, 3],
                        [2, 0, 1, 3],
                        [2, 0, 1, 3],
                        [2, 0, 1, 3]])

    for operation in  [median_filter,
                       gaussian, opener, closure, laplacian_of_gaussian, high_pass_filter, max_filter, mean_filter, \
                       min_filter, non_local_means, std_filter, var_filter, wiener_filter
                       ]:
        print(operation)

        operation(image)



