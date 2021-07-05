import itkConfig
itkConfig.LazyLoading = False
import itk

#import itk
#from itk import itkSimoncelliIsotropicWaveletPython
#from itk import itkImageFileReaderPython
#from itk import ForwardFFTImageFilter


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
r1.SetFileName("/home/pranjal.sahu/for_pranjal/garbage1/A13_mct_man_regFinal_InputImage_1.nrrd")
r1.Update()

# Get Volume
v1 = r1.GetOutput()

# FFT Filter object
i1 = itk.ForwardFFTImageFilter.IF3ICF3.New()
i1.SetInput(v1)
i1.Update()

# Get FFT output
o1 = i1.GetOutput()


# Frequency Filter Bank Generator
forwardFilterBank = itk.WaveletFrequencyFilterBankGenerator.ICF3SimoncelliF3PD3.New()
forwardFilterBank.SetHighPassSubBands(4)
forwardFilterBank.SetSize(i1.GetOutput().GetLargestPossibleRegion().GetSize())
m1 = forwardFilterBank.GetModifiableWaveletFunction()
print(forwardFilterBank.GetHighPassSubBands())

highSubBands = 4
ComplexToRealFilter = itk.ComplexToRealImageFilter.ICF3IF3.New()
print("Real part of complex image:")
for i in range(highSubBands + 1):
    print("Band #: ",  i , " / " , forwardFilterBank.GetHighPassSubBands())
    print("Largest Region: ", forwardFilterBank.GetOutput(i).GetLargestPossibleRegion().GetSize())
    ComplexToRealFilter.SetInput(forwardFilterBank.GetOutput(i))
    ComplexToRealFilter.Update()

