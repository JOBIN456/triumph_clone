from django.db import models
from django.core.validators import FileExtensionValidator 
# from embed_video.fields import EmbedVideoField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name
class Bike(models.Model):
    image = models.ImageField(upload_to='bike_images/')
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    description3 = models.TextField(blank=True)
    cc_engine=models.IntegerField(blank=True, null=True)
    ps_peak_power=models.IntegerField(blank=True, null=True)
    torque=models.IntegerField(blank=True, null=True)
    year=models.IntegerField(blank=True, null=True)
    accesories=models.IntegerField(blank=True, null=True)
    mile_service=models.IntegerField(blank=True, null=True)
    cylinders=models.IntegerField(blank=True, null=True)
    rpm=models.IntegerField(blank=True, null=True)
    kg_wet =models.IntegerField(blank=True, null=True)
    kg_lighter = models.IntegerField(blank=True, null=True)
    nm = models.IntegerField(blank=True, null=True)
    engine = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
	
    def __str__(self):
        return self.name

class BikeDetails(models.Model):
    name=models.CharField(max_length=100,default='SOME STRING')
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    paragraph=models.TextField(blank=True)

    small_image=models.ImageField(upload_to='bike_images/',null=True)
    big_image=models.ImageField(upload_to='bike_images/',null=True)
    card_image=models.ImageField(upload_to='bike_images/',null=True)

    price = models.IntegerField(blank=True, null=True)

    cc_engine=models.IntegerField(blank=True, null=True)
    ps_peak_power=models.IntegerField(blank=True, null=True)
    torque=models.IntegerField(blank=True, null=True)
    miles=models.IntegerField(blank=True, null=True)


    bike = models.ForeignKey(Bike, on_delete=models.CASCADE,null=True)
    carousel_image=models.ImageField(upload_to='bike_images/',null=True)
    carousel_image2=models.ImageField(upload_to='bike_images/',null=True)
    carousel_image3=models.ImageField(upload_to='bike_images/',null=True)

    carousel_title1=models.TextField(blank=True)
    carousel_title2=models.TextField(blank=True)
    carousel_title3=models.TextField(blank=True)
    vedio_url=models.URLField(blank=True, max_length=600)
    vedio_url1=models.URLField(blank=True, max_length=600)
    vedio_url2=models.URLField(blank=True, max_length=600)
    type=models.CharField(max_length=800,blank=True)
    Capacity =models.CharField(max_length=800,blank=True)
    Bore =models.CharField(max_length=800,blank=True)
    Stroke =models.CharField(max_length=800,blank=True)
    
    Compression =models.CharField(max_length=800,blank=True)
    Max_Power_EC  =models.CharField(max_length=800,blank=True)
    Max_Torque_EC =models.CharField(max_length=800,blank=True)
    System =models.CharField(max_length=800,blank=True)
    Exhauste =models.CharField(max_length=800,blank=True)
    Final_Drive =models.CharField(max_length=800,blank=True)
    Clutch =models.CharField(max_length=800,blank=True)
    Gearbox =models.CharField(max_length=800,blank=True)
    
    Frame =models.CharField(max_length=800,blank=True)
    Swingarm =models.CharField(max_length=800,blank=True)
    Front_Wheel=models.CharField(max_length=800,blank=True)
    Rear_Wheel=models.CharField(max_length=800,blank=True)
    Front_Tyre=models.CharField(max_length=800,blank=True)
    Rear_Tyre=models.CharField(max_length=800,blank=True)
    Front_Suspension  =models.CharField(max_length=800,blank=True)
    Rear_Suspension  =models.CharField(max_length=800,blank=True)
    Front_Brakes  =models.CharField(max_length=800,blank=True)
    Rear_Brakes   =models.CharField(max_length=800,blank=True)
    Instrument    =models.CharField(max_length=800,blank=True)
    Handlebars   =models.CharField(max_length=800,blank=True)
    Height   =models.CharField(max_length=800,blank=True)
    Seat_Height    =models.CharField(max_length=800,blank=True)
    Wheelbase   =models.CharField(max_length=800,blank=True)
    Rake   =models.CharField(max_length=800,blank=True)
    Trail   =models.CharField(max_length=800,blank=True)
    Tank   =models.CharField(max_length=800,blank=True)
    Wet_Weight   =models.CharField(max_length=800,blank=True)
    Fuel_Consumption    =models.CharField(max_length=800,blank=True)
    CO2_Figures    =models.CharField(max_length=4000,blank=True)
    Service_Interval    =models.CharField(max_length=800,blank=True)
    Engine =models.CharField(max_length=800,blank=True) 
    Power_Torque  =models.CharField(max_length=800,blank=True) 
    Compliance =models.CharField(max_length=800,blank=True) 
    Clutch =models.CharField(max_length=800,blank=True) 
    Traction_Control  =models.CharField(max_length=800,blank=True) 
    Riding_Modes  =models.CharField(max_length=800,blank=True) 
    Shift_Assist  =models.CharField(max_length=800,blank=True) 
    Suspension  =models.CharField(max_length=800,blank=True) 
    Brakes =models.CharField(max_length=800,blank=True) 
    Instruments =models.CharField(max_length=800,blank=True) 
    Connectivity =models.CharField(max_length=800,blank=True) 
    Lighting =models.CharField(max_length=800,blank=True) 

    mc_image1=models.ImageField(upload_to='bike_images/',null=True)
    mc_image2=models.ImageField(upload_to='bike_images/',null=True)
    mc_image3=models.ImageField(upload_to='bike_images/',null=True)
    mc_image4=models.ImageField(upload_to='bike_images/',null=True)
    mc_image5=models.ImageField(upload_to='bike_images/',null=True)

    mc_tittle1=models.TextField(blank=True)
    mc_tittle2=models.TextField(blank=True)
    mc_tittle3=models.TextField(blank=True)
    mc_tittle4=models.TextField(blank=True)
    mc_tittle5=models.TextField(blank=True)

    mc_para1=models.TextField(blank=True)
    mc_para2=models.TextField(blank=True)
    mc_para3=models.TextField(blank=True)
    mc_para4=models.TextField(blank=True)
    mc_para5=models.TextField(blank=True)


    c_image1=models.ImageField(upload_to='bike_images/',null=True)
    c_image2=models.ImageField(upload_to='bike_images/',null=True)

    c_tittle1=models.TextField(blank=True)
    c_tittle2=models.TextField(blank=True)

    c_para1=models.TextField(blank=True)
    c_para2=models.TextField(blank=True)

    reason_image=models.ImageField(upload_to='bike_images/',null=True)

    reason_para1=models.TextField(blank=True)
    reason_para2=models.TextField(blank=True)
    reason_para3=models.TextField(blank=True)
    reason_para4=models.TextField(blank=True)
    reason_para5=models.TextField(blank=True)
    reason_para6=models.TextField(blank=True)
    reason_para7=models.TextField(blank=True)
    reason_para8=models.TextField(blank=True)
    reason_para9=models.TextField(blank=True)
    reason_para10=models.TextField(blank=True)
    reason_para11=models.TextField(blank=True)
    reason_para12=models.TextField(blank=True)


    reason_tittle1=models.TextField(blank=True)
    reason_tittle2=models.TextField(blank=True)
    reason_tittle3=models.TextField(blank=True)
    reason_tittle4=models.TextField(blank=True)
    reason_tittle5=models.TextField(blank=True)
    reason_tittle6=models.TextField(blank=True)
    reason_tittle7=models.TextField(blank=True)
    reason_tittle8=models.TextField(blank=True)

    reason_video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    reason_image1=models.ImageField(upload_to='bike_images/',null=True)
    reason_image2=models.ImageField(upload_to='bike_images/',null=True)
    reason_image3=models.ImageField(upload_to='bike_images/',null=True)



    access_para1=models.TextField(blank=True)
    access_para2=models.TextField(blank=True)
    access_para3=models.TextField(blank=True)
    access_para4=models.TextField(blank=True)
    access_para5=models.TextField(blank=True)
    access_para6=models.TextField(blank=True)
    access_para6=models.TextField(blank=True)
    access_para8=models.TextField(blank=True)
    access_para9=models.TextField(blank=True)
    access_para10=models.TextField(blank=True)
    access_para11=models.TextField(blank=True)
    access_para12=models.TextField(blank=True)


    bold_tittle1=models.TextField(blank=True)
    bold_tittle2=models.TextField(blank=True)
    bold_tittle3=models.TextField(blank=True)
    bold_tittle4=models.TextField(blank=True)

    access_li1=models.TextField(blank=True)
    access_li2=models.TextField(blank=True)
    access_li3=models.TextField(blank=True)
    access_li4=models.TextField(blank=True)
    access_li5=models.TextField(blank=True)
    access_li6=models.TextField(blank=True)
    access_li7=models.TextField(blank=True)
    access_li8=models.TextField(blank=True)
    access_li9=models.TextField(blank=True)
    access_li10=models.TextField(blank=True)
    access_li11=models.TextField(blank=True)
    access_li12=models.TextField(blank=True)
    access_li13=models.TextField(blank=True)
    access_li14=models.TextField(blank=True)
    access_li15=models.TextField(blank=True)
    access_li16=models.TextField(blank=True)
    access_li17=models.TextField(blank=True)


    access_image1=models.ImageField(upload_to='bike_images/',null=True)
    access_image2=models.ImageField(upload_to='bike_images/',null=True)
    access_image3=models.ImageField(upload_to='bike_images/',null=True)
    access_image4=models.ImageField(upload_to='bike_images/',null=True)
    access_image5=models.ImageField(upload_to='bike_images/',null=True)
    access_image6=models.ImageField(upload_to='bike_images/',null=True)
    def __str__(self):
        return self.name
