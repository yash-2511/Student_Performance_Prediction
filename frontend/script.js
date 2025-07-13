
document.getElementById('predictForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const data = {
    hours_studied: +document.getElementById('hours_studied').value,
    attendance: +document.getElementById('attendance').value,
    previous_grade: +document.getElementById('previous_grade').value,
    internet: document.getElementById('internet').value,
    parent_education: document.getElementById('parent_education').value
  };
  const response = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  const result = await response.json();
  document.getElementById('result').textContent = "Predicted Performance: " + result.prediction;
});
