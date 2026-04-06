function analyze() {
    const text = document.getElementById("textToAnalyze").value;
    const resultElement = document.getElementById("result");

    fetch(`/sentimentAnalyzer?textToAnalyze=${encodeURIComponent(text)}`)
        .then((response) => response.text())
        .then((data) => {
            resultElement.innerText = data;
        })
        .catch(() => {
            resultElement.innerText = "An error occurred while analyzing the text.";
        });
}