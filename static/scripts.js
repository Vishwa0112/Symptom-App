const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  const selectedList = document.getElementById('selected-list');
  const passer = document.getElementById('passer');
  const selectedItems = [];

  // Sample data (you can replace it with your own data)
  const data = ['Abdominal pain', 'Abnormal menstruation', 'Acidity', 'Acute liver failure', 'Altered sensorium', 'Anxiety', 'Back pain', 'Belly pain', 'Blackheads', 'Bladder discomfort', 'Blister', 'Blood in sputum', 'Bloody stool', 'Blurred and distorted vision', 'Breathlessness', 'Brittle nails', 'Bruising', 'Burning micturition', 'Chest pain', 'Chills', 'Cold hands and feets', 'Coma', 'Congestion', 'Constipation', 'Continuous feel of urine', 'Continuous sneezing', 'Cough', 'Cramps', 'Dark urine', 'Dehydration', 'Depression', 'Diarrhoea', 'Dischromic patches', 'Distention of abdomen', 'Dizziness', 'Drying and tingling lips', 'Enlarged thyroid', 'Excessive hunger', 'Extra marital contacts', 'Family history', 'Fast heart rate', 'Fatigue', 'Fluid overload', 'Fluid overload', 'Foul smell ofurine', 'Headache', 'High fever', 'Hip joint pain', 'History of alcohol consumption', 'Increased appetite', 'Indigestion', 'Inflammatory nails', 'Internal itching', 'Irregular sugar level', 'Irritability', 'Irritation in anus', 'Itching', 'Joint pain', 'Knee pain', 'Lack of concentration', 'Lethargy', 'Loss of appetite', 'Loss of balance', 'Loss of smell', 'Malaise', 'Mild fever', 'Mood swings', 'Movement stiffness', 'Mucoid sputum', 'Muscle pain', 'Muscle wasting', 'Muscle weakness', 'Nausea', 'Neck pain', 'Nodal skin eruptions', 'Obesity', 'Pain behind the eyes', 'Pain during bowel movements', 'Pain in anal region', 'Painful walking', 'Palpitations', 'Passage of gases', 'Patches in throat', 'Phlegm', 'Polyuria', 'Prognosis', 'Prominent veins on calf', 'Puffy face and eyes', 'Pus filled pimples', 'Receiving blood transfusion', 'Receiving unsterile injections', 'Red sore around nose', 'Red spots over body', 'Redness of eyes', 'Restlessness', 'Runny nose', 'Rusty sputum', 'Scurring', 'Shivering', 'Silver like dusting', 'Sinus pressure', 'Skin peeling', 'Skin rash', 'Slurred speech', 'Small dents in nails', 'Spinning movements', 'Spotting urination', 'Stiff neck', 'Stomach bleeding', 'Stomach pain', 'Sunken eyes', 'Sweating', 'Swelled lymph nodes', 'Swelling joints', 'Swelling of stomach', 'Swollen blood vessels', 'Swollen extremeties', 'Swollen legs', 'Throat irritation', 'Toxic look (typhos)', 'Ulcers on tongue', 'Unsteadiness', 'Visual disturbances', 'Vomiting', 'Watering from eyes', 'Weakness in limbs', 'Weakness of one body side', 'Weight gain', 'Weight loss', 'Yellow crust ooze', 'Yellow urine', 'Yellowing of eyes', 'Yellowish skin'];

  function updateResults(query) {
    const filteredData = data.filter(item => item.toLowerCase().includes(query.toLowerCase()));

    // Clear previous results
    searchResults.innerHTML = '';

    // Display filtered results
    filteredData.forEach(item => {
      const resultItem = document.createElement('div');
      resultItem.textContent = item;
      resultItem.addEventListener('click', function() {
        addToSelectedList(item);
      });
      searchResults.appendChild(resultItem);
    });
  }

  function addToSelectedList(item) {
    if (!selectedItems.includes(item)) {
      selectedItems.push(item);
      const listItem = document.createElement('li');
      listItem.textContent = item;
      selectedList.appendChild(listItem);
      console.log(selectedItems)
      passer.value = selectedItems

    }
  }

  // Initial display
  searchInput.addEventListener('focusin', function (){
    searchResults.hidden = false;
    updateResults('');

  })


  // Event listener for input change
  searchInput.addEventListener('input', function() {
    updateResults(this.value);
  });