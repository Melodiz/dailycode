The provided text is a problem statement for a competitive programming task related to digital art restoration. Here's a structured breakdown of the problem statement:

1. **Problem Context**:
   - Oleg creates digital art using a computer and sells it online. His work became so popular that competitors are trying to replicate his success.
   - After a weekend away, Oleg discovered that his algorithm, which creates his art, was corrupted by a trojan.
   - Oleg's algorithm consists of three parts, each applied sequentially to an image, resulting in a matrix of numbers. Each part works the same way but with different processing coefficients.

2. **Task Description**:
   - The algorithm takes an image as input and outputs a matrix of numbers.
   - The algorithm involves a matrix operation where a matrix of the same size as the processing coefficients is taken, elements are multiplied and summed, and the result is placed in the output matrix at the center of the taken matrix.
   - Two of the three algorithms remain intact, but one is lost, along with the order of application.
   - The task is to restore the lost algorithm and determine the order of application.

3. **Input Format**:
   - The data is provided in an archive:
     - All input images are in PNG format with a single channel.
     - A saved collection of Oleg's artworks is in text files of number arrays, one file per input image, saved using `numpy.savetxt("", arr)`.
     - A file `algos.csv` contains data for the algorithms in random order, with each line representing a 3x3 matrix in linear form (9 numbers per line).

4. **Output Format**:
   - Save the two known and one restored algorithm in the order of application in a CSV file.
   - The output should have 3 lines, each with 9 numbers separated by commas.

5. **Evaluation**:
   - The task does not expect an exact answer. Each answer is evaluated as the average of three Mean Squared Errors (MSE) for each algorithm's coefficient matrix.
   - Note that there are only 10 attempts allowed for this task.

This problem involves understanding the matrix operations used in Oleg's algorithm, restoring the missing part, and determining the correct sequence of operations to recreate the digital art.