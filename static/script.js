async function translateText(){

    const text = document.getElementById("inputText").value;

    const targetLanguage =
        document.getElementById("targetLanguage").value;

    const response = await fetch(
        `/translate?text=${encodeURIComponent(text)}&target_language=${targetLanguage}`
    );

    const data = await response.json();

    document.getElementById("outputText").value =
        data.translated_text;
}

// #The frontend uses an asynchronous JavaScript function to 
// #collect user input and selected language from the DOM. 
// #It sends the data to the backend translation API using fetch(). 
// #The backend processes the request using the translation model 
// #and returns a JSON response. Then the frontend parses the 
// #JSON and dynamically updates the UI with the translated text