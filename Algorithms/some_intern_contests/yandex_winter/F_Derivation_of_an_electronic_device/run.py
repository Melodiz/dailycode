import numpy as np
import csv
import os
from glob import glob
from PIL import Image

def load_images_and_matrices(images_dir, arrays_dir, algo_file):
    """
    Example loader function.
    1) Read PNG images from images_dir.
    2) Read numpy-saved arrays from arrays_dir (one per image).
    3) Read algos.csv which should contain three lines of 9 coefficients each 
       (representing three 3x3 matrices).
    Return them for further analysis.
    """
    # 1) Load PNG images:
    image_files = sorted(glob(os.path.join(images_dir, "*.png")))
    loaded_images = []
    for fpath in image_files:
        im = Image.open(fpath).convert("L")  # single-channel
        loaded_images.append((os.path.basename(fpath), np.array(im)))

    # 2) Load arrays (saved with numpy.savetxt) from arrays_dir:
    array_files = sorted(glob(os.path.join(arrays_dir, "*.txt")))
    loaded_arrays = []
    for fpath in array_files:
        arr = np.loadtxt(fpath)
        loaded_arrays.append((os.path.basename(fpath), arr))

    # 3) Load existing algorithms from algos.csv (possibly not in correct order, 
    #    and we might have a missing filter).
    #    Each line has 9 floats, so shape can be reshaped to 3x3.
    with open(algo_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        algo_filters = []
        for row in reader:
            if len(row) == 9:
                # Convert each line to float and reshape to (3, 3)
                filter_3x3 = np.array(list(map(float, row))).reshape((3, 3))
                algo_filters.append(filter_3x3)
            else:
                # Possibly corrupted line or missing?
                # We'll store None or partial data
                algo_filters.append(None)

    return loaded_images, loaded_arrays, algo_filters

def apply_filter_to_image(img_array, filter_3x3):
    """
    Applies a 3x3 filter to a single-channel 2D image array.
    This is a standard convolution / correlation approach:
        Output pixel = sum_{i=-1..1, j=-1..1} input[x+i, y+j]*filter[i,j]
    For simplicity, this example uses 'valid' convolution. 
    For real usage, you might replicate Oleg’s “centered transformation,” 
    or even use a standard library function like scipy.signal.convolve2d.
    """
    from scipy.signal import convolve2d
    # Ensure 2D
    if img_array.ndim != 2:
        raise ValueError("Expected single-channel 2D image array.")
    return convolve2d(img_array, filter_3x3, mode='same', boundary='fill', fillvalue=0)

def guess_missing_filter(known_filters, loaded_images, loaded_arrays):
    """
    Pseudocode / skeleton for deducing the missing 3x3 filter.
    1) We have (some) input images and their final transformations.
    2) We have two known filters. 
    3) We must guess the third filter that, in sequence with the others, 
       reproduces Oleg's final arrays from the original images.
    This can be approached in numerous ways depending on the data you have.
    """
    # For demonstration, we return a dummy filter:
    # In practice, you might attempt an iterative approach:
    # - Possibly guess the order for the two known filters,
    #   then optimize the third filter’s 9 coefficients by comparing
    #   the final produced array to the array given in loaded_arrays.
    # - You can solve a large least-squares system if the images are large.
    
    # Example dummy approach:
    guessed_filter = np.zeros((3, 3))
    guessed_filter[1, 1] = 1.0  # just identity
    return guessed_filter

def determine_filter_order(filters, loaded_images, loaded_arrays):
    """
    Given that we have 3 filters (two known + one guessed),
    we want to figure out in which order they are applied. 
    For example, test all permutations of the 3 filters 
    to see which yields the lowest error w.r.t. final arrays in loaded_arrays.
    Return the best ordering as a list of indices.
    """
    from itertools import permutations

    all_indices = [0, 1, 2]
    best_order = None
    best_error = float("inf")

    # We assume each item in loaded_arrays is a final output for a given image. 
    # A real scenario might store “final output of the pipeline.” 
    # For each image, we can try applying a candidate pipeline and compare MSE.
    
    for perm in permutations(all_indices):
        total_mse = 0.0
        count = 0
        for (img_name, img_array), (arr_name, final_array) in zip(loaded_images, loaded_arrays):
            # apply filters in order perm to img_array
            out = img_array.copy()
            for idx in perm:
                out = apply_filter_to_image(out, filters[idx])
            # compute MSE
            mse = np.mean((out - final_array)**2)
            total_mse += mse
            count += 1
        avg_mse = total_mse / max(count, 1)
        if avg_mse < best_error:
            best_error = avg_mse
            best_order = perm

    return best_order, best_error

def main():
    # Example directory structure, adapt to real paths:
    images_dir = "./images"
    arrays_dir = "./arrays"
    algo_file = "./algos.csv"
    
    # Step 1: Load images, arrays, existing (possibly incomplete) filters
    loaded_images, loaded_arrays, algo_filters = load_images_and_matrices(
        images_dir, arrays_dir, algo_file
    )
    
    # We have 3 “spots” for filters, e.g. [filter_1, filter_2, filter_3].
    # Some may be None if corrupted or missing. Identify them:
    known_filters = []
    missing_indices = []
    
    for i, f3x3 in enumerate(algo_filters):
        if f3x3 is None:
            missing_indices.append(i)
        else:
            known_filters.append(f3x3)
    
    # Step 2: If exactly one filter is missing, guess it:
    if len(missing_indices) == 1:
        missing_idx = missing_indices[0]
        guessed_filter = guess_missing_filter(known_filters, loaded_images, loaded_arrays)
        # Insert guessed filter back in the list
        algo_filters[missing_idx] = guessed_filter
    else:
        # If no missing or more than one missing, 
        # handle accordingly or raise an error for this simplified approach.
        pass
    
    # At this point, algo_filters should contain three 3x3 filters (two original, one guessed).
    # Step 3: Determine best order:
    final_order, final_error = determine_filter_order(algo_filters, loaded_images, loaded_arrays)