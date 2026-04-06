function analyze() {
    const text = document.getElementById("textToAnalyze").value;

    fetch(`/sentimentAnalyzer?textToAnalyze=${encodeURIComponent(text)}`)
        .then(res => res.text())
        .then(data => {
            document.getElementById("result").innerText = data;
        });
}