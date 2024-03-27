void test(Complex num1, Complex num2)
{
    std::complex<double> n1(num1.re, num1.im);
    std::complex<double> n2(num2.re, num2.im);
    double dif = 0.0001;

    assert((num1 + num2).re - real(n1 + n2) < dif && (num1 + num2).im - imag(n1 + n2) < dif);
    std::cout << "Checkpoint #1\n";

    assert((num1 - num2).re - real(n1 - n2) < dif && (num1 - num2).im - imag(n1 - n2) < dif);
    std::cout << "Checkpoint #2\n";

    assert((num1 * num2).re - real(n1 * n2) < dif && (num1 * num2).im - imag(n1 * n2) < dif);
    std::cout << "Checkpoint #3\n";

    assert((num1 / num2).re - real(n1 / n2) < dif && (num1 / num2).im - imag(n1 / n2) < dif);
    assert((num2 / num1).re - real(n2 / n1) < dif && (num2 / num1).im - imag(n2 / n1) < dif);
    std::cout << "Checkpoint #4\n";

    assert((num1 - 5.43).re - real(n1 - 5.43) < dif && (num1 - 5.43).im - imag(n1 - 5.43) < dif);

    assert((num1 + 5.43).re - real(n1 + 5.43) < dif && (num1 + 5.43).im - imag(n1 + 5.43) < dif);
    std::cout << "Checkpoint #5\n";

    assert((-num1).re - real(-n1) < dif && (-num1).im - imag(-n1) < dif);
    assert((+num1).re - real(+n1) < dif && (+num1).im - imag(+n1) < dif);
    std::cout << "Checkpoint #6\n";

    assert((num1 * 5.43).re - real(n1 * 5.43) < dif && (num1 * 5.43).im - imag(n1 * 5.43) < dif);
    assert((num1 / 5.43).re - real(n1 / 5.43) < dif && (num1 / 5.43).im - imag(n1 / 5.43) < dif);
    std::cout << "Checkpoint #7\n";

    assert(num1.Im() == num1.im && num1.Re() == num1.re);
    std::cout << "Checkpoint #7\n";

    assert(abs(num1) == std::abs(n1));
    std::cout << "Checkpoint #8\n";

    assert(num1 == num1 && num1 != num2);
    std::cout << "Checkpoint #9\n";

    std::cout << "All tests are passed" << std::endl;