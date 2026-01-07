''' fun_helper
Helper functions for common figures.
'''

def stefan_boltzmann(T):
    ''' Implement Stefan-Boltzmann Law to calculate emitted radiation
    from temperature
    Argument:
        T -- temperature in Kelvin
    Returns:
        rad_wm2 -- emitted radiation in W/m2
    '''
    #  sigma in W/m2
    sigma = 5.67 * 10 ** -8
    rad_wm2 = sigma * T ** 4
    return rad_wm2

def wiens(T):
    ''' Implement Wien's Law to calculate wavelength of peak emission
    from temperature
    Argument:
        T -- temperature in Kelvin
    Returns:
        lambda_peak -- wavelength of peak emission in micron
    '''
    #  constant is in units of micron Kelvin
    constant = 2897
    lambda_peak = constant / T
    return lambda_peak
