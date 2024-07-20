from flask import Flask
from flask import render_template, request
from prediction_model import predictor

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template("home.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    
    if request.method == "POST":
        disease_diet_chart = {
    "Fungal infection": ["Garlic", "Onions", "Yogurt", "Probiotics"],
    "Allergy": ["Quercetin-rich foods (apples, onions)", "Omega-3 fatty acids (fish, flaxseed)"],
    "GERD": ["Oatmeal", "Ginger", "Green vegetables", "Lean meats"],
    "Chronic cholestasis": ["Low-fat diet", "Small, frequent meals", "Fresh fruits and vegetables"],
    "Drug Reaction": ["Simple foods (rice, boiled potatoes)", "Clear liquids", "Avoid spicy or acidic foods"],
    "Peptic ulcer disease": ["High-fiber foods", "Cabbage juice", "Broccoli", "Whole grains"],
    "AIDS": ["High-protein foods (lean meats, beans)", "Vitamin-rich fruits and vegetables", "Whole grains"],
    "Diabetes": ["Whole grains", "Fiber-rich foods (beans, oats)", "Healthy fats (avocado, nuts)"],
    "Gastroenteritis": ["BRAT diet (bananas, rice, applesauce, toast)", "Clear fluids", "Plain crackers"],
    "Bronchial Asthma": ["Omega-3 fatty acids (fish)", "Vitamin D-rich foods", "Antioxidant-rich fruits (berries, citrus)"],
    "Hypertension": ["Low-sodium foods", "Potassium-rich foods (bananas, potatoes)", "Lean proteins (chicken, fish)"],
    "Migraine": ["Magnesium-rich foods (spinach, almonds)", "Avoid triggers (chocolate, aged cheese, caffeine)"],
    "Cervical spondylosis": ["Calcium-rich foods (milk, yogurt)", "Vitamin D-rich foods (salmon, eggs)", "Whole grains"],
    "Paralysis (brain hemorrhage)": ["High-protein foods (lean meats, fish)", "Omega-3 fatty acids (flaxseed, walnuts)", "Fresh fruits and vegetables"],
    "Jaundice": ["Easy-to-digest foods (boiled vegetables, fruits)", "Low-fat dairy products", "Plenty of fluids (water, coconut water)"],
    "Malaria": ["High-calorie foods (bananas, rice)", "Fluids (oral rehydration solutions)", "Soft, bland foods"],
    "Chicken pox": ["High-protein foods (chicken, eggs)", "Vitamin C-rich foods (citrus fruits, bell peppers)", "Comfort foods (soup, oatmeal)"],
    "Dengue": ["Fluids (oral rehydration solutions)", "High-protein foods (poultry, fish)", "Vitamin C-rich foods (kiwi, strawberries)"],
    "Typhoid": ["Soft, bland foods (rice, bananas)", "Well-cooked vegetables", "Electrolyte-rich fluids (coconut water, broth)"],
    "Hepatitis A": ["High-calorie foods (whole grains, nuts)", "Lean proteins (chicken, tofu)", "Avoid fatty or fried foods"],
    "Hepatitis B": ["Low-fat, high-fiber foods", "Lean proteins (fish, beans)", "Plenty of fluids (water, herbal teas)"],
    "Hepatitis C": ["Low-fat, high-protein diet", "Foods rich in antioxidants (berries, dark leafy greens)", "Avoid alcohol and processed foods"],
    "Hepatitis D": ["Balanced diet with vitamins and minerals", "Protein-rich foods (eggs, dairy)", "Avoid alcohol and fatty foods"],
    "Hepatitis E": ["High-fiber foods (whole grains, legumes)", "Lean proteins (chicken, turkey)", "Limit salt and processed foods"],
    "Alcoholic hepatitis": ["High-protein foods (lean meats, fish)", "Fruits and vegetables", "Whole grains"],
    "Tuberculosis": ["High-calorie, high-protein foods", "Vitamin-rich foods (fruits, vegetables)", "Nuts and seeds"],
    "Common Cold": ["Foods rich in vitamin C (citrus fruits, berries)", "Garlic", "Ginger tea"],
    "Pneumonia": ["Protein-rich foods (eggs, dairy, lean meats)", "Fluids (water, herbal teas)", "Easy-to-digest foods (soups, broths)"],
    "Dimorphic hemmorhoids (piles)": ["High-fiber foods (whole grains, fruits, vegetables)", "Plenty of fluids (water, herbal teas)", "Avoid spicy and fatty foods"],
    "Heart attack": ["Omega-3 fatty acids (fatty fish like salmon, flaxseeds)", "Whole grains", "Fruits and vegetables"],
    "Varicose veins": ["Fiber-rich foods (beans, whole grains)", "Fruits and vegetables", "Low-sodium foods"],
    "Hypothyroidism": ["Iodine-rich foods (seafood, dairy)", "Selenium-rich foods (Brazil nuts, sunflower seeds)", "Whole grains"],
    "Hyperthyroidism": ["Calcium-rich foods (dairy, leafy greens)", "Iron-rich foods (lean meats, beans)", "Healthy fats (avocado, nuts)"],
    "Hypoglycemia": ["Complex carbohydrates (whole grains, legumes)", "Protein-rich foods (poultry, eggs)", "Small, frequent meals"],
    "Osteoarthristis": ["Omega-3 fatty acids (fish, flaxseeds)", "Vitamin C-rich foods (citrus fruits, bell peppers)", "Calcium-rich foods (dairy, leafy greens)"],
    "Arthritis": ["Anti-inflammatory foods (berries, fatty fish)", "Healthy fats (olive oil, nuts)", "Whole grains"],
    "Vertigo (Paroxysmal Positional Vertigo)": ["Low-sodium diet", "Hydration (water)", "Avoid caffeine and alcohol"],
    "Acne": ["Fruits and vegetables", "Whole grains", "Hydration (water)", "Limit dairy and sugary foods"],
    "Urinary tract infection": ["Cranberry juice or supplements", "Plenty of water", "High-fiber foods (fruits, vegetables, whole grains)"],
    "Psoriasis": ["Anti-inflammatory foods (fatty fish, nuts)", "Colorful fruits and vegetables", "Whole grains"],
    "Impetigo": ["High-protein foods (lean meats, dairy)", "Vitamin C-rich foods (citrus fruits)", "Plenty of fluids (water, herbal teas)"]

}
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        symptoms = list(request.form.get("passer").split(","))
        print(symptoms)
        prediction = predictor.predictor(symptoms)
        diet_list = disease_diet_chart[prediction]
        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": symptoms,
            "prediction": prediction,
            "diet_list":diet_list
        }
        print(data)
        return render_template("results.html", data=data)
    return "Wrong request"


if __name__ == '__main__':
    app.run()
