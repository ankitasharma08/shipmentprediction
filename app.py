from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("shipment_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_shipment = request.form["Shipment_Time"]
        Shipment_day = int(pd.to_datetime(date_shipment, format="%Y-%m-%d").day)
        Shipment_month = int(pd.to_datetime(date_shipment, format ="%Y-%m-%d").month)
        Shipment_week = int(pd.to_datetime(date_shipment, format ="%Y-%m-%d").dayofweek)

        # source
        # Al Jubail = 0 (not in column)
        source=request.form['SourceCity']
        if(source =='Dammam'):
            Dammam = 1
            Jeddah = 0
            Riyadh = 0
            Tiles_Plant = 0
           

        elif (source=='Jeddah'):
            Dammam = 0
            Jeddah = 1
            Riyadh = 0
            Tiles_Plant= 0

        elif (source=='Riyadh'):
            Dammam = 0
            Jeddah = 0
            Riyadh = 1
            Tiles_Plant= 0
            
        elif (source=='Tiles Plant 2'):
            Dammam = 0
            Jeddah = 0
            Riyadh = 0
            Tiles_Plant= 1
            
        
        else:
            Dammam = 0
            Jeddah = 0
            Riyadh = 0
            Tiles_Plant= 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # DestinationCity
        # Abu Dhabi = 0 (not in column)
        DestinationCity = request.form["DestinationCity"]
        if (DestinationCity == 'Ad Diriyah'):
            Ad_Diriyah = 1
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0 
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Al Duwadimi'):
            Ad_Diriyah = 0
            Al_Duwadimi = 1
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0 
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Al Hofuf'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 1
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0 
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Al Jubail'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 1
            Al_Khobar = 0
            Al_Rashid = 0 
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0
        
        elif (DestinationCity == 'Al Khobar'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 1
            Al_Rashid = 0 
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Al Rashid'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 1 
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Amajiah'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 1
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Bahrain'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 1
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Buraydah'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 1
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Dammam'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 1
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Dubai'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 1
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Hafar Al Batin'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 1
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        
        elif (DestinationCity == 'Hail'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 1
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Jeddah'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 1
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Kuwait'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 1
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Medina'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 1
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Riyadh'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 1
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Tabuk'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 1
            Taif = 0
            Tammamah = 0

        elif (DestinationCity == 'Taif'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 1
            Tammamah = 0

        elif (DestinationCity == 'Tammamah'):
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 1
        
            
        else:
            Ad_Diriyah = 0
            Al_Duwadimi = 0
            Al_Hofuf = 0
            Al_Jubail = 0
            Al_Khobar = 0
            Al_Rashid = 0
            Amajiah = 0
            Bahrain = 0
            Buraydah = 0
            Dammam = 0
            Dubai = 0
            Hafar_Al_Batin = 0
            Hail = 0
            Jeddah = 0
            Kuwait = 0
            Medina = 0
            Riyadh = 0
            Tabuk = 0
            Taif = 0
            Tammamah = 0

        
        # Destination Country 
        # Bahrain = 0 (not in column)
        DestinationCountry = request.form["DestinationCountry"]
        if (DestinationCountry == 'KSA'):
            KSA = 1
            Kuwait = 0
            UAE = 0
            
        
        elif (DestinationCountry == 'Kuwait'):
            KSA = 0
            Kuwait = 1
            UAE = 0

        elif (DestinationCountry == 'UAE'):
            KSA = 0
            Kuwait = 1
            UAE = 0

        else:
            KSA = 0
            Kuwait = 0
            UAE = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    


        
        prediction=model.predict([[
            Shipment_day,
            Shipment_week,
            Shipment_month,
            Ad_Diriyah,
            Al_Duwadimi,
            Al_Hofuf,
            Al_Jubail,
            Al_Khobar,
            Al_Rashid,
            Amajiah,
            Bahrain,
            Buraydah,
            Dammam,
            Dubai,
            Hafar_Al_Batin,
            Hail,
            Jeddah,
            Kuwait,
            Medina,
            Riyadh,
            Tabuk,
            Taif,
            Tammamah,
            KSA,
            Kuwait,
            UAE,
            Dammam,
            Jeddah,
            Riyadh,
            Tiles_Plant

        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Shipment price is {} SAR".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
