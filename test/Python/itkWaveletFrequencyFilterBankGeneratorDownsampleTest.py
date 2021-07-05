a = itk.itkSimoncelliIsotropicWaveletPython.itkSimoncelliIsotropicWaveletF2PD2.New()
p1 = itk.Point.F2([0.2,0.2])
a.Magnitude(p1)
a.GetHighPassSubBands()

# For reading the volume
r1 = itk.itkImageFileReaderPython.itkImageFileReaderVIF3.New()
r1.SetFileName("/home/pranjal.sahu/for_pranjal/garbage1/A13_mct_man_regFinal_InputImage_1.nrrd")
r1.Update()
r1.GetOutput()


# Image Reader
r1 = itk.itkImageFileReaderPython.itkImageFileReaderIF3.New()
r1.SetFileName("/home/pranjal/for_pranjal/garbage1/A13_mct_man_regFinal_InputImage_1.nrrd")
r1.Update()

# Get Volume
v1 = r1.GetOutput()

# FFT Filter object
i1 = itk.ForwardFFTImageFilter.IF3ICF3.New()
i1.SetInput(v1)
i1.Update()

# Get FFT output
o1 = i1.GetOutput()
