from django.shortcuts import render

# Create your views here.
def convert_temparature(request):
    if request.method=='POST':
        unit_from=request.POST['unit_form']
        temp_value=float(request.POST['temp_value'])
        
        #intialize the conversion result
        celsius=fahrenheit=kelvin=None
        
        # convert based on the select unit
        if unit_from=='celsius':
            celsius=temp_value
            fahrenheit=(temp_value*9/5)+32
            kelvin=temp_value+273.15
        elif unit_from=='fahrenheit':
            fahrenheit=temp_value
            celsius=(temp_value-32)*5/9
            kelvin=celsius+273.15
        elif unit_from=='kelvin':
            kelvin=temp_value
            celsius=temp_value-273.15
            fahrenheit=(celsius*9/5)+32
            
        # pass the convert values to the templates
        context={
            'celsius':celsius,
            'fahrenheit':fahrenheit,
            'kelvin':kelvin
        }
        return render(request,'result.html',context)
    
    return render(request,'form.html')