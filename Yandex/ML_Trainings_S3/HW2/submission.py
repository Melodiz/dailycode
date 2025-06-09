import numpy as np

def compute_sobel_gradients_two_loops(image):
    # Get image dimensions
    height, width = image.shape

    # Initialize output gradients
    gradient_x = np.zeros_like(image, dtype=np.float64)
    gradient_y = np.zeros_like(image, dtype=np.float64)

    # Pad the image with zeros to handle borders
    padded_image = np.pad(image, ((1, 1), (1, 1)), mode='constant', constant_values=0)

    # Define the Sobel kernels for X and Y gradients
    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Apply Sobel filter for X and Y gradients using convolution
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            gradient_x[i - 1, j - 1] = np.sum(sobel_x * padded_image[i - 1:i + 2, j - 1:j + 2])
            gradient_y[i - 1, j - 1] = np.sum(sobel_y * padded_image[i - 1:i + 2, j - 1:j + 2])
    return gradient_x, gradient_y

def compute_gradient_magnitude(sobel_x, sobel_y):
    '''
    Compute the magnitude of the gradient given the x and y gradients.

    Inputs:
        sobel_x: numpy array of the x gradient.
        sobel_y: numpy array of the y gradient.

    Returns:
        magnitude: numpy array of the same shape as the input [0] with the magnitude of the gradient.
    '''
    return np.sqrt(sobel_x**2 + sobel_y**2)

def compute_gradient_direction(sobel_x, sobel_y):
    '''
    Compute the direction of the gradient given the x and y gradients. Angle must be in degrees in the range (-180; 180].
    Use arctan2 function to compute the angle.

    Inputs:
        sobel_x: numpy array of the x gradient.
        sobel_y: numpy array of the y gradient.

    Returns:
        gradient_direction: numpy array of the same shape as the input [0] with the direction of the gradient.
    '''
    return np.degrees(np.arctan2(sobel_y, sobel_x))

def compute_hog(image, pixels_per_cell=(7, 7), bins=9):
    # 1. Convert the image to grayscale if it's not already (assuming the image is in RGB or BGR)
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)  # Simple averaging to convert to grayscale
    
    # 2. Compute gradients with Sobel filter
    gradient_x, gradient_y = compute_sobel_gradients_two_loops(image)  

    # 3. Compute gradient magnitude and direction
    magnitude = compute_gradient_magnitude(gradient_x, gradient_y)
    direction = compute_gradient_direction(gradient_x, gradient_y)

    # 4. Create histograms of gradient directions for each cell
    cell_height, cell_width = pixels_per_cell
    n_cells_x = image.shape[1] // cell_width
    n_cells_y = image.shape[0] // cell_height

    histograms = np.zeros((n_cells_y, n_cells_x, bins))

    for i in range(n_cells_y):
        for j in range(n_cells_x):
            # Get the cell region
            cell_magnitude = magnitude[i*cell_height:(i+1)*cell_height, 
                                      j*cell_width:(j+1)*cell_width]
            cell_direction = direction[i*cell_height:(i+1)*cell_height, 
                                      j*cell_width:(j+1)*cell_width]
            
            # Define bin edges from -180 to 180 degrees
            bin_edges = np.linspace(-180, 180, bins+1)
            
            # Find which bin each direction belongs to
            bin_indices = np.digitize(cell_direction, bin_edges) - 1
            
            # Clip to ensure all indices are within valid range (0 to bins-1)
            bin_indices = np.clip(bin_indices, 0, bins-1)
            
            # For each pixel in the cell, add its magnitude to the appropriate bin
            for y in range(cell_height):
                for x in range(cell_width):
                    if y < cell_magnitude.shape[0] and x < cell_magnitude.shape[1]:  # Check bounds
                        bin_idx = bin_indices[y, x]
                        histograms[i, j, bin_idx] += cell_magnitude[y, x]
            
            # Normalize the histogram for this cell
            if np.sum(histograms[i, j]) > 0:  # Avoid division by zero
                histograms[i, j] /= np.sum(histograms[i, j])

    return histograms